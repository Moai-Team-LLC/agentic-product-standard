#!/usr/bin/env python3
"""aps — the canon tool for The Agentic Product Standard.

The enumerable facts of the standard (principles, the Autonomy × Oversight ladder, the
harness, the Definition of Done, the anti-patterns, the scorecard) live once, in canon/*.yaml.
Every document that repeats them carries a generated region, and CI fails if a region, a
generated file, or a count in prose drifts from the canon.

    python3 tools/aps.py validate             canon integrity: ids, numbering, cross-references
    python3 tools/aps.py render               rewrite generated regions and files from the canon
    python3 tools/aps.py check                validate + render --check + prose lint (what CI runs)
    python3 tools/aps.py skills validate      Agent Skills spec rules + hidden-content scan
    python3 tools/aps.py skills lock          rewrite skills-lock.json
    python3 tools/aps.py skills verify DIR    compare an installed skills dir against the lock
    python3 tools/aps.py conformance FILE     score a product's aps-conformance.yaml (see --help)
    python3 tools/aps.py template             print a blank aps-conformance.yaml

Requires Python 3.9+ and PyYAML (`pip install pyyaml`). `jsonschema`, when installed, adds
JSON Schema validation of the canon and of conformance files.
"""

from __future__ import annotations

import argparse
import ast
import functools
import itertools
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANON_DIR = ROOT / "canon"
SCHEMA_DIR = CANON_DIR / "schema"

sys.path.insert(0, str(Path(__file__).resolve().parent))


def _yaml():
    try:
        import yaml  # type: ignore
    except ImportError:  # pragma: no cover - environment guard
        sys.exit("aps: PyYAML is required — pip install pyyaml")
    return yaml


def load_yaml(path: Path):
    with open(path, encoding="utf-8") as fh:
        return _yaml().safe_load(fh)


# ---------------------------------------------------------------------------------------
# Conditions: a tiny, safe expression language over a product profile.
#   flags: multi_tenant mcp multi_agent cross_boundary llm_judge retrieval regulated fleet
#          multi_provider      ints: autonomy (0–4)  oversight (0–2)
#   e.g.   "multi_agent and oversight >= 1"      "autonomy >= 3 or oversight >= 1"
# ---------------------------------------------------------------------------------------

FLAGS = (
    "multi_tenant", "mcp", "multi_agent", "cross_boundary", "llm_judge",
    "retrieval", "regulated", "fleet", "multi_provider",
)
NUMERIC = ("autonomy", "oversight")

CONDITION_LABELS = {
    "multi_tenant": "if multi-tenant",
    "mcp": "if MCP",
    "multi_agent": "if multi-agent",
    "cross_boundary": "if delegating across a trust boundary",
    "llm_judge": "if LLM judges",
    "retrieval": "if memory/retrieval",
    "regulated": "if regulated",
    "fleet": "if running a fleet",
    "multi_provider": "if multi-provider",
    "oversight >= 1": "O1+",
    "oversight >= 2": "O2",
    "autonomy >= 3 or oversight >= 1": "L3+ or O1+",
    "multi_agent and oversight >= 1": "multi-agent, O1+",
    "multi_provider and multi_tenant": "multi-provider, multi-tenant",
}


class ConditionError(ValueError):
    pass


def parse_condition(expr: str):
    if not isinstance(expr, str):  # checked before the cache, which would choke on a list
        raise ConditionError(f"a condition must be a string, got {expr!r} (quote it in YAML)")
    return _parse_condition(expr)


@functools.lru_cache(maxsize=None)
def _parse_condition(expr: str):
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as exc:
        raise ConditionError(f"unparseable condition {expr!r}: {exc}") from None
    _check_node(tree.body, expr)
    return tree


def _check_node(node, expr):
    if isinstance(node, ast.BoolOp) and isinstance(node.op, (ast.And, ast.Or)):
        for v in node.values:
            _check_node(v, expr)
    elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        _check_node(node.operand, expr)
    elif isinstance(node, ast.Compare):
        _check_node(node.left, expr)
        for op in node.ops:
            if not isinstance(op, (ast.GtE, ast.LtE, ast.Gt, ast.Lt, ast.Eq, ast.NotEq)):
                raise ConditionError(f"operator not allowed in {expr!r}")
        for c in node.comparators:
            _check_node(c, expr)
    elif isinstance(node, ast.Name):
        if node.id not in FLAGS + NUMERIC:
            raise ConditionError(f"unknown name {node.id!r} in {expr!r}")
    elif isinstance(node, ast.Constant):
        if not isinstance(node.value, (bool, int)):
            raise ConditionError(f"only int/bool constants allowed in {expr!r}")
    else:
        raise ConditionError(f"construct {type(node).__name__} not allowed in {expr!r}")


