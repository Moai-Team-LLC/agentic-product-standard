# AITM-SMB Metrics Model

## 1. Metric hierarchy

AITM-SMB distinguishes:

```text
Business Outcome Metrics
        ↓
Capability Metrics
        ↓
Operating Metrics
        ↓
AI Evaluation Metrics
```

Lower-level metrics explain performance.

They do not replace higher-level outcomes.

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
  class:
  owner:
  definition:
  source:
  baseline:
  target:
  cadence:
  linked_outcomes: []
  linked_capabilities: []
  linked_initiatives: []
```

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
