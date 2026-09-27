# AI Evaluation Model

## 1. Purpose

AI components require explicit evaluation before and during operation.

---

## 2. Evaluation dimensions

Depending on the task evaluate:

```text
task success
accuracy
precision / recall
groundedness
hallucination rate
instruction following
policy compliance
tool selection
tool-call success
structured output validity
escalation quality
human correction rate
latency
cost
robustness
```

---

## 3. Reference-based versus reference-free

### Reference-based

Compare against known expected output.

Use when:

```text
labels exist
golden cases exist
rules can produce expected result
```

### Reference-free

Use rubric, model judge, human review, or behavioral outcome when no single expected answer exists.

Reference-free evaluation SHOULD be calibrated.

---

## 4. Production evals

Production evaluation MAY include:

```text
sampled human review
policy-violation checks
outcome-based feedback
customer corrections
agent trajectory review
tool failure analysis
drift monitoring
```

---

## 5. Evals before autonomy

Higher autonomy requires stronger evaluation.

As autonomy increases, evaluation SHOULD shift from:

```text
output quality
```

toward:

```text
trajectory quality
action correctness
policy compliance
state integrity
and outcome safety
```
