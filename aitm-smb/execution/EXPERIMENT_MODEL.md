# Experiment Model

## 1. Purpose

Use experiments when uncertainty is high and a full pilot is unnecessary.

Experiments answer one bounded question.

---

## 2. Experiment examples

```text
Can required context be retrieved reliably?
Can the model classify the cases above threshold?
Can users understand AI recommendations?
Can a policy prevent unsafe tool actions?
Does the new workflow reduce cycle time?
```

---

## 3. Experiment contract

```yaml
experiment:
  id: EXP-###
  question:
  hypothesis:
  linked_gap_ids: []
  linked_intervention_ids: []
  method:
  sample:
  metric:
  threshold:
  result:
  limitations:
  next_decision:
```

---

## 4. Experiment hierarchy

Prefer the cheapest experiment capable of reducing the uncertainty that blocks a decision.

Possible forms:

```text
offline dataset evaluation
workflow simulation
paper process
shadow execution
user test
limited production test
A/B test
```

---

## 5. Rule

Do not build production infrastructure to answer a question that can be resolved with a cheaper experiment.
