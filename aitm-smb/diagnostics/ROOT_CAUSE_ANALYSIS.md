# Root Cause Analysis

## 1. Purpose

AITM-SMB distinguishes:

```text
Observation
≠ Symptom
≠ Gap
≠ Cause
```

This prevents automating symptoms.

---

## 2. Root-cause ladder

For every material Symptom ask:

```text
What directly causes this condition?
What system condition allows that cause to persist?
What architectural condition created that system behavior?
```

Example:

```text
Symptom:
quotes take 3 days

Direct cause:
founder approval queue

System condition:
pricing judgment is centralized

Architectural condition:
pricing rules and exception boundaries are tacit
```

The intervention should address the lowest useful causal layer, not necessarily the visible symptom.

---

## 3. Cause classes

AITM-SMB uses these common cause classes:

```text
DEMAND
FLOW
OWNERSHIP
DECISION_RIGHTS
INFORMATION
KNOWLEDGE
PROCESS_DESIGN
SYSTEM_BOUNDARY
INTEGRATION
AUTOMATION
CONTROL
INCENTIVE
SKILL
CAPACITY
MEASUREMENT
FEEDBACK
```

AI is not a cause class.

"Lack of AI" is generally not a valid root cause.

---

## 4. Evidence test

For every Cause Hypothesis ask:

```text
What evidence would support this?
What evidence would falsify this?
What competing explanation exists?
What would we observe if this were not the cause?
```

---

## 5. Intervention trap test

Before solving, ask:

```text
If this intervention succeeds technically,
could the business problem remain unchanged?
```

If yes, diagnosis is probably incomplete.

---

## 6. Multi-cause gaps

A Gap may have multiple causes.

Example:

```text
Capability:
Customer Issue Resolution

Gap:
resolution time too high

Causes:
- fragmented knowledge
- poor routing
- unclear escalation authority
- missing customer context
```

A single AI assistant may improve only one cause.

---

## 7. Root-cause confidence

```yaml
cause:
  hypothesis_id:
  gap_id:
  cause_class:
  statement:
  evidence_for: []
  evidence_against: []
  alternative_causes: []
  validation_method:
  confidence: low | medium | high
  status: hypothesized | tested | validated | rejected
```
