---
artifact_type: target-operating-architecture
framework_version: 1.1.0
status: canonical
entity: Target Operating Architecture
id_prefix: TOA
owner_module: design/TARGET_OPERATING_ARCHITECTURE.md
produced_by: [06-design-target-system, 20-design-target-operating-architecture]
---

# Target Operating Architecture

## Purpose

Describe the integrated target operating system across the relevant Capabilities, composed from their Capability Target States. Required from the Standard profile; in Compact, the Capability Target States stand in for it.

## Record

```yaml
target_operating_architecture:
  id: TOA-###
  outcome_ids: []
  value_stream_ids: []
  capability_ids: []
  target_state_ids: []        # STA-### (type TARGET) of every Capability in capability_ids
  system_constraint_ids: []   # CST-### the architecture addresses
  role_model:
  decision_model:             # Decision Rights: artifacts/decision-rights-map.md
  coordination_model:
  information_model:
  knowledge_model:
  application_model:
  automation_model:
  ai_model:
  governance_model:
  metric_model:
  metric_ids: []              # system-level Metrics (MET-###)
  economic_model:
  constraints: []             # design Constraints (ontology/ONTOLOGY.md)
  assumption_ids: []
  status: proposed | approved
```

## Rules

`status: approved` requires a Decision closing `HG-TOA` that lists this `TOA-###` in `subject_ids` ([`STANDARD.md`](../STANDARD.md) §8). Phase 6 relies only on an approved TOA.

Before approval, run the system checks in [`design/SYSTEM_TRANSFORMATION_MODEL.md`](../design/SYSTEM_TRANSFORMATION_MODEL.md) §6 and the consistency rules in [`design/TARGET_OPERATING_ARCHITECTURE.md`](../design/TARGET_OPERATING_ARCHITECTURE.md) §4.

## Validation

- [ ] composes the Capability Target State of every Capability in `capability_ids` (`target_state_ids`)
- [ ] role ownership, decision authority, information and knowledge ownership, and application boundaries are explicit
- [ ] AI authority does not exceed the approved Authority Ceilings ([`artifacts/autonomy-assessment.md`](autonomy-assessment.md))
- [ ] local metrics do not conflict with system Outcomes; system-level Metrics exist (`metric_ids`)
- [ ] pre-approval system checks done, including downstream capacity and likely Constraint Migration
- [ ] approved through `HG-TOA` before Phase 6 uses it
