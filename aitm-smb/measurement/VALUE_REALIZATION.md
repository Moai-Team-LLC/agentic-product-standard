# Value Realization Model

## 1. Purpose

AITM-SMB distinguishes projected value from realized value.

---

## 2. Value states

```text
HYPOTHESIZED
BASELINED
OBSERVED
ATTRIBUTED
REALIZED
SUSTAINED
```

---

## 3. Value record

```yaml
value_realization:
  initiative_id:
  outcome_id:
  metric_id:
  baseline:
  target:
  observed:
  attribution_confidence:
  implementation_cost:
  operating_cost:
  realized_value:
  sustainability_period:
  conclusion:
```

---

## 4. Attribution

Not every observed improvement was caused by the transformation.

Record attribution confidence:

```text
LOW
MEDIUM
HIGH
```

and competing explanations.

---

## 5. Sustained value

An Initiative SHOULD NOT be called fully successful based only on a temporary post-launch improvement.

Where relevant, confirm that value persists across a meaningful operating period.
