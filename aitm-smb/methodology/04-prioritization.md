# Phase 4 — Decide (Prioritization)

## Objective

Select the Initiatives with the highest justified leverage from the candidate Interventions, and record a decision with rationale for every candidate.

## Required inputs

- candidate Interventions ready for prioritization (Intervention Map, Phase 3 exit);
- AI Suitability and Autonomy Assessments for `AI_*` candidates;
- approved Outcomes and their Metrics;
- economic assumptions (`ASM-###`) and the Evidence Register;
- System Constraint, where one has been identified;
- Transformation Portfolio, when the Portfolio profile is active and a portfolio exists.

## Method

Use:

1. `artifacts/prioritization-matrix.md` (dimensions)
2. `economics/TRANSFORMATION_ECONOMICS.md` §5 (economic hypothesis)
3. `design/CONSTRAINT_ANALYSIS.md` §6, when a System Constraint exists
4. `portfolio/PORTFOLIO_PRIORITIZATION.md`, when the Portfolio profile is active
5. `CORE_MODEL.md` §7 (Initiative record)

Selection is provisional when the profile requires a System Constraint (Standard and above) and none has been identified yet: the selection Decision carries a `review_trigger` naming the Phase 5 System Constraint and System Effect Assessments.

## Activities

1. group candidate Interventions into candidates: one or more Interventions that would be delivered together;
2. assess each candidate on the matrix dimensions, with ordinal values and written rationale; add Constraint Relevance where a System Constraint exists, and the portfolio criteria when the Portfolio profile is active;
3. prepare an economic hypothesis (`economics/TRANSFORMATION_ECONOMICS.md` §5) for each material candidate before `HG-BUDGET`;
4. decide per candidate: select, defer, reject, or investigate; record the rationale;
5. Portfolio profile: before adding an Initiative, check the stop conditions (`portfolio/PORTFOLIO_PRIORITIZATION.md` §5); while one holds, select only with a Decision recording the override;
6. for each selected candidate, create the Initiative record (`INI-###`, `status: proposed`) in the Transformation Roadmap with `intervention_ids`, `capability_ids`, `expected_outcome_ids`, `success_metric_ids`, `evidence_ids`, owner, and scope;
7. submit material selections and material budget for approval; the budget request cites the economic hypotheses from activity 3;
8. once decided (material selections: after `HG-INITIATIVE`), set the Initiative `status: approved` and each Intervention's `status` to selected, deferred, or rejected, with `status_rationale`.

## Outputs

- Initiative records (`INI-###`) in the Transformation Roadmap (`artifacts/transformation-roadmap.md`);
- Intervention status updates in the Intervention Map (`artifacts/intervention-map.md`);
- Prioritization Matrix (`artifacts/prioritization-matrix.md`), where the profile requires it (Standard, Portfolio); otherwise decisions and rationale sit in the Intervention Map and the selection Decision;
- economic hypotheses (`economics/TRANSFORMATION_ECONOMICS.md` §5) for material candidates;
- Decision & Assumption Log (`artifacts/decision-assumption-log.md`): selection and budget Decisions, provisional-selection review triggers, Assumptions.

## Human gates

- `HG-INITIATIVE` — stop with `HUMAN_DECISION_REQUIRED` until a Decision closing it lists the selected material `INI-###` in `subject_ids` (`STANDARD.md` §8).
- `HG-BUDGET` — when a selection commits material budget; the Decision cites each material candidate's economic hypothesis as `economics/TRANSFORMATION_ECONOMICS.md` §5 specifies.

Any other gate applies whenever its trigger occurs.

## Exit condition

Matches `EXECUTION_MODEL.md` §2:

```text
selected Initiatives recorded as INI records linked to Outcomes (expected_outcome_ids),
  Capabilities, Gaps (through their Interventions), Interventions, and Metrics (success_metric_ids)
AND rejected and deferred candidates carry a rationale
AND material selection approved (HG-INITIATIVE)
AND material budget approved (HG-BUDGET) by a Decision that cites each material
  candidate's economic hypothesis (economics/TRANSFORMATION_ECONOMICS.md §5)
AND Portfolio: no Initiative is selected while a portfolio/PORTFOLIO_PRIORITIZATION.md §5
  stop condition holds, unless a DEC records the override
```

Refinements: each selected Initiative also links Evidence (`evidence_ids`, or a visible `MISSING:` entry with Evidence Debt; INV-14, `TRACEABILITY.md` §4); a provisional selection carries its `review_trigger`.

In addition, as in every phase: facts and assumptions are separated; every material conclusion is traceable to Evidence (`EVD-###`) or labeled `[ASSUMPTION]` or `[HYPOTHESIS]` (`AGENTS.md` §3); unresolved critical uncertainty is visible.

## Prohibited shortcut

Selecting an Initiative only because it is easy, visible, uses AI, or stakeholders like it (`transition/TRANSFORMATION_SEQUENCING.md` §5), or letting a numeric score replace written judgment.
