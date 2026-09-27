# Agentic Autonomy Suitability

## 1. Purpose

AITM-SMB separates:

```text
AI usefulness
from
AI authority
```

A task may be a strong AI fit but a poor autonomy fit.

---

## 2. Autonomy ladder

```text
L0 — No AI
L1 — Suggest
L2 — Draft
L3 — Execute with explicit approval
L4 — Execute within bounded policy
L5 — Pursue bounded objective and escalate exceptions
```

---

## 3. Autonomy dimensions

Evaluate:

```text
Action Reversibility
Financial Impact
Customer Impact
Legal Impact
Security Impact
Decision Ambiguity
Policy Clarity
Observability
Verification Quality
Exception Detectability
Recovery Quality
Identity / Permission Precision
```

---

## 4. Autonomy-positive conditions

Higher autonomy is more defensible when:

```text
actions are reversible
impact is bounded
policy is explicit
exceptions are detectable
outputs are observable
quality can be evaluated
recovery is reliable
permissions are narrow
```

---

## 5. Autonomy-negative conditions

Lower autonomy is preferred when:

```text
actions are irreversible
financial commitment is material
legal rights are affected
safety risk exists
identity or permissions are ambiguous
evaluation is weak
failure may remain invisible
exceptions are common
```

---

## 6. Authority ceiling

Each capability SHOULD define an authority ceiling:

```yaml
authority_ceiling:
  capability_id:
  max_autonomy_level:
  prohibited_actions: []
  approval_required: []
  rationale:
  owner:
```

No technical implementation may exceed the approved ceiling.

---

## 7. Autonomy assessment

```yaml
autonomy_assessment:
  intervention_id:
  recommended_level:
  max_allowed_level:
  reversibility:
  impact:
  policy_clarity:
  observability:
  verification:
  recoverability:
  escalation:
  rationale:
```
