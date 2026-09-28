# AITM-SMB Public Methodology API

**Version:** 1.1.0  
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

All other prefixes registered in `ontology/ONTOLOGY.md` are reserved and MUST NOT be repurposed within 1.x.

Identifier format, uniqueness, and supersession: `ontology/ONTOLOGY.md`.

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

This is the compatibility floor for Extensions. The minimum valid path of an application is `EXECUTION_MODEL.md` §6; conformance requirements are in `CONFORMANCE.md` §1.

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

Definitions: `design/INTERVENTION_PATTERNS.md`. Challenge order: `STANDARD.md` §5.

An `AI_*` family names the kind of AI contribution; authority is set only by the autonomy level (§7).

Extensions MAY add subtypes but MUST NOT redefine these semantics.

---

## 7. Stable autonomy levels

```text
L0 — No AI
L1 — Suggest
L2 — Draft
L3 — Execute with explicit approval
L4 — Execute within bounded policy
L5 — Pursue bounded objective and escalate exceptions
```

Authority definitions per level: `diagnostics/AUTONOMY_SUITABILITY.md` §2. Levels are assessed per action class of a Capability. They are authority levels, not maturity or software-architecture levels (`STANDARD.md` §6).

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

- `COMPLETE` — all required outputs produced; all required validations passed; no gate left open.
- `PARTIAL` — some outputs produced; no blocker; remaining work is listed.
- `BLOCKED` — a required input, dependency, or unresolved normative conflict prevents progress.
- `HUMAN_DECISION_REQUIRED` — work stopped at a human gate (`STANDARD.md` §8); `open_gates` lists it.
- `INSUFFICIENT_EVIDENCE` — proceeding would require invented business facts.

When several apply, report the first in this order: `BLOCKED`, `INSUFFICIENT_EVIDENCE`, `HUMAN_DECISION_REQUIRED`, `PARTIAL`, `COMPLETE`; list the others in `status_reason` (`AGENT_OUTPUT_STANDARD.md`).

Domain result enums elsewhere (e.g. pilot result `INSUFFICIENT_EVIDENCE`) are separate `result` values, not agent statuses.

---

## 9. Compatibility promise

Within AITM-SMB 1.x:

- stable object meanings will not change incompatibly;
- stable identifiers will not be repurposed;
- core trace will not be weakened;
- deprecated artifacts will retain redirect guidance;
- new optional modules may be added without changing Core semantics.

An incompatible change requires AITM-SMB 2.0. Version classes: `VERSIONING.md`.