def eval_condition(expr: str | None, profile: dict) -> bool:
    if expr is None:
        return True
    tree = parse_condition(expr)

    def ev(node):
        if isinstance(node, ast.BoolOp):
            vals = [ev(v) for v in node.values]
            return all(vals) if isinstance(node.op, ast.And) else any(vals)
        if isinstance(node, ast.UnaryOp):
            return not ev(node.operand)
        if isinstance(node, ast.Compare):
            left = ev(node.left)
            for op, comp in zip(node.ops, node.comparators):
                right = ev(comp)
                ok = {
                    ast.GtE: left >= right, ast.LtE: left <= right, ast.Gt: left > right,
                    ast.Lt: left < right, ast.Eq: left == right, ast.NotEq: left != right,
                }[type(op)]
                if not ok:
                    return False
                left = right
            return True
        if isinstance(node, ast.Name):
            return profile[node.id]
        if isinstance(node, ast.Constant):
            return node.value
        raise ConditionError("unreachable")

    return bool(ev(tree.body))


def _names(expr: str) -> set[str]:
    return {n.id for n in ast.walk(parse_condition(expr)) if isinstance(n, ast.Name)}


def implies(a: str | None, b: str | None) -> bool:
    """True when every profile that satisfies `a` also satisfies `b` (exhaustive over the names they use)."""
    if b is None:
        return True
    names = sorted(_names(b) | (_names(a) if a else set()))
    domains = [range(5) if n == "autonomy" else range(3) if n == "oversight" else (False, True) for n in names]
    for values in itertools.product(*domains):
        prof = dict(zip(names, values))
        if eval_condition(a, prof) and not eval_condition(b, prof):
            return False
    return True


def condition_label(expr: str | None) -> str | None:
    if expr is None:
        return None
    return CONDITION_LABELS.get(expr, expr)


# ---------------------------------------------------------------------------------------
# The canon
# ---------------------------------------------------------------------------------------

BANDS = ("M0", "M1", "M2", "M3")


class Canon:
    def __init__(self, root: Path = ROOT):
        self.root = root
        d = root / "canon"
        self.meta = load_yaml(d / "meta.yaml")
        self.principles = load_yaml(d / "principles.yaml")["principles"]
        self.ladder = load_yaml(d / "ladder.yaml")
        self.patterns = load_yaml(d / "patterns.yaml")
        self.harness = load_yaml(d / "harness.yaml")
        self.checklist = load_yaml(d / "checklist.yaml")
        dod = load_yaml(d / "dod.yaml")
        self.dod_groups = dod["groups"]
        self.dod = dod["items"]
        self.antipatterns = load_yaml(d / "antipatterns.yaml")["antipatterns"]
        self.scorecard = load_yaml(d / "scorecard.yaml")
        self.regulatory = load_yaml(d / "regulatory.yaml")["frameworks"]

    # -- convenience -------------------------------------------------------------------
    @property
    def version(self) -> str:
        return str(self.meta["version"])

    @property
    def prerelease(self) -> bool:
        return "-" in self.version

    def dod_by_n(self) -> dict:
        return {i["n"]: i for i in self.dod}

    def dod_in_group(self, key: str) -> list:
        return sorted((i for i in self.dod if i["group"] == key), key=lambda i: i["n"])

    def scorecard_items(self):
        for sec in self.scorecard["sections"]:
            for item in sec["items"]:
                yield sec, item

    def dod_band(self, n: int) -> str | None:
        bands = [it["band"] for _, it in self.scorecard_items() if n in it.get("dod", [])]
        return min(bands, key=BANDS.index) if bands else None

    def sub_skills(self) -> list[str]:
        base = self.root / "skills" / "agentic-product-architect"
        return sorted(p.parent.name for p in base.glob("*/SKILL.md"))

    def counts(self) -> dict:
        return {
            "principles": len(self.principles),
            "layers": len(self.harness["layers"]),
            "dod": len(self.dod),
            "antipatterns": len(self.antipatterns),
            "sub_skills": len(self.sub_skills()),
            "patterns": len(self.patterns["patterns"]),
        }


