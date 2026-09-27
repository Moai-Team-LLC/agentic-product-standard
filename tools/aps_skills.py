"""Skills: the instruction supply chain (STANDARD.md Part IV) applied to this repo's own skills.

validate  every SKILL.md against the Agent Skills specification (https://agentskills.io/specification)
          plus a hidden-content scan of every file a skill ships
lock      skills-lock.json — a SHA-256 per file and per skill, so a change to what an agent
          loads is a visible diff, and an installed copy can be checked against a release
verify    compare an installed skills directory against the lock
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

LOCK_PATH = "skills-lock.json"

# Agent Skills specification — frontmatter rules.
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
MAX_BODY_LINES = 500          # "Keep your main SKILL.md under 500 lines."
MAX_BODY_TOKENS = 5000        # "Instructions (< 5000 tokens recommended)" — estimated at 4 chars/token

# Hidden-content scan: characters that render as nothing (or reorder text) but reach the model.
HIDDEN = re.compile(
    "[​-‏‪-‮⁠-⁤⁦-⁩﻿]|[\U000e0000-\U000e007f]"
)
HTML_COMMENT = re.compile(r"<!--(.*?)-->", re.S)
CANON_MARKER = re.compile(r"^\s*(canon:(begin|end):[a-z0-9.\-]+|Generated from canon/ by tools/aps\.py[^<>]*)\s*$")
PIPE_TO_SHELL = re.compile(r"\b(curl|wget)\b[^\n|]*\|\s*(ba|z)?sh\b")
BLOB = re.compile(r"[A-Za-z0-9+/=]{200,}")
TEXT_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".ts", ".py", ".js", ".sh", ""}


def skill_dirs(root: Path) -> list[Path]:
    return sorted(p.parent for p in (root / "skills").rglob("SKILL.md"))


IGNORED_NAMES = {".DS_Store", "Thumbs.db"}
IGNORED_DIRS = {"__pycache__", ".git", "node_modules"}


def owned_files(skill_dir: Path, all_skill_dirs: list[Path]) -> list[Path]:
    """Files that belong to this skill: everything under it except nested skills and local cruft."""
    nested = [d for d in all_skill_dirs if d != skill_dir and skill_dir in d.parents]
    out = []
    for f in sorted(skill_dir.rglob("*")):
        if not f.is_file() or f.name in IGNORED_NAMES or f.suffix == ".pyc":
            continue
        if any(part in IGNORED_DIRS for part in f.relative_to(skill_dir).parts):
            continue
        if not any(n == f.parent or n in f.parents for n in nested):
            out.append(f)
    return out


def split_frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return None, text
    return m.group(1), m.group(2)


def validate_skill(skill_dir: Path, all_dirs: list[Path]):
    import yaml  # type: ignore

    errors, warnings = [], []
    path = skill_dir / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    fm_text, body = split_frontmatter(text)
    if fm_text is None:
        return [f"{path}: missing YAML frontmatter"], []
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as exc:
        return [f"{path}: frontmatter is not valid YAML: {exc}"], []
    name = fm.get("name")
    if not isinstance(name, str) or not (1 <= len(name) <= 64) or not NAME_RE.match(name):
        errors.append(f"{path}: name must be 1–64 chars of a-z, 0-9 and single hyphens (got {name!r})")
    elif name != skill_dir.name:
        errors.append(f"{path}: name {name!r} must match its directory {skill_dir.name!r}")
    desc = fm.get("description")
    if not isinstance(desc, str) or not (1 <= len(desc) <= 1024):
        errors.append(f"{path}: description must be 1–1024 characters (got {len(desc) if isinstance(desc, str) else desc!r})")
    unknown = set(fm) - SPEC_FIELDS
    if unknown:
        errors.append(f"{path}: fields not in the Agent Skills spec: {', '.join(sorted(unknown))}")
    comp = fm.get("compatibility")
    if comp is not None and (not isinstance(comp, str) or not (1 <= len(comp) <= 500)):
        errors.append(f"{path}: compatibility must be a 1–500 character string")
    meta = fm.get("metadata")
    if meta is not None and (not isinstance(meta, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in meta.items())):
        errors.append(f"{path}: metadata must map string keys to string values")
    lines = body.count("\n")
    if lines > MAX_BODY_LINES:
        warnings.append(f"{path}: body is {lines} lines (spec recommends < {MAX_BODY_LINES}; move detail to a referenced file)")
    if len(body) // 4 > MAX_BODY_TOKENS:
        warnings.append(f"{path}: body is ~{len(body) // 4} tokens (spec recommends < {MAX_BODY_TOKENS})")

    for f in owned_files(skill_dir, all_dirs):
        if f.suffix not in TEXT_SUFFIXES:
            continue
        content = f.read_text(encoding="utf-8", errors="replace")
        for lineno, line in enumerate(content.splitlines(), 1):
            if HIDDEN.search(line):
                errors.append(f"{f}:{lineno}: invisible or bidi-control character — hidden text reaches the model")
            if PIPE_TO_SHELL.search(line):
                warnings.append(f"{f}:{lineno}: pipes a download into a shell")
            if BLOB.search(line):
                warnings.append(f"{f}:{lineno}: long encoded blob — review what it decodes to")
        if f.suffix == ".md":
            for m in HTML_COMMENT.finditer(content):
                if not CANON_MARKER.match(m.group(1)):
                    lineno = content[: m.start()].count("\n") + 1
                    warnings.append(f"{f}:{lineno}: HTML comment in skill content is invisible to reviewers but not to the model")
    return errors, warnings


def cmd_validate(c, quiet: bool = False) -> int:
    dirs = skill_dirs(c.root)
    n_err = 0
    for d in dirs:
        errors, warnings = validate_skill(d, dirs)
        for e in errors:
            print(f"::error::skills: {e}")
        if not quiet:
            for w in warnings:
                print(f"::warning::skills: {w}")
        n_err += len(errors)
    if not quiet and n_err == 0:
        print(f"skills OK — {len(dirs)} skills conform to the Agent Skills spec; no hidden content")
    return 1 if n_err else 0


def _sha(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def render_lock(c, overrides: dict | None = None) -> str:
    overrides = overrides or {}
    dirs = skill_dirs(c.root)
    skills = {}
    for d in dirs:
        files = {}
        for f in owned_files(d, dirs):
            rel_repo = f.relative_to(c.root).as_posix()
            data = overrides[rel_repo].encode("utf-8") if rel_repo in overrides else f.read_bytes()
            files[f.relative_to(d).as_posix()] = _sha(data)
        tree = "".join(f"{k}\0{v}\n" for k, v in sorted(files.items())).encode("utf-8")
        skills[d.relative_to(c.root / "skills").as_posix()] = {"digest": _sha(tree), "files": files}
    lock = {
        "standard": c.version,
        "spec": "https://agentskills.io/specification",
        "algorithm": "sha256",
        "note": "Generated by tools/aps.py. Verify an installed copy: python3 tools/aps.py skills verify <dir>",
        "skills": skills,
    }
    return json.dumps(lock, indent=2, ensure_ascii=False) + "\n"


def cmd_lock(c) -> int:
    out = render_lock(c)
    (c.root / LOCK_PATH).write_text(out, encoding="utf-8")
    print(f"wrote {LOCK_PATH}")
    return 0


def cmd_verify(c, target: str | None, lock_path: str | None) -> int:
    if not target:
        print("usage: aps.py skills verify <installed-skills-dir> [--lock skills-lock.json]")
        return 2
    lock = json.loads(Path(lock_path or c.root / LOCK_PATH).read_text(encoding="utf-8"))
    base = Path(target).expanduser()
    rc = 0
    checked = 0
    for name, entry in sorted(lock["skills"].items()):
        # installs flatten the tree differently: accept <dir>/<name> or <dir>/<last segment>
        candidates = [base / name, base / Path(name).name]
        sdir = next((p for p in candidates if (p / "SKILL.md").exists()), None)
        if sdir is None:
            continue
        checked += 1
        for rel, digest in entry["files"].items():
            f = sdir / rel
            if not f.exists():
                print(f"::error::{name}: missing {rel}")
                rc = 1
            elif _sha(f.read_bytes()) != digest:
                print(f"::error::{name}: {rel} differs from the locked content (standard {lock['standard']})")
                rc = 1
    if checked == 0:
        print(f"no locked skills found under {base}")
        return 1
    if rc == 0:
        print(f"verified {checked} installed skill(s) against {LOCK_PATH} (standard {lock['standard']})")
    return rc
