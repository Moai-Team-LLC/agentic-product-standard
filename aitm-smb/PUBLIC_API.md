# AITM-SMB Public Methodology API

**Version:** 1.0.0  
**Stability:** Stable for the 1.x line

This document defines the semantic surface that Extensions, tools, skills, and external implementations may rely on.

---

## 1. Stable primary objects

```text
Outcome
Capability
State
Gap
Cause / Hypothesis
Intervention
Initiative
Metric
Evidence
```

---

## 2. Stable system objects

```text
Capability Network
System Constraint
Capability Target State
Target Operating Architecture
Transition State
Pilot
Evaluation
Value Realization
```

---

## 3. Stable identifiers

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
ASM-###  Assumption
HYP-###  Hypothesis
CPN-###  Capability Network
DEP-###  Capability Dependency
CST-###  System Constraint
TOA-###  Target Operating Architecture
PLT-###  Pilot
EXP-###  Experiment
EVL-###  Evaluation
INC-###  Incident
```

---

## 4. Stable core trace

```text
Outcome
→ Capability
→ Gap
→ Intervention
→ Initiative
→ Metric
→ Evidence
```

1.x-compatible Extensions MUST preserve this trace.

---

## 5. Stable profiles

```text
Compact
Standard
Governed
Portfolio
Measured
```

Profiles are composable.

---

## 6. Stable intervention families

```text
ELIMINATE
SIMPLIFY
STANDARDIZE
INSTRUMENT
INTEGRATE
PROCESS
ROLE
DECISION
DATA
KNOWLEDGE
SOFTWARE
AUTOMATION
AI_ASSIST
AI_AUTOMATE
AI_AUGMENT
AI_AUTONOMIZE
CONTROL
FEEDBACK
```

Extensions MAY add subtypes but MUST NOT redefine these semantics.

---

## 7. Stable autonomy levels

```text
L0 No AI
L1 Suggest
L2 Draft
L3 Execute with approval
L4 Execute within bounded policy
L5 Pursue bounded objective
```

Extensions MAY add controls around a level but MUST NOT silently reinterpret its authority.

---

## 8. Stable agent statuses

```text
COMPLETE
PARTIAL
BLOCKED
HUMAN_DECISION_REQUIRED
INSUFFICIENT_EVIDENCE
```

---

## 9. Compatibility promise

Within AITM-SMB 1.x:

- stable object meanings will not change incompatibly;
- stable identifiers will not be repurposed;
- core trace will not be weakened;
- deprecated artifacts will retain redirect guidance;
- new optional modules may be added without changing Core semantics.

An incompatible change requires AITM-SMB 2.0.
