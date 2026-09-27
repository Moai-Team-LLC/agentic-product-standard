# Pilot Model

## 1. Purpose

A Pilot is a bounded operational test of a transformation hypothesis under real or production-representative conditions.

A pilot is not:

```text
demo
prototype
proof that the model can respond
```

It must test business-system behavior.

---

## 2. Pilot contract

```yaml
pilot:
  id: PLT-###
  initiative_id:
  hypothesis_ids: []
  capability_ids: []
  target_outcomes: []
  scope:
  participants:
  duration_or_volume:
  baseline:
  intervention:
  control_or_comparison:
  metrics: []
  risks: []
  guardrails: []
  rollback:
  success_criteria: []
  stop_criteria: []
  evidence_plan:
  owner:
```

---

## 3. Pilot types

### Shadow Pilot

New behavior runs without controlling production action.

Use for:

```text
quality evaluation
recommendation quality
routing accuracy
prediction
policy compliance
```

### Assisted Pilot

AI or new system assists humans while humans retain authority.

### Controlled Execution Pilot

System executes within a small bounded domain with explicit approval or policy.

### Limited Autonomous Pilot

Agentic execution is allowed within narrow permissions and strong observability.

---

## 4. Pilot scope

A pilot SHOULD constrain some combination of:

```text
users
customers
transactions
geography
workflow type
risk class
time window
autonomy level
```

---

## 5. Pilot validity

A pilot is invalid if:

```text
success criteria are defined after results
baseline is absent without acknowledged evidence debt
production behavior differs materially from test behavior
participants can bypass the intended workflow without measurement
or only AI-quality metrics are observed
```

---

## 6. Pilot result

```text
PROMOTE
REVISE
REPEAT
STOP
INSUFFICIENT_EVIDENCE
```
