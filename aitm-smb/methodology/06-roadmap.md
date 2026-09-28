# Phase 6 — Design Transition (Roadmap)

## Objective

Move from the Current State to the Capability Target States (integrated in the Target Operating Architecture, where one exists) through bounded, operable Transition States and executable Transformation Slices, with experiments and pilots designed where material uncertainty remains.

## Required inputs

- approved Target Operating Architecture (Compact: approved Capability Target States);
- selected Initiatives (`INI-###`) and their System Effect Assessments;
- Capability Network and System Constraint, where the profile requires them;
- Decision Rights Map and Autonomy Assessments (Authority Ceilings), where AI authority changes;
- Uncertainty records (`UNC-###`, Evidence Register) and Risk records (`RSK-###`, Decision & Assumption Log).

## Method

Use:

1. [`transition/TRANSFORMATION_SEQUENCING.md`](../transition/TRANSFORMATION_SEQUENCING.md)
2. [`transition/TRANSITION_STATE_MODEL.md`](../transition/TRANSITION_STATE_MODEL.md)
3. [`execution/DELIVERY_SLICE.md`](../execution/DELIVERY_SLICE.md)
4. [`execution/EXPERIMENT_MODEL.md`](../execution/EXPERIMENT_MODEL.md) and [`execution/PILOT_MODEL.md`](../execution/PILOT_MODEL.md), where material uncertainty remains (INV-11)
5. [`evaluation/EVALUATION_SYSTEM.md`](../evaluation/EVALUATION_SYSTEM.md) (pre-registered evaluation of each pilot)
6. [`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md) §3 (planned authority increases)
7. [`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md)
8. [`portfolio/TRANSFORMATION_PORTFOLIO.md`](../portfolio/TRANSFORMATION_PORTFOLIO.md), when the Portfolio profile is active

Decision gates are the Initiative `decision_gates` ([`CORE_MODEL.md`](../CORE_MODEL.md) §7): Execution Gate records (`GAT-###`; required under the Governed profile, optional otherwise, [`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2) and/or mappings `{gate: HG-*, subject_ids: []}`.

## Activities

1. map Initiative dependencies and sequence the Initiatives (constraint relevance, dependency order, learning, risk);
2. create independently operable Transition States (skill 21), where the profile requires them;
3. define vertical Transformation Slices (`SLC-###`) for each Initiative, in the Transformation Roadmap `slices` unless the Pilot Plan holds them;
4. define each Initiative's decision gates;
5. design the required Experiments and Pilots with pre-registered evaluation: Pilot Plan (skill 25), Evaluation Plan (skill 26), Evaluation Dataset for AI components (skill 27);
6. define the evidence each Initiative and slice must produce (`evidence_to_produce`);
7. sequence authority increases: each planned increase stays within the approved Authority Ceiling, sits behind a `{gate: HG-AUTHORITY, subject_ids: [AUT-###]}` decision gate, and plans the evidence its criteria need ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md) §3: (a) for a bounded pilot within the ceiling; (b) for an increase beyond pilot scope);
8. define rollback or recovery;
9. Portfolio profile: build the Transformation Portfolio and bound transformation WIP (skill 22);
10. submit material budget for approval.

## Outputs

Produce only the outputs the active profile requires ([`APPLICATION_PROFILES.md`](../APPLICATION_PROFILES.md), [`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2); other outputs are optional under INV-15.

- every profile: Transformation Roadmap ([`artifacts/transformation-roadmap.md`](../artifacts/transformation-roadmap.md)) with execution-ready Initiative records;
- Transformation Slices (`SLC-###`, [`execution/DELIVERY_SLICE.md`](../execution/DELIVERY_SLICE.md)), the preferred implementation unit ([`STANDARD.md`](../STANDARD.md) §10), linked from `slice_ids` and held in the roadmap `slices` unless the Pilot Plan holds them;
- Standard adds: Transition States ([`artifacts/transition-state.md`](../artifacts/transition-state.md)); Pilot Plan ([`artifacts/pilot-plan.md`](../artifacts/pilot-plan.md)) and Evaluation Plan ([`artifacts/evaluation-plan.md`](../artifacts/evaluation-plan.md)) where a pilot is required;
- Governed adds: Execution Gate records C–G per Initiative ([`artifacts/execution-gate.md`](../artifacts/execution-gate.md); Gates A and B exist from Phases 4 and 5); Evaluation Datasets for AI components;
- Portfolio adds: Transformation Portfolio ([`artifacts/transformation-portfolio.md`](../artifacts/transformation-portfolio.md)) with a WIP limit;
- Experiments (`EXP-###`, [`execution/EXPERIMENT_MODEL.md`](../execution/EXPERIMENT_MODEL.md)), where used, in the roadmap `experiments` unless the Pilot Plan holds them;
- Decision & Assumption Log updates.

## Human gates

- `HG-BUDGET` — stop with `HUMAN_DECISION_REQUIRED` until a Decision closing it covers the material budget the roadmap, a pilot, or the portfolio commits.

Planned authority increases, including a pilot's grant, are placed behind `HG-AUTHORITY` decision gates naming their `AUT-###`; planning an increase does not trigger the gate. The gate is triggered and closed when the increase is due: before the pilot starts or before the rollout stage that raises the level (Phase 7; skill 08 invokes skill 34), or in Phase 8. A pilot that accepts material risk reaches `HG-RISK` before it runs. Any other gate applies whenever its trigger occurs. Governed profile: Execution Gate C ([`execution/EXECUTION_GATE_MODEL.md`](../execution/EXECUTION_GATE_MODEL.md)).

## Exit condition

Matches [`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2:

```text
every material Initiative has owner, bounded scope, dependency context, evidence plan,
  decision gates, rollback/recovery, and success metrics
AND Transition States operable where the profile requires them
AND planned AI authority increases sit behind an HG-AUTHORITY decision gate naming its AUT-###
AND required pilots and experiments designed with pre-registered evaluation
AND transformation WIP bounded (Portfolio)
```

Refinements: an operable Transition State passes [`transition/TRANSITION_STATE_MODEL.md`](../transition/TRANSITION_STATE_MODEL.md) §8; no gate triggered in this phase remains open (e.g. `HG-BUDGET`).

In addition, as in every phase: facts and assumptions are separated; every material conclusion is traceable to Evidence (`EVD-###`) or labeled `[ASSUMPTION]` or `[HYPOTHESIS]` ([`AGENTS.md`](../AGENTS.md) §3); unresolved critical uncertainty is visible.

## Prohibited shortcut

Big-bang migration, scale before proof, or autonomy before observability ([`transition/TRANSFORMATION_SEQUENCING.md`](../transition/TRANSFORMATION_SEQUENCING.md) §3).
