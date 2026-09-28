# Phase 3 — Design Interventions (Intervention Design)

## Objective

Determine which changes could close diagnosed Capability Gaps, across all intervention families, and where AI is justified.

## Required inputs

- intervention-ready Gaps (Capability Diagnosis);
- their cause Hypotheses (`validated` or `accepted_as_testable`);
- constraints (Transformation Intent);
- evidence (Evidence Register).

## Method

Use:

1. [`design/INTERVENTION_PATTERNS.md`](../design/INTERVENTION_PATTERNS.md)
2. [`DECISION_MODEL.md`](../DECISION_MODEL.md) (§1 intervention challenge; §3 autonomy challenge)
3. [`diagnostics/AI_SUITABILITY.md`](../diagnostics/AI_SUITABILITY.md) (`AI_*` candidates)
4. [`diagnostics/AUTONOMY_SUITABILITY.md`](../diagnostics/AUTONOMY_SUITABILITY.md) (`AI_*` candidates)
5. [`evidence/UNCERTAINTY_MODEL.md`](../evidence/UNCERTAINTY_MODEL.md)
6. [`economics/TRANSFORMATION_ECONOMICS.md`](../economics/TRANSFORMATION_ECONOMICS.md)

For each Gap apply the challenge order in [`STANDARD.md`](../STANDARD.md) §5. It is a challenge heuristic, not a mandatory pipeline.

## Activities

1. generate multiple candidate Interventions for each intervention-ready Gap, each addressing named causes (`hypothesis_ids`);
2. assign each candidate a `type` from [`PUBLIC_API.md`](../PUBLIC_API.md) §6; include non-AI candidates, and consider the families without a challenge position (PROCESS, ROLE, DECISION, DATA, KNOWLEDGE, SOFTWARE, CONTROL, FEEDBACK) wherever the diagnosed cause points to them;
3. for candidates whose type is `AI_*`: assess AI suitability and classify AI fit A–E (skill 13);
4. for `AI_*` candidates proposed for selection, i.e. carried into Phase 4 (classes A–C, or D with a recorded justification, [`diagnostics/AI_SUITABILITY.md`](../diagnostics/AI_SUITABILITY.md) §5; never E, which is rejected): assess autonomy separately per action class and propose the Authority Ceiling (skill 14);
5. define required context, actions, permissions, verification, and risks;
6. record material uncertainties (`UNC-###`) and economic assumptions (`ASM-###`);
7. record rejected candidates with their rationale.

## Outputs

- Intervention Map ([`artifacts/intervention-map.md`](../artifacts/intervention-map.md)): Intervention records (`INT-###`);
- AI Suitability Assessments ([`artifacts/ai-suitability-assessment.md`](../artifacts/ai-suitability-assessment.md)) for `AI_*` candidates;
- Autonomy Assessments with proposed Authority Ceilings ([`artifacts/autonomy-assessment.md`](../artifacts/autonomy-assessment.md)) for `AI_*` candidates proposed for selection;
- Uncertainty records and economic assumptions, where material;
- rejected alternatives with rationale (`status: rejected`, `status_rationale`).

## Human gates

- `HG-AUTHORITY` — for each `AI_*` candidate proposed for selection, a Decision closing it lists the `AUT-###` in `subject_ids` and states the ceiling's level and scope in `statement` ([`diagnostics/AUTONOMY_SUITABILITY.md`](../diagnostics/AUTONOMY_SUITABILITY.md) §6). A proposed ceiling takes effect only after approval; an L0 ceiling needs no gate. The Intervention is not selected in Phase 4 until the ceiling is approved.

Any other [`STANDARD.md`](../STANDARD.md) §8 gate applies whenever its trigger occurs.

## Exit condition

Matches [`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2. For candidates of every family:

```text
each intervention-ready Gap has at least one candidate Intervention (INT)
  with gap_ids, hypothesis_ids, type (PUBLIC_API.md §6), expected_effect
AND simpler alternatives considered (simpler_alternatives_considered)
AND rejected candidates carry a rationale
```

In addition, an `AI_*` candidate is ready for prioritization only when:

```text
Gap trace exists
AND AI need is justified (classes A–C, or D with a recorded justification;
    never E; diagnostics/AI_SUITABILITY.md §5)
AND simpler alternatives were considered
AND verification is plausible
AND authority assumptions are explicit (Autonomy Assessment with proposed Authority Ceiling)
```

The phase MAY exit while `HG-AUTHORITY` for a proposed ceiling is open ([`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2).

In addition, as in every phase: facts and assumptions are separated; every material conclusion is traceable to Evidence (`EVD-###`) or labeled `[ASSUMPTION]` or `[HYPOTHESIS]` ([`AGENTS.md`](../AGENTS.md) §3); unresolved critical uncertainty is visible.

## Prohibited shortcut

Selecting AI because it is fashionable, offered by a vendor, or technically possible ([`diagnostics/AI_SUITABILITY.md`](../diagnostics/AI_SUITABILITY.md) §7), or treating AI fit as authority (INV-06).
