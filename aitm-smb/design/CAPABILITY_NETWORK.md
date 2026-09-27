# Capability Network Design

## 1. Purpose

A Capability Map identifies abilities.

A Capability Network explains how those abilities depend on one another.

---

## 2. Relation types

AITM-SMB uses the following dependency relations:

```text
SUPPLIES_INFORMATION_TO
SUPPLIES_WORK_TO
REQUIRES_OUTPUT_FROM
REQUIRES_KNOWLEDGE_FROM
REQUIRES_DECISION_FROM
REQUIRES_CONTROL_FROM
SHARES_RESOURCE_WITH
SHARES_SYSTEM_WITH
CONSTRAINS
ENABLES
```

---

## 3. Capability dependency record

```yaml
dependency:
  id: DEP-###
  source_capability:
  relation:
  target_capability:
  criticality: low | medium | high
  evidence_ids: []
  failure_effect:
  capacity_effect:
  notes:
```

---

## 4. Critical dependency

A dependency is critical when failure or degradation materially affects:

```text
Outcome
throughput
quality
risk
economics
or decision latency
```

---

## 5. Dependency questions

For each Capability ask:

```text
What does it consume?
What does it produce?
Who depends on that output?
What information does it require?
What knowledge does it require?
What approval does it require?
What shared resource can become constrained?
```

---

## 6. Shared capability warning

Capabilities such as:

```text
Knowledge Management
Data Quality
Identity
Financial Control
Resource Allocation
Compliance
```

may serve several value streams.

Optimizing one downstream process without strengthening the shared capability may create repeated local fixes.

---

## 7. Agent rule

An agent SHOULD surface the smallest set of dependencies necessary to reason about the transformation.

AITM-SMB does not require mapping the entire company.
