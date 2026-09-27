# Observability Model

## 1. Purpose

A transformed capability must be observable as a business system.

AITM-SMB observability is broader than technical monitoring.

---

## 2. Observability layers

```text
Business
Capability
Workflow
Decision
AI / Agent
Application
Infrastructure
Economics
Risk
```

---

## 3. Minimum observable questions

For any production AI-enabled capability:

```text
What happened?
Why did it happen?
Who or what decided?
What information was used?
What action was taken?
Did the action succeed?
What did it cost?
Was a policy violated?
Did a human override?
What was the business outcome?
```

---

## 4. Trace model

```yaml
operation_trace:
  trace_id:
  capability_id:
  workflow_id:
  user_or_actor:
  ai_component:
  model:
  context_sources: []
  tools_called: []
  decisions: []
  approvals: []
  actions: []
  result:
  cost:
  latency:
  policy_events: []
  linked_business_outcome:
```

---

## 5. Observability proportionality

Not every low-risk AI interaction requires full forensic trace.

Trace depth SHOULD increase with:

```text
authority
risk
financial impact
customer impact
irreversibility
regulatory significance
```

---

## 6. Dark automation

AITM-SMB considers automation unsafe when important business state changes occur without sufficient observability.

Avoid:

```text
unlogged decisions
untracked agent tool actions
unowned failures
silent retries changing state
```
