# Decision Rights Architecture

## 1. Purpose

AI transformation changes not only tasks but who is allowed to decide.

Decision Rights Architecture makes this explicit.

---

## 2. Decision record

```yaml
business_decision:
  id: BDS-###
  name:
  capability_id:
  current_authority:
  target_authority:
  information_required: []
  knowledge_required: []
  policy_constraints: []
  frequency:
  impact:
  escalation:
  metric_ids: []
```

---

## 3. Authority models

```text
HUMAN
HUMAN_WITH_AI
AI_RECOMMENDS_HUMAN_DECIDES
AI_DRAFTS_HUMAN_APPROVES
AI_EXECUTES_WITH_APPROVAL
AI_EXECUTES_WITHIN_POLICY
AGENT_PURSUES_BOUNDED_OBJECTIVE
```

---

## 4. Decision decomposition

Large decisions often contain smaller decisions.

Example:

```text
"approve proposal"
```

may decompose into:

```text
validate completeness
calculate price
check margin
check legal terms
approve exception
send commitment
```

Some sub-decisions may be automated while others remain human.

---

## 5. Principle

Do not automate the label of a decision.

Decompose the actual authority structure.
