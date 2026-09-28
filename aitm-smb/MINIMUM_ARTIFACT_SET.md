# Minimum Artifact Set

Maps the profile content defined in `APPLICATION_PROFILES.md` to artifact contracts. Subordinate to it (`NORMATIVE_INDEX.md` tier 8): on conflict, `APPLICATION_PROFILES.md` wins. Requirement status: `CONFORMANCE.md` §3. Per-artifact view (records, owning module, producing skills): `artifacts/INDEX.md`.

## 1. Purpose

AITM-SMB is artifact-driven, but not document-driven.

The method requires semantic completeness, not paperwork volume.

A contract is not a file: contracts MAY be merged into fewer instance files or split (§3, §4). Instances live in the engagement workspace (`artifacts/_ARTIFACT_CONTRACT.md`).

---

## 2. Profile-to-contract map

### 2.1 Compact

Every application, whatever its profiles:

| Content (`APPLICATION_PROFILES.md` §3) | Artifact contract |
|---|---|
| Transformation Intent (with Outcome records) | `artifacts/transformation-intent.md` |
| Capability Map (with CURRENT States) | `artifacts/capability-map.md` |
| Capability Diagnosis (Gaps, Cause Hypotheses) | `artifacts/capability-diagnosis.md`; Hypothesis records in `artifacts/decision-assumption-log.md` |
| Intervention Map | `artifacts/intervention-map.md` |
| Capability Target State | `artifacts/capability-target-state.md` |
| Transformation Roadmap (Initiative records) | `artifacts/transformation-roadmap.md` |
| system-effect check, per selected Initiative | `artifacts/system-effect-assessment.md` (a short record suffices) |
| Governance minimum, when any `AI_*` Intervention is selected | `artifacts/autonomy-assessment.md` with an approved Authority Ceiling; `artifacts/ai-governance-canvas.md` fields `owner`, `permissions`, `prohibited_actions`, `approval_required`, `escalation_conditions`, `recovery_path` |
| Transformation Scorecard (Metric records) | `artifacts/transformation-scorecard.md` |
| Evidence Register | `artifacts/evidence-register.md` |
| Decision & Assumption Log | `artifacts/decision-assumption-log.md` |

### 2.2 Standard adds

| Content (`APPLICATION_PROFILES.md` §4) | Artifact contract |
|---|---|
| Business System Map | `artifacts/business-system-map.md` |
| Capability Network | `artifacts/capability-network.md` |
| System Constraint | `artifacts/system-constraint.md` |
| System Effect Assessment | `artifacts/system-effect-assessment.md` (full) |
| Prioritization Matrix | `artifacts/prioritization-matrix.md` |
| Decision Rights Map | `artifacts/decision-rights-map.md` |
| Target Operating Architecture | `artifacts/target-operating-architecture.md` |
| Transition States | `artifacts/transition-state.md` |
| Pilot Plan + Evaluation Plan, where a pilot is required | `artifacts/pilot-plan.md`, `artifacts/evaluation-plan.md` |
| Observability Plan | `artifacts/observability-plan.md` |
| Operating Model | `artifacts/operating-model.md` |
| Adoption Plan | `artifacts/adoption-plan.md` |
| Rollout Plan, where rolling out | `artifacts/rollout-plan.md` |
| Value Realization Report (value state + Evidence) | `artifacts/value-realization-report.md` |

### 2.3 Governed adds

AI-specific rows apply where AI is used (`APPLICATION_PROFILES.md` §5).

| Content (`APPLICATION_PROFILES.md` §5) | Artifact contract |
|---|---|
| complete AI Governance Canvas with a named risk owner | `artifacts/ai-governance-canvas.md` (all fields) |
| approved Authority Ceiling for every Capability in which AI is used | `artifacts/autonomy-assessment.md`; approval: HG-AUTHORITY Decision in `artifacts/decision-assumption-log.md` |
| AI Change Control (CHG records) | `artifacts/ai-governance-canvas.md` `changes` |
| incident handling (INC records) | `artifacts/incident-record.md` |
| Evaluation Dataset for AI components | `artifacts/evaluation-plan.md` `datasets` |
| Execution Gate records (GAT) | `artifacts/execution-gate.md` |
| Operational Readiness Audit | `artifacts/execution-gate.md` (Gate E) |
| explicit risk ownership (RSK records with named owners; HG-RISK Decisions for accepted material Risks) | `artifacts/decision-assumption-log.md` (Risk and Decision records) |

### 2.4 Portfolio adds

| Content (`APPLICATION_PROFILES.md` §6) | Artifact contract |
|---|---|
| Transformation Portfolio | `artifacts/transformation-portfolio.md` |
| Portfolio Prioritization | `artifacts/prioritization-matrix.md` (criteria and stop condition: `portfolio/PORTFOLIO_PRIORITIZATION.md`) |
| shared-enabler model; change saturation controls (WIP limit) | `artifacts/transformation-portfolio.md` |
| cross-capability dependency analysis | `artifacts/capability-network.md` (DEP records) |

### 2.5 Measured adds

| Content (`APPLICATION_PROFILES.md` §7) | Artifact contract |
|---|---|
| Benefit Evidence Chain; attribution confidence; sustained-value review | `artifacts/value-realization-report.md` (required also with Compact + Measured) |

---

## 3. Artifact merging

Artifacts MAY be merged when:

```text
scope is small
traceability remains intact
ownership remains clear
agent parsing remains reliable
```

Example:

```text
Capability Map + Capability Diagnosis
```

MAY exist as one file if stable IDs and sections remain distinct. Each record keeps its ID and its record type stays identifiable (`CONFORMANCE.md` §4, `artifacts/_ARTIFACT_CONTRACT.md`).

---

## 4. Artifact splitting

Artifacts MAY be split when:

```text
scope is large
multiple owners exist
independent lifecycle exists
agent context size requires it
```

Splitting keeps every ID (`ontology/ONTOLOGY.md`).

---

## 5. Rule

Do not create documents to satisfy a checklist.

Create artifacts to preserve:

```text
decision quality
traceability
evidence
ownership
execution
```
