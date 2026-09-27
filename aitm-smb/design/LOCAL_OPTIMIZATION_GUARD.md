# Local Optimization Guard

## 1. Purpose

AITM-SMB prevents local improvement from degrading the wider operating system.

---

## 2. Required challenge

For every selected Initiative ask:

```text
What new demand will this create?
Which downstream capability receives it?
Which upstream capability must support it?
What shared resource becomes more constrained?
Which metric may be gamed?
Which role absorbs new exceptions?
```

---

## 3. Common local-optimization failures

### Faster intake, unchanged delivery

```text
intake throughput ↑
delivery capacity unchanged
→ backlog ↑
```

### More AI-generated work, unchanged review

```text
generation throughput ↑
review capacity unchanged
→ queue ↑
```

### More automation, weaker exception handling

```text
routine work ↓
exception complexity ↑
expert burden ↑
```

### Better local KPI, worse system outcome

```text
support closes tickets faster
but repeat contact increases
```

---

## 4. System effect record

```yaml
system_effect:
  initiative_id:
  upstream_effects: []
  downstream_effects: []
  shared_resource_effects: []
  constraint_migration:
  incentive_risks: []
  mitigation:
```

---

## 5. Approval rule

A material Initiative SHOULD NOT be approved until expected system effects are considered.
