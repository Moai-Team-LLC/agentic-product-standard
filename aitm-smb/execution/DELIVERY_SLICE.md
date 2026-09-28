# Transformation Slice

## 1. Purpose

A Transformation Slice (`SLC-###`) is the smallest implementation unit that changes a real business behavior and can be evaluated.

It is vertical: it crosses every layer needed to change that behavior (`execution/EXECUTION_PRINCIPLES.md` §2). Also called a vertical slice or delivery slice.

---

## 2. Slice contract

```yaml
slice:
  id: SLC-###
  initiative_id:
  capability_ids: []
  behavior_change:
  scope:
  process_changes: []
  role_changes: []
  decision_changes: []
  data_changes: []
  knowledge_changes: []
  application_changes: []
  automation_changes: []
  ai_changes: []
  control_changes: []
  metric_ids: []
  tests: []
  rollout:
  rollback:
  owner:
```

Only the layers the slice changes need content.

---

## 3. Definition of Done

A slice is done only when:

```text
implemented
AND verified
AND observable
AND operational ownership assigned
AND documentation updated
AND required controls operate
```

If it changes AI behavior:

```text
evaluation also required
```
