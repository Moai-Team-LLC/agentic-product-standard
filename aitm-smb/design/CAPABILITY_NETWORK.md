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

Direction: a dependency reads source RELATION target (record fields `source_capability_id`, `target_capability_id`).

```text
SUPPLIES_*_TO          the target depends on the source
REQUIRES_*_FROM        the source depends on the target
SHARES_*_WITH          mutual; record once
CONSTRAINS, ENABLES    the target depends on the source, which limits it or makes it possible
```

Record each dependency once, with one relation. Each dependency record realizes the trace relation `Capability DEPENDS_ON Capability` ([`TRACEABILITY.md`](../TRACEABILITY.md) §2).

---

## 3. Capability dependency record

Capability Network (`CPN-###`) and Capability Dependency (`DEP-###`) records: record contract [`artifacts/capability-network.md`](../artifacts/capability-network.md).

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