# ---------------------------------------------------------------------------------------
# validate
# ---------------------------------------------------------------------------------------

LINK_RE = re.compile(r"\]\(@/([^)#\s]+)(#[^)]*)?\)")
SCORECARD_ID_RE = re.compile(r"^[a-z]+\.[a-z0-9]+(?:-[a-z0-9]+)*$")
KEY_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def _contiguous(ns: list[int], what: str, errors: list[str]):
    if sorted(ns) != list(range(1, len(ns) + 1)):
        errors.append(f"{what}: numbers must be exactly 1..{len(ns)} with no gaps or repeats — got {sorted(ns)}")


def _walk_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _walk_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _walk_strings(v)


def validate(c: Canon) -> list[str]:
    errors: list[str] = []

    # meta
    if not re.match(r"^\d+\.\d+\.\d+(-[0-9A-Za-z.]+)?$", c.version):
        errors.append(f"meta.version {c.version!r} is not SemVer")
    major_minor = ".".join(c.version.split("-")[0].split(".")[:2])
    if c.meta.get("version_label") != f"v{major_minor}":
        errors.append(f"meta.version_label must be v{major_minor}")

    _contiguous([p["n"] for p in c.principles], "principles", errors)
    _contiguous([p["n"] for p in c.patterns["patterns"]], "patterns", errors)
    _contiguous([layer["n"] for layer in c.harness["layers"]], "harness.layers", errors)
    _contiguous([s["n"] for s in c.harness["stack"]], "harness.stack", errors)
    layer_ns = {layer["n"] for layer in c.harness["layers"]}
    for s in c.harness["stack"]:
        for h in s.get("harness", []):
            if h not in layer_ns:
                errors.append(f"stack {s['n']} maps to unknown harness layer {h}")

    if [lv["id"] for lv in c.ladder["autonomy"]["levels"]] != [f"L{i}" for i in range(5)]:
        errors.append("ladder.autonomy.levels must be L0..L4 in order")
    if [m["id"] for m in c.ladder["oversight"]["modes"]] != ["O0", "O1", "O2"]:
        errors.append("ladder.oversight.modes must be O0..O2 in order")

    if len(c.checklist["core"]) != 10:
        errors.append(f"checklist.core must hold exactly 10 questions (CI checks the decision tree against them) — has {len(c.checklist['core'])}")

    # dod
    group_keys = [g["key"] for g in c.dod_groups]
    if len(set(group_keys)) != len(group_keys):
        errors.append("dod.groups: duplicate keys")
    _contiguous([i["n"] for i in c.dod], "dod.items", errors)
    seen_keys = set()
    for i in c.dod:
        where = f"dod {i.get('n')}"
        for f in ("key", "group", "title", "text", "since", "audit", "crosswalk"):
            if f not in i:
                errors.append(f"{where}: missing '{f}'")
        if i.get("key") in seen_keys or not KEY_RE.match(str(i.get("key", ""))):
            errors.append(f"{where}: key {i.get('key')!r} missing, duplicate, or not kebab-case")
        seen_keys.add(i.get("key"))
        if i.get("group") not in group_keys:
            errors.append(f"{where}: unknown group {i.get('group')!r}")
        audit = i.get("audit") or {}
        if not audit.get("checks") or not audit.get("why") or not audit.get("gap"):
            errors.append(f"{where}: audit needs checks, why, and gap")
        if "applies_if" in i:
            if not i.get("binds") or not i.get("binds_short"):
                errors.append(f"{where}: a conditional item needs 'binds' and 'binds_short'")
            try:
                parse_condition(i["applies_if"])
            except ConditionError as exc:
                errors.append(f"{where}: {exc}")
        for fw, ids in (i.get("crosswalk") or {}).items():
            if fw not in c.regulatory:
                errors.append(f"{where}: crosswalk framework {fw!r} not in canon/regulatory.yaml")
                continue
            known = {str(e["id"]) for e in c.regulatory[fw]["entries"]}
            for x in ids:
                if str(x) not in known:
                    errors.append(f"{where}: crosswalk {fw} entry {x!r} not in canon/regulatory.yaml")
    for g in group_keys:
        if not c.dod_in_group(g):
            errors.append(f"dod group {g!r} has no items")

    # anti-patterns
    _contiguous([a["n"] for a in c.antipatterns], "antipatterns", errors)
    for a in c.antipatterns:
        for f in ("title", "summary", "signal", "failure_mode", "fix", "severity", "since"):
            if not a.get(f):
                errors.append(f"antipattern {a.get('n')}: missing '{f}'")

    # scorecard
    if [b["id"] for b in c.scorecard["bands"]] != list(BANDS):
        errors.append("scorecard.bands must be M0..M3 in order")
    ids = set()
    dod_ns = {i["n"] for i in c.dod}
    covered = set()
    for sec, item in c.scorecard_items():
        iid = item.get("id", "")
        if not SCORECARD_ID_RE.match(iid) or iid in ids:
            errors.append(f"scorecard item {iid!r}: id must be unique and look like 'section.slug'")
        ids.add(iid)
        if item.get("band") not in BANDS[1:]:
            errors.append(f"scorecard item {iid}: band must be M1, M2 or M3")
        for n in item.get("dod", []):
            if n not in dod_ns:
                errors.append(f"scorecard item {iid}: references unknown DoD item {n}")
            covered.add(n)
        conds_ok = True
        for cond in (item.get("applies_if"), sec.get("applies_if")):
            if cond is None:
                continue
            try:
                parse_condition(cond)
            except ConditionError as exc:
                errors.append(f"scorecard item {iid}: {exc}")
                conds_ok = False
                continue
            if cond not in CONDITION_LABELS:
                errors.append(f"scorecard item {iid}: condition {cond!r} has no label in CONDITION_LABELS")
        # a section's condition is display-only; the item's own condition is what scoring uses,
        # so it must be at least as narrow — or the item would bind products the section excludes
        if conds_ok and not implies(item.get("applies_if"), sec.get("applies_if")):
            errors.append(f"scorecard item {iid}: its applies_if does not imply its section's "
                          f"({sec.get('applies_if')!r}) — the item would bind products the section excludes")
    for n in sorted(dod_ns - covered):
        errors.append(f"DoD item {n} is not evidenced by any scorecard item — add one to canon/scorecard.yaml")
    for rule in c.scorecard["envelope_rules"]:
        if rule.get("when") != "True":
            try:
                parse_condition(rule.get("when"))
            except ConditionError as exc:
                errors.append(f"scorecard.envelope_rules: {exc}")
        if rule.get("requires") not in BANDS:
            errors.append(f"scorecard.envelope_rules: unknown band {rule.get('requires')!r}")

    # SARIF: GitHub keeps 10 tags per rule and rejects a rule with more than 20 — fail here, not there
    import aps_conformance as K
    for _, item in c.scorecard_items():
        if item.get("id") and all(n in dod_ns for n in item.get("dod", [])):
            tags = K.sarif_tags(c, item)
            if len(tags) > K.MAX_TAGS:
                errors.append(f"scorecard item {item['id']}: {len(tags)} SARIF tags (max {K.MAX_TAGS}) — "
                              f"split the item or trim TAG_FRAMEWORKS")

    # links (@/path) resolve — to a file in the repo or one the canon generates
    import aps_render as R
    generated = set(R.FILES)
    for name in ("dod", "antipatterns", "scorecard"):
        for s in _walk_strings(getattr(c, name)):
            for m in LINK_RE.finditer(s):
                if not (c.root / m.group(1)).exists() and m.group(1) not in generated:
                    errors.append(f"{name}: link target @/{m.group(1)} does not exist")

    errors.extend(_validate_schemas(c))
    return errors


