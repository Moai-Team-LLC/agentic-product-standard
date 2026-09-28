#!/usr/bin/env python3
"""AITM-SMB integrity checks.

Framework mode (default) checks the methodology itself: references resolve,
skill and artifact contracts are well-formed, versions agree, identifiers are
registered, deprecated terms do not leak into active files.

Engagement mode (--engagement DIR) checks an engagement workspace: every
referenced ID is defined once, IDs use registered prefixes, the minimum valid
path (EXECUTION_MODEL.md §6) is present, core trace links exist, and approved
records are backed by human-gate Decisions.

Standard library only. Exit code 0 = no errors, 1 = errors, 2 = usage error.
Warnings never fail the run unless --strict is given.
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ID_RE = re.compile(r"\b([A-Z]{3})-(\d{3,})\b")
TEMPLATE_ID_RE = re.compile(r"\b([A-Z]{3})-###")
GATE_RE = re.compile(r"\bHG-[A-Z]+(?:-[A-Z]+)*\b")
FENCE_RE = re.compile(r"^(```|~~~)")

# Files that record history. References from them to removed paths are warnings.
HISTORICAL = ("CHANGELOG.md", "releases/", "audits/")
# Files allowed to name deprecated artifacts.
DEPRECATION_ALLOWED = (
    "CHANGELOG.md", "releases/", "audits/", "decisions/",
    "artifacts/INDEX.md", "artifacts/target-architecture.md",
    "artifacts/ai-opportunity-map.md", "VERSIONING.md", "tools/",
)
DEPRECATED_ARTIFACTS = ("artifacts/target-architecture.md", "artifacts/ai-opportunity-map.md")
DEPRECATED_TERMS = ("AI Opportunity Map",)

SKILL_CATEGORIES = {
    "orchestrator", "diagnostic-specialist", "design-specialist",
    "execution-governance", "framework-operations",
}
SKILL_REQUIRED_KEYS = (
    "name", "description", "version", "minimum_framework_version",
    "framework", "status", "category", "phase", "human_gate",
)
SKILL_REQUIRED_HEADINGS = ("Purpose", "Required inputs", "Produces", "Procedure", "Handoff")


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, where, msg):
        self.errors.append("%s: %s" % (where, msg))

    def warn(self, where, msg):
        self.warnings.append("%s: %s" % (where, msg))


# --------------------------------------------------------------------------
# Minimal YAML subset parser (block mappings, block sequences, flow lists,
# comments, scalars). Enough for AITM-SMB contracts and engagement records.
# --------------------------------------------------------------------------

def _strip_comment(line):
    out, quote = [], None
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            break
        out.append(ch)
    return "".join(out).rstrip()


def _scalar(text):
    text = text.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        return text[1:-1]
    if text.startswith("[") and text.endswith("]"):
        inner = text[1:-1].strip()
        if not inner:
            return []
        return [_scalar(part) for part in inner.split(",") if part.strip()]
    if text.startswith("{") and text.endswith("}"):
        inner = text[1:-1].strip()
        result = {}
        for part in inner.split(","):
            if ":" in part:
                k, v = part.split(":", 1)
                result[k.strip()] = _scalar(v)
        return result
    return text


PARSE_WARNINGS = []

_KEY_RE = re.compile(r"^([A-Za-z_][\w.-]*|\"[^\"]+\")\s*:(\s+(.*))?$")


def parse_yaml(text):
    lines = []
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        stripped = _strip_comment(raw)
        if not stripped.strip():
            continue
        indent = len(stripped) - len(stripped.lstrip(" "))
        lines.append((indent, stripped.strip()))
    node, _ = _parse_block(lines, 0, 0)
    return node


def _parse_block(lines, i, indent):
    if i >= len(lines):
        return None, i
    if lines[i][1].startswith("- ") or lines[i][1] == "-":
        return _parse_seq(lines, i, lines[i][0])
    return _parse_map(lines, i, lines[i][0])


def _parse_map(lines, i, indent):
    result = {}
    while i < len(lines):
        ind, text = lines[i]
        if ind < indent or (ind == indent and text.startswith("- ")):
            break
        if ind > indent:
            i += 1  # stray deeper line; tolerate
            continue
        m = _KEY_RE.match(text)
        if not m:
            i += 1
            continue
        key = m.group(1).strip('"')
        value = (m.group(3) or "").strip()
        i += 1
        if key in result:
            PARSE_WARNINGS.append("duplicate key `%s` in one mapping (the later value hides the earlier one; "
                                  "use a list or separate blocks)" % key)
        if value.startswith("[") and not value.endswith("]"):
            while i < len(lines) and lines[i][0] > indent and not value.endswith("]"):
                value += " " + lines[i][1]
                i += 1
        if value in ("|", ">", "|-", ">-"):
            parts = []
            while i < len(lines) and lines[i][0] > indent:
                parts.append(lines[i][1])
                i += 1
            result[key] = "\n".join(parts)
        elif value:
            result[key] = _scalar(value)
        elif i < len(lines) and (lines[i][0] > indent or
                                 (lines[i][0] == indent and lines[i][1].startswith("- "))):
            child, i = _parse_block(lines, i, lines[i][0])
            result[key] = child
        else:
            result[key] = None
    return result, i


def _parse_seq(lines, i, indent):
    result = []
    while i < len(lines):
        ind, text = lines[i]
        if ind != indent or not (text.startswith("- ") or text == "-"):
            break
        body = text[1:].strip()
        i += 1
        if not body:
            if i < len(lines) and lines[i][0] > indent:
                child, i = _parse_block(lines, i, lines[i][0])
                result.append(child)
            else:
                result.append(None)
        elif _KEY_RE.match(body) and not body.startswith(("\"", "'")):
            sub = [(indent + 2, body)]
            while i < len(lines) and lines[i][0] > indent:
                sub.append(lines[i])
                i += 1
            child, _ = _parse_map(sub, 0, indent + 2)
            result.append(child)
        else:
            result.append(_scalar(body))
    return result, i


# --------------------------------------------------------------------------
# Markdown helpers
# --------------------------------------------------------------------------

def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def rel(path, base=ROOT):
    return os.path.relpath(path, base).replace(os.sep, "/")


def list_files(base, exts=(".md",)):
    out = []
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = sorted(d for d in dirnames
                             if not d.startswith(".") and d not in ("dist", "__pycache__", "node_modules"))
        for name in sorted(filenames):
            if name.endswith(exts):
                out.append(os.path.join(dirpath, name))
    return out


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    return parse_yaml(text[4:end]) or {}


def split_fences(text):
    """Yield (in_fence, lang, line) for every line."""
    in_fence, lang = False, ""
    for line in text.splitlines():
        m = FENCE_RE.match(line.strip())
        if m:
            if not in_fence:
                in_fence, lang = True, line.strip()[3:].strip()
            else:
                in_fence, lang = False, ""
            yield None, "", line
            continue
        yield in_fence, lang, line


def yaml_blocks(text):
    blocks, current, collecting = [], [], False
    for in_fence, lang, line in split_fences(text):
        if in_fence is None:
            if collecting:
                blocks.append("\n".join(current))
                current, collecting = [], False
            continue
        if in_fence and lang in ("yaml", "yml"):
            collecting = True
            current.append(line)
    return blocks


def inline_code_refs(text):
    """Backticked path-like tokens outside fenced blocks."""
    refs = []
    for in_fence, _, line in split_fences(text):
        if in_fence or in_fence is None:
            continue
        for token in re.findall(r"`([^`\s]+)`", line):
            refs.append(token)
    return refs


def md_links(text):
    links = []
    for in_fence, _, line in split_fences(text):
        if in_fence or in_fence is None:
            continue
        for target in re.findall(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", line):
            links.append(target)
    return links


def headings(text):
    return [re.sub(r"^#+\s*", "", line).strip()
            for in_fence, _, line in split_fences(text)
            if in_fence is False and line.startswith("#")]


def looks_like_path(token):
    if any(c in token for c in "<>*{}|$") or "###" in token or token.startswith(("http", "-")):
        return False
    if token.endswith("/"):
        return "/" in token[:-1] or token[:-1].isidentifier() or re.match(r"^[\w.-]+$", token[:-1])
    return bool(re.search(r"\.(md|py|cff|ya?ml)$", token)) and not token.startswith(".")


def resolve(token, file_dir):
    token = token.split("#", 1)[0]
    if not token:
        return True
    for base in (ROOT, file_dir):
        if os.path.exists(os.path.normpath(os.path.join(base, token))):
            return True
    return False


def is_historical(relpath):
    return relpath.startswith(HISTORICAL)


def semver(v):
    m = re.match(r"^(\d+)\.(\d+)\.(\d+)$", str(v or "").strip())
    return tuple(int(x) for x in m.groups()) if m else None


# --------------------------------------------------------------------------
# Framework checks
# --------------------------------------------------------------------------

def manifest():
    text = read(os.path.join(ROOT, "MANIFEST.md"))
    for block in yaml_blocks(text):
        data = parse_yaml(block)
        if isinstance(data, dict) and "framework" in data:
            if isinstance(data["framework"], dict):
                data.setdefault("version", data["framework"].get("version"))
            return data
    return {}


def registered_prefixes():
    text = read(os.path.join(ROOT, "ontology", "ONTOLOGY.md"))
    return set(m.group(1) for m in TEMPLATE_ID_RE.finditer(text))


def declared_gates():
    text = read(os.path.join(ROOT, "STANDARD.md"))
    return set(GATE_RE.findall(text))


def check_references(files, rep):
    for path in files:
        relpath = rel(path)
        text = read(path)
        file_dir = os.path.dirname(path)
        for token in inline_code_refs(text):
            if not looks_like_path(token):
                continue
            if not resolve(token, file_dir):
                (rep.warn if is_historical(relpath) else rep.error)(
                    relpath, "unresolved reference `%s`" % token)
        for target in md_links(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0]
            if clean and not os.path.exists(os.path.normpath(os.path.join(file_dir, clean))):
                (rep.warn if is_historical(relpath) else rep.error)(
                    relpath, "broken link (%s)" % target)


def check_skills(version, gates, rep):
    skills_dir = os.path.join(ROOT, "skills")
    index_text = read(os.path.join(skills_dir, "INDEX.md"))
    numbers = {}
    for name in sorted(os.listdir(skills_dir)):
        path = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.isfile(path):
            continue
        relpath = rel(path)
        text = read(path)
        fm = frontmatter(text)
        if fm is None:
            rep.error(relpath, "missing frontmatter")
            continue
        for key in SKILL_REQUIRED_KEYS:
            if fm.get(key) in (None, ""):
                rep.error(relpath, "frontmatter missing `%s`" % key)
        if fm.get("name") != name:
            rep.error(relpath, "name `%s` does not match directory `%s`" % (fm.get("name"), name))
        desc = fm.get("description") or ""
        if isinstance(desc, str) and len(desc) > 1024:
            rep.error(relpath, "description longer than 1024 characters")
        if fm.get("framework") != "AITM-SMB":
            rep.error(relpath, "framework must be AITM-SMB")
        if fm.get("category") not in SKILL_CATEGORIES:
            rep.error(relpath, "unknown category `%s`" % fm.get("category"))
        mfv = semver(fm.get("minimum_framework_version"))
        if not mfv:
            rep.error(relpath, "minimum_framework_version is not semver")
        elif version and mfv > version:
            rep.error(relpath, "minimum_framework_version is newer than the framework")
        gate_flag = str(fm.get("human_gate")).lower()
        skill_gates = fm.get("gates") or []
        if isinstance(skill_gates, str):
            skill_gates = [skill_gates]
        if gate_flag == "true":
            if not skill_gates:
                rep.error(relpath, "human_gate is true but `gates` is empty")
        elif gate_flag == "false":
            if skill_gates:
                rep.error(relpath, "human_gate is false but `gates` is set")
        else:
            rep.error(relpath, "human_gate must be true or false")
        for g in skill_gates:
            if g not in gates:
                rep.error(relpath, "gate `%s` is not declared in STANDARD.md" % g)
        heads = headings(text)
        for h in SKILL_REQUIRED_HEADINGS:
            if not any(x == h or x.startswith(h) for x in heads):
                rep.error(relpath, "missing section `## %s`" % h)
        if fm.get("category") == "orchestrator" and not any(x.startswith("Specialist skills") for x in heads):
            rep.error(relpath, "orchestrator missing `## Specialist skills`")
        m = re.match(r"^(\d{2})-", name)
        if not m:
            rep.error(relpath, "skill directory must start with a two-digit number")
        else:
            if m.group(1) in numbers:
                rep.error(relpath, "skill number %s reused by %s" % (m.group(1), numbers[m.group(1)]))
            numbers[m.group(1)] = name
            if name not in index_text:
                rep.error("skills/INDEX.md", "skill `%s` is not listed" % name)
        produces = section(text, "Produces")
        for token in re.findall(r"`(artifacts/[\w.-]+\.md)`", produces):
            if token in DEPRECATED_ARTIFACTS:
                rep.error(relpath, "produces deprecated artifact `%s`" % token)
    root_skill = os.path.join(ROOT, "SKILL.md")
    if not os.path.isfile(root_skill):
        rep.error("SKILL.md", "missing root skill adapter")
    else:
        fm = frontmatter(read(root_skill)) or {}
        if fm.get("name") != "aitm-smb":
            rep.error("SKILL.md", "name must be `aitm-smb`")
        if not fm.get("description"):
            rep.error("SKILL.md", "missing description")
    return numbers


def section(text, title):
    out, active, level = [], False, 0
    for in_fence, _, line in split_fences(text):
        if in_fence is False and line.startswith("#"):
            lvl = len(line) - len(line.lstrip("#"))
            name = line.lstrip("#").strip()
            if active and lvl <= level:
                break
            if name.startswith(title):
                active, level = True, lvl
                continue
        if active:
            out.append(line)
    return "\n".join(out)


def skill_outputs(skills):
    """Map artifact path -> set of skills whose `## Produces` names it."""
    out = {}
    for name in skills.values():
        text = read(os.path.join(ROOT, "skills", name, "SKILL.md"))
        for token in set(re.findall(r"artifacts/[\w.-]+\.md", section(text, "Produces"))):
            out.setdefault(token, set()).add(name)
    return out


def check_artifacts(version, prefixes, skills, rep):
    art_dir = os.path.join(ROOT, "artifacts")
    outputs = skill_outputs(skills)
    index_text = read(os.path.join(art_dir, "INDEX.md"))
    for name in sorted(os.listdir(art_dir)):
        if not name.endswith(".md") or name in ("INDEX.md", "_ARTIFACT_CONTRACT.md"):
            continue
        path = os.path.join(art_dir, name)
        relpath = rel(path)
        text = read(path)
        fm = frontmatter(text)
        if fm is None:
            rep.error(relpath, "missing frontmatter")
            continue
        stem = name[:-3]
        if fm.get("artifact_type") != stem:
            rep.error(relpath, "artifact_type `%s` does not match file name" % fm.get("artifact_type"))
        if name not in index_text:
            rep.error("artifacts/INDEX.md", "artifact `%s` is not listed" % name)
        status = fm.get("status")
        if status == "deprecated":
            repl = fm.get("replacement") or []
            if isinstance(repl, str):
                repl = [repl]
            if not repl:
                rep.error(relpath, "deprecated artifact without replacement")
            for r in repl:
                if not os.path.exists(os.path.join(ROOT, r)):
                    rep.error(relpath, "replacement `%s` does not exist" % r)
            if not fm.get("removal_target"):
                rep.error(relpath, "deprecated artifact without removal_target")
            continue
        if status != "canonical":
            rep.error(relpath, "status must be canonical or deprecated")
        if semver(fm.get("framework_version")) != version:
            rep.error(relpath, "framework_version `%s` != framework version" % fm.get("framework_version"))
        if fm.get("id_prefix") and fm.get("id_prefix") not in prefixes:
            rep.error(relpath, "id_prefix `%s` is not registered in ontology/ONTOLOGY.md" % fm.get("id_prefix"))
        owner = fm.get("owner_module")
        if owner and not os.path.exists(os.path.join(ROOT, str(owner).split(" ")[0])):
            rep.error(relpath, "owner_module `%s` does not exist" % owner)
        produced = fm.get("produced_by") or []
        if isinstance(produced, str):
            produced = [produced]
        if not produced:
            rep.error(relpath, "produced_by is empty")
        for skill in produced:
            if skill not in skills.values():
                rep.error(relpath, "produced_by names unknown skill `%s`" % skill)
        declared, actual = set(produced), outputs.get("artifacts/" + name, set())
        for skill in sorted(actual - declared):
            rep.error(relpath, "skill `%s` produces this artifact but is not in produced_by" % skill)
        for skill in sorted(declared - actual):
            rep.error(relpath, "produced_by lists `%s` but its `## Produces` does not name this artifact" % skill)
        heads = headings(text)
        for h in ("Purpose", "Validation"):
            if not any(x.startswith(h) for x in heads):
                rep.error(relpath, "missing section `## %s`" % h)


def check_versions(man, rep):
    version = semver(man.get("version"))
    if not version:
        rep.error("MANIFEST.md", "framework version missing or not semver")
        return None
    vstr = "%d.%d.%d" % version
    for path in list_files(ROOT):
        relpath = rel(path)
        if is_historical(relpath) or relpath.startswith(("examples/", "decisions/")):
            continue
        for m in re.finditer(r"^\*\*Version:\*\*\s*`?([\d.]+)`?", read(path), re.M):
            if m.group(1) != vstr:
                rep.error(relpath, "Version header %s != MANIFEST version %s" % (m.group(1), vstr))
    changelog = read(os.path.join(ROOT, "CHANGELOG.md"))
    if not re.search(r"^## \[?%s\]?" % re.escape(vstr), changelog, re.M):
        rep.error("CHANGELOG.md", "no entry for %s" % vstr)
    citation = os.path.join(ROOT, "CITATION.cff")
    if os.path.exists(citation):
        m = re.search(r"^version:\s*\"?([\d.]+)", read(citation), re.M)
        if not m or m.group(1) != vstr:
            rep.error("CITATION.cff", "version does not match MANIFEST (%s)" % vstr)
    readme = read(os.path.join(ROOT, "README.md"))
    if vstr not in readme:
        rep.error("README.md", "does not mention the current version %s" % vstr)
    return version


def check_core(man, rep):
    index_text = read(os.path.join(ROOT, "NORMATIVE_INDEX.md"))
    for key in ("canonical_core", "registries"):
        for entry in man.get(key) or []:
            if not os.path.exists(os.path.join(ROOT, entry)):
                rep.error("MANIFEST.md", "%s entry `%s` does not exist" % (key, entry))
            elif entry not in index_text:
                rep.error("NORMATIVE_INDEX.md", "%s entry `%s` from MANIFEST is not listed" % (key, entry))
    standard = read(os.path.join(ROOT, "STANDARD.md"))
    invariants = re.findall(r"^### (INV-\d{2})", standard, re.M)
    declared = man.get("core_invariants") or []
    if len(invariants) != len(declared):
        rep.error("MANIFEST.md", "core_invariants lists %d items, STANDARD.md defines %d" % (len(declared), len(invariants)))
    profiles_text = read(os.path.join(ROOT, "APPLICATION_PROFILES.md"))
    for profile in ("Compact", "Standard", "Governed", "Portfolio", "Measured"):
        if not re.search(r"^#+ .*\b%s\b" % profile, profiles_text, re.M):
            rep.error("APPLICATION_PROFILES.md", "profile `%s` has no section" % profile)


def check_identifiers(files, prefixes, gates, rep):
    public_api = read(os.path.join(ROOT, "PUBLIC_API.md"))
    for p in set(m.group(1) for m in TEMPLATE_ID_RE.finditer(public_api)):
        if p not in prefixes:
            rep.error("PUBLIC_API.md", "stable prefix %s is not registered in ontology/ONTOLOGY.md" % p)
    for path in files:
        relpath = rel(path)
        if is_historical(relpath) or relpath.startswith("examples/"):
            continue
        text = read(path)
        for m in TEMPLATE_ID_RE.finditer(text):
            if m.group(1) not in prefixes:
                rep.error(relpath, "identifier prefix %s-### is not registered" % m.group(1))
        for g in set(GATE_RE.findall(text)):
            if g not in gates:
                rep.error(relpath, "human gate %s is not declared in STANDARD.md" % g)


def check_deprecated(files, rep):
    for path in files:
        relpath = rel(path)
        if relpath.startswith(DEPRECATION_ALLOWED):
            continue
        text = read(path)
        for term in DEPRECATED_ARTIFACTS + DEPRECATED_TERMS:
            if term in text:
                rep.error(relpath, "mentions deprecated `%s`" % term)


def check_orphans(files, rep):
    corpus = {rel(p): read(p) for p in files}
    entry = {"README.md", "SKILL.md", "CHANGELOG.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
             "SECURITY.md", "LICENSE"}
    for relpath in corpus:
        if relpath in entry or is_historical(relpath) or relpath.startswith(("examples/", "decisions/", ".github/")):
            continue
        base = os.path.basename(relpath)
        needle_dir = os.path.dirname(relpath) + "/"
        referenced = False
        for other, text in corpus.items():
            if other == relpath:
                continue
            if relpath in text or (base in text and base != "SKILL.md") or (
                    base == "SKILL.md" and os.path.dirname(relpath) in text):
                referenced = True
                break
        if not referenced and needle_dir not in "".join(corpus.values()):
            rep.warn(relpath, "no inbound reference (orphan)")


def run_framework(rep):
    files = list_files(ROOT)
    man = manifest()
    version = check_versions(man, rep)
    prefixes = registered_prefixes()
    gates = declared_gates()
    if not gates:
        rep.error("STANDARD.md", "no human gate identifiers (HG-*) declared")
    check_references(files, rep)
    check_core(man, rep)
    skills = check_skills(version, gates, rep)
    check_artifacts(version, prefixes, skills, rep)
    check_identifiers(files, prefixes, gates, rep)
    check_deprecated(files, rep)
    check_orphans(files, rep)
    return {
        "version": "%d.%d.%d" % version if version else "?",
        "files": len(files),
        "skills": len(skills),
        "prefixes": len(prefixes),
        "gates": len(gates),
    }


# --------------------------------------------------------------------------
# Engagement checks
# --------------------------------------------------------------------------

def walk_records(node, out, source):
    if isinstance(node, dict):
        ident = node.get("id")
        if isinstance(ident, str) and ID_RE.fullmatch(ident.strip()):
            out.append((ident.strip(), node, source))
        for key, value in node.items():
            if key == "artifact":  # instance metadata (_ARTIFACT_CONTRACT.md), not a record
                continue
            walk_records(value, out, source)
    elif isinstance(node, list):
        for item in node:
            walk_records(item, out, source)


def ids_in(value):
    found = set()
    if isinstance(value, dict):
        for v in value.values():
            found |= ids_in(v)
    elif isinstance(value, list):
        for v in value:
            found |= ids_in(v)
    elif isinstance(value, str):
        found |= set("%s-%s" % m.groups() for m in ID_RE.finditer(value))
    return found


def is_missing_marker(value):
    """TRACEABILITY.md: a missing link is recorded visibly as `MISSING:<reason>`."""
    if isinstance(value, str):
        return value.strip().startswith("MISSING")
    if isinstance(value, list):
        return any(isinstance(v, str) and v.strip().startswith("MISSING") for v in value)
    return False


def field_ids(record, *names):
    found = set()
    for name in names:
        found |= ids_in(record.get(name))
    return found


def run_engagement(target, rep, extra_prefixes=()):
    prefixes = registered_prefixes() | set(extra_prefixes)
    gates = declared_gates()
    files = list_files(target, (".md", ".yaml", ".yml"))
    records, references = [], {}
    for path in files:
        relpath = rel(path, target)
        text = read(path)
        blocks = [text] if path.endswith((".yaml", ".yml")) else yaml_blocks(text)
        for block in blocks:
            del PARSE_WARNINGS[:]
            try:
                walk_records(parse_yaml(block), records, relpath)
            except Exception as exc:  # pragma: no cover - defensive
                rep.warn(relpath, "could not parse a yaml block (%s)" % exc)
            for msg in PARSE_WARNINGS:
                rep.error(relpath, msg)
        for m in ID_RE.finditer(text):
            # Tokens with unregistered prefixes (e.g. ISO-9001, ORD-1234) are business text, not references.
            if m.group(1) in prefixes:
                references.setdefault("%s-%s" % m.groups(), set()).add(relpath)
        for g in set(GATE_RE.findall(text)):
            if g not in gates:
                rep.error(relpath, "unknown human gate %s" % g)

    defined = {}
    for ident, rec, source in records:
        if ident in defined:
            rep.error(source, "%s is defined more than once (also in %s)" % (ident, defined[ident][1]))
        else:
            defined[ident] = (rec, source)
        if ident.split("-")[0] not in prefixes:
            rep.error(source, "%s uses an unregistered prefix" % ident)
    for ident, sources in sorted(references.items()):
        if ident not in defined:
            rep.error(", ".join(sorted(sources)), "%s is referenced but never defined" % ident)

    by_prefix = {}
    for ident, (rec, _) in defined.items():
        by_prefix.setdefault(ident.split("-")[0], []).append((ident, rec))

    # Minimum valid path (EXECUTION_MODEL.md §6).
    for prefix, label in (("OUT", "Outcome"), ("CAP", "Capability"), ("GAP", "Gap"),
                          ("INT", "Intervention"), ("INI", "Initiative"), ("MET", "Metric"),
                          ("EVD", "Evidence")):
        if prefix not in by_prefix:
            rep.error(target, "minimum valid path: no %s (%s-###) defined" % (label, prefix))
    if not any(str(rec.get("type", "")).upper() == "TARGET" for _, rec in by_prefix.get("STA", [])):
        rep.error(target, "minimum valid path: no Target State (STA-### with type TARGET) defined")

    def need(prefix, fields, target_prefix, what):
        for ident, rec in by_prefix.get(prefix, []):
            linked = [i for i in field_ids(rec, *fields) if i.startswith(target_prefix + "-")]
            missing_marker = any(is_missing_marker(rec.get(f)) for f in fields)
            if not linked:
                if missing_marker:
                    rep.warn(defined[ident][1], "%s declares a missing %s link" % (ident, what))
                else:
                    rep.error(defined[ident][1], "%s has no %s link (%s)" % (ident, what, "/".join(fields)))

    need("OUT", ("metric_ids",), "MET", "Metric")
    need("CAP", ("outcome_ids",), "OUT", "Outcome")
    need("GAP", ("capability_id",), "CAP", "Capability")
    need("INT", ("gap_ids",), "GAP", "Gap")
    need("INI", ("intervention_ids",), "INT", "Intervention")
    need("INI", ("expected_outcome_ids",), "OUT", "Outcome")
    need("INI", ("success_metric_ids",), "MET", "Metric")
    need("STA", ("capability_id",), "CAP", "Capability")

    # Gate evidence: approved records need an approved gate Decision.
    decisions = by_prefix.get("DEC", [])

    def gate_decision(gate, subject):
        for ident, rec in decisions:
            if rec.get("gate") == gate and subject in ids_in(rec.get("subject_ids")):
                return ident, rec
        return None, None

    gated = (("OUT", ("approved",), "HG-OUTCOME"),
             ("INI", ("approved", "active", "completed"), "HG-INITIATIVE"),
             ("TOA", ("approved",), "HG-TOA"))
    for prefix, statuses, gate in gated:
        for ident, rec in by_prefix.get(prefix, []):
            if str(rec.get("status", "")).strip() in statuses:
                dec_id, dec = gate_decision(gate, ident)
                if not dec:
                    rep.error(defined[ident][1], "%s is %s but no Decision closes %s for it"
                              % (ident, rec.get("status"), gate))
                elif str(dec.get("status")).strip() != "approved":
                    rep.error(defined[dec_id][1], "%s closes %s for %s but is not approved"
                              % (dec_id, gate, ident))
    def level(value):
        m = re.match(r"^L([0-5])\b", str(value or "").strip())
        return int(m.group(1)) if m else 0

    for ident, rec in by_prefix.get("AUT", []):
        if max(level(rec.get("maximum_allowed_level")), level(rec.get("current_level"))) > 0:
            dec_id, dec = gate_decision("HG-AUTHORITY", ident)
            if not dec:
                rep.error(defined[ident][1], "%s grants AI authority above L0 but no Decision closes HG-AUTHORITY for it"
                          % ident)
            elif str(dec.get("status")).strip() != "approved":
                rep.warn(defined[dec_id][1], "%s (HG-AUTHORITY for %s) is not approved yet" % (dec_id, ident))
    for ident, rec in by_prefix.get("RSK", []):
        if str(rec.get("status", "")).strip() == "accepted":
            dec_ids = [i for i in ids_in(rec.get("acceptance_decision_id")) if i in defined]
            if not dec_ids:
                rep.error(defined[ident][1], "%s is accepted but acceptance_decision_id names no Decision" % ident)
            for dec_id in dec_ids:
                if str(defined[dec_id][0].get("status")).strip() != "approved":
                    rep.error(defined[ident][1], "%s is accepted by %s, which is not approved" % (ident, dec_id))
    for ident, rec in decisions:
        if rec.get("gate") and str(rec.get("status")).strip() == "approved" and not rec.get("approved_by"):
            rep.error(defined[ident][1], "%s approves %s without `approved_by`" % (ident, rec.get("gate")))
        if rec.get("gate") and rec.get("gate") not in gates:
            rep.error(defined[ident][1], "%s names unknown gate %s" % (ident, rec.get("gate")))

    return {"files": len(files), "records": len(defined),
            "prefixes": ", ".join("%s:%d" % (p, len(v)) for p, v in sorted(by_prefix.items()))}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--engagement", metavar="DIR", help="check an engagement workspace instead of the framework")
    parser.add_argument("--extra-prefixes", metavar="ABC,XYZ", default="",
                        help="ID prefixes registered by an Extension (engagement mode)")
    parser.add_argument("--strict", action="store_true", help="treat warnings as errors")
    parser.add_argument("--quiet", action="store_true", help="print only problems and the summary line")
    args = parser.parse_args(argv)

    rep = Report()
    if args.engagement:
        target = os.path.abspath(args.engagement)
        if not os.path.isdir(target):
            print("not a directory: %s" % args.engagement, file=sys.stderr)
            return 2
        extra = [p.strip() for p in args.extra_prefixes.split(",") if p.strip()]
        stats = run_engagement(target, rep, extra)
        label = "engagement %s" % rel(target, os.getcwd())
    else:
        stats = run_framework(rep)
        label = "AITM-SMB framework"

    for w in rep.warnings:
        print("warning: " + w)
    for e in rep.errors:
        print("error: " + e)
    summary = ", ".join("%s=%s" % kv for kv in stats.items())
    failed = bool(rep.errors) or (args.strict and bool(rep.warnings))
    print("%s %s — %s; %d error(s), %d warning(s)" % (
        "FAIL" if failed else "PASS", label, summary, len(rep.errors), len(rep.warnings)))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
