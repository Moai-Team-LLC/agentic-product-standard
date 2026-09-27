"""aps-conformance: score a product's aps-conformance.yaml against the canon scorecard.

Output: the maturity band achieved, the band the declared operating point requires, DoD
coverage, and every failing control — as a console report, JSON, SARIF 2.1.0 (for code
scanning), a Markdown summary, and a shields.io endpoint badge. Evidence-based by default:
a `yes` without evidence counts as `no`.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from aps import BANDS, ConditionError, _yaml, eval_condition, load_yaml

LEVELS = {f"L{i}": i for i in range(5)}
MODES = {f"O{i}": i for i in range(3)}
FLAGS = ("multi_tenant", "mcp", "multi_agent", "cross_boundary", "llm_judge",
         "retrieval", "regulated", "fleet", "multi_provider")
BADGE_COLORS = {"M0": "red", "M1": "yellow", "M2": "green", "M3": "brightgreen"}
URL_RE = re.compile(r"^[a-z][a-z0-9+.-]*://", re.I)


class ConformanceError(ValueError):
    pass


def _band_index(b: str) -> int:
    return BANDS.index(b)


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
            raise ConformanceError(f"profile.{f} must be true or false")
        out[f] = v
    return out


def _schema_errors(c, doc) -> list[str]:
    try:
        import jsonschema  # type: ignore
    except ImportError:
        return []
    path = c.root / "canon" / "schema" / "aps-conformance.schema.json"
    if not path.exists():
        return []
    schema = json.loads(path.read_text(encoding="utf-8"))
    doc = json.loads(json.dumps(doc, default=str))  # YAML dates → strings, as JSON Schema sees them
    v = jsonschema.Draft202012Validator(schema)
    return [f"{'/'.join(str(p) for p in e.path) or '<root>'}: {e.message}" for e in v.iter_errors(doc)]


def evidence_exists(root: Path, ev: str) -> bool:
    """A URL is taken as given; a path must exist inside the repo root (no absolute paths, no escaping)."""
    if URL_RE.match(ev):
        return True
    rel = Path(ev.split("#")[0])
    if rel.is_absolute():
        return False
    base = root.resolve()
    target = (base / rel).resolve()
    return (target == base or base in target.parents) and target.exists()


def normalize(doc: dict) -> dict:
    """YAML 1.1 (PyYAML) reads unquoted yes/no as booleans; accept both spellings."""
    items = doc.get("items")
    if isinstance(items, dict):
        for ans in items.values():
            if isinstance(ans, dict) and isinstance(ans.get("status"), bool):
                ans["status"] = "yes" if ans["status"] else "no"
    return doc


def score(c, doc: dict, root: Path, allow_unevidenced: bool = False) -> dict:
    """Pure scoring: returns the full report dict. Raises ConformanceError on malformed input."""
    if not isinstance(doc, dict):
        raise ConformanceError("the file must be a YAML mapping")
    doc = normalize(doc)
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
        elif not isinstance(ans, dict) or ans.get("status") not in ("yes", "no", "na"):
            rec.update(status="no", reason="malformed answer (need status: yes | no | na)", passed=False)
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
            status = "n/a"
        elif all(r["passed"] for r in mapped):
            status = "pass"
        else:
            status = "fail"
        dod.append({"n": n, "title": d["title"], "status": status,
                    "failing": [r["id"] for r in mapped if not r["passed"]]})

    warnings = list(notes)
    base = (doc.get("baselines") or {})
    canon_mcp = c.meta["baselines"]["mcp"]["revision"]
    if profile["mcp"] and str(base.get("mcp", "")) != canon_mcp:
        warnings.append(f"MCP revision {base.get('mcp')!r} differs from the baseline {canon_mcp} — "
                        f"sec.mcp-baseline needs a dated sunset for it")
    if profile["regulated"]:
        eu = ((doc.get("regulatory") or {}).get("eu_ai_act") or {})
        if "EU" in ((doc.get("regulatory") or {}).get("jurisdictions") or []) and not (eu.get("role") and eu.get("risk_class")):
            warnings.append("regulated with EU exposure, but regulatory.eu_ai_act.role / risk_class are empty (DoD 31)")

    return {
        "standard": c.version,
        "product": doc.get("product") or {},
        "operating_point": {"autonomy": f"L{profile['autonomy']}", "oversight": f"O{profile['oversight']}"},
        "profile": profile,
        "achieved": achieved,
        "required": required,
        "envelope_ok": _band_index(achieved) >= _band_index(required),
        "items": items,
        "dod": dod,
        "warnings": warnings,
    }


def _line_of(text: str, item_id: str) -> int:
    m = re.search(r"^\s*" + re.escape(item_id) + r"\s*:", text, re.M)
    return text[: m.start()].count("\n") + 1 if m else 1


def _tags(c, rec) -> list[str]:
    tags = [rec["band"]]
    by_n = c.dod_by_n()
    for n in rec["dod"]:
        tags.append(f"DoD-{n}")
        for fw, ids in by_n[n].get("crosswalk", {}).items():
            prefix = {"eu_ai_act": "EU-AI-Act-Art-", "owasp_asi": "", "nist_ai_rmf": "NIST-", "imda": "IMDA-"}[fw]
            tags += [f"{prefix}{str(x).replace(' ', '-')}" for x in ids]
    return sorted(set(tags), key=tags.index)


def to_sarif(c, report: dict, file_rel: str, file_text: str) -> dict:
    help_base = f"{c.meta['repo']}/blob/v{c.version}/SCORECARD.md"
    rules, results = [], []
    req = _band_index(report["required"])
    for rec in report["items"]:
        rules.append({
            "id": rec["id"],
            "shortDescription": {"text": re.sub(r"[*`]", "", rec["text"])[:1000]},
            "helpUri": help_base,
            "properties": {"tags": _tags(c, rec), "band": rec["band"]},
        })
        if rec["passed"]:
            continue
        level = "error" if _band_index(rec["band"]) <= req else "warning"
        results.append({
            "ruleId": rec["id"],
            "level": level,
            "message": {"text": f"[{rec['band']}] {re.sub(r'[*`]', '', rec['text'])} — {rec['reason']}"},
            "locations": [{"physicalLocation": {
                "artifactLocation": {"uri": file_rel},
                "region": {"startLine": _line_of(file_text, rec["id"])},
            }}],
        })
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
            "properties": {k: report[k] for k in ("achieved", "required", "envelope_ok", "operating_point")},
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


def to_markdown(c, report: dict) -> str:
    op = report["operating_point"]
    name = report["product"].get("name", "product")
    verdict = "✅ within its envelope" if report["envelope_ok"] else "❌ operating above its maturity"
    out = [f"## APS conformance — {name}", "",
           f"Scored against **{c.meta['standard']} v{c.version}**.", "",
           "| Operating point | Required band | Achieved band | Verdict |", "|---|---|---|---|",
           f"| `{op['autonomy']} · {op['oversight']}` | **{report['required']}** | **{report['achieved']}** | {verdict} |", ""]
    failing = [r for r in report["items"] if not r["passed"]]
    if failing:
        out += ["### Open controls", "", "| Band | Item | Why it fails | DoD |", "|---|---|---|---|"]
        for r in sorted(failing, key=lambda r: (_band_index(r["band"]), r["id"])):
            text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", re.sub(r"[*`]", "", r["text"]))
            out.append(f"| {r['band']} | `{r['id']}` — {text} | {r['reason']} | {', '.join(map(str, r['dod'])) or '—'} |")
        out.append("")
    d = report["dod"]
    counts = {s: sum(1 for x in d if x["status"] == s) for s in ("pass", "fail", "n/a")}
    out += [f"**Definition of Done:** {counts['pass']} pass · {counts['fail']} fail · {counts['n/a']} n/a "
            f"(of {len(d)}).", ""]
    if counts["fail"]:
        out.append("Failing DoD items: " + ", ".join(f"{x['n']} {x['title']}" for x in d if x["status"] == "fail") + ".")
        out.append("")
    for w in report["warnings"]:
        out.append(f"> ⚠️ {w}")
    return "\n".join(out).rstrip() + "\n"


def cmd_conformance(c, args) -> int:
    path = Path(args.file)
    try:
        text = path.read_text(encoding="utf-8")
        doc = load_yaml(path)
        report = score(c, doc, Path(args.root), args.allow_unevidenced)
    except (OSError, UnicodeDecodeError, ConformanceError, _yaml().YAMLError) as exc:
        msg = f"aps-conformance: {exc}".replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        print(f"::error file={args.file}::{msg}")
        return 2
    try:
        file_rel = path.resolve().relative_to(Path(args.root).resolve()).as_posix()
    except ValueError:
        file_rel = path.as_posix()
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if args.sarif:
        Path(args.sarif).write_text(json.dumps(to_sarif(c, report, file_rel, text), indent=2, ensure_ascii=False) + "\n",
                                    encoding="utf-8")
    if args.badge:
        Path(args.badge).write_text(json.dumps(to_badge(c, report)) + "\n", encoding="utf-8")
    md = to_markdown(c, report)
    if args.summary:
        with open(args.summary, "a", encoding="utf-8") as fh:
            fh.write(md)
    print(md)
    floor = args.fail_under or report["required"]
    return 0 if _band_index(report["achieved"]) >= _band_index(floor) else 1
