# Role Transition Model

## 1. Purpose

AI transformation can remove tasks without removing the need for a role, and can create new responsibilities.

---

## 2. Task disposition

For each affected task classify:

```text
RETAIN
ASSIST
AUTOMATE
TRANSFER
ELIMINATE
CREATE_NEW
```

---

## 3. Role transition record

```yaml
role_transition:
  role:
  current_responsibilities: []
  target_responsibilities: []
  removed_tasks: []
  new_tasks: []
  decision_right_changes: []
  skill_changes: []
  performance_metric_changes: []
  risks: []
```

---

## 4. New responsibilities commonly created by AI

```text
exception handling
knowledge curation
evaluation
policy ownership
AI quality review
workflow improvement
incident response
```

---

## 5. Rule

AITM-SMB SHOULD make role changes explicit before rollout.

Hidden role redesign creates adoption failure.
