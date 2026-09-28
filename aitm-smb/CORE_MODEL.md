# AITM-SMB Core Model

**Version:** 1.1.0

This document defines the primary semantic objects of AITM-SMB.

§1–§4, §6, and §7 are the record contracts for their objects; every other record contract is named in [`CANONICAL_CONCEPTS.md`](CANONICAL_CONCEPTS.md). Files that hold instances reference the record contract and MAY add fields only where they say so explicitly ("extends <record> with: …").

Identifiers: [`ontology/ONTOLOGY.md`](ontology/ONTOLOGY.md). Materiality: [`STANDARD.md`](STANDARD.md) §16. Missing links: [`TRACEABILITY.md`](TRACEABILITY.md) §4.

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
  status: proposed | approved | retired
```

Instances: [`artifacts/transformation-intent.md`](artifacts/transformation-intent.md).

`status: approved` requires a Decision closing HG-OUTCOME ([`STANDARD.md`](STANDARD.md) §8).

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
  current_state_id:   # STA-### (type CURRENT)
  target_state_id:    # STA-### (type TARGET)
  metric_ids: []
  evidence_ids: []
```

Instances: [`artifacts/capability-map.md`](artifacts/capability-map.md). Discovery and granularity test: [`diagnostics/CAPABILITY_DISCOVERY.md`](diagnostics/CAPABILITY_DISCOVERY.md).

How the Capability operates (people, decision rights, process, data, knowledge, applications, automation, AI, controls, metrics, economics, feedback) is recorded in its States (§3), not in this record. Design Constraints ([`ontology/ONTOLOGY.md`](ontology/ONTOLOGY.md)) are recorded in the `constraints` fields of target designs; Risks in Intervention `risks` or as Risk records (`RSK-###`, [`artifacts/decision-assumption-log.md`](artifacts/decision-assumption-log.md)).

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

```yaml
state:
  id: STA-###
  type: CURRENT | TRANSITION | TARGET
  capability_id: CAP-###
  as_of:              # observation date (CURRENT) or intended horizon (TRANSITION, TARGET)
  people:
  decision_rights:
  process:
  data:
  knowledge:
  applications:
  automation:
  ai:
  controls:
  metric_ids: []
  economics:
  feedback:
  evidence_ids: []
  assumption_ids: []
```

The dimensions are the [`STANDARD.md`](STANDARD.md) §4 system model. A State SHOULD consider them; only dimensions relevant to the transformation boundary need content.

Instances:

- CURRENT: [`artifacts/capability-map.md`](artifacts/capability-map.md);
- TARGET: [`artifacts/capability-target-state.md`](artifacts/capability-target-state.md) (extends this record);
- TRANSITION: [`artifacts/transition-state.md`](artifacts/transition-state.md) (extends this record).

---

## 4. Gap

A material difference between current Capability behavior and required behavior.

```yaml
gap:
  id: GAP-###
  capability_id: CAP-###
  current_state_id:   # STA-### (type CURRENT)
  current_condition:
  required_condition:
  business_impact:
  cause_status: unknown | hypothesized | accepted_as_testable | validated
  hypothesis_ids: []
  evidence_ids: []
```

Instances: [`artifacts/capability-diagnosis.md`](artifacts/capability-diagnosis.md).

`cause_status` summarizes the Gap's Cause Hypotheses (`hypothesis_ids`, §5): it is `accepted_as_testable` or `validated` only when a listed Hypothesis has that status ([`diagnostics/ROOT_CAUSE_ANALYSIS.md`](diagnostics/ROOT_CAUSE_ANALYSIS.md) §7).

---

## 5. Cause

A condition explaining why a Gap exists.

A Cause begins as a Hypothesis (`HYP-###`) unless Evidence justifies stronger status. The ID is unchanged when the Cause is validated.

Canonical diagnostic logic is defined in [`diagnostics/ROOT_CAUSE_ANALYSIS.md`](diagnostics/ROOT_CAUSE_ANALYSIS.md).

Record contract: Hypothesis record in [`artifacts/decision-assumption-log.md`](artifacts/decision-assumption-log.md).

---

## 6. Intervention

A bounded design choice intended to close one or more Gaps.

```yaml
intervention:
  id: INT-###
  gap_ids: []
  hypothesis_ids: []          # causes this intervention addresses
  type:                       # one PUBLIC_API §6 family
  description:
  expected_effect:
  simpler_alternatives_considered: []
  risks: []
  assumption_ids: []
  status: candidate | selected | deferred | rejected
```

Instances: [`artifacts/intervention-map.md`](artifacts/intervention-map.md) (extends this record).

A candidate that Phase 4 decides to investigate keeps `status: candidate`; an Evidence Debt item names what must be learned ([`methodology/04-prioritization.md`](methodology/04-prioritization.md)).

Family definitions: [`design/INTERVENTION_PATTERNS.md`](design/INTERVENTION_PATTERNS.md). Challenge order: [`STANDARD.md`](STANDARD.md) §5.

