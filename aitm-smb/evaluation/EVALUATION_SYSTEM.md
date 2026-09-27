# Evaluation System

## 1. Purpose

AITM-SMB evaluates both:

```text
business-system effect
and
AI-component quality
```

These are separate but connected.

---

## 2. Evaluation layers

```text
L1 Business Outcome
L2 Capability Performance
L3 Operating Performance
L4 Human-AI Interaction
L5 AI Task Quality
L6 Technical Reliability
L7 Economics
L8 Risk / Governance
```

---

## 3. Evaluation questions

### Business Outcome

Did the intended business result improve?

### Capability

Can the organization now perform the capability at the required level?

### Operating

Did cycle time, cost, throughput, rework, or exception load change?

### Human-AI

Are roles, trust, overrides, and escalation working?

### AI Task

Does the model perform the bounded task well enough?

### Technical

Is the system available, observable, and reliable?

### Economics

Is cost per successful outcome acceptable?

### Governance

Are policies, permissions, and audit expectations met?

---

## 4. Evaluation record

```yaml
evaluation:
  id: EVL-###
  initiative_id:
  layer:
  metric_ids: []
  method:
  sample:
  threshold:
  actual:
  conclusion:
  limitations:
  evidence_ids: []
```

---

## 5. Evaluation conclusion

Use:

```text
PASS
PASS_WITH_LIMITATIONS
FAIL
INSUFFICIENT_EVIDENCE
```

A passing AI evaluation does not imply a passing business evaluation.
