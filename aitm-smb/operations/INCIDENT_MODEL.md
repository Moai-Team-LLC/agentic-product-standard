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

Record contract: [`artifacts/incident-record.md`](../artifacts/incident-record.md) (`INC-###`).

Severity:

```text
high     material exposure (STANDARD.md §16), or any AUTHORITY or SECURITY incident
medium   business impact without material exposure
low      no business impact beyond the affected case
```

An organization MAY use its own severity scale if it maps each level to one of these. A high-severity incident is material; when materiality is unclear, treat the incident as material ([`STANDARD.md`](../STANDARD.md) §16).

---

## 4. Incident feedback loop

Every material incident SHOULD update one or more of:

```text
policy
evaluation dataset
prompt / workflow
knowledge base
permissions
AI authority level or Authority Ceiling
observability
training
Capability Target State or Target Operating Architecture
```

When an incident matches a demotion trigger, authority MAY be reduced immediately; restoring it requires `HG-AUTHORITY` ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md) §4).

---

## 5. Rule

Incident handling is part of transformation governance, not merely IT support.
