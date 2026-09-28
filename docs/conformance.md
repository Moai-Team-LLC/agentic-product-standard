# Conformance in CI — `aps-conformance`

*The scorecard, machine-checked. New in Standard v4.0.*

[`SCORECARD.md`](../SCORECARD.md) has always asked a team to prove the standard against a real deployment. `aps-conformance` makes that proof part of CI: a product keeps its answers in an **`aps-conformance.yaml`**, every *Yes* carries **evidence**, and on every pull request the tool reports the maturity band the product reached, the band its operating point requires, and each open control as a finding. The canon behind it is the same one this repository renders its documents from ([`canon/`](../canon/)), so the tool and the prose cannot disagree.

It is a self-assessment made auditable, not a certification: the tool checks that evidence exists, not that it is good. Reviewers still have to look — the file tells them where.

## 1. Write the file

Start from the generated template — one entry per scorecard item, all `no`:

```bash
cp templates/conformance/aps-conformance.template.yaml my-product/aps-conformance.yaml
# or, from a clone of this repo:
python3 tools/aps.py template > my-product/aps-conformance.yaml
```

Then fill it in with the team:

- **`profile`** — the operating point (`autonomy: L0–L4`, `oversight: O0–O2`) and what the product contains (`multi_tenant`, `mcp`, `multi_agent`, `cross_boundary`, `llm_judge`, `retrieval`, `regulated`, `fleet`, `multi_provider`). Every flag is required; absent is not false. Items whose condition does not hold for your profile are marked N/A automatically.
- **`items`** — for each scorecard id: `status: yes | no | na`.
  - `yes` needs **`evidence`**: a file or directory in your repo (optionally with `#anchor`) or an `https://` URL — the test, the trace schema, the checklist, the runbook that proves it. A path that does not exist, the repo root, a bare `#anchor`, or a path outside the repo fails the item.
  - `na` needs a **`reason`** ("we have no destructive actions" is a reason; "not important" is not).
  - Anything unanswered counts as `no`. Half-met is `no`.
- **`baselines`** — the MCP revision and the `semantic-conventions-genai` commit you actually speak (DoD 26, 29).
- **`regulatory`** — your classification record (DoD 31): jurisdictions, EU AI Act role and risk class, Art. 50 duties, owner, review date.

The ids are stable across releases (never reused); the small print in [`SCORECARD.md`](../SCORECARD.md) shows each id next to its item and the DoD items it evidences. The file's schema is [`canon/schema/aps-conformance.schema.json`](../canon/schema/aps-conformance.schema.json).

## 2. Score it

Locally, from a clone of this repository (Python 3.9+ and PyYAML):

```bash
python3 tools/aps.py conformance path/to/aps-conformance.yaml --root path/to/product-repo
```

In CI, with the GitHub Action — pin it to the standard version you conform to:

```yaml
# .github/workflows/aps-conformance.yml in your product repo
name: aps-conformance
on: [pull_request, push]
permissions:
  contents: read
  security-events: write        # to upload SARIF to code scanning
jobs:
  conformance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - id: aps
        uses: Moai-Team-LLC/agentic-product-standard@v4.0.0
        with:
          file: aps-conformance.yaml
          badge: aps-badge.json            # optional shields.io endpoint JSON
      - if: always()
        uses: github/codeql-action/upload-sarif@v4
        with:
          sarif_file: aps-conformance.sarif
          category: aps-conformance
```

Inputs: `file`, `sarif`, `badge`, `fail-under` (a band; default — the band your operating point requires), `require-dod` (default `false`; `true` also fails while a binding DoD item is open), `allow-unevidenced` (default `false`). Outputs: `band`, `required`, `envelope-ok`, `production-ready`. The job summary shows the result table and every open control.

## 3. How it scores

1. **Applicability.** Each scorecard item may carry a condition over the profile (e.g. `mcp`, `oversight >= 1`, `multi_agent and oversight >= 1`). Items whose condition is false are N/A.
2. **Answers.** An applicable item passes only as `yes` with evidence that exists, or `na` with a reason. Everything else — `no`, unanswered, `yes` without evidence, `na` without a reason — fails.
3. **Band.** M1, M2, M3 in order: the band is the highest one whose items at or below it all pass. No partial credit, no skipping.
4. **Envelope.** The operating point sets the band you must reach to ship: L4 → **M3**; L3, or any system at O1/O2 → **M2**; everything else → **M1** (a `prototype` stage requires nothing). A product that runs above its band is flagged — *operating above its maturity*.
5. **DoD coverage.** Each binding Definition of Done item passes when every applicable scorecard item that evidences it passes; an item whose evidence was all declared N/A is reported as *n/a (declared)*, not as a pass. **Production-ready** = within the envelope **and** no binding DoD item open. Shippable is not production-ready: an `L2 · O0` system may ship at M1, but the DoD still asks for M2's items.
6. **Exit code.** 0 when the band reaches the envelope (or `--fail-under`) — and, with `--require-dod`, when no binding DoD item is open; 1 when it does not; 2 when the file cannot be scored (malformed, a duplicate key, a different major version of the standard, an unwritable output path).

## 4. Outputs

| Output | What it's for |
|---|---|
| **SARIF 2.1.0** (`--sarif`) | One result per open control, at the line of your file that answers it. `error` if it blocks the band you need (or, with `--require-dod`, an open DoD item), `warning` if it only blocks a higher one. Rules are tagged with the band, the DoD items, and their EU AI Act, OWASP ASI, and NIST AI RMF entries — `EU-AI-Act-Art-14`, `ASI03`, `NIST-MANAGE-1` — so code scanning can filter by obligation; the full crosswalk, IMDA included, is in each rule's `properties.crosswalk` (GitHub keeps at most 10 tags per rule). |
| **Markdown summary** (`--summary`) | The table and open controls, for `$GITHUB_STEP_SUMMARY` or a PR comment. |
| **JSON report** (`--json`) | Everything above, machine-readable: per-item status and reason, DoD coverage, `production_ready`, warnings. |
| **Badge** (`--badge`) | A [shields.io endpoint](https://shields.io/badges/endpoint-badge) JSON, e.g. `APS v4.0 · M2 · L3·O1`. Publish it wherever shields can fetch it (a branch, a Pages site, a gist) — a badge computed from evidence on every run, not a static claim. |

## 5. Why evidence-based by default

A scorecard answered from memory drifts towards green. Requiring a pointer for every *Yes* changes the conversation from "do we do this?" to "show me where", and it gives the next reviewer — or an assessor asking about Art. 14 — a place to start. `--allow-unevidenced` exists for a first draft; don't ship a badge built on it.

## Versioning

The tool refuses a file whose `standard` is a different major version: a v3 answer to a v4 contract means nothing. Pin the Action to the exact tag you conform to (`@v4.0.0`), and move the pin as a deliberate change. Within a major version, moving the pin should not lower your band: tightening what "conformant" means takes a major release ([`GOVERNANCE.md`](../GOVERNANCE.md)), so a minor release does not add a required item to a band you have already reached.
