---
artifact_type: pilot-plan
framework_version: 1.1.0
status: canonical
entity: Pilot
id_prefix: PLT
owner_module: execution/PILOT_MODEL.md
produced_by: [07-build-roadmap, 25-design-pilot]
---

# Pilot Plan

## Purpose

Define a bounded operational test of a transformation Hypothesis under real or production-representative conditions (`execution/PILOT_MODEL.md` §1), fixed before the pilot runs.

## Record

```yaml
pilot:
  id: PLT-###
  initiative_id:            # INI-###
  hypothesis_ids: []        # HYP-### tested
  capability_ids: []        # CAP-###
  outcome_ids: []           # OUT-### the pilot targets
  pilot_type: shadow | assisted | controlled_execution | limited_autonomous   # execution/PILOT_MODEL.md §3
  autonomy_level: L0 | L1 | L2 | L3 | L4 | L5   # highest level the pilot operates at
  scope:                    # dimensions constrained (execution/PILOT_MODEL.md §4)
  participants:
  duration_or_volume:
  baseline:                 # MET-### baselines, or the recorded baseline gap
  intervention:             # the change applied: INT-### and a short description
  control_or_comparison:    # comparison method: control group, prior period, shadow comparison
  metric_ids: []            # MET-###
  risks: []                 # RSK-### (artifacts/decision-assumption-log.md)
  guardrails: []
  rollback:
  success_criteria: []      # fixed before execution
  stop_criteria: []         # fixed before execution
  evidence_plan:            # evidence to collect; evaluations are pre-registered in the Evaluation Plan
  owner:
  decision_owner:           # human who decides promotion after the pilot (HG-PROMOTION)
```

Level meanings: `diagnostics/AUTONOMY_SUITABILITY.md` §2.

## Rules

The pilot's evaluations are pre-registered in `artifacts/evaluation-plan.md` (`pilot_id` set) before the pilot runs. Its result is recorded there as `pilot_result`.

`autonomy_level` MUST NOT exceed the approved Authority Ceiling (`artifacts/autonomy-assessment.md`). A level above the currently approved one requires a Decision closing `HG-AUTHORITY` before the pilot starts; accepting a material Risk (`RSK-###`) requires `HG-RISK` (`STANDARD.md` §8).

Governed: Execution Gate C (`artifacts/execution-gate.md`) passes before the pilot starts.

## Validation

- [ ] linked to one Initiative, the Hypotheses it tests, its Capabilities, and its Outcomes
- [ ] pilot type and autonomy level stated; the level is within the Authority Ceiling and approved
- [ ] baseline (or Evidence Debt for its absence) and comparison method stated
- [ ] success and stop criteria and the Evaluation Plan are fixed before execution
- [ ] none of the invalidity conditions in `execution/PILOT_MODEL.md` §5 holds
- [ ] guardrails, rollback, owner, and decision owner are named
