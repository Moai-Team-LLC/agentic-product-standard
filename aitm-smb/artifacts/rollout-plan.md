---
artifact_type: rollout-plan
framework_version: 1.1.0
status: canonical
entity: Rollout Plan
id_prefix: ROL
owner_module: execution/ROLLOUT_MODEL.md
produced_by: [08-design-operating-model, 29-plan-rollout]
---

# Rollout Plan

## Purpose

Expand a validated transformation in controlled stages, each entered only after its gates are verified ([`execution/ROLLOUT_MODEL.md`](../execution/ROLLOUT_MODEL.md)).

## Record

```yaml
rollout:
  id: ROL-###
  initiative_id:            # INI-###
  pilot_id:                 # PLT-### the rollout follows; empty when no pilot was required
  promotion_decision_id:    # DEC-### closing HG-PROMOTION, for a material pilot; it records any waiver of unmet pilot criteria
  evaluation_ids: []        # EVL-### the promotion relied on
  current_scope:
  target_scope:
  stages:                   # progressive stages (execution/ROLLOUT_MODEL.md §4)
    - name:
      dimensions: []        # execution/ROLLOUT_MODEL.md §2 dimensions expanded in this stage
      scope:
      autonomy_level: L0 | L1 | L2 | L3 | L4 | L5   # within the Authority Ceiling
      gate_id:              # GAT-### (Gate E) for this stage, Governed
  entry_gates: []           # verified before every stage: at least execution/ROLLOUT_MODEL.md §3, plus stage-specific gates
  monitoring: []            # signals from the Observability Plan watched during rollout
  support_model:
  rollback:                 # execution/ROLLOUT_MODEL.md §5: return to the previous operating state
  recovery:                 # execution/ROLLOUT_MODEL.md §5: correct state and continue on the new system
  legacy_retirement:
  completion_criteria: []   # at least execution/ROLLOUT_MODEL.md §6
  owner:
```

## Rules

A rollout that follows a material pilot starts only after `HG-PROMOTION` ([`STANDARD.md`](../STANDARD.md) §8).

A stage whose `autonomy_level` is above the currently approved level (AUT `current_level`) requires `HG-AUTHORITY` before it starts (criteria: [`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md) §3 (b)) and MUST NOT exceed the Authority Ceiling ([`artifacts/autonomy-assessment.md`](autonomy-assessment.md)). A stage that only widens scope at the approved level, for the same action class and ceiling, is not an authority increase ([`STANDARD.md`](../STANDARD.md) §8).

Readiness is verified before each stage (skill 35; Governed: Gate E).

## Validation

- [ ] linked to one Initiative and, where a pilot preceded it, to that pilot, its evaluations, and the promotion Decision
- [ ] every stage names its dimensions and scope, and the [`execution/ROLLOUT_MODEL.md`](../execution/ROLLOUT_MODEL.md) §3 gates are verified before it starts
- [ ] no stage exceeds the Authority Ceiling; a stage above the approved level has an `HG-AUTHORITY` Decision
- [ ] rollback or recovery is stated for each material stage ([`execution/ROLLOUT_MODEL.md`](../execution/ROLLOUT_MODEL.md) §5)
- [ ] completion criteria cover [`execution/ROLLOUT_MODEL.md`](../execution/ROLLOUT_MODEL.md) §6