def _validate_schemas(c: Canon) -> list[str]:
    try:
        import jsonschema  # type: ignore
    except ImportError:
        return []
    pairs = [("dod.schema.json", "dod.yaml"), ("antipatterns.schema.json", "antipatterns.yaml"),
             ("scorecard.schema.json", "scorecard.yaml")]
    errs = []
    for schema_name, doc_name in pairs:
        schema_path = c.root / "canon" / "schema" / schema_name
        if not schema_path.exists():
            continue
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        doc = load_yaml(c.root / "canon" / doc_name)
        cls = getattr(jsonschema, "Draft202012Validator", None)
        if cls is None:  # jsonschema < 4: optional dependency, too old to use
            return []
        validator = cls(schema)
        for e in sorted(validator.iter_errors(doc), key=lambda e: list(e.path)):
            loc = "/".join(str(p) for p in e.path)
            errs.append(f"canon/{doc_name}: schema: {loc}: {e.message}")
    return errs


# ---------------------------------------------------------------------------------------
# render / check
# ---------------------------------------------------------------------------------------

REGION_RE = re.compile(
    r"(<!-- canon:begin:(?P<name>[a-z0-9.\-]+) -->\n)(?P<body>.*?)(<!-- canon:end:(?P=name) -->)",
    re.S,
)


