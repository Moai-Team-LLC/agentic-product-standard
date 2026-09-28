# Phase 0 — Frame (Transformation Intent)

## Objective

Define why transformation is being considered, which measurable Outcomes matter, who owns them, and which Application Profiles apply.

## Required inputs

- business context supplied by the accountable owner;
- access to the owner and relevant stakeholders;
- direct evidence where available;
- where evidence is absent, Assumptions the owner states or accepts ([`evidence/EVIDENCE_STANDARD.md`](../evidence/EVIDENCE_STANDARD.md) §7).

## Method

Use:

1. [`CORE_MODEL.md`](../CORE_MODEL.md) §1 (Outcome)
2. [`METRICS.md`](../METRICS.md) (baselines)
3. [`PROFILE_SELECTION.md`](../PROFILE_SELECTION.md), through [`skills/36-select-application-profile/SKILL.md`](../skills/36-select-application-profile/SKILL.md)
4. [`evidence/EVIDENCE_STANDARD.md`](../evidence/EVIDENCE_STANDARD.md)
5. [`STANDARD.md`](../STANDARD.md) §16 (materiality)

## Activities

1. identify the business problem or opportunity and why it matters now;
2. define the desired Outcomes as Outcome records (`OUT-###`) with owner, baseline or known baseline gap, target, and horizon;
3. record a Metric (`MET-###`) for each Outcome; where its baseline is unmeasured, `baseline` holds `MISSING:<reason>` and an Evidence Debt item is recorded ([`METRICS.md`](../METRICS.md) §7);
4. identify constraints and non-goals;
5. establish success and failure criteria (Outcome targets and their Metrics);
6. select the Application Profiles with skill 36 and record the selection as a Decision; it stays `status: proposed` until approved together with `HG-OUTCOME`;
7. optionally record materiality thresholds as a Decision ([`STANDARD.md`](../STANDARD.md) §16);
8. submit the Outcomes and the profile Decision for approval.

## Outputs

- Transformation Intent ([`artifacts/transformation-intent.md`](../artifacts/transformation-intent.md)) with Outcome records and constraints;
- Metric records ([`METRICS.md`](../METRICS.md) §6), at least one per Outcome, in the Transformation Scorecard ([`artifacts/transformation-scorecard.md`](../artifacts/transformation-scorecard.md));
- Evidence and Evidence Debt ([`artifacts/evidence-register.md`](../artifacts/evidence-register.md));
- Decision & Assumption Log ([`artifacts/decision-assumption-log.md`](../artifacts/decision-assumption-log.md)): profile Decision, `HG-OUTCOME` approval, Assumptions.

## Human gates

- `HG-OUTCOME` — stop with `HUMAN_DECISION_REQUIRED` until a Decision closing it lists the `OUT-###` IDs and the profile Decision in `subject_ids`, or the profile Decision is approved by a separate Decision ([`STANDARD.md`](../STANDARD.md) §8).

Any other gate applies whenever its trigger occurs.

## Exit condition

Matches [`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2:

```text
Outcome records (OUT) with owner, baseline or known baseline gap, target, horizon
AND a Metric record (MET) for every Outcome; an unmeasured baseline holds
  MISSING:<reason> with an Evidence Debt item (METRICS.md §7)
AND constraints recorded
AND Application Profiles selected (DEC)
AND Outcomes and the profile Decision approved with HG-OUTCOME (one Decision
  listing both, or a separate Decision approving the profile)
```

An Outcome baseline resting only on agent inference does not satisfy this exit ([`AGENTS.md`](../AGENTS.md) §3).

In addition, as in every phase: facts and assumptions are separated; every material conclusion is traceable to Evidence (`EVD-###`) or labeled `[ASSUMPTION]` or `[HYPOTHESIS]` ([`AGENTS.md`](../AGENTS.md) §3); unresolved critical uncertainty is visible.

## Prohibited shortcut

Proceeding without a meaningful business Outcome or an accountable owner. An Outcome that is a means (adopt AI, deploy agents, automate more, use a specific vendor) is not an Outcome ([`CORE_MODEL.md`](../CORE_MODEL.md) §1). Stop instead.
