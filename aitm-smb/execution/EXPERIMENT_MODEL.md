# Experiment Model

## 1. Purpose

Use experiments when uncertainty is high and a full pilot is unnecessary.

Experiments answer one bounded question.

A test whose result is the evidence for promoting an Initiative to rollout is recorded as a Pilot (`PLT-###`, [`execution/PILOT_MODEL.md`](PILOT_MODEL.md)), so that pilot validity and the promotion decision apply; otherwise use an Experiment (`EXP-###`).

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
  initiative_id:            # INI-###, where the experiment serves a selected Initiative
  question:
  hypothesis:               # HYP-### or statement
  linked_gap_ids: []
  linked_intervention_ids: []
  method:
  sample:
  metric:
  threshold:
  result:
  limitations:
  evidence_ids: []
  next_decision:
  owner:
```

Instances: the `experiments` section of [`artifacts/transformation-roadmap.md`](../artifacts/transformation-roadmap.md), unless the Pilot Plan ([`artifacts/pilot-plan.md`](../artifacts/pilot-plan.md)) the experiment serves holds it.

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
