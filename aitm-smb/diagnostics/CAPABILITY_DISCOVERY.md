# Capability Discovery Method

## 1. Purpose

Capability discovery identifies stable organizational abilities required to produce outcomes.

AITM-SMB uses capabilities because:

```text
org charts change
processes change
tools change
AI changes
```

but the organization still needs to remain capable of producing value.

---

## 2. Discovery sequence

### Step 1 — Start from Outcome

Ask:

```text
What must the organization be able to do reliably
for this Outcome to improve?
```

### Step 2 — Inspect Value Streams

Identify the end-to-end flow through which value is created.

### Step 3 — Extract abilities

Convert activities into stable abilities.

Example transformation:

```text
Activity:
"Salesperson manually reviews inbound form"

Capability:
"Lead Qualification"
```

### Step 4 — Normalize boundaries

A capability should be neither:

```text
too broad:
"Run the business"

nor too narrow:
"Open CRM record"
```

### Step 5 — Validate independence from tools

Ask:

```text
If the current software disappeared tomorrow,
would this organizational ability still be required?
```

If no, it may be a tool function rather than a capability.

---

## 3. Naming convention

Prefer noun phrases describing organizational abilities:

```text
Lead Qualification
Customer Onboarding
Demand Forecasting
Knowledge Retrieval
Pricing
Issue Resolution
Resource Allocation
```

Avoid:

```text
CRM Administration
Chatbot Usage
Spreadsheet Reporting
Marketing Department
```

---

## 4. Capability granularity test

A useful capability:

```text
has a clear purpose
has an identifiable owner
affects at least one Outcome
can be assessed independently
can be improved independently
has meaningful performance metrics
```

---

## 5. Capability decomposition

Use decomposition only when the parent capability is too broad to diagnose.

Example:

```text
Customer Support
├── Intake & Classification
├── Knowledge Retrieval
├── Response Generation
├── Escalation
└── Resolution Verification
```

Do not decompose indefinitely.

The stopping rule is:

> Stop when a capability is sufficiently specific to make transformation decisions.

---

## 6. Capability dependency

Capabilities MAY depend on other capabilities.

Example:

```text
Pricing
depends on:
- Cost Intelligence
- Customer Segmentation
- Approval Governance
```

Dependencies matter because changing one capability may move the bottleneck elsewhere.

Record them in the Capability's `dependencies`; where a Capability Network is used, as Capability Dependencies (`DEP-###`, [`artifacts/capability-network.md`](../artifacts/capability-network.md)).

---

## 7. Capability record

Record each accepted Capability in the Capability Map ([`artifacts/capability-map.md`](../artifacts/capability-map.md); record contract [`CORE_MODEL.md`](../CORE_MODEL.md) §2 with the Capability Map extensions: `dependencies`, `confidence`, `boundary_notes`).

A candidate not yet accepted MAY be recorded without an `id`. The `CAP-###` ID is assigned when the candidate is accepted into the Capability Map and never reused.

Each accepted Capability in scope gets a CURRENT State ([`CORE_MODEL.md`](../CORE_MODEL.md) §3) in Phase 1.
