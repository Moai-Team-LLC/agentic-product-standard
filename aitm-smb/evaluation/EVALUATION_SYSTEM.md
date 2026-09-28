# Evaluation System

## 1. Purpose

AITM-SMB evaluates both:

```text
business-system effect
and
AI-component quality
```

These are separate but connected.

This is the engagement evaluation system: it evaluates the transformed business system and its AI components. It is not `rubrics/`, which holds informative rubrics for judging AITM-SMB outputs themselves.

Related: AI-component evaluation `evaluation/AI_EVALS.md`; evaluation datasets `evaluation/EVALUATION_DATASET.md`.

---

## 2. Evaluation layers

```text
Layer                        layer value
1 Business Outcome           business_outcome
2 Capability Performance     capability
3 Operating Performance      operating
4 Human-AI Interaction       human_ai
5 AI Task Quality            ai_task
6 Technical Reliability      technical
7 Economics                  economics
8 Risk / Governance          risk_governance
```

Layer numbers are ordinals. They are not autonomy levels (L0–L5, `diagnostics/AUTONOMY_SUITABILITY.md` §2).

An evaluation covers the layers relevant to its scope. Where AI is used, human-AI interaction and technical reliability are relevant.

---

## 3. Evaluation questions

### Business Outcome

Did the intended business result improve?

### Capability

Can the organization now perform the capability at the required level?

### Operating

Did cycle time, cost, throughput, rework, or exception load change?

### Human-AI

Are roles, trust, overrides, and escalation working?

### AI Task

Does the model perform the bounded task well enough?

### Technical

Is the system available, observable, and reliable?

### Economics

Is cost per successful outcome acceptable?

### Governance

Are policies, permissions, and audit expectations met?

---

## 4. Evaluation record

```yaml
evaluation:
  id: EVL-###
  initiative_id:
  layer:                    # §2 layer value
  metric_ids: []
  method:
  sample:
  threshold:
  owner:
  # result fields, completed after execution
  actual:
  conclusion:               # §5
  limitations:
  evidence_ids: []
```

Plan fields (`layer` to `owner`) are fixed before execution and MUST NOT change after results are known. Result fields are added after execution. A repeated evaluation gets a new record.

Instances: `artifacts/evaluation-plan.md`, which holds the plan fields as registered and appends the result fields in its results section, keyed by `evaluation_id`.

---

## 5. Evaluation conclusion

Use:

```text
PASS
PASS_WITH_LIMITATIONS
FAIL
INSUFFICIENT_EVIDENCE
```

These are result values, not agent statuses (`PUBLIC_API.md` §8).

A passing AI evaluation does not imply a passing business evaluation.