AI is one intervention family among several.

---

## 7. Initiative

An executable change package implementing one or more Interventions.

```yaml
initiative:
  id: INI-###
  name:
  capability_ids: []
  intervention_ids: []
  owner:
  scope:
  entry_state_id:             # STA-###
  exit_state_id:              # STA-###
  expected_outcome_ids: []
  success_metric_ids: []
  evidence_ids: []
  dependencies: []            # INI-### ids this Initiative depends on
  decision_gates: []          # GAT-### ids and/or {gate: HG-*, subject_ids: []}
  rollback_or_recovery:
  status: proposed | approved | active | paused | stopped | completed
```

Instances: [`artifacts/transformation-roadmap.md`](artifacts/transformation-roadmap.md) (extends this record).

A `decision_gates` mapping names what its gate will decide in `subject_ids`; a planned AI authority increase lists its `AUT-###`.

An Initiative record is created no later than its selection (Phase 4). `status: approved` for a material Initiative requires a Decision closing HG-INITIATIVE ([`STANDARD.md`](STANDARD.md) §8).

A Capability is the unit of transformation.

An Initiative is the unit of coordinated delivery.

---

## 8. Metric

A defined measurable signal used to evaluate an Outcome, Capability, Initiative, AI component, economic effect, or risk.

Canonical semantics and record contract: [`METRICS.md`](METRICS.md) (record: §6).

---

## 9. Evidence

A verifiable source supporting a claim.

Canonical semantics and record contract: [`evidence/EVIDENCE_STANDARD.md`](evidence/EVIDENCE_STANDARD.md) (Evidence: §3; Evidence Debt: §5). Instances: [`artifacts/evidence-register.md`](artifacts/evidence-register.md).

---

## 10. Capability Network

A set of relevant Capabilities and their material dependencies.

Canonical semantics are defined in [`design/CAPABILITY_NETWORK.md`](design/CAPABILITY_NETWORK.md).

---

## 11. System Constraint

The condition that most limits improvement of the target Outcome.

Not a design Constraint ([`ontology/ONTOLOGY.md`](ontology/ONTOLOGY.md)).

Canonical semantics are defined in [`design/CONSTRAINT_ANALYSIS.md`](design/CONSTRAINT_ANALYSIS.md).

---

## 12. Capability Target State

The required future behavior of one Capability: a State (§3) of type TARGET.

Record contract: [`artifacts/capability-target-state.md`](artifacts/capability-target-state.md) (extends §3).

---

## 13. Target Operating Architecture

The integrated target design across relevant Capabilities, roles, Decision Rights, information, knowledge, applications, automation, AI, controls, metrics, and economics.

Canonical semantics are defined in [`design/TARGET_OPERATING_ARCHITECTURE.md`](design/TARGET_OPERATING_ARCHITECTURE.md).

---

## 14. Transition State

An independently operable intermediate State between Current and Target: a State (§3) of type TRANSITION.

A Transition State MAY change several Capabilities at once; its contract ([`artifacts/transition-state.md`](artifacts/transition-state.md)) says how it extends the State record for that case.

Canonical semantics are defined in [`transition/TRANSITION_STATE_MODEL.md`](transition/TRANSITION_STATE_MODEL.md).

---

## 15. Pilot

A bounded operational test of a transformation Hypothesis.

Canonical semantics are defined in [`execution/PILOT_MODEL.md`](execution/PILOT_MODEL.md).

---

## 16. Transformation Slice

The smallest vertical implementation unit that changes a real business behavior and can be evaluated (`SLC-###`).

Canonical semantics are defined in [`execution/DELIVERY_SLICE.md`](execution/DELIVERY_SLICE.md).

---

## 17. Rollout

Controlled expansion of a validated transformation.

Canonical semantics are defined in [`execution/ROLLOUT_MODEL.md`](execution/ROLLOUT_MODEL.md).

---

## 18. Operating Model

Who operates the transformed system and how it is run, decided, observed, supported, and governed after transformation.

Canonical semantics are defined in [`methodology/07-operating-model-governance.md`](methodology/07-operating-model-governance.md).

---

## 19. Evaluation

A structured test of business, capability, operating, human-AI interaction, AI, technical, economic, or governance performance.

Canonical semantics are defined in [`evaluation/EVALUATION_SYSTEM.md`](evaluation/EVALUATION_SYSTEM.md).

---

## 20. Value Realization

Observed and sufficiently sustained business value attributable to a transformation with stated confidence.

Canonical semantics are defined in [`measurement/VALUE_REALIZATION.md`](measurement/VALUE_REALIZATION.md).

---

## 21. Evolution

Revising the diagnosis, target, roadmap, or AI authority from Phase 8 evidence.

Canonical semantics are defined in [`methodology/08-measurement-evolution.md`](methodology/08-measurement-evolution.md).

---

## 22. Semantic integrity

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
