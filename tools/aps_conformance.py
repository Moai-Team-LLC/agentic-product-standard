"""aps-conformance: score a product's aps-conformance.yaml against the canon scorecard.

Output: the maturity band achieved, the band the declared operating point requires, whether
every binding Definition of Done item is evidenced (production-ready), and every failing
control — as a console report, JSON, SARIF 2.1.0 (for code scanning), a Markdown summary,
and a shields.io endpoint badge. Evidence-based by default: a `yes` without evidence
counts as `no`.

Exit codes: 0 the gate holds · 1 it does not (below the band, or --require-dod and a binding
DoD item open) · 2 the file could not be scored (malformed, wrong major version, I/O).
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from aps import BANDS, ConditionError, _yaml, eval_condition

LEVELS = {f"L{i}": i for i in range(5)}
MODES = {f"O{i}": i for i in range(3)}
FLAGS = ("multi_tenant", "mcp", "multi_agent", "cross_boundary", "llm_judge",
         "retrieval", "regulated", "fleet", "multi_provider")
BADGE_COLORS = {"M0": "red", "M1": "yellow", "M2": "green", "M3": "brightgreen"}
URL_RE = re.compile(r"^https?://[^/\s?#]+", re.I)   # a web URL with a host — not file://, not "x://"
STATUSES = ("yes", "no", "na")
ANSWER_KEYS = {"status", "evidence", "reason", "note"}
TOP_KEYS = {"standard", "product", "profile", "baselines", "regulatory", "items"}
# SARIF tags: GitHub keeps 10 per rule and rejects a file with more than 20, so tags carry the
# band, the DoD items and the three largest crosswalks; the full crosswalk rides in properties.
TAG_FRAMEWORKS = {"eu_ai_act": "EU-AI-Act-Art-", "owasp_asi": "", "nist_ai_rmf": "NIST-"}
MAX_TAGS = 10


class ConformanceError(ValueError):
    pass


def _band_index(b: str) -> int:
    return BANDS.index(b)


# ---------------------------------------------------------------------------------------
# Loading and structural validation — enforced in code, so the score never depends on
# whether the optional jsonschema package happens to be installed.
# ---------------------------------------------------------------------------------------

def load_conformance(path: Path):
    """YAML with duplicate keys refused: a later `sec.trifecta:` silently overriding an earlier one is a forgery."""
    yaml = _yaml()

    class Loader(yaml.SafeLoader):
        pass

    def mapping(loader, node, deep=False):
        seen = set()
        for key_node, _ in node.value:
            key = loader.construct_object(key_node, deep=deep)
            try:
                dup = key in seen
            except TypeError:
                raise ConformanceError(f"line {key_node.start_mark.line + 1}: unhashable mapping key") from None
            if dup:
                raise ConformanceError(f"line {key_node.start_mark.line + 1}: duplicate key {key!r}")
            seen.add(key)
        return loader.construct_mapping(node, deep=deep)

    Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    with open(path, encoding="utf-8") as fh:
        return yaml.load(fh, Loader=Loader)  # noqa: S506 — SafeLoader subclass


def structure_errors(doc) -> list[str]:
    errs = []
    if not isinstance(doc, dict):
        return ["the file must be a YAML mapping"]
    for k in sorted(set(map(str, doc)) - TOP_KEYS):
        errs.append(f"unknown top-level key {k!r}")
    for k in ("standard", "profile", "items"):
        if k not in doc:
            errs.append(f"missing required key {k!r}")
    if "standard" in doc and not isinstance(doc["standard"], str):
        errs.append("standard must be a quoted version string, e.g. \"4.0.0\"")
    for k in ("product", "baselines", "regulatory"):
        if k in doc and doc[k] is not None and not isinstance(doc[k], dict):
            errs.append(f"{k} must be a mapping")
    prod = doc.get("product")
    if isinstance(prod, dict):
        if prod.get("stage") not in (None, "prototype", "production"):
            errs.append("product.stage must be prototype or production")
        for k in ("name", "owner"):
            if k in prod and not isinstance(prod[k], str):
                errs.append(f"product.{k} must be a string")
    reg = doc.get("regulatory")
    if isinstance(reg, dict):
        if "jurisdictions" in reg and not (isinstance(reg["jurisdictions"], list)
                                           and all(isinstance(j, str) for j in reg["jurisdictions"])):
            errs.append("regulatory.jurisdictions must be a list of strings")
        if "eu_ai_act" in reg and reg["eu_ai_act"] is not None and not isinstance(reg["eu_ai_act"], dict):
            errs.append("regulatory.eu_ai_act must be a mapping")
    items = doc.get("items")
    if "items" in doc:
        if items is None:
            items = {}
        if not isinstance(items, dict):
            errs.append("items must be a mapping of scorecard id → answer")
        else:
            for iid, ans in items.items():
                if not isinstance(iid, str):
                    errs.append(f"items: key {iid!r} must be a scorecard id string")
                    continue
                if not isinstance(ans, dict):
                    errs.append(f"items.{iid}: must be a mapping like {{status: yes, evidence: path}}")
                    continue
                for k in sorted(set(map(str, ans)) - ANSWER_KEYS):
                    errs.append(f"items.{iid}: unknown key {k!r}")
                if ans.get("status") not in STATUSES:
                    errs.append(f"items.{iid}.status must be yes, no, or na (got {ans.get('status')!r})")
                for k in ("evidence", "reason", "note"):
                    if ans.get(k) is not None and not isinstance(ans[k], str):
                        errs.append(f"items.{iid}.{k} must be a string")
    return errs


def _schema_errors(c, doc) -> list[str]:
    try:
        import jsonschema  # type: ignore
    except ImportError:
        return []
    cls = getattr(jsonschema, "Draft202012Validator", None)
    path = c.root / "canon" / "schema" / "aps-conformance.schema.json"
    if cls is None or not path.exists():  # jsonschema < 4 is too old to use: the code checks still run
        return []
    schema = json.loads(path.read_text(encoding="utf-8"))
    try:
        doc = json.loads(json.dumps(doc, default=str))  # YAML dates → strings, as JSON Schema sees them
    except ValueError as exc:  # a recursive YAML alias
        raise ConformanceError(f"the file cannot be represented as JSON: {exc}") from None
    errors = [f"{'/'.join(str(p) for p in e.path) or '<root>'}: {e.message}" for e in cls(schema).iter_errors(doc)]
    return sorted(errors)


def evidence_exists(root: Path, ev: str) -> bool:
    """A web URL is taken as given; a path must name a file or directory inside the repo root.

    Not evidence: an empty path, a bare `#anchor`, the repo root itself, an absolute path, a path
    that escapes the root, or anything with a NUL byte.
    """
    if URL_RE.match(ev):
        return True
    rel = ev.split("#", 1)[0].strip()
    if not rel or "\0" in rel:
        return False
    try:
        p = Path(rel)
        if p.is_absolute():
            return False
        base = root.resolve()
        target = (base / p).resolve()
    except (OSError, ValueError):
        return False
    return base in target.parents and target.exists()


def normalize(doc: dict) -> dict:
    """YAML 1.1 (PyYAML) reads unquoted yes/no as booleans; accept both spellings."""
    items = doc.get("items")
    if isinstance(items, dict):
        for ans in items.values():
            if isinstance(ans, dict) and isinstance(ans.get("status"), bool):
                ans["status"] = "yes" if ans["status"] else "no"
    return doc


def parse_profile(doc: dict) -> dict:
    prof = doc.get("profile")
    if not isinstance(prof, dict):
        raise ConformanceError("missing `profile` mapping")
    out = {}
    try:
        out["autonomy"] = LEVELS[str(prof.get("autonomy"))]
        out["oversight"] = MODES[str(prof.get("oversight"))]
    except KeyError:
        raise ConformanceError("profile.autonomy must be L0–L4 and profile.oversight O0–O2") from None
    for f in FLAGS:
        v = prof.get(f)
        if not isinstance(v, bool):
            raise ConformanceError(f"profile.{f} must be true or false (absent is not false)")
        out[f] = v
    unknown = sorted(set(map(str, prof)) - set(FLAGS) - {"autonomy", "oversight"})
    if unknown:
        raise ConformanceError(f"profile: unknown key(s) {', '.join(unknown)}")
    return out


# ---------------------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------------------

def score(c, doc: dict, root: Path, allow_unevidenced: bool = False) -> dict:
    """Pure scoring: returns the full report dict. Raises ConformanceError on malformed input."""
    if isinstance(doc, dict):
        doc = normalize(doc)
    problems = structure_errors(doc)
    if problems:
        raise ConformanceError("; ".join(problems[:10]))
    schema_errors = _schema_errors(c, doc)
    if schema_errors:
        raise ConformanceError("schema: " + "; ".join(schema_errors[:10]))
    declared = str(doc.get("standard", ""))
    if declared.split(".")[0] != c.version.split(".")[0]:
        raise ConformanceError(
            f"file declares standard {declared!r} but this tool scores v{c.version} — use the matching action/tag")
    profile = parse_profile(doc)
    stage = (doc.get("product") or {}).get("stage", "production")
    answers = doc.get("items") or {}
    known = {it["id"] for _, it in c.scorecard_items()}
    notes = [f"unknown item id {k!r} ignored (from another version?)" for k in answers if k not in known]

    items = []
    for sec, it in c.scorecard_items():
        try:
            applies = eval_condition(it.get("applies_if"), profile)
        except ConditionError as exc:  # canon bug — surfaced, not swallowed
            raise ConformanceError(str(exc)) from None
        rec = {"id": it["id"], "band": it["band"], "section": sec["title"], "text": it["text"],
               "dod": it.get("dod", []), "applies": applies}
        if not applies:
            rec.update(status="na", reason="condition does not hold for this profile", auto=True, passed=True)
            items.append(rec)
            continue
        ans = answers.get(it["id"])
        if ans is None:
            rec.update(status="no", reason="unanswered", passed=False)
        else:
            st = ans["status"]
            ev = str(ans.get("evidence") or "").strip()
            rec["evidence"] = ev or None
            if st == "yes":
                if not ev:
                    rec.update(status="yes" if allow_unevidenced else "no",
                               reason="claimed without evidence", passed=allow_unevidenced)
                elif not evidence_exists(root, ev):
                    rec.update(status="no", reason=f"evidence not found in the repo: {ev}", passed=False)
                else:
                    rec.update(status="yes", reason=None, passed=True)
            elif st == "na":
                reason = str(ans.get("reason") or "").strip()
                if reason:
                    rec.update(status="na", reason=reason, passed=True)
                else:
                    rec.update(status="no", reason="N/A without a reason", passed=False)
            else:
                rec.update(status="no", reason="answered no", passed=False)
        items.append(rec)

    achieved = "M0"
    for band in BANDS[1:]:
        gate = [r for r in items if _band_index(r["band"]) <= _band_index(band)]
        if all(r["passed"] for r in gate):
            achieved = band
        else:
            break

    required = "M0"
    if stage != "prototype":
        for rule in c.scorecard["envelope_rules"]:
            if rule["when"] == "True" or eval_condition(rule["when"], profile):
                required = rule["requires"]
                break

    by_n = c.dod_by_n()
    dod = []
    for n in sorted(by_n):
        d = by_n[n]
        applies = eval_condition(d.get("applies_if"), profile)
        mapped = [r for r in items if n in r["dod"] and r["applies"]]
        if not applies or not mapped:
            status, declared_na = "n/a", False
        elif not all(r["passed"] for r in mapped):
            status, declared_na = "fail", False
        elif all(r["status"] == "na" for r in mapped):
            # every control that evidences it was declared N/A by the product, not proven
            status, declared_na = "n/a", True
        else:
            status, declared_na = "pass", False
        dod.append({"n": n, "title": d["title"], "status": status, "declared_na": declared_na,
                    "binds": applies, "failing": [r["id"] for r in mapped if not r["passed"]]})

    warnings = list(notes)
    base = doc.get("baselines") or {}
    canon_mcp = c.meta["baselines"]["mcp"]["revision"]
    if profile["mcp"] and str(base.get("mcp", "")) != canon_mcp:
        warnings.append(f"MCP revision {base.get('mcp')!r} differs from the baseline {canon_mcp} — "
                        f"sec.mcp-baseline needs a dated sunset for it")
    if profile["regulated"]:
        reg = doc.get("regulatory") or {}
        eu = reg.get("eu_ai_act") or {}
        if "EU" in (reg.get("jurisdictions") or []) and not (eu.get("role") and eu.get("risk_class")):
            warnings.append("regulated with EU exposure, but regulatory.eu_ai_act.role / risk_class are empty (DoD 31)")

    envelope_ok = _band_index(achieved) >= _band_index(required)
    dod_open = [x["n"] for x in dod if x["status"] == "fail"]
    return {
        "standard": c.version,
        "product": doc.get("product") or {},
        "operating_point": {"autonomy": f"L{profile['autonomy']}", "oversight": f"O{profile['oversight']}"},
        "profile": profile,
        "achieved": achieved,
        "required": required,
        "envelope_ok": envelope_ok,
        "dod_open": dod_open,
        # shippable at its operating point AND every binding Definition of Done item evidenced
        "production_ready": stage != "prototype" and envelope_ok and not dod_open,
        "items": items,
        "dod": dod,
        "warnings": warnings,
    }


# ---------------------------------------------------------------------------------------
# Outputs
# ---------------------------------------------------------------------------------------

def _line_of(text: str, item_id: str) -> int:
    m = re.search(r"^[ \t]*[\"']?" + re.escape(item_id) + r"[\"']?[ \t]*:", text, re.M)
    return text[: m.start()].count("\n") + 1 if m else 1


def _plain(text: str) -> str:
    """Canon text → plain text: no emphasis markers, links reduced to their label."""
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", re.sub(r"[*`]", "", text))


def _crosswalk(c, dod_ns) -> dict:
    by_n = c.dod_by_n()
    out: dict[str, list[str]] = {}
    for n in dod_ns:
        for fw, ids in by_n[n].get("crosswalk", {}).items():
            for x in ids:
                v = str(x)
                if v not in out.setdefault(fw, []):
                    out[fw].append(v)
    return out


def sarif_tags(c, item: dict) -> list[str]:
    tags = [item["band"]] + [f"DoD-{n}" for n in item.get("dod", [])]
    for fw, ids in _crosswalk(c, item.get("dod", [])).items():
        if fw in TAG_FRAMEWORKS:
            tags += [f"{TAG_FRAMEWORKS[fw]}{x.replace(' ', '-')}" for x in ids]
    return sorted(set(tags), key=tags.index)


def to_sarif(c, report: dict, file_rel: str, file_text: str, floor: str | None = None,
             require_dod: bool = False) -> dict:
    blob = f"{c.meta['repo']}/blob/v{c.version}"
    floor_i = _band_index(floor or report["required"])
    open_dod = set(report.get("dod_open", []))
    rules, results = [], []
    for rec in report["items"]:
        text = _plain(rec["text"])
        cw = _crosswalk(c, rec["dod"])
        refs = ", ".join(f"DoD {n}" for n in rec["dod"]) or "no Definition of Done item"
        rules.append({
            "id": rec["id"],
            "shortDescription": {"text": text[:1000]},
            "fullDescription": {"text": f"[{rec['band']}] {text}"},
            "help": {
                "text": f"{text}\n\nBand {rec['band']}; evidences {refs}. Answer it in aps-conformance.yaml "
                        f"with status yes + evidence, or na + reason.",
                "markdown": f"**{rec['band']}** · evidences {refs}\n\n{text}\n\n"
                            f"Answer `{rec['id']}` in `aps-conformance.yaml` with `status: yes` plus `evidence`, "
                            f"or `status: na` plus a `reason`. [Scorecard]({blob}/SCORECARD.md) · "
                            f"[Crosswalk]({blob}/CROSSWALK.md)",
            },
            "helpUri": f"{blob}/SCORECARD.md",
            "properties": {"tags": sarif_tags(c, rec)[:MAX_TAGS], "band": rec["band"],
                           "dod": rec["dod"], "crosswalk": cw},
        })
        if rec["passed"]:
            continue
        blocks = _band_index(rec["band"]) <= floor_i or (require_dod and bool(open_dod & set(rec["dod"])))
        results.append({
            "ruleId": rec["id"],
            "level": "error" if blocks else "warning",
            "message": {"text": f"[{rec['band']}] {text} — {rec['reason']}"},
            "locations": [{"physicalLocation": {
                "artifactLocation": {"uri": file_rel},
                "region": {"startLine": _line_of(file_text, rec["id"])},
            }}],
        })
    props = {k: report[k] for k in ("achieved", "required", "envelope_ok", "production_ready", "operating_point")}
    props["fail_under"] = floor or report["required"]
    return {
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "version": "2.1.0",
        "runs": [{
            "tool": {"driver": {
                "name": "aps-conformance",
                "version": c.version,
                "informationUri": c.meta["repo"],
                "rules": rules,
            }},
            "results": results,
            "properties": props,
        }],
    }


def to_badge(c, report: dict) -> dict:
    op = report["operating_point"]
    msg = f"{report['achieved']} · {op['autonomy']}·{op['oversight']}"
    color = BADGE_COLORS[report["achieved"]]
    if not report["envelope_ok"]:
        msg = f"{report['achieved']} < {report['required']} required"
        color = "red"
    return {"schemaVersion": 1, "label": f"APS {c.meta['version_label']}", "message": msg, "color": color}


def _cell(s) -> str:
    """User-supplied text in a Markdown table cell (and on stdout): one line, pipes escaped.

    Collapsing line breaks also keeps a crafted value from starting a line with `::`, which
    the Actions runner would execute as a workflow command.
    """
    return re.sub(r"[\r\n\u2028\u2029\x0b\x0c\x85]+", " ", str(s)).replace("|", "\\|")


def to_markdown(c, report: dict) -> str:
    op = report["operating_point"]
    name = _cell(report["product"].get("name", "product"))
    verdict = "✅ within its envelope" if report["envelope_ok"] else "❌ operating above its maturity"
    ready = "✅ yes" if report["production_ready"] else "❌ no"
    out = [f"## APS conformance — {name}", "",
           f"Scored against **{c.meta['standard']} v{c.version}**.", "",
           "| Operating point | Required band | Achieved band | Envelope | Production-ready (DoD) |",
           "|---|---|---|---|---|",
           f"| `{op['autonomy']} · {op['oversight']}` | **{report['required']}** | **{report['achieved']}** | "
           f"{verdict} | {ready} |", ""]
    failing = [r for r in report["items"] if not r["passed"]]
    if failing:
        out += ["### Open controls", "", "| Band | Item | Why it fails | DoD |", "|---|---|---|---|"]
        for r in sorted(failing, key=lambda r: (_band_index(r["band"]), r["id"])):
            out.append(f"| {r['band']} | `{r['id']}` — {_cell(_plain(r['text']))} | {_cell(r['reason'])} | "
                       f"{', '.join(map(str, r['dod'])) or '—'} |")
        out.append("")
    d = report["dod"]
    counts = {s: sum(1 for x in d if x["status"] == s) for s in ("pass", "fail", "n/a")}
    declared = sum(1 for x in d if x.get("declared_na"))
    out += [f"**Definition of Done:** {counts['pass']} pass · {counts['fail']} open · {counts['n/a']} n/a"
            + (f" ({declared} declared by the product)" if declared else "") + f" (of {len(d)}). "
            "A product is production-ready when its band covers its operating point **and** no binding item is open.", ""]
    if counts["fail"]:
        out.append("Open DoD items: " + ", ".join(f"{x['n']} {x['title']}" for x in d if x["status"] == "fail") + ".")
        out.append("")
    for w in report["warnings"]:
        out.append(f"> ⚠️ {_cell(w)}")
    return "\n".join(out).rstrip() + "\n"


def _gh_escape(msg: str) -> str:
    return msg.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def _write(path: str, content: str, append: bool = False) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a" if append else "w", encoding="utf-8") as fh:
        fh.write(content)


def cmd_conformance(c, args) -> int:
    path = Path(args.file)
    try:
        text = path.read_text(encoding="utf-8")
        doc = load_conformance(path)
        report = score(c, doc, Path(args.root), args.allow_unevidenced)
    except (OSError, UnicodeDecodeError, ConformanceError, _yaml().YAMLError, RecursionError) as exc:
        print(f"::error file={_gh_escape(str(args.file))}::{_gh_escape(f'aps-conformance: {exc}')}")
        return 2
    except Exception as exc:  # anything else is still "could not score", never "below band"
        print(f"::error::{_gh_escape(f'aps-conformance: could not score {args.file}: {type(exc).__name__}: {exc}')}")
        return 2
    try:
        file_rel = path.resolve().relative_to(Path(args.root).resolve()).as_posix()
    except ValueError:
        file_rel = path.as_posix()
    floor = args.fail_under or report["required"]
    require_dod = getattr(args, "require_dod", False)
    try:
        if args.json_out:
            _write(args.json_out, json.dumps(report, indent=2, ensure_ascii=False) + "\n")
        if args.sarif:
            sarif = to_sarif(c, report, file_rel, text, floor=args.fail_under, require_dod=require_dod)
            _write(args.sarif, json.dumps(sarif, indent=2, ensure_ascii=False) + "\n")
        if args.badge:
            _write(args.badge, json.dumps(to_badge(c, report)) + "\n")
        md = to_markdown(c, report)
        if args.summary:
            _write(args.summary, md, append=True)
    except OSError as exc:
        print(f"::error::{_gh_escape(f'aps-conformance: cannot write output: {exc}')}")
        return 2
    print(md)
    ok = _band_index(report["achieved"]) >= _band_index(floor)
    if require_dod and report["dod_open"]:
        ok = False
    return 0 if ok else 1
