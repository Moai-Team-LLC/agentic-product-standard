# AITM-SMB Ontology

## Core entities

### Outcome
A measurable business result the transformation intends to change.

### Capability
An ability the organization must possess to produce value.

### Value Stream
An end-to-end flow that produces value for a customer or stakeholder.

### Process
A repeatable sequence of activities.

### Role
A human or machine responsibility inside the system.

### Decision
A choice that changes system state or directs action.

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

### Metric
A measurable signal describing outcome, performance, quality, risk, or cost.

### Initiative
A bounded transformation effort moving the system toward a target state.

### Constraint
A limit that the architecture must respect.

### Risk
A potential failure with impact and likelihood.

### Evidence
A source supporting a claim about the business or system.

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

## Capability record

```yaml
capability:
  id: CAP-###
  name:
  purpose:
  owner:
  outcomes:
  value_streams:
  current_state:
  target_state:
  people:
  decisions:
  processes:
  data:
  knowledge:
  applications:
  automation:
  ai:
  controls:
  metrics:
  constraints:
  risks:
  evidence:
```


## Canonical identifiers

AITM-SMB uses stable identifiers for traceability:

```text
OUT-###  Outcome
CAP-###  Capability
STA-###  State
GAP-###  Gap
INT-###  Intervention
INI-###  Initiative
MET-###  Metric
EVD-###  Evidence
DEC-###  Decision
RSK-###  Risk
ASM-###  Assumption
HYP-###  Hypothesis
```

Identifiers SHOULD remain stable across artifact revisions.


## Diagnostic identifiers

```text
DIA-###  Diagnostic Record
AIS-###  AI Suitability Assessment
AUT-###  Autonomy Assessment
UNC-###  Uncertainty
```


## Transformation design identifiers

```text
CPN-###  Capability Network
DEP-###  Capability Dependency
CST-###  System Constraint
TOA-###  Target Operating Architecture
PTF-###  Transformation Portfolio
SFX-###  System Effect Assessment
BDS-###  Business Decision
```


## Execution identifiers

```text
PLT-###  Pilot
EXP-###  Experiment
SLC-###  Transformation Slice
GAT-###  Execution Gate
EVL-###  Evaluation
INC-###  Incident
CHG-###  AI Change
```
