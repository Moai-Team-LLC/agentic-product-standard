# Rollout Model

## 1. Purpose

Rollout expands a validated transformation while preserving control.

---

## 2. Rollout dimensions

Expansion may occur by:

```text
user group
customer segment
transaction class
geography
workflow scope
data scope
AI capability
autonomy level
```

---

## 3. Rollout gates

Before expanding scope verify:

```text
pilot success criteria met
failure modes understood
monitoring active
ownership assigned
support path exists
rollback/recovery exists
governance controls operate
cost envelope acceptable
```

---

## 4. Progressive rollout

Preferred pattern:

```text
small cohort
→ broader cohort
→ default path
→ legacy path retired
```

---

## 5. Rollback versus recovery

### Rollback

Return to the previous operating state.

### Recovery

Continue with the new system after correcting state or handling failure.

Every material rollout SHOULD know which is possible.

---

## 6. Rollout completion

Rollout is complete only when:

```text
target scope operates on new model
old temporary paths are retired or explicitly retained
ownership is transferred to operations
metrics are stable
known risks are accepted
```
