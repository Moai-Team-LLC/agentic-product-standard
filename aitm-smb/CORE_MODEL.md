# AITM-SMB Core Model

**Version:** 1.0.0

This document defines the primary semantic objects of AITM-SMB.

---

## 1. Outcome

A measurable business result that matters independently of AI.

```yaml
outcome:
  id: OUT-###
  name:
  owner:
  baseline:
  target:
  horizon:
  metric_ids: []
  evidence_ids: []
```

Invalid Outcome definitions include:

```text
adopt AI
deploy agents
automate more
use a specific vendor
```

These are means, not Outcomes.

---

## 2. Capability

A stable organizational ability required to produce value.

```yaml
capability:
  id: CAP-###
  name:
  purpose:
  owner:
  outcome_ids: []
  value_stream_ids: []
  current_state_id:
  target_state_id:
  metric_ids: []
```

A Capability is not:

```text
a department
a software product
a single task
an AI use case
```

---

## 3. State

A structured description of how a Capability operates at a point in time.

Types:

```text
CURRENT
TRANSITION
TARGET
```

A State SHOULD consider:

```text
People
Decisions
Process
Data
Knowledge
Applications
Automation
AI
Controls
Metrics
```

---

## 4. Gap

A material difference between current Capability behavior and required behavior.

```yaml
gap:
  id: GAP-###
  capability_id:
  current_condition:
  required_condition:
  business_impact:
  cause_status:
  evidence_ids: []
```

---

## 5. Cause

A condition explaining why a Gap exists.

A Cause begins as a Hypothesis unless Evidence justifies stronger status.

Canonical diagnostic logic is defined in `diagnostics/ROOT_CAUSE_ANALYSIS.md`.

---

## 6. Intervention

A bounded design choice intended to close one or more Gaps.

```yaml
intervention:
  id: INT-###
  gap_ids: []
  type:
  description:
  expected_effect:
  simpler_alternatives_considered: []
  risks: []
  assumptions: []
```

AI is one intervention family among several.

---

## 7. Initiative

An executable change package implementing one or more Interventions.

```yaml
initiative:
  id: INI-###
  capability_ids: []
  intervention_ids: []
  owner:
  entry_state:
  exit_state:
  expected_outcome_ids: []
  success_metric_ids: []
  dependencies: []
  decision_gates: []
  rollback_or_recovery:
```

A Capability is the unit of transformation.

An Initiative is the unit of coordinated delivery.

---

## 8. Metric

A defined measurable signal used to evaluate an Outcome, Capability, Initiative, AI component, economic effect, or risk.

Canonical semantics are defined in `METRICS.md`.

---

## 9. Evidence

A verifiable source supporting a claim.

Canonical semantics are defined in `evidence/EVIDENCE_STANDARD.md`.

---

## 10. Capability Network

A set of relevant Capabilities and their material dependencies.

Canonical semantics are defined in `design/CAPABILITY_NETWORK.md`.

---

## 11. System Constraint

The condition that most limits improvement of the target Outcome.

Canonical semantics are defined in `design/CONSTRAINT_ANALYSIS.md`.

---

## 12. Capability Target State

The required future behavior of one Capability.

Artifact:

```text
artifacts/capability-target-state.md
```

---

## 13. Target Operating Architecture

The integrated target design across relevant Capabilities, roles, Decision Rights, information, knowledge, applications, automation, AI, controls, metrics, and economics.

Canonical semantics are defined in `design/TARGET_OPERATING_ARCHITECTURE.md`.

---

## 14. Transition State

An independently operable intermediate State between Current and Target.

Canonical semantics are defined in `transition/TRANSITION_STATE_MODEL.md`.

---

## 15. Pilot

A bounded operational test of a transformation Hypothesis.

Canonical semantics are defined in `execution/PILOT_MODEL.md`.

---

## 16. Evaluation

A structured test of business, capability, operating, AI, technical, economic, or governance performance.

Canonical semantics are defined in `evaluation/EVALUATION_SYSTEM.md`.

---

## 17. Value Realization

Observed and sufficiently sustained business value attributable to a transformation with stated confidence.

Canonical semantics are defined in `measurement/VALUE_REALIZATION.md`.

---

## 18. Semantic integrity

A material Initiative is architecture-ready only when it can answer:

```text
Which Outcome does this serve?
Which Capability must change?
What Gap exists?
What Cause explains the Gap?
What Intervention is selected?
What Target State is required?
What Metric proves effect?
What Evidence supports the model?
```

At system level it must additionally answer:

```text
What dependencies matter?
What is the current System Constraint?
What local/system effects are expected?
How will transition occur?
How will value be demonstrated?
```
