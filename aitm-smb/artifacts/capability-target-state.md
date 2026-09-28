---
artifact_type: capability-target-state
framework_version: 1.1.0
status: canonical
entity: State
id_prefix: STA
owner_module: design/TARGET_STATE_DESIGN.md
produced_by: [06-design-target-system, 15-design-target-state]
---

# Capability Target State

## Purpose

Describe the required future behavior of one Business Capability: its State of type TARGET.

This artifact is capability-scoped. It MUST NOT be used as a substitute for the system-level Target Operating Architecture ([`STANDARD.md`](../STANDARD.md) §7).

## Record

Record contract: State [`CORE_MODEL.md`](../CORE_MODEL.md) §3, with `type: TARGET` and `as_of` set to the intended horizon. One per selected Capability, referenced by the Capability's `target_state_id`.

Extends `state` with:

```yaml
state:
  statement:                  # target capability statement (design/TARGET_STATE_DESIGN.md §2)
  outcome_ids: []             # OUT-### this target serves
  gap_ids: []                 # GAP-### this target closes
  constraints: []             # design Constraints the target respects (ontology/ONTOLOGY.md)
  ai_authority:               # where AI is present: one entry per action class
    - action_class:
      autonomy_assessment_id: # AUT-### holding the Authority Ceiling for this action class
      target_level: L0 | L1 | L2 | L3 | L4 | L5
      may_read: []
      may_recommend: []
      may_execute: []
      prohibited_actions: []
      approval_required: []
      escalation_conditions: []
      verification: []
```

Fill the State dimensions as [`design/TARGET_STATE_DESIGN.md`](../design/TARGET_STATE_DESIGN.md) §3 describes. `people` includes ownership of target work; `applications` includes system boundaries ([`design/APPLICATION_BOUNDARIES.md`](../design/APPLICATION_BOUNDARIES.md)); `ai` describes the AI role.

## Rules

`target_level` MUST NOT exceed the approved `maximum_allowed_level` of the referenced Autonomy Assessment ([`artifacts/autonomy-assessment.md`](autonomy-assessment.md)), and `prohibited_actions` include the ceiling's. A level above the ceiling requires re-assessing the ceiling first ([`diagnostics/AUTONOMY_SUITABILITY.md`](../diagnostics/AUTONOMY_SUITABILITY.md) §6).

A target level is a design. AI authority takes effect only through `HG-AUTHORITY` ([`STANDARD.md`](../STANDARD.md) §8).

In the Compact profile, approval of the Capability Target States closes `HG-TOA`.

## Validation

- [ ] `type: TARGET`, one `capability_id`, and that Capability's `target_state_id` points to this record
- [ ] linked to at least one Outcome (`outcome_ids`) and closes at least one diagnosed Gap (`gap_ids`)
- [ ] complete per [`design/TARGET_STATE_DESIGN.md`](../design/TARGET_STATE_DESIGN.md) §6, including `statement`, ownership, decision rights, required information and knowledge, and system boundaries
- [ ] where AI is present, every action class has an `ai_authority` entry whose `target_level` is within the approved Authority Ceiling
- [ ] Metrics explicit (`metric_ids`)
