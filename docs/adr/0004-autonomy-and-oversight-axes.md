# ADR-0004: Autonomy and oversight are two axes; the Loop License binds on oversight

- **Status:** Accepted (v4.0.0-rc.1) — breaking change to Canon 1 and Part IV
- **Date:** 2026-09-27

## Context

The v1–v3 Autonomy Ladder had one axis, L0–L4, and v3.0 bound the Loop License to "L3+ unattended." That phrase fused two different questions: *who chooses the next step* (the model or the code) and *whether a human approves each consequential action*. The fusion produced cases the standard could not classify:

- an L3 orchestrator whose every external action waits for approval was formally "L3+" but plainly not unattended;
- an L2 pipeline that auto-applies its output every night was "below L3," so the Loop License did not bind — though nothing checks its actions before they land;
- L3 was named "Orchestrator-Worker," the same name as composition pattern 4, so "L3" was read as a topology rather than a degree of autonomy.

Outside evidence pointed the same way. The EU AI Act already separates the two: it defines AI systems by their "varying levels of autonomy" (Art. 3(1)) and makes human oversight a requirement of its own (Art. 14). Singapore IMDA's *Model AI Governance Framework for Agentic AI* (January 2026, updated May 2026) makes meaningful human accountability one of its four dimensions and asks for measurement of automation bias (override rates, response times). METR's work on time horizons shows autonomy capability is domain-specific, and its *Frontier Risk Report* (May 2026) found at least 16% of successful runs on tasks over eight hours illegitimate on review — both arguments for governing *oversight* on its own evidence.

## Decision

1. **Two axes.** Autonomy **L0–L4** (who picks the next step) × oversight **O0** (human in the loop — approves each consequential, P3+ action) / **O1** (human on the loop — supervises live, can veto) / **O2** (unattended). A system declares its **operating point**, e.g. `L3 · O0`.
2. **L3 is renamed "Bounded decomposition"** (formerly Orchestrator-Worker) to separate the autonomy level from the composition pattern.
3. **The Loop License binds at O1+**, at any autonomy level. This deliberately keeps v3's meaning of "without a human in each turn": the research that motivated v4.0 proposed binding at O2 only, but that would have released on-the-loop systems (O1) from the license — a loosening, since a live supervisor cannot bound spend or blast radius at machine speed, and automation bias erodes exactly that supervision. O2 adds the success-legitimacy audit (DoD 30). Stop conditions (DoD 17) bind at L3+ **or** O1+, because a loop needs a way to stop even when every action is approved.
4. **Escalation rules per axis.** Climb autonomy on pass@1 ≥ 90%. Relax oversight only under a Loop License whose eval gate adds pass^5 ≥ a declared threshold, and at O2 a legitimacy-rate floor. The standard sets no hour thresholds: benchmark time horizons do not transfer to a product.
5. **The weakest-link bound and the scorecard follow the new axis:** an unlicensed node caps a path at O0; the maturity band a product must reach is set by its operating point (L4 → M3; L3 or O1/O2 → M2; else M1).

## Consequences

- Every "L3+" binding in the standard, the skills, the checklists, and the decision tree was re-expressed as O1+ (or L3+ or O1+ for stop conditions). Systems that relied on "below L3" to avoid the Loop License while acting without approval now owe it; systems at L3 under per-action approval no longer do.
- Products must declare an operating point; the scorecard (`arch.operating-point`) and the conformance tool check it against the band achieved.
- Migration note in `CHANGELOG.md` [4.0.0].

## Alternatives considered

- **Keep one ladder and add "L3u" for unattended.** Encodes the fusion instead of removing it. Rejected.
- **Bind the Loop License at O2 only** (the proposal in the v4.0 research). Rejected for the loosening described above.
- **More oversight modes** (e.g. sampled review as its own mode). Sampling is how an O1/O2 oversight program is run (DoD 33), not a separate mode. Rejected for now.
