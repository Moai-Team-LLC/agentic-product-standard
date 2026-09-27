# AI-Enabled Operations Incident Model

## 1. Purpose

AI-enabled capabilities introduce failure modes that differ from deterministic systems.

---

## 2. Incident classes

```text
QUALITY
POLICY
AUTHORITY
DATA
SECURITY
TOOL_ACTION
STATE_INTEGRITY
COST
AVAILABILITY
MODEL_CHANGE
KNOWLEDGE_DRIFT
HUMAN_PROCESS
```

---

## 3. Incident record

```yaml
incident:
  id: INC-###
  capability_id:
  initiative_id:
  class:
  severity:
  detected_at:
  impact:
  affected_state:
  containment:
  recovery:
  root_cause:
  corrective_action:
  eval_case_added:
  owner:
```

---

## 4. Incident feedback loop

Every material incident SHOULD update one or more of:

```text
policy
evaluation dataset
prompt / workflow
knowledge base
permissions
observability
training
target architecture
```

---

## 5. Rule

Incident handling is part of transformation governance, not merely IT support.
