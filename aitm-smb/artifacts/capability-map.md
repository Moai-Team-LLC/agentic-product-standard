---
artifact_type: capability-map
framework_version: 1.0.0
status: canonical
---

# Capability Map

## Purpose

Represent what the organization must be capable of doing, independently of current org chart or software.

## Record

```yaml
capability:
  id: CAP-###
  name:
  purpose:
  owner:
  outcome_ids: []
  value_stream_ids: []
  dependencies: []
  current_state_ref:
  target_state_ref:
  metric_ids: []
```

## Rules

A capability SHOULD:

- be phrased as an organizational ability;
- remain meaningful if people or software change;
- connect to at least one Outcome.

A capability SHOULD NOT be named after a tool or department unless the organizational ability is genuinely identical.
