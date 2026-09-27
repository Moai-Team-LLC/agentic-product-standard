# Evaluation Dataset Standard

## 1. Purpose

Evaluation quality depends on representative cases.

---

## 2. Dataset composition

Where relevant include:

```text
common cases
rare cases
edge cases
policy-sensitive cases
ambiguous cases
historical failures
adversarial cases
high-impact cases
```

---

## 3. Dataset record

```yaml
eval_case:
  id:
  capability_id:
  task:
  input:
  expected_behavior:
  unacceptable_behavior:
  risk_class:
  source:
  notes:
```

---

## 4. Leakage rule

Cases used for evaluation SHOULD NOT be silently optimized into prompts or workflows without tracking the resulting evaluation leakage.

---

## 5. Maintenance

Evaluation datasets SHOULD evolve when:

```text
new failure patterns appear
business policy changes
customer behavior changes
models change
tools change
autonomy increases
```
