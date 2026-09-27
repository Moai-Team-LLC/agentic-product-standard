# Uncertainty Model

## 1. Purpose

AITM-SMB treats uncertainty as a first-class architecture input.

---

## 2. Uncertainty classes

```text
FACTUAL
CAUSAL
TECHNICAL
ECONOMIC
BEHAVIORAL
ORGANIZATIONAL
REGULATORY
MODEL_PERFORMANCE
```

---

## 3. Handling uncertainty

For each material uncertainty choose:

```text
ACCEPT
REDUCE
TEST
DEFER
AVOID
```

---

## 4. Experiment over debate

When a question can be answered cheaply and reversibly through evidence, prefer an experiment.

Examples:

```text
shadow mode
human-in-the-loop pilot
offline evaluation
sample workflow test
A/B test
limited cohort
simulation
```

---

## 5. Uncertainty record

```yaml
uncertainty:
  id:
  type:
  statement:
  impact:
  current_confidence:
  resolution_method:
  owner:
  gate:
```