def marker_problem(path: str, text: str) -> str | None:
    """A region marker must appear exactly once per name, and no region may swallow another's begin.

    A marker quoted as an example (in a code fence, say) would otherwise become a region, and
    `render` would silently replace the prose between it and the real end marker.
    """
    for kind in ("begin", "end"):
        names = re.findall(rf"<!-- canon:{kind}:([a-z0-9.\-]+) -->", text)
        dupes = sorted({n for n in names if names.count(n) > 1})
        if dupes:
            return (f"{path} has more than one canon:{kind} marker for {', '.join(dupes)} — alter a marker shown "
                    f"as an example (e.g. canon:begin:NAME) or it becomes a region")
    for m in REGION_RE.finditer(text):
        if "<!-- canon:begin:" in m.group("body"):
            return f"{path}: region {m.group('name')!r} contains another begin marker — an unterminated region?"
    return None


def relink(text: str, target: str) -> str:
    """Rewrite `](@/path)` links to be relative to the directory of `target` (repo path)."""
    base = os.path.dirname(target) or "."

    def sub(m):
        rel = os.path.relpath(m.group(1), base)
        return f"]({rel}{m.group(2) or ''})"

    return LINK_RE.sub(sub, text)


def render_all(c: Canon) -> dict[str, str]:
    """Return {repo path: new full content} for every file the canon owns (regions + files)."""
    import aps_render as R
    import aps_skills as S

    out: dict[str, str] = {}
    for path, regions in R.REGIONS.items():
        full = c.root / path
        text = full.read_text(encoding="utf-8")
        problem = marker_problem(path, text)
        if problem:
            raise SystemExit(f"aps: {problem}")
        found = {m.group("name") for m in REGION_RE.finditer(text)}
        missing = set(regions) - found
        unknown = found - set(regions)
        if missing:
            raise SystemExit(f"aps: {path} is missing generated region(s): {', '.join(sorted(missing))}")
        if unknown:
            raise SystemExit(f"aps: {path} has unknown region(s): {', '.join(sorted(unknown))}")

        def sub(m, path=path, regions=regions):
            body = regions[m.group("name")](c, path)
            body = relink(body.rstrip("\n") + "\n\n", path)  # blank line: tables end cleanly
            return m.group(1) + body + m.group(4)

        out[path] = REGION_RE.sub(sub, text)
    # the bundled copy of AGENT_STANDARD.md is byte-identical to the root copy
    out["skills/agent-builder/AGENT_STANDARD.md"] = out["AGENT_STANDARD.md"]
    for path, fn in R.FILES.items():
        out[path] = relink(fn(c, path), path)
    # the lock hashes the skills as they will be written
    out[S.LOCK_PATH] = S.render_lock(c, overrides=out)
    return out


def cmd_render(c: Canon, check: bool) -> int:
    outputs = render_all(c)
    drift = []
    for path, content in outputs.items():
        full = c.root / path
        current = full.read_text(encoding="utf-8") if full.exists() else None
        if current != content:
            drift.append(path)
            if not check:
                full.parent.mkdir(parents=True, exist_ok=True)
                full.write_text(content, encoding="utf-8")
    if check:
        for p in drift:
            print(f"::error file={p}::{p} is out of date with canon/ — run: python3 tools/aps.py render")
        return 1 if drift else 0
    for p in drift:
        print(f"rendered {p}")
    if not drift:
        print("everything already matches the canon")
    return 0


