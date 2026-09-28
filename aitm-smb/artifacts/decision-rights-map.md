---
artifact_type: decision-rights-map
framework_version: 1.1.0
status: canonical
entity: Business Decision
id_prefix: BDS
owner_module: design/DECISION_RIGHTS_ARCHITECTURE.md
produced_by: [06-design-target-system, 23-design-decision-rights]
---

# Decision Rights Map

## Purpose

Make explicit who, or what, is allowed to make each material operational business decision today and in the target state. Engagement decisions (`DEC-###`) belong in `artifacts/decision-assumption-log.md`.

## Record

```yaml
business_decision:
  id: BDS-###
  name:
  capability_id:
  part_of:                    # BDS-### of the compound decision this one decomposes, if any
  decision_owner:             # role accountable for the decision in the target state
  current_authority:          # one authority model (design/DECISION_RIGHTS_ARCHITECTURE.md §3)
  target_authority:           # one authority model; its autonomy level stays within the Authority Ceiling
  autonomy_assessment_id:     # AUT-### whose Authority Ceiling bounds target_authority, where AI takes part
  information_required: []
  knowledge_required: []
  policy_constraints: []
  frequency:
  impact:
  escalation:
  metric_ids: []
```

## Rules

The autonomy level of `target_authority` (`design/DECISION_RIGHTS_ARCHITECTURE.md` §3) MUST NOT exceed `maximum_allowed_level` of the referenced Autonomy Assessment.

A material change from `current_authority` to `target_authority` takes effect only through a Decision closing `HG-DECISION-RIGHTS` that lists the `BDS-###` in `subject_ids`; an increase in AI authority also requires `HG-AUTHORITY` (`STANDARD.md` §8).

## Validation

- [ ] every material business decision has a record with a named `decision_owner`
- [ ] `current_authority` and `target_authority` are authority models from `design/DECISION_RIGHTS_ARCHITECTURE.md` §3
- [ ] where AI takes part, `autonomy_assessment_id` is set and the target level does not exceed the approved ceiling
- [ ] information, knowledge, policy, and escalation requirements are explicit
- [ ] compound decisions are decomposed where authority differs between parts (`part_of`)
