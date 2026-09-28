# Target Operating Architecture

## 1. Purpose

The Target Operating Architecture (`TOA-###`) describes how the transformed business system operates across capabilities.

It composes the Capability Target States of the Capabilities in scope. The two levels MUST NOT be merged (`STANDARD.md` §7). In the Compact profile, the Capability Target States stand in for the TOA (`EXECUTION_MODEL.md` §2).

It integrates:

```text
Outcomes
Capabilities
Value Streams
Roles
Decision Rights
Information
Knowledge
Applications
Automation
AI
Controls
Metrics
Economics
```

---

## 2. Architecture layers

```text
Layer 1 — Outcomes
Layer 2 — Value Streams
Layer 3 — Capabilities
Layer 4 — Roles & Decision Rights
Layer 5 — Process & Coordination
Layer 6 — Information & Knowledge
Layer 7 — Applications & Integration
Layer 8 — Automation & AI
Layer 9 — Controls & Governance
Layer 10 — Metrics & Economics
```

Layers are numbered, not labeled `L<n>`: `L0`–`L5` are autonomy levels (`STANDARD.md` §6).

---

## 3. Target Operating Architecture record

Record contract: `artifacts/target-operating-architecture.md`.

The record holds the §2 layers as fields, the Capability Target States it composes (`target_state_ids`), the System Constraints it addresses, and the system-level Metrics.

Approval: `HG-TOA` (`STANDARD.md` §8), after the pre-approval system checks in `design/SYSTEM_TRANSFORMATION_MODEL.md` §6.

---

## 4. Architecture consistency rules

### Role consistency

Every material responsibility has an owner.

### Decision consistency

Every material decision has one clear authority model (`design/DECISION_RIGHTS_ARCHITECTURE.md` §3).

### Information consistency

Critical facts have an authoritative source.

### Knowledge consistency

Required knowledge has an explicit maintenance owner.

### Application consistency

Systems have defined responsibilities and boundaries.

### AI consistency

AI does not receive authority beyond approved governance: no level exceeds the approved Authority Ceiling (`diagnostics/AUTONOMY_SUITABILITY.md` §6).

### Metric consistency

Local metrics do not incentivize behavior that harms the target Outcome.

---

## 5. Design principle

The Target Operating Architecture SHOULD minimize unnecessary coordination.

Transformation should reduce the need for:

```text
manual synchronization
repeated approvals
context reconstruction
knowledge hunting
status chasing
duplicate entry
managerial routing
```

rather than merely making those activities faster.

---

## 6. AI-native operating architecture

An AI-native operating architecture does not mean:

```text
AI everywhere
```

It means:

```text
the operating model is intentionally designed
around the comparative strengths of humans,
deterministic software,
automation,
and probabilistic AI.
```
