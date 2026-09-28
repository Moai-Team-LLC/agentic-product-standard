# Evaluation Dataset Standard

## 1. Purpose

Evaluation quality depends on representative cases.

An evaluation dataset is the set of cases an AI component is evaluated against (`evaluation/EVALUATION_SYSTEM.md`, `evaluation/AI_EVALS.md`). Instances: the `datasets` of `artifacts/evaluation-plan.md`.

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
eval_dataset:
  id:                       # free text, unique within the engagement; no registered prefix
  capability_id:
  ai_component:
  composition: []           # §2 case types included
  location:                 # where the cases are kept, when they live in evaluation tooling
  leakage:                  # §4: cases used to tune prompts or workflows, and the effect on results
  last_reviewed:            # §5
  owner:
  cases: []                 # eval_case records, or empty when `location` holds them

eval_case:
  id:                       # unique within its dataset; referenced as <dataset id>/<case id>
  capability_id:
  task:
  input:
  expected_behavior:
  unacceptable_behavior:
  risk_class:
  source:                   # e.g. historical case, INC-###, synthetic
  notes:
```

Inputs taken from real cases follow `evidence/EVIDENCE_STANDARD.md` §8: minimize and redact personal or confidential content, or reference the source instead of copying it.

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

Material incidents are a main source of new cases (`operations/INCIDENT_MODEL.md` §4).
