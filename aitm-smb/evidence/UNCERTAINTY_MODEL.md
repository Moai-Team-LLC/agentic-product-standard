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
  id: UNC-###
  type:                 # one §2 class: FACTUAL | CAUSAL | TECHNICAL | ECONOMIC | BEHAVIORAL | ORGANIZATIONAL | REGULATORY | MODEL_PERFORMANCE
  statement:
  impact:
  current_confidence: low | medium | high   # diagnostics/DIAGNOSTIC_MODEL.md §5
  resolution_method:    # one §3 choice: ACCEPT | REDUCE | TEST | DEFER | AVOID; for TEST, name the experiment (§4)
  owner:
  gate:                 # HG-*, GAT-###, or phase exit by which it must be resolved
```

Record material uncertainties only (INV-15). Instances: the Evidence Register (`artifacts/evidence-register.md`).
