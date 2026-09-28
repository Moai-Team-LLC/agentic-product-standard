---
artifact_type: transformation-intent
framework_version: 1.1.0
status: canonical
entity: Transformation Intent
id_prefix: ATI
owner_module: methodology/00-intent.md
produced_by: [01-discover-transformation, 38-audit-conformance]
---

# Transformation Intent

## Purpose

Frame the transformation problem and its Outcomes before any solution is designed. It holds the engagement's Outcome records and, once audited, its conformance declaration.

## Record

```yaml
intent:
  id: ATI-###
  problem_statement:
  business_context:          # including why now
  owner:                     # accountable Outcome owner
  horizon:
  outcomes: []               # Outcome records, CORE_MODEL.md §1
  baseline_metric_ids: []    # MET-### carrying the Outcome baselines, where measured (METRICS.md §6)
  constraints: []
  non_goals: []
  known_risks: []
  profile_decision_id:       # DEC-### selecting the Application Profiles (skill 36)
  evidence_ids: []
  assumption_ids: []
  conformance:               # CONFORMANCE.md §5 declaration; written by skill 38
```

Record contracts: Outcome `CORE_MODEL.md` §1; Metric `METRICS.md` §6 (records held in the Transformation Scorecard); conformance declaration `CONFORMANCE.md` §5. A baseline not yet measured is stated as a known baseline gap in the Outcome `baseline` and recorded as Evidence Debt (`evidence/EVIDENCE_STANDARD.md` §5).

## Required questions

1. What business result must change?
2. Why now?
3. What evidence shows the current state?
4. Who owns the result?
5. What is explicitly out of scope?
6. What constraints cannot be ignored?

## Rules

This artifact is incomplete if the stated goal is only:

```text
introduce AI
automate processes
build agents
increase AI adoption
```

Such goals are means, not Outcomes (`CORE_MODEL.md` §1).

Outcomes are approved only by a Decision closing `HG-OUTCOME` (`STANDARD.md` §8) that lists their `OUT-###` IDs and the profile Decision in `subject_ids`.

## Validation

- [ ] every Outcome has an owner, a baseline or known baseline gap, a target, and a horizon
- [ ] no Outcome is a means (adopt AI, deploy agents, automate more, use a vendor)
- [ ] constraints and non-goals are recorded
- [ ] the profile Decision is referenced
- [ ] Outcomes are approved through `HG-OUTCOME` before downstream use
