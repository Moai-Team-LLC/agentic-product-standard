"""Renderers: canon → Markdown/YAML for every generated region and file.

A region renderer is fn(canon, target_path) -> str. Write repo-root links as `@/path`;
aps.render_all() rewrites them relative to the target file.
"""

from __future__ import annotations

import re

from aps import condition_label

GENERATED_NOTE = "Generated from canon/ by tools/aps.py — edit the canon, not this file."


# ---------------------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------------------

def _cell(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def _flat(text: str) -> str:
    return " ".join(str(text).split())


def version_line(c) -> str:
    return f"*v{c.version} · assembled from production practices as of {c.meta['as_of']}*"


def _badge_message(c) -> str:
    return ("v" + c.version).replace("-", "--")


# ---------------------------------------------------------------------------------------
# shared pieces
# ---------------------------------------------------------------------------------------

def harness_diagram(c, lowercase_tag: bool = False) -> str:
    layers = c.harness["layers"]
    cross = [layer for layer in layers if layer.get("cross_cutting")][::-1]
    stacked = [layer for layer in layers if not layer.get("cross_cutting")][::-1]
    tag = "(cross-cutting)" if lowercase_tag else "(CROSS-CUTTING)"

    def label(layer):
        text = f"{layer['n']}. {layer['name']}"
        if layer.get("detail"):
            text += f" ({layer['detail']})"
        return text

    name_w = max(len(label(layer)) for layer in layers)
    inner = max(name_w + 4, max(len(layer["name"]) for layer in cross) + len(tag) + 10)
    rows = []
    for layer in cross:
        left = f"  {layer['n']}. {layer['name']}"
        rows.append((left.ljust(inner - len(tag) - 2) + tag + "  ", layer["role"]))
    sep = len(rows)
    for layer in stacked:
        rows.append((("   " + label(layer)).ljust(inner), layer["role"]))
    out = ["```", "╔" + "═" * inner + "╗"]
    for i, (text, role) in enumerate(rows):
        if i == sep:
            out.append("╠" + "═" * inner + "╣")
        out.append(f"║{text}║ ← {role}")
    out.append("╚" + "═" * inner + "╝")
    out += [
        "              ↕ MCP / function calling",
        "       ┌──────────────────────────┐",
        "       │   Tools & Resources      │",
        "       └──────────────────────────┘",
        "```",
    ]
    return "\n".join(out)


def autonomy_table(c, with_cost: bool = False) -> str:
    head = "| Level | What it is | Use when |" + (" Cost / latency |" if with_cost else "")
    sep = "|---|---|---|" + ("---|" if with_cost else "")
    rows = [head, sep]
    for lv in c.ladder["autonomy"]["levels"]:
        name = lv["name"]
        if lv.get("formerly"):
            name += f" *(formerly {lv['formerly']})*"
        row = f"| **{lv['id']}** · {name} | {_cell(lv['what'])} | {_cell(lv['use_when'])} |"
        if with_cost:
            row += f" {lv['cost']} |"
        rows.append(row)
    return "\n".join(rows)


def oversight_table(c) -> str:
    rows = ["| Mode | What it means | Requires |", "|---|---|---|"]
    for m in c.ladder["oversight"]["modes"]:
        rows.append(f"| **{m['id']}** · {m['name']} | {_cell(m['what'])} | {_cell(m['requires'])} |")
    return "\n".join(rows)


def escalation_block(c, quote: bool = True) -> str:
    e = c.ladder["escalation"]
    lines = [
        "**Escalation rules — each axis is earned separately:**",
        "",
        f"- {_flat(e['climb'])}",
        f"- {_flat(e['relax'])}",
        f"- {_flat(e['horizon'])}",
    ]
    if quote:
        return "\n".join(("> " + ln) if ln else ">" for ln in lines)
    return "\n".join(lines)


def ladder_section(c, with_cost: bool = False, examples: bool = True) -> str:
    parts = [
        f"**{c.ladder['autonomy']['title']}.**",
        "",
        autonomy_table(c, with_cost),
        "",
        f"**{c.ladder['oversight']['title']}.** {_flat(c.ladder['oversight']['consequential'])}",
        "",
        oversight_table(c),
        "",
        escalation_block(c),
    ]
    if examples:
        parts += ["", "An **operating point** is one of each:", ""]
        parts += [f"- `{x['point']}` — {x['note']}." for x in c.ladder["examples"]]
    return "\n".join(parts)


def checklist_block(c, extended: bool = False, hints: bool = False) -> str:
    qs = list(c.checklist["core"]) + (list(c.checklist["extended"]) if extended else [])
    out = ["```"]
    for q in qs:
        out.append(f"□ {q['q']}")
        if hints and q.get("hint"):
            out.append(f"  {q['hint']}")
    out.append("```")
    return "\n".join(out)


def patterns_list(c, examples: bool = False) -> str:
    out = []
    for p in c.patterns["patterns"]:
        line = f"{p['n']}. **{p['name']}** — {p['summary']}"
        if examples and p.get("example"):
            line += f" ({p['example']})"
        out.append(line)
    return "\n".join(out)


def antipattern_titles(c) -> str:
    out = []
    for a in c.antipatterns:
        t = a["title"] + (f" ({a['gloss']})" if a.get("gloss") else "")
        out.append(f"{a['n']}. {t}")
    return "\n".join(out)


def dod_intro(c, style: str = "standard") -> str:
    n = len(c.dod)
    if style == "readme":
        return (
            f"An agentic product is **not production-ready** until every Definition of Done item that binds to it is "
            f"satisfied — **{n} items**, each with a stable number (numbers are identifiers, so a group may list them "
            f"out of order). Items marked with a condition bind only when it holds; the rest bind for every production "
            f"system. [`SCORECARD.md`](@/SCORECARD.md) says which items evidence each one and the band at which a "
            f"system may *ship* before it is production-ready; [`CROSSWALK.md`](@/CROSSWALK.md) maps each to the EU "
            f"AI Act, OWASP, NIST, and IMDA. Full text in "
            f"[`STANDARD.md`](@/STANDARD.md#part-iii-production-readiness--definition-of-done)."
        )
    return (
        f"An agentic product is **not production-ready** until every item below that binds to it is satisfied. There "
        f"are **{n} items**. Numbers are stable identifiers — never reused or renumbered — so a group may list them out "
        f"of order. An item marked with a condition in italics binds only when that condition holds; every other item "
        f"binds for every production system. [`SCORECARD.md`](@/SCORECARD.md) names the items that evidence each one "
        f"and sets the lower band at which a system may *ship* at its operating point — shippable is not "
        f"production-ready; [`CROSSWALK.md`](@/CROSSWALK.md) maps each item to the EU AI Act, the OWASP Top 10 "
        f"for Agentic Applications, the NIST AI RMF, and IMDA's agentic framework."
    )


# ---------------------------------------------------------------------------------------
# README
# ---------------------------------------------------------------------------------------

def readme_badges(c, path):
    color = "orange" if c.prerelease else "blue"
    return "\n".join([
        "[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)",
        "[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)",
        "[![Claude Code Skills](https://img.shields.io/badge/Claude%20Code-Skills-d97757.svg)](skills/agentic-product-architect)",
        f"[![Standard v{c.version}](https://img.shields.io/badge/Standard-{_badge_message(c)}-{color}.svg)](STANDARD.md)",
        "[![Self-assessment scorecard](https://img.shields.io/badge/scorecard-M0–M3-success.svg)](SCORECARD.md)",
        "[![Conformance: aps-conformance](https://img.shields.io/badge/conformance-aps--conformance-informational.svg)](docs/conformance.md)",
        "[![Stars](https://img.shields.io/github/stars/Moai-Team-LLC/agentic-product-standard?style=social)](https://github.com/Moai-Team-LLC/agentic-product-standard/stargazers)",
    ])


def readme_principles(c, path):
    rows = ["| # | Principle | What it means |", "|---|---|---|"]
    for p in c.principles:
        rows.append(f"| {p['n']} | **{p['name']}** | {_cell(p['summary'])} |")
    return "\n".join(rows)


def readme_ladder(c, path):
    return ladder_section(c)


def readme_patterns(c, path):
    return patterns_list(c) + "\n\n**Meta-principle:** " + _flat(c.patterns["meta_principle"]).replace(
        "A full agent loop is the last resort.", "A full agent loop is the *last* resort.")


def readme_harness(c, path):
    return harness_diagram(c)


def readme_checklist(c, path):
    return checklist_block(c)


def readme_bands(c, path):
    rows = ["| Band | Operating envelope | Means |", "|---|---|---|"]
    for b in c.scorecard["bands"]:
        rows.append(f"| **{b['id']} · {b['name']}** | {_cell(b['envelope'])} | {_cell(_flat(b['meaning']))} |")
    return "\n".join(rows)


def readme_dod(c, path):
    rows = ["| Group | Items |", "|---|---|"]
    for g in c.dod_groups:
        cells = []
        for i in c.dod_in_group(g["key"]):
            t = f"**{i['n']}** {i['title']}"
            if i.get("binds_short"):
                t += f" *({i['binds_short']})*"
            cells.append(t)
        rows.append(f"| {g['title']} | {' · '.join(cells)} |")
    return dod_intro(c, "readme") + "\n\n" + "\n".join(rows)


def readme_antipatterns(c, path):
    return antipattern_titles(c)


def readme_footer(c, path):
    return version_line(c)


# ---------------------------------------------------------------------------------------
# STANDARD.md
# ---------------------------------------------------------------------------------------

def standard_title(c, path):
    out = f"# {c.meta['standard']} {c.meta['version_label']}"
    if c.prerelease:
        out += (f"\n\n> **Release candidate {c.version}** — *{c.meta['release_name']}*. Open for comment before "
                f"the final release; what changed and why: [`CHANGELOG.md`](@/CHANGELOG.md).")
    return out


def standard_principles(c, path):
    return "\n".join(f"{p['n']}. **{p['name']}** — {_flat(p['statement'])}" for p in c.principles)


def standard_ladder(c, path):
    return ladder_section(c)


def standard_patterns(c, path):
    return patterns_list(c) + "\n\n**Meta-principle:** " + _flat(c.patterns["meta_principle"])


def standard_harness(c, path):
    return harness_diagram(c)


def standard_dod(c, path):
    out = [dod_intro(c)]
    for g in c.dod_groups:
        out += ["", f"### {g['title']}"]
        for i in c.dod_in_group(g["key"]):
            cond = f"*({i['binds']})* " if i.get("binds") else ""
            out.append(f"- [ ] **{i['n']}.** {cond}{_flat(i['text'])}")
    out += ["", "> **Score yourself.** [`SCORECARD.md`](@/SCORECARD.md) turns this DoD into a Yes/No maturity "
                "self-assessment (M0–M3, mapped to the operating envelope) — run it with the team against a real "
                "deployment each release, or let [`aps-conformance`](@/docs/conformance.md) score it in CI."]
    return "\n".join(out)


def standard_antipatterns(c, path):
    out = ["**Do not do this:**", ""]
    for a in c.antipatterns:
        title = a["title"].rstrip(".")
        out.append(f"{a['n']}. **{title}.** {_flat(a['summary'])}")
    return "\n".join(out)


def standard_checklist(c, path):
    return checklist_block(c, extended=True)


def standard_footer(c, path):
    return version_line(c)


# ---------------------------------------------------------------------------------------
# SCORECARD.md
# ---------------------------------------------------------------------------------------

def scorecard_bands(c, path):
    rows = ["| Level | Operating envelope | Meaning |", "|---|---|---|"]
    for b in c.scorecard["bands"]:
        rows.append(f"| **{b['id']} — {b['name']}** | {_cell(b['envelope'])} | {_cell(_flat(b['meaning']))} |")
    rules = [f"{r['label']} → **{r['requires']}**" for r in c.scorecard["envelope_rules"]]
    return ("\n".join(rows) + "\n\n**Your level is the highest band whose every applicable gate item is satisfied.** One "
            "unmet gate item caps you at the level below — there is no partial credit, and no skipping a band. The "
            "operating point you run at sets the band you must reach to ship: " + "; ".join(rules) + ".\n\n"
            "**Shippable is not production-ready.** The band is the floor for putting a system in front of users at "
            "its operating point. *Production-ready* is the Definition of Done ([`STANDARD.md`](@/STANDARD.md) Part III): "
            "every DoD item that binds to the product, each evidenced by the scorecard items mapped to it — for most "
            "products, that means M2's items. [`aps-conformance`](@/docs/conformance.md) reports both; "
            "`--require-dod` makes the second one gate CI.")


def scorecard_items(c, path):
    out = []
    for sec in c.scorecard["sections"]:
        title = sec["title"]
        if sec.get("condition"):
            title += f" *({sec['condition']})*"
        elif sec.get("note"):
            title += f" *({sec['note']})*"
        out += [f"### {title}"]
        for item in sec["items"]:
            label = item["band"]
            cond = item.get("applies_if")
            if cond and cond != sec.get("applies_if"):
                label += f", {condition_label(cond)}"
            dods = item.get("dod", [])
            ref = f"`{item['id']}`" + (" · DoD " + ", ".join(str(n) for n in dods) if dods else "")
            out.append(f"- [ ] **({label})** {_flat(item['text'])} <sub>{ref}</sub>")
        out.append("")
    return "\n".join(out).rstrip("\n")


# ---------------------------------------------------------------------------------------
# CONTEXT.md, AGENT_STANDARD.md
# ---------------------------------------------------------------------------------------

def context_ladder(c, path):
    def lc(text):
        text = _flat(text)
        return text[:1].lower() + text[1:]

    out = ["**Autonomy** — who chooses the next step:", ""]
    for lv in c.ladder["autonomy"]["levels"]:
        out.append(f"- **{lv['id']}** — {lc(lv['name'])} ({lc(lv['what'])}).")
    out += ["", "**Oversight** — whether a human approves each consequential (P3+) action:", ""]
    for m in c.ladder["oversight"]["modes"]:
        out.append(f"- **{m['id']}** — {m['name'].lower()}: {lc(m['what'])}.")
    e = c.ladder["escalation"]
    out += ["", f"**Escalation** — {_flat(e['climb'])} {_flat(e['relax'])}"]
    return "\n".join(out)


def context_harness(c, path):
    stacked = [layer for layer in c.harness["layers"] if not layer.get("cross_cutting")]
    cross = [layer for layer in c.harness["layers"] if layer.get("cross_cutting")]
    s = " · ".join(f"{layer['n']}. {layer['name']}" for layer in stacked)
    x = " and ".join(f"{layer['n']}. {layer['name']} ({layer['role']})" for layer in cross)
    words = "zero one two three four five six seven eight nine ten".split()
    n_cross = words[len(cross)] if len(cross) < len(words) else str(len(cross))
    same = [st["n"] for st in c.harness["stack"] if st.get("harness") == [st["n"]]]
    same_txt = " and ".join(map(str, same)) if same else "no number"
    return (f"{s} — over MCP / function calling to Tools. {n_cross.capitalize()} cross-cutting "
            f"layer{'s' if len(cross) != 1 else ''} constrain{'' if len(cross) != 1 else 's'} all "
            f"{len(stacked)}: {x}.\n\n\"Layer N\" always means a harness layer. `STANDARD.md` Part II is the "
            f"technology stack, numbered **Stack N**; the two coincide only at {same_txt}.")


def agent_standard_ladder(c, path):
    def lc(text):
        text = _flat(text)
        return text[:1].lower() + text[1:]

    rows = ["| Level | Pattern | Use When |", "|---|---|---|"]
    for lv in c.ladder["autonomy"]["levels"]:
        rows.append(f"| {lv['id']} | {lv['name']} | {_cell(lv['use_when'])} |")
    rows += ["", "| Oversight | Mode | Requires |", "|---|---|---|"]
    for m in c.ladder["oversight"]["modes"]:
        req = _cell(m["requires"]).replace("(DoD", "(`STANDARD.md` DoD")
        rows.append(f"| {m['id']} | {m['name']} — {_cell(lc(m['what']))} | {req} |")
    return "\n".join(rows)


def agent_standard_harness(c, path):
    return harness_diagram(c, lowercase_tag=True).replace("```", "```text", 1)


# ---------------------------------------------------------------------------------------
# skills
# ---------------------------------------------------------------------------------------

def skill_master_principles(c, path):
    return "\n".join(f"{p['n']}. **{p['name']}.** {_flat(p['statement'])[0].upper() + _flat(p['statement'])[1:]}"
                     for p in c.principles)


def skill_master_ladder(c, path):
    return ladder_section(c, examples=False)


def skill_master_checklist(c, path):
    return checklist_block(c, hints=True)


def skill_master_patterns(c, path):
    return patterns_list(c, examples=True)


def skill_master_antipatterns(c, path):
    return antipattern_titles(c)


def skill_architecture_ladder(c, path):
    return ladder_section(c, with_cost=True)


def skill_harness_diagram(c, path):
    return harness_diagram(c, lowercase_tag=True)


def skill_readiness_summary(c, path):
    rows = ["| # | Item | Group | Binds | Band |", "|---|---|---|---|---|"]
    groups = {g["key"]: g["title"] for g in c.dod_groups}
    for g in c.dod_groups:
        for i in c.dod_in_group(g["key"]):
            rows.append(f"| {i['n']} | {_cell(i['title'])} | {_cell(groups[i['group']])} | "
                        f"{_cell(i.get('binds', 'always'))} | {c.dod_band(i['n']) or '—'} |")
    return (f"**{len(c.dod)} items.** Walk them with the checks, the *why*, and the common gap for each in "
            f"[`DOD.md`](DOD.md) (generated from the canon, bundled with this skill).\n\n" + "\n".join(rows))


def skill_antipatterns_items(c, path):
    out = []
    for a in c.antipatterns:
        title = a["title"] + (f" ({a['gloss']})" if a.get("gloss") else "")
        out += [f"### {a['n']}. {title}", "",
                f"**Signal:** {_flat(a['signal'])}", "",
                f"**Failure mode:** {_flat(a['failure_mode'])}", ""]
        fix = a["fix"].strip()
        out += ["**Fix:** " + (fix if "\n" in fix else _flat(fix)), ""]
        out += [f"**Severity:** {_flat(a['severity'])}", "", "---", ""]
    return "\n".join(out).rstrip("\n").rstrip("-").rstrip("\n")


# ---------------------------------------------------------------------------------------
# whole files
# ---------------------------------------------------------------------------------------

def render_dod_file(c, path):
    out = [f"<!-- {GENERATED_NOTE} -->", "",
           f"# Definition of Done — the audit points (Standard v{c.version})", "",
           "The normative text of each item is in `STANDARD.md` Part III; this file is the audit view the "
           "`production-readiness` skill walks. For every item: the checks to run, why it matters, and the gap teams "
           "most often leave. Mark each **pass**, **gap**, or **N/A with a reason** — \"N/A because we have no "
           "destructive actions\" is fine; \"N/A because we don't think it matters\" is not.", ""]
    for g in c.dod_groups:
        out += [f"## {g['title']}", ""]
        for i in c.dod_in_group(g["key"]):
            out += [f"### {i['n']}. {i['title']}", ""]
            if i.get("binds"):
                out += [f"*Binds: {i['binds']}.*", ""]
            for chk in i["audit"]["checks"]:
                out.append(f"- [ ] {_flat(chk)}")
            out += ["", f"**Why:** {_flat(i['audit']['why'])}", "",
                    f"**Common gap:** {_flat(i['audit']['gap'])}", "", "---", ""]
    return "\n".join(out).rstrip("\n").rstrip("-").rstrip("\n") + "\n"


def render_crosswalk(c, path):
    fw = c.regulatory
    eu, asi, nist, imda = fw["eu_ai_act"], fw["owasp_asi"], fw["nist_ai_rmf"], fw["imda"]
    names = {
        "eu_ai_act": {str(e["id"]): e["title"] for e in eu["entries"]},
        "owasp_asi": {str(e["id"]): e["title"] for e in asi["entries"]},
        "nist_ai_rmf": {str(e["id"]): e["title"] for e in nist["entries"]},
        "imda": {str(e["id"]): e["title"] for e in imda["entries"]},
    }

    def fmt(key, ids):
        if not ids:
            return "—"
        if key == "eu_ai_act":
            return ", ".join(f"Art. {x}" for x in ids)
        return ", ".join(str(x) for x in ids)

    out = [f"<!-- {GENERATED_NOTE} -->", "",
           "# Regulatory & framework crosswalk", "",
           f"*Standard v{c.version} · as of {c.meta['as_of']}.*", "",
           "Each Definition of Done item produces evidence — a test, a trace, a record, a gate. This page maps that "
           "evidence onto the external frameworks teams are asked about: the **EU AI Act**, the **OWASP Top 10 for "
           "Agentic Applications**, the **NIST AI RMF**, and Singapore **IMDA**'s Model AI Governance Framework for "
           "Agentic AI.", "",
           "> **This is a crosswalk, not a compliance claim, and not legal advice.** A mapping means *the evidence "
           "this item produces supports that obligation or practice* — nothing more. Whether an obligation applies to "
           "you depends on your role and risk class; that assessment starts from the regulatory classification "
           "record (DoD 31) and ends with your counsel.", "",
           "## EU AI Act — dates that bind", "",
           f"{_flat(eu['citation'])}. Consolidated text: [EUR-Lex]({eu['url']}); amending act: "
           f"[Regulation (EU) 2026/1744]({eu['amendment_url']}).", "",
           "| From | What applies |", "|---|---|"]
    for d in eu["dates"]:
        out.append(f"| {d['date']} | {_cell(_flat(d['what']))} |")
    out += ["", f"*{_flat(eu['note'])}*", "",
            "Date sources: " + " · ".join(f"[{i + 1}]({u})" for i, u in enumerate(eu["date_sources"])) + ".", "",
            "## Definition of Done → frameworks", "",
            "| DoD | Item | EU AI Act | OWASP ASI | NIST AI RMF | IMDA |", "|---|---|---|---|---|---|"]
    for i in sorted(c.dod, key=lambda i: i["n"]):
        cw = i.get("crosswalk", {})
        out.append(f"| {i['n']} | {_cell(i['title'])} | {fmt('eu_ai_act', cw.get('eu_ai_act'))} | "
                   f"{fmt('owasp_asi', cw.get('owasp_asi'))} | {fmt('nist_ai_rmf', cw.get('nist_ai_rmf'))} | "
                   f"{fmt('imda', cw.get('imda'))} |")
    out += ["", "## By framework", ""]
    for key, f in (("eu_ai_act", eu), ("owasp_asi", asi), ("nist_ai_rmf", nist), ("imda", imda)):
        out += [f"### {f['name']}", "", f"{_flat(f['citation'])}. Source: <{f['url']}>", ""]
        if f.get("note") and key != "eu_ai_act":
            out += [f"*{_flat(f['note'])}*", ""]
        first = {"eu_ai_act": "Article", "owasp_asi": "Risk", "nist_ai_rmf": "Category", "imda": "Dimension"}[key]
        out += [f"| {first} | Title | DoD items |", "|---|---|---|"]
        for e in f["entries"]:
            eid = str(e["id"])
            hits = [str(i["n"]) for i in sorted(c.dod, key=lambda i: i["n"])
                    if eid in [str(x) for x in i.get("crosswalk", {}).get(key, [])]]
            label = f"Art. {eid}" if key == "eu_ai_act" else eid
            out.append(f"| {label} | {_cell(names[key][eid])} | {', '.join(hits) if hits else '— *(not covered by the DoD)*'} |")
        out.append("")
    out += ["## How to use it", "",
            "- **Answering an assessor:** start from the framework table, follow the DoD numbers, and hand over the "
            "evidence those items already produce — the trace, the eval report, the license checklist.",
            "- **Planning a classification change:** if the classification record (DoD 31) moves you into high-risk, "
            "the EU AI Act rows show which DoD evidence carries over and where the Act asks for more (e.g. technical "
            "documentation and conformity assessment, which this standard does not cover).",
            "- **In CI:** `aps-conformance` tags each SARIF finding with the DoD items and crosswalk entries it "
            "touches, so a failing control shows up against the obligation it supports ([docs](@/docs/conformance.md)).",
            ""]
    return "\n".join(out)


def render_conformance_template(c, path):
    p = c.meta
    lines = [
        f"# aps-conformance.yaml — self-assessment against {p['standard']} v{c.version}.",
        f"# {GENERATED_NOTE}",
        "#",
        "# Copy to your product repo, fill it in with the team, and score it:",
        "#   python3 tools/aps.py conformance aps-conformance.yaml --sarif aps.sarif",
        f"#   or: uses: Moai-Team-LLC/agentic-product-standard@v{c.version}",
        "#",
        "# status: yes | no | na.  A `yes` needs `evidence` — a repo-relative path or a URL; an `na` needs a",
        "# `reason`. Items whose condition does not hold for your profile are N/A automatically.",
        "# Half-met is `no`. The first `no` in the lowest band is your next piece of work.",
        f'standard: "{c.version}"',
        "",
        "product:",
        "  name: my-agentic-product",
        "  owner: team@example.com",
        "  stage: production           # prototype | production",
        "",
        "# The operating point you run at, and what the product contains.",
        "profile:",
        "  autonomy: L2                # L0–L4 — who chooses the next step",
        "  oversight: O0               # O0 in the loop · O1 on the loop · O2 unattended",
        "  multi_tenant: false",
        "  mcp: false                  # speaks MCP as client or server",
        "  multi_agent: false          # more than one agent composed",
        "  cross_boundary: false       # delegates across an org / vendor / service trust boundary (e.g. A2A)",
        "  llm_judge: false            # uses LLM judges in evals or gates",
        "  retrieval: false            # has a memory or retrieval component",
        "  regulated: false            # exposed to a regulated jurisdiction (e.g. EU users)",
        "  fleet: false                # runs a persistent fleet of scheduled agents",
        "  multi_provider: false       # model calls fan out over several models/providers",
        "",
        "# The protocol revisions you actually speak (DoD 26, 29).",
        "baselines:",
        f'  mcp: "{p["baselines"]["mcp"]["revision"]}"',
        '  otel_genai: ""              # the semantic-conventions-genai commit you pin',
        "",
        "# DoD 31 — the regulatory classification record (fill in if regulated).",
        "regulatory:",
        "  jurisdictions: []           # e.g. [EU, US-CA, SG]",
        "  eu_ai_act:",
        "    role: \"\"                  # provider | deployer | both",
        "    risk_class: \"\"            # prohibited | high-risk-annex-iii | high-risk-annex-i | transparency | minimal",
        "    art50: []                 # e.g. [ai-interaction-disclosure, synthetic-content-marking]",
        "    owner: \"\"",
        "    reviewed: \"\"              # YYYY-MM-DD",
        "",
        "items:",
    ]
    for sec in c.scorecard["sections"]:
        head = sec["title"] + (f" ({sec['condition']})" if sec.get("condition") else "")
        lines += ["", f"  # ── {head} ──"]
        for item in sec["items"]:
            cond = item.get("applies_if")
            tag = item["band"] + (f", {condition_label(cond)}" if cond else "")
            dods = item.get("dod", [])
            ref = (" · DoD " + ", ".join(str(n) for n in dods)) if dods else ""
            text = _flat(item["text"]).replace("*", "").replace("`", "")
            text = re.sub(r"\(\[([^\]]+)\]\([^)]+\)\)", r"(\1)", text)
            text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
            lines.append(f"  # ({tag}{ref}) {text}")
            lines.append(f"  {item['id']}: {{status: no, evidence: \"\"}}")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------------------
# registries
# ---------------------------------------------------------------------------------------

REGIONS = {
    "README.md": {
        "readme.badges": readme_badges,
        "readme.principles": readme_principles,
        "readme.ladder": readme_ladder,
        "readme.patterns": readme_patterns,
        "readme.harness": readme_harness,
        "readme.checklist": readme_checklist,
        "readme.bands": readme_bands,
        "readme.dod": readme_dod,
        "readme.antipatterns": readme_antipatterns,
        "readme.footer": readme_footer,
    },
    "STANDARD.md": {
        "standard.title": standard_title,
        "standard.principles": standard_principles,
        "standard.ladder": standard_ladder,
        "standard.patterns": standard_patterns,
        "standard.harness": standard_harness,
        "standard.dod": standard_dod,
        "standard.antipatterns": standard_antipatterns,
        "standard.checklist": standard_checklist,
        "standard.footer": standard_footer,
    },
    "SCORECARD.md": {
        "scorecard.bands": scorecard_bands,
        "scorecard.items": scorecard_items,
    },
    "CONTEXT.md": {
        "context.ladder": context_ladder,
        "context.harness": context_harness,
    },
    "AGENT_STANDARD.md": {
        "agent-standard.ladder": agent_standard_ladder,
        "agent-standard.harness": agent_standard_harness,
    },
    "skills/agentic-product-architect/SKILL.md": {
        "skill.master.principles": skill_master_principles,
        "skill.master.ladder": skill_master_ladder,
        "skill.master.checklist": skill_master_checklist,
        "skill.master.patterns": skill_master_patterns,
        "skill.master.antipatterns": skill_master_antipatterns,
    },
    "skills/agentic-product-architect/architecture-design/SKILL.md": {
        "skill.architecture.ladder": skill_architecture_ladder,
    },
    "skills/agentic-product-architect/harness-engineering/SKILL.md": {
        "skill.harness.diagram": skill_harness_diagram,
    },
    "skills/agentic-product-architect/production-readiness/SKILL.md": {
        "skill.readiness.summary": skill_readiness_summary,
    },
    "skills/agentic-product-architect/antipatterns-review/SKILL.md": {
        "skill.antipatterns.items": skill_antipatterns_items,
    },
}

FILES = {
    "CROSSWALK.md": render_crosswalk,
    "skills/agentic-product-architect/production-readiness/DOD.md": render_dod_file,
    "templates/conformance/aps-conformance.template.yaml": render_conformance_template,
}
