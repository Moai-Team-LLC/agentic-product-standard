# Phase 0 — Frame (Transformation Intent)

## Objective

Define why transformation is being considered, which measurable Outcomes matter, who owns them, and which Application Profiles apply.

## Required inputs

- business context supplied by the accountable owner;
- access to the owner and relevant stakeholders;
- direct evidence where available;
- explicit assumptions where evidence is absent.

## Method

Use:

1. `CORE_MODEL.md` §1 (Outcome)
2. `METRICS.md` (baselines)
3. `PROFILE_SELECTION.md`, through `skills/36-select-application-profile/SKILL.md`
4. `evidence/EVIDENCE_STANDARD.md`
5. `STANDARD.md` §16 (materiality)

## Activities

1. identify the business problem or opportunity and why it matters now;
2. define the desired Outcomes as Outcome records (`OUT-###`) with owner, baseline or known baseline gap, target, and horizon;
3. record measured baselines as Metrics (`MET-###`); record unmeasured baselines as Evidence Debt;
4. identify constraints and non-goals;
5. establish success and failure criteria (Outcome targets and their Metrics);
6. select the Application Profiles with skill 36 and record the selection as a Decision; it stays provisional until `HG-OUTCOME`;
7. optionally record materiality thresholds as a Decision (`STANDARD.md` §16);
8. submit the Outcomes and the profile Decision for approval.

## Outputs

- Transformation Intent (`artifacts/transformation-intent.md`) with Outcome records and constraints;
- baseline Metric records (`METRICS.md` §6) where a baseline is measured;
- Evidence and Evidence Debt (`artifacts/evidence-register.md`);
- Decision & Assumption Log (`artifacts/decision-assumption-log.md`): profile Decision, `HG-OUTCOME` approval, Assumptions.

## Human gates

- `HG-OUTCOME` — stop with `HUMAN_DECISION_REQUIRED` until a Decision closing it lists the `OUT-###` IDs and the profile Decision in `subject_ids` (`STANDARD.md` §8).

Any other gate applies whenever its trigger occurs.

## Exit condition

Matches `EXECUTION_MODEL.md` §2:

```text
Outcome records (OUT) with owner, baseline or known baseline gap, target, horizon
AND constraints recorded
AND Application Profiles selected (DEC)
AND Outcomes approved (HG-OUTCOME)
```

In addition, as in every phase: facts and assumptions are separated; every material conclusion is traceable to Evidence (`EVD-###`) or labeled `[ASSUMPTION]` or `[HYPOTHESIS]` (`AGENTS.md` §3); unresolved critical uncertainty is visible.

## Prohibited shortcut

Proceeding without a meaningful business Outcome or an accountable owner. An Outcome that is a means (adopt AI, deploy agents, automate more, use a specific vendor) is not an Outcome (`CORE_MODEL.md` §1). Stop instead.
