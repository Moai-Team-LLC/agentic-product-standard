# ADR-0005: "Layer N" is the harness; Part II sections are "Stack N"

- **Status:** Accepted (v4.0.0-rc.1)
- **Date:** 2026-09-27

## Context

Since v2.0 two different lists were both numbered "Layer 1–9": the **harness** in Canon 4 (Agent Loop, Context & Memory, Durable Execution, Guardrails, Human-in-the-Loop, Evaluation, Observability, Security & Identity, Cost & FinOps) and the **technology stack** in Part II (Model & provider, Tool integration, Context engineering, Memory, Durable execution, Observability & evals, Framework selection, Security & Identity, Cost & FinOps). They coincide only at 8 and 9. "Layer 5" meant Human-in-the-Loop in one sentence and Durable execution in the next; the ecosystem map mixed both schemes in one table. The v3.3 "nine layers" count was itself imported from the stack list into the harness.

## Decision

- **"Layer N" always means a harness layer** (Canon 4, `canon/harness.yaml` → `layers`). The harness has nine: seven stacked around the loop plus two cross-cutting (8 Security & Identity, 9 Cost & FinOps).
- **Part II sections are "Stack N"** (`canon/harness.yaml` → `stack`, each mapped to the harness layers it serves). Stack 8 and 9 are the stack view of Layers 8 and 9.
- Case studies under `examples/` are documents of record against earlier versions; they keep their original "Layer N" wording with a terminology note rather than being rewritten.

## Consequences

- Cross-references in `STANDARD.md`, the skills, and `ECOSYSTEM.md` were rewritten to the scheme above.
- Anchors to Part II headings changed (`#layer-8-…` → `#stack-8-…`); external links to the old anchors land at the top of `STANDARD.md`.

## Alternatives considered

- **Renumber the stack to match the harness.** The lists answer different questions (architecture vs. technology choice) and do not align item for item. Rejected.
- **Drop the stack numbers entirely.** Several sections are cited by number across the ecosystem; a stable short name is useful. Rejected.
