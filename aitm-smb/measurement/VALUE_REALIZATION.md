# Value Realization Model

## 1. Purpose

AITM-SMB distinguishes projected value from realized value.

---

## 2. Value states

```text
HYPOTHESIZED
→ OBSERVED
→ ATTRIBUTED
→ REALIZED
→ SUSTAINED
```

Entry criteria:

```text
HYPOTHESIZED  expected value stated for an Initiative against an Outcome, with baseline and target
              (an unmeasured baseline is recorded as Evidence Debt)
OBSERVED      the Outcome metric changed against a measured baseline, with Evidence
ATTRIBUTED    the change is linked to the transformation with attribution confidence MEDIUM or HIGH
              and competing explanations recorded (§4)
REALIZED      attributed effect reaches the target, or an approved partial target, net of
              implementation and operating cost
SUSTAINED     realized value persists across the stated sustainability period (§5)
```

A baseline must be measured before a state can move beyond HYPOTHESIZED.

Declaring REALIZED or SUSTAINED requires `HG-VALUE` (`STANDARD.md` §8).

---

## 3. Value record

Record contract: `artifacts/value-realization-report.md` (`VRL-###`).

A value record ties one Initiative and Outcome metric to its baseline, target and observed value, its business, capability and economic effect, implementation and operating cost, realized value, attribution confidence, sustainability period, value state (§2), and value conclusion (§6), with Evidence.

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

---

## 6. Value conclusion

```text
VALUE_CONFIRMED        value state REALIZED, or SUSTAINED where a sustainability period applies,
                       approved through HG-VALUE
PARTIAL_VALUE          attributed value below target, or realized for only part of the scope
NO_VALUE               no attributable effect
NEGATIVE_VALUE         attributable effect is negative, or costs exceed the value created
INSUFFICIENT_EVIDENCE  the Evidence supports no other conclusion; the gap is recorded as Evidence Debt
```

An Initiative is value-confirmed only when:

```text
business effect evidenced
AND capability effect evidenced
AND economics acceptable
AND governance remains effective
AND effect is sufficiently sustained
```

The value conclusion is distinct from the effect conclusion of the Transformation Scorecard (`artifacts/transformation-scorecard.md`), which states whether metrics moved. These are result values, not agent statuses (`PUBLIC_API.md` §8).
