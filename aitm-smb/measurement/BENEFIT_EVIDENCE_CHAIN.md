# Benefit Evidence Chain

## 1. Purpose

Connect technical change to business effect.

---

## 2. Chain

```text
Technical / Process Change
→ Behavior Change
→ Capability Performance Change
→ Business Outcome Change
→ Economic Value
```

---

## 3. Record

```yaml
benefit_chain:
  initiative_id:
  change:                     # technical / process change delivered
  expected_behavior_change:
  capability_metric:          # MET-###
  outcome_metric:             # MET-###
  economic_effect:
  evidence_ids: []            # Evidence for each link of the chain
  attribution_confidence:     # LOW | MEDIUM | HIGH (measurement/VALUE_REALIZATION.md §4)
```

Instances: the `benefit_chain` of a Value Realization record (`artifacts/value-realization-report.md`). Required with the Measured profile (`APPLICATION_PROFILES.md`).

A link without Evidence stays visible as a missing link (`TRACEABILITY.md` §4).

---

## 4. Rule

AITM-SMB does not accept:

```text
"agent deployed"
```

as evidence that value was realized.
