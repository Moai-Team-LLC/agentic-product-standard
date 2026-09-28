# AITM-SMB Ontology

## Core entities

Transformation objects (Outcome, Capability, State, Gap, Cause / Hypothesis, Intervention, Initiative, Metric, Evidence) are defined in [`CORE_MODEL.md`](../CORE_MODEL.md). The entries below point there and add the business-system entities.

### Outcome
See [`CORE_MODEL.md`](../CORE_MODEL.md) §1.

### Capability
See [`CORE_MODEL.md`](../CORE_MODEL.md) §2.

### State
See [`CORE_MODEL.md`](../CORE_MODEL.md) §3.

### Gap
See [`CORE_MODEL.md`](../CORE_MODEL.md) §4.

### Cause / Hypothesis
See [`CORE_MODEL.md`](../CORE_MODEL.md) §5.

### Intervention
See [`CORE_MODEL.md`](../CORE_MODEL.md) §6.

### Initiative
See [`CORE_MODEL.md`](../CORE_MODEL.md) §7.

### Metric
See [`CORE_MODEL.md`](../CORE_MODEL.md) §8.

### Evidence
See [`CORE_MODEL.md`](../CORE_MODEL.md) §9.

### Value Stream
An end-to-end flow that produces value for a customer or stakeholder.

Value Streams have no registered identifier in 1.x; `value_stream_ids` fields hold the Value Stream names used in the Business System Map ([`artifacts/business-system-map.md`](../artifacts/business-system-map.md)). In Compact, which has no Business System Map, they hold the names used in the Transformation Intent or Capability Map.

### Process
A repeatable sequence of activities.

### Role
A human or machine responsibility inside the system.

### Decision
A choice that changes system state or directs action.

This is an operational business decision; decision rights over it are recorded as `BDS-###` ([`design/DECISION_RIGHTS_ARCHITECTURE.md`](../design/DECISION_RIGHTS_ARCHITECTURE.md)). Engagement decisions about the transformation itself are `DEC-###` ([`DECISION_MODEL.md`](../DECISION_MODEL.md)).

### Data Asset
Structured information used by the system.

### Knowledge Asset
Context, rules, expertise, documents, patterns, or memory required for competent action.

### Application
Software supporting one or more capabilities.

### Automation
Deterministic execution of predefined logic.

### AI Component
Probabilistic model-based component used for generation, classification, retrieval, prediction, reasoning, or perception.

### Agent
A bounded AI-driven actor that can pursue an objective through state, tools, permissions, and verification.

### Control
A mechanism constraining risk, authority, access, or behavior.

### Constraint
A limit that the architecture must respect.

A design limit; not the System Constraint (`CST-###`, [`CORE_MODEL.md`](../CORE_MODEL.md) §11), which is the condition that most limits improvement of a target Outcome. Design Constraints are recorded in `constraints` fields.

### Risk
A potential failure with impact and likelihood.

A Risk record (`RSK-###`; record contract: [`artifacts/decision-assumption-log.md`](../artifacts/decision-assumption-log.md)) names one owner. A Risk MAY stay a statement in Intervention `risks` until it needs an owner, controls, or acceptance. Accepting a material Risk requires HG-RISK ([`STANDARD.md`](../STANDARD.md) §8); the Risk record cites the accepting Decision in `acceptance_decision_id`.

## Key relations

```text
Outcome REQUIRES Capability
ValueStream USES Capability
Capability IS_REALIZED_BY Process
Process IS_PERFORMED_BY Role
Role MAKES Decision
Decision USES DataAsset
Decision USES KnowledgeAsset
Capability USES Application
Application CONTAINS Automation
Application MAY_USE AIComponent
Agent USES Tool
Agent HAS Permission
Agent IS_CONSTRAINED_BY Control
Initiative CHANGES Capability
Initiative MOVES CurrentState TO TargetState
Metric MEASURES Outcome
Evidence SUPPORTS Claim
```

Trace relations between transformation objects and the fields that record them: [`TRACEABILITY.md`](../TRACEABILITY.md) §2.

## Capability record

Record contract: [`CORE_MODEL.md`](../CORE_MODEL.md) §2.

System-dimension detail (people, decision rights, processes, data, knowledge, applications, automation, AI, controls, metrics, economics, feedback) and its evidence are recorded in the Capability's State records ([`CORE_MODEL.md`](../CORE_MODEL.md) §3), not in the Capability record. Where design Constraints and Risks are recorded: [`CORE_MODEL.md`](../CORE_MODEL.md) §2.

## Canonical identifiers

This is the complete identifier registry. The 1.x stable subset is [`PUBLIC_API.md`](../PUBLIC_API.md) §3; every other prefix below is reserved and MUST NOT be repurposed within 1.x. Where each record shape is defined: [`CANONICAL_CONCEPTS.md`](../CANONICAL_CONCEPTS.md).

### Core

```text
OUT-###  Outcome
CAP-###  Capability
STA-###  State (CURRENT / TRANSITION / TARGET)
GAP-###  Gap
HYP-###  Hypothesis (incl. Cause; ID unchanged when validated)
INT-###  Intervention
INI-###  Initiative
MET-###  Metric
EVD-###  Evidence
DEC-###  Decision
ASM-###  Assumption
RSK-###  Risk
```

### Engagement

```text
ATI-###  Transformation Intent
```

### Diagnostic

```text
DIA-###  Diagnostic Record
AIS-###  AI Suitability Assessment
AUT-###  Autonomy Assessment
UNC-###  Uncertainty
```

### Design

```text
CPN-###  Capability Network
DEP-###  Capability Dependency
CST-###  System Constraint
TOA-###  Target Operating Architecture
PTF-###  Transformation Portfolio
SFX-###  System Effect Assessment
BDS-###  Business Decision (decision-rights entry)
```

### Execution

```text
PLT-###  Pilot
EXP-###  Experiment
SLC-###  Transformation Slice
GAT-###  Execution Gate
EVL-###  Evaluation
INC-###  Incident
CHG-###  AI Change
ROL-###  Rollout Plan
VRL-###  Value Realization
```

### Identifier rules

- Format in instances: prefix + `-` + three or more digits (e.g. `OUT-001`).
- An ID is unique per prefix within an engagement. Allocate the next number above the highest one in use across the engagement's artifacts.
- IDs are never reused within an engagement.
- A revised record keeps its ID. A superseded record keeps its ID and gets `status: superseded`; every record MAY carry this value, in addition to the status values its contract lists.
- Identifiers SHOULD remain stable across artifact revisions and framework upgrades.
