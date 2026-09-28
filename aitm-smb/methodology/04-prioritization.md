# Phase 4 — Decide (Prioritization)

## Objective

Select the Initiatives with the highest justified leverage from the candidate Interventions, and record a decision with rationale for every candidate.

## Required inputs

- candidate Interventions ready for prioritization (Intervention Map, Phase 3 exit);
- AI Suitability and Autonomy Assessments for `AI_*` candidates (an `AI_*` Intervention is selected only once its Authority Ceiling is approved);
- approved Outcomes and their Metrics;
- economic assumptions (`ASM-###`) and the Evidence Register;
- System Constraint, where one has been identified;
- Transformation Portfolio, when the Portfolio profile is active and a portfolio exists.

## Method

Use:

1. [`artifacts/prioritization-matrix.md`](../artifacts/prioritization-matrix.md) (dimensions)
2. [`economics/TRANSFORMATION_ECONOMICS.md`](../economics/TRANSFORMATION_ECONOMICS.md) §5 (economic hypothesis, held on the Initiative)
3. [`design/LOCAL_OPTIMIZATION_GUARD.md`](../design/LOCAL_OPTIMIZATION_GUARD.md) §2, §4 (system-effect check before selection, skill 19)
4. [`design/CONSTRAINT_ANALYSIS.md`](../design/CONSTRAINT_ANALYSIS.md) §6, when a System Constraint exists
5. [`portfolio/PORTFOLIO_PRIORITIZATION.md`](../portfolio/PORTFOLIO_PRIORITIZATION.md), when the Portfolio profile is active
6. [`CORE_MODEL.md`](../CORE_MODEL.md) §7 (Initiative record)

Selection is provisional when the profile requires a System Constraint (Standard and above) and none has been identified yet: the selection Decision carries a `review_trigger` naming the Phase 5 System Constraint and the refined System Effect Assessments.

## Activities

1. group candidate Interventions into candidates: one or more Interventions that would be delivered together;
2. assess each candidate on every matrix dimension, with ordinal values and written rationale, or `not_relevant` with a reason; add Constraint Relevance where a System Constraint exists, and the portfolio criteria when the Portfolio profile is active;
3. propose per candidate: select, defer, reject, or investigate; record the rationale; `investigate` keeps the Interventions at `status: candidate` and records an Evidence Debt item naming what must be learned ([`evidence/EVIDENCE_STANDARD.md`](../evidence/EVIDENCE_STANDARD.md) §5);
4. Portfolio profile: before adding an Initiative, check the stop conditions ([`portfolio/PORTFOLIO_PRIORITIZATION.md`](../portfolio/PORTFOLIO_PRIORITIZATION.md) §5); while one holds, select only with an approved Decision of the portfolio owner recording the override and its reason;
5. for each candidate proposed for selection, create the Initiative record (`INI-###`, `status: proposed`) in the Transformation Roadmap with `intervention_ids`, `capability_ids`, `expected_outcome_ids`, `success_metric_ids`, `evidence_ids`, owner, and scope;
6. for each material Initiative, once its record exists, record its economic hypothesis on it (`economic_hypothesis`, [`artifacts/transformation-roadmap.md`](../artifacts/transformation-roadmap.md); [`economics/TRANSFORMATION_ECONOMICS.md`](../economics/TRANSFORMATION_ECONOMICS.md) §5) before `HG-BUDGET`;
7. for each Initiative proposed for selection, record at least a draft System Effect Assessment (skill 19; [`design/LOCAL_OPTIMIZATION_GUARD.md`](../design/LOCAL_OPTIMIZATION_GUARD.md) §4) before `HG-INITIATIVE` decides;
8. Governed profile: record Execution Gate A for each Initiative ([`artifacts/execution-gate.md`](../artifacts/execution-gate.md)), with evidence that its Gaps meet the Phase 2 readiness condition;
9. submit material selections, with their System Effect Assessments, and material budget for approval; the budget request cites each material Initiative's economic hypothesis;
10. once decided (material selections: after `HG-INITIATIVE`), set the Initiative `status: approved` and each Intervention's `status` to selected, deferred, or rejected, with `status_rationale`; an `AI_*` Intervention becomes selected only once its Authority Ceiling is approved.