# Prose lint: counts written in free text must match the canon. History (CHANGELOG, ADRs,
# advisories, case studies of record) is exempt; a line can opt out with canon:lint-ignore.
LINT_SKIP = ("CHANGELOG.md", "docs/adr/", "docs/advisories/", "examples/", "family/")
WORDS = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
    "fifteen sixteen seventeen eighteen nineteen twenty".split())}
_N = r"\b(\d+|" + "|".join(WORDS) + r")\b"
# (pattern, canon count, noun) — every number group is word-bounded, so "often" is not "ten"
LINT_RULES = [
    (_N + r"[- ]layer (?:harness|scaffolding|model|stack)", "layers", "harness layers"),
    (r"harness (?:has|contains|of) " + _N + r" layers", "layers", "harness layers"),
    (_N + r" harness layers", "layers", "harness layers"),
    (r"\bthe " + _N + r" layers around", "layers", "harness layers"),
    (r"\beach of the " + _N + r" layers", "layers", "harness layers"),
    (r"\(" + _N + r" layers\)", "layers", "harness layers"),
    (_N + r" layers, of which", "layers", "harness layers"),
    (_N + r"-point (?:Definition of Done|DoD)", "dod", "Definition of Done items"),
    (_N + r"-item (?:Definition of Done|DoD)", "dod", "Definition of Done items"),
    (_N + r" (?:Definition of Done|DoD) items", "dod", "Definition of Done items"),
    (_N + r" (?:canonical |known )?anti-?patterns", "antipatterns", "anti-patterns"),
    (r"through " + _N + r" known failure modes", "antipatterns", "anti-patterns"),
    (_N + r" principles\b", "principles", "principles"),
    (r"(?<![–\-\d])" + _N + r" (?:specialized )?sub-skills\b", "sub_skills", "architect sub-skills"),
]
LINT_RULES = [(re.compile(rx, re.I), key, what) for rx, key, what in LINT_RULES]
# "the first two principles", "these three anti-patterns": a subset, not a count of the whole
_SUBSET_WORDS = {"first", "last", "these", "those", "both", "top", "other", "remaining", "next", "previous"}


def _num(tok: str) -> int | None:
    tok = tok.lower()
    if tok.isdigit():
        return int(tok)
    return WORDS.get(tok)


def lint_text(counts: dict, rel: str, text: str) -> list[str]:
    """Counts stated in one document that disagree with the canon."""
    problems = []
    for lineno, raw in enumerate(text.splitlines(), 1):
        if "canon:lint-ignore" in raw:
            continue
        line = re.sub(r"[*_]", "", raw)  # **eight** harness layers → eight harness layers
        for rx, key, what in LINT_RULES:
            for m in rx.finditer(line):
                n = _num(m.group(1))
                if n is None or n == counts[key] or n >= 1000:  # 1000+: a year ("the 2026 anti-patterns")
                    continue
                before = line[: m.start()].split()
                if before and before[-1].lower() in _SUBSET_WORDS:
                    continue
                problems.append(f"{rel}:{lineno}: says {m.group(0)!r} but the canon has {counts[key]} {what}")
    return problems


def repo_files(root: Path, pattern: str = "*") -> list[Path]:
    """Files git would commit (tracked + untracked, minus ignored); a plain walk outside a git checkout."""
    try:
        out = subprocess.run(["git", "-C", str(root), "ls-files", "-z", "--cached", "--others",
                              "--exclude-standard", "--", pattern],
                             capture_output=True, check=True).stdout
        return sorted(root / p for p in out.decode("utf-8", "replace").split("\0") if p and (root / p).is_file())
    except (OSError, subprocess.CalledProcessError):
        walk = root.rglob(pattern) if any(ch in pattern for ch in "*?[") else (root / pattern).rglob("*")
        return sorted(p for p in walk
                      if p.is_file() and not ({".git", "node_modules"} & set(p.relative_to(root).parts)))


