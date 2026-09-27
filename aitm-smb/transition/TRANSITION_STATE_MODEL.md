# Transition State Model

## 1. Purpose

AITM-SMB transforms an operating system through explicit intermediate states.

The target state is rarely reachable safely in one step.

---

## 2. State sequence

```text
Current State
→ Transition State 1
→ Transition State 2
→ ...
→ Target State
```

Each Transition State MUST be independently operable.

---

## 3. Transition State contract

```yaml
transition_state:
  id: STA-###
  name:
  predecessor:
  successor:
  capability_changes: []
  role_changes: []
  decision_right_changes: []
  process_changes: []
  data_changes: []
  application_changes: []
  ai_changes: []
  governance_changes: []
  evidence_to_collect: []
  entry_conditions: []
  exit_conditions: []
  rollback_or_recovery:
```

---

## 4. Transition design principles

Prefer states that are:

```text
operable
observable
reversible where possible
bounded
measurable
safe under partial adoption
```

---

## 5. Shadow State

For high uncertainty, introduce a shadow state:

```text
AI / new process runs
but does not control production action
```

Use it to evaluate:

```text
quality
latency
cost
policy compliance
exception rate
```

before authority increases.

---

## 6. Parallel State

Old and new systems may temporarily coexist.

This is justified when:

```text
migration risk is high
data conversion is uncertain
behavior requires comparison
rollback must remain possible
```

Parallel operation has cost and SHOULD be time-bounded.

---

## 7. Authority transition

Authority MAY increase across states:

```text
L1 Suggest
→ L2 Draft
→ L3 Execute with approval
→ L4 Bounded execution
```

Authority SHOULD NOT jump directly to the maximum technically possible level.

---

## 8. Transition-state failure

A Transition State is invalid if:

```text
the business cannot operate in it
ownership is ambiguous
critical metrics cannot be observed
failure cannot be contained
or exit conditions are undefined
```
