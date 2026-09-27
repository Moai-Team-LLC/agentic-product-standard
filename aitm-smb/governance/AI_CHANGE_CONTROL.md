# AI Change Control

## 1. Purpose

AI system behavior can change even when business code does not.

Change control SHOULD consider:

```text
model
provider
prompt
system instruction
retrieval logic
knowledge corpus
toolset
permission scope
evaluation rubric
workflow
memory behavior
```

---

## 2. Change classes

### Low

Small reversible change with low business impact.

### Medium

Change that may affect quality, cost, or workflow behavior.

### High

Change affecting:

```text
authority
critical customer behavior
financial decisions
security
data access
legal exposure
high-risk process
```

---

## 3. Change record

```yaml
ai_change:
  id: CHG-###
  component:
  class:
  reason:
  expected_effect:
  evaluation_required:
  rollout_required:
  approval_required:
  rollback:
  evidence:
```

---

## 4. Rule

A model upgrade is not automatically a low-risk change.
