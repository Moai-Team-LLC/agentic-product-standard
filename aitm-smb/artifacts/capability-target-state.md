---
artifact_type: capability-target-state
framework_version: 1.0.0
status: canonical
entity: State
id_prefix: STA
---

# Capability Target State

## Purpose

Describe the required future behavior of one Business Capability.

This artifact is capability-scoped.

It MUST NOT be used as a substitute for the system-level Target Operating Architecture.

## Contract

```yaml
target_state:
  id: STA-###
  type: TARGET
  capability_id: CAP-###
  outcome_ids: []
  people:
  decisions:
  process:
  data:
  knowledge:
  applications:
  automation:
  ai:
  controls:
  metrics: []
  assumptions: []
  constraints: []
```

## Target capability statement

```text
The organization can <perform ability>
at <required quality / speed / cost>
under <constraints>
without <current structural limitation>.
```

## AI authority

Where AI is present:

```yaml
authority:
  may_read: []
  may_recommend: []
  may_execute: []
  prohibited: []
  approval_required: []
  escalation: []
  verification: []
```

## Validation

- [ ] linked to at least one Outcome
- [ ] closes one or more diagnosed Gaps
- [ ] Decision Rights are explicit
- [ ] AI authority is explicit where relevant
- [ ] required information and knowledge are explicit
- [ ] metrics are explicit