## Outputs

- Initiative records (`INI-###`) in the Transformation Roadmap ([`artifacts/transformation-roadmap.md`](../artifacts/transformation-roadmap.md)), each material one with its `economic_hypothesis`;
- one System Effect Assessment per Initiative ([`artifacts/system-effect-assessment.md`](../artifacts/system-effect-assessment.md));
- Intervention status updates in the Intervention Map ([`artifacts/intervention-map.md`](../artifacts/intervention-map.md));
- Prioritization Matrix ([`artifacts/prioritization-matrix.md`](../artifacts/prioritization-matrix.md)), where the profile requires it (Standard, Portfolio); otherwise decisions and rationale sit in the Intervention Map and the selection Decision;
- Evidence Debt for each `investigate` decision ([`artifacts/evidence-register.md`](../artifacts/evidence-register.md));
- Governed: Execution Gate A per Initiative ([`artifacts/execution-gate.md`](../artifacts/execution-gate.md));
- Decision & Assumption Log ([`artifacts/decision-assumption-log.md`](../artifacts/decision-assumption-log.md)): selection and budget Decisions, provisional-selection review triggers, Assumptions.

## Human gates

- `HG-INITIATIVE` — stop with `HUMAN_DECISION_REQUIRED` until a Decision closing it lists the selected material `INI-###` in `subject_ids` ([`STANDARD.md`](../STANDARD.md) §8); the human decides with each Initiative's System Effect Assessment in hand.
- `HG-BUDGET` — when a selection commits material budget; the Decision cites each material Initiative's economic hypothesis as [`economics/TRANSFORMATION_ECONOMICS.md`](../economics/TRANSFORMATION_ECONOMICS.md) §5 specifies.

Any other gate applies whenever its trigger occurs.

## Exit condition

Matches [`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2:

```text
selected Initiatives recorded as INI records linked to Outcomes (expected_outcome_ids),
  Capabilities, Gaps (through their Interventions), Interventions, and Metrics (success_metric_ids)
AND expected system effects (INV-09) recorded per selected Initiative (SFX)
AND rejected and deferred candidates carry a rationale
AND material selection approved (HG-INITIATIVE)
AND no AI_* Intervention selected before its Authority Ceiling is approved
AND material budget approved (HG-BUDGET) by a Decision that cites each material
  Initiative's economic hypothesis (economic_hypothesis, economics/TRANSFORMATION_ECONOMICS.md §5)
AND Portfolio: no Initiative is selected while a portfolio/PORTFOLIO_PRIORITIZATION.md §5
  stop condition holds, unless an approved Decision of the portfolio owner records
  the override and its reason
```

Refinements: each selected Initiative also links Evidence (`evidence_ids`, or a visible `MISSING:` entry with Evidence Debt; INV-14, [`TRACEABILITY.md`](../TRACEABILITY.md) §4); a provisional selection carries its `review_trigger`; each `investigate` decision has its Evidence Debt item; Governed: Execution Gate A recorded per Initiative ([`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2).

In addition, as in every phase: facts and assumptions are separated; every material conclusion is traceable to Evidence (`EVD-###`) or labeled `[ASSUMPTION]` or `[HYPOTHESIS]` ([`AGENTS.md`](../AGENTS.md) §3); unresolved critical uncertainty is visible.

## Prohibited shortcut

Selecting an Initiative only because it is easy, visible, uses AI, or stakeholders like it ([`transition/TRANSFORMATION_SEQUENCING.md`](../transition/TRANSFORMATION_SEQUENCING.md) §5), or letting a numeric score replace written judgment.
