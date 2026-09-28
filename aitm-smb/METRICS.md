# AITM-SMB Metrics Model

## 1. Metric classes

AITM-SMB distinguishes a hierarchy:

```text
Business Outcome Metrics      class: outcome
        ↓
Capability Metrics            class: capability
        ↓
Operating Metrics             class: operating
        ↓
AI Evaluation Metrics         class: ai_evaluation
```

and, alongside the hierarchy:

```text
Economic Metrics              class: economic          (§8)
Risk / Governance Metrics     class: risk_governance   (§9)
```

Lower-level metrics explain performance.

They do not replace higher-level outcomes.

Economic and Risk / Governance Metrics qualify an effect; they do not replace business Outcome metrics either.

---

## 2. Business Outcome Metrics

Examples:

```text
revenue
gross margin
retention
conversion
cash conversion
customer lifetime value
risk loss
capacity
```

---

## 3. Capability Metrics

Measure whether the capability performs its purpose.

Examples:

```text
quote-to-close rate
time-to-resolution
forecast accuracy
onboarding completion
knowledge retrieval success
delivery predictability
```

---

## 4. Operating Metrics

Examples:

```text
cycle time
queue time
handoffs
rework
error rate
cost per transaction
human minutes per transaction
throughput
```

---

## 5. AI Evaluation Metrics

Examples:

```text
task success
groundedness
precision / recall
policy compliance
tool-call success
escalation quality
latency
cost per successful task
human correction rate
```

---

## 6. Metric contract

```yaml
metric:
  id: MET-###
  name:
  class: outcome | capability | operating | ai_evaluation | economic | risk_governance
  owner:
  definition:
  source:
  baseline:
  target:
  cadence:
  outcome_ids: []
  capability_ids: []
  initiative_ids: []
```

Instances: `artifacts/transformation-scorecard.md`.

---

## 7. Metric integrity rules

A metric MUST have:

```text
definition
owner
source
baseline or explicit baseline gap
measurement cadence
```

Avoid:

```text
"AI usage"
"number of prompts"
"number of automated tasks"
```

unless they explain a higher-level outcome.

---

## 8. Economic Metrics

Measure the cost and economic effect of the transformation. Economic lenses and the economic hypothesis: `economics/TRANSFORMATION_ECONOMICS.md`.

Examples:

```text
implementation cost
operating cost
cost per successful business outcome
human oversight cost
failure cost
payback against the economic hypothesis
```

---

## 9. Risk / Governance Metrics

Measure whether risk and AI authority stay within approved bounds.

Examples:

```text
incidents by severity
policy or permission violations
escalations and their resolution time
human overrides of AI actions
actions outside the Authority Ceiling
time to detect and recover
```