def lint_prose(c: Canon) -> list[str]:
    counts = c.counts()
    problems = []
    for path in repo_files(c.root, "*.md"):
        rel = path.relative_to(c.root).as_posix()
        if "node_modules/" in rel or any(rel.startswith(s) or rel == s for s in LINT_SKIP):
            continue
        problems += lint_text(counts, rel, path.read_text(encoding="utf-8", errors="replace"))
    # every architect sub-skill is routed by the master skill and listed in the README tree
    master = (c.root / "skills/agentic-product-architect/SKILL.md").read_text(encoding="utf-8")
    readme = (c.root / "README.md").read_text(encoding="utf-8")
    for name in c.sub_skills():
        if f"{name}/" not in master:
            problems.append(f"skills/agentic-product-architect/SKILL.md: sub-skill {name!r} is not routed or indexed")
        if f"{name}/" not in readme:
            problems.append(f"README.md: sub-skill {name!r} missing from the repo tree")
    return problems


def cmd_check(c: Canon) -> int:
    rc = 0
    errs = validate(c)
    for e in errs:
        print(f"::error::canon: {e}")
    rc |= 1 if errs else 0
    if errs:
        return rc  # rendering from an invalid canon is meaningless
    rc |= cmd_render(c, check=True)
    for p in lint_prose(c):
        print(f"::error::prose drift: {p}")
        rc |= 1
    import aps_skills as S
    rc |= S.cmd_validate(c, quiet=True)
    if rc == 0:
        n = c.counts()
        print(f"canon OK — v{c.version}: {n['principles']} principles · {n['layers']} harness layers · "
              f"{n['dod']} DoD items · {n['antipatterns']} anti-patterns · "
              f"{sum(1 for _ in c.scorecard_items())} scorecard items")
    return rc


# ---------------------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="aps", description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate", help="check canon integrity")
    r = sub.add_parser("render", help="rewrite generated regions and files")
    r.add_argument("--check", action="store_true", help="fail instead of writing when out of date")
    sub.add_parser("check", help="validate + render --check + prose lint (CI)")
    sk = sub.add_parser("skills", help="skills: validate | lock | verify DIR")
    sk.add_argument("action", choices=("validate", "lock", "verify"))
    sk.add_argument("dir", nargs="?", help="installed skills directory (verify)")
    sk.add_argument("--lock", default=None, help="lock file to verify against (default: repo skills-lock.json)")
    cf = sub.add_parser("conformance", help="score a product's aps-conformance.yaml")
    cf.add_argument("file")
    cf.add_argument("--sarif", help="write SARIF 2.1.0 here")
    cf.add_argument("--json", dest="json_out", help="write the machine-readable report here")
    cf.add_argument("--badge", help="write a shields.io endpoint JSON here")
    cf.add_argument("--summary", help="write a Markdown summary here (e.g. $GITHUB_STEP_SUMMARY)")
    cf.add_argument("--root", default=".", help="repo root that relative evidence paths resolve against")
    cf.add_argument("--allow-unevidenced", action="store_true",
                    help="count a `yes` without evidence as yes (default: it counts as no)")
    cf.add_argument("--fail-under", choices=BANDS, default=None,
                    help="exit non-zero if the achieved band is below this (default: the band the declared operating point requires)")
    cf.add_argument("--require-dod", action="store_true",
                    help="also exit non-zero while any binding Definition of Done item is open (production-ready gate)")
    sub.add_parser("template", help="print a blank aps-conformance.yaml for this version")
    args = ap.parse_args(argv)

    c = Canon()
    if args.cmd == "validate":
        errs = validate(c)
        for e in errs:
            print(f"::error::canon: {e}")
        if not errs:
            print("canon valid")
        return 1 if errs else 0
    if args.cmd == "render":
        errs = validate(c)
        if errs:
            for e in errs:
                print(f"::error::canon: {e}")
            return 1
        return cmd_render(c, check=args.check)
    if args.cmd == "check":
        return cmd_check(c)
    if args.cmd == "skills":
        import aps_skills as S
        if args.action == "validate":
            return S.cmd_validate(c)
        if args.action == "lock":
            return S.cmd_lock(c)
        return S.cmd_verify(c, args.dir, args.lock)
    if args.cmd == "conformance":
        import aps_conformance as K
        return K.cmd_conformance(c, args)
    if args.cmd == "template":
        import aps_render as R
        sys.stdout.write(R.render_conformance_template(c, "aps-conformance.yaml"))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
