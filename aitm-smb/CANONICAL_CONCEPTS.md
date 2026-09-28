# AITM-SMB Canonical Concept Registry

**Version:** 1.1.0

Each record shape is defined exactly once; this registry names where. Modules own meaning and rules (Semantics); the record contract owns field names. Files that hold instances reference the record contract and MAY add fields only where they say so explicitly ("extends <record> with: …"). Where the record contract is an artifact contract, higher-precedence files reference it and MUST NOT restate its schema.

Identifier registry and rules: `ontology/ONTOLOGY.md`. Instance metadata: `artifacts/_ARTIFACT_CONTRACT.md`.

## 1. Objects and records

| Concept | Semantics | Record contract | ID |
|---|---|---|---|
| Transformation Intent | `methodology/00-intent.md` | `artifacts/transformation-intent.md` | `ATI-###` |
| Outcome | `CORE_MODEL.md` §1 | `CORE_MODEL.md` §1 (instances: `artifacts/transformation-intent.md`) | `OUT-###` |
| Capability | `CORE_MODEL.md` §2 | `CORE_MODEL.md` §2 (instances: `artifacts/capability-map.md`) | `CAP-###` |
| State | `CORE_MODEL.md` §3 | `CORE_MODEL.md` §3 (CURRENT: `artifacts/capability-map.md`; TARGET: `artifacts/capability-target-state.md` extends it; TRANSITION: `artifacts/transition-state.md` extends it) | `STA-###` |
| Gap | `CORE_MODEL.md` §4 | `CORE_MODEL.md` §4 (instances: `artifacts/capability-diagnosis.md`) | `GAP-###` |
| Observation, Symptom | `diagnostics/DIAGNOSTIC_MODEL.md` | `artifacts/diagnostic-record.md` (`observations`, `symptoms`) | — |
| Cause / Hypothesis | `diagnostics/ROOT_CAUSE_ANALYSIS.md` | `artifacts/decision-assumption-log.md` Hypothesis record | `HYP-###` (ID unchanged when validated) |
| Intervention | `CORE_MODEL.md` §6 | `CORE_MODEL.md` §6 (instances: `artifacts/intervention-map.md` extends it) | `INT-###` |
| Intervention family | `design/INTERVENTION_PATTERNS.md` (tokens: `PUBLIC_API.md` §6; challenge order: `STANDARD.md` §5) | value of Intervention `type` | — |
| Initiative | `CORE_MODEL.md` §7 | `CORE_MODEL.md` §7 (instances: `artifacts/transformation-roadmap.md` extends it) | `INI-###` |
| Metric | `METRICS.md` | `METRICS.md` §6 (instances: `artifacts/transformation-scorecard.md`) | `MET-###` |
| Economic hypothesis | `economics/TRANSFORMATION_ECONOMICS.md` | `economics/TRANSFORMATION_ECONOMICS.md` §5 | — |
| Evidence, Evidence Debt | `evidence/EVIDENCE_STANDARD.md` | `evidence/EVIDENCE_STANDARD.md` §3, §5 (instances: `artifacts/evidence-register.md`) | `EVD-###` |
| Decision (engagement decision) | `DECISION_MODEL.md` | `artifacts/decision-assumption-log.md` | `DEC-###` |
| Assumption | `evidence/EVIDENCE_STANDARD.md` §7 (labels: `AGENTS.md` §3) | `artifacts/decision-assumption-log.md` | `ASM-###` |
| Uncertainty | `evidence/UNCERTAINTY_MODEL.md` | `evidence/UNCERTAINTY_MODEL.md` §5 (instances: `artifacts/evidence-register.md` `uncertainties`) | `UNC-###` |
| Business-system entities (Value Stream, Process, Role, Data Asset, Knowledge Asset, Application, Automation, AI Component, Agent, Control, design Constraint) | `ontology/ONTOLOGY.md` | instances: `artifacts/business-system-map.md` | — |
| Risk | `ontology/ONTOLOGY.md` | `artifacts/decision-assumption-log.md` Risk record | `RSK-###` |
| AI Suitability | `diagnostics/AI_SUITABILITY.md` | `artifacts/ai-suitability-assessment.md` | `AIS-###` |
| Autonomy, Authority Ceiling | `diagnostics/AUTONOMY_SUITABILITY.md` | `artifacts/autonomy-assessment.md` | `AUT-###` |
| Diagnostic Record | `diagnostics/DIAGNOSTIC_MODEL.md` | `artifacts/diagnostic-record.md` | `DIA-###` |
| Capability Network, Capability Dependency | `design/CAPABILITY_NETWORK.md` | `artifacts/capability-network.md` | `CPN-###`, `DEP-###` |
| System Constraint, Constraint Migration | `design/CONSTRAINT_ANALYSIS.md` | `artifacts/system-constraint.md` | `CST-###` |
| System Effect | `design/LOCAL_OPTIMIZATION_GUARD.md` | `artifacts/system-effect-assessment.md` | `SFX-###` |
| Capability Target State | `CORE_MODEL.md` §12 | `artifacts/capability-target-state.md` (extends `CORE_MODEL.md` §3) | `STA-###` |
| Target Operating Architecture | `design/TARGET_OPERATING_ARCHITECTURE.md` | `artifacts/target-operating-architecture.md` | `TOA-###` |
| Decision Rights, Business Decision | `design/DECISION_RIGHTS_ARCHITECTURE.md` | `artifacts/decision-rights-map.md` | `BDS-###` |
| Transition State | `transition/TRANSITION_STATE_MODEL.md` | `artifacts/transition-state.md` (extends `CORE_MODEL.md` §3) | `STA-###` |
| Transformation Portfolio | `portfolio/TRANSFORMATION_PORTFOLIO.md` | `artifacts/transformation-portfolio.md` | `PTF-###` |
| Transformation Slice | `execution/DELIVERY_SLICE.md` | `execution/DELIVERY_SLICE.md` | `SLC-###` |
| Experiment | `execution/EXPERIMENT_MODEL.md` | `execution/EXPERIMENT_MODEL.md` | `EXP-###` |
| Pilot | `execution/PILOT_MODEL.md` | `artifacts/pilot-plan.md` | `PLT-###` |
| Execution Gate | `execution/EXECUTION_GATE_MODEL.md` | `artifacts/execution-gate.md` | `GAT-###` |
| Evaluation | `evaluation/EVALUATION_SYSTEM.md` | `evaluation/EVALUATION_SYSTEM.md` §4 (plans and results: `artifacts/evaluation-plan.md`) | `EVL-###` |
| Evaluation Dataset | `evaluation/EVALUATION_DATASET.md` | `evaluation/EVALUATION_DATASET.md` (instances: `artifacts/evaluation-plan.md` `datasets`) | — |
| Rollout | `execution/ROLLOUT_MODEL.md` | `artifacts/rollout-plan.md` | `ROL-###` |
| Operating Model | `methodology/07-operating-model-governance.md` | `artifacts/operating-model.md` | — |
| Observability | `operations/OBSERVABILITY_MODEL.md` | `artifacts/observability-plan.md` | — |
| Incident | `operations/INCIDENT_MODEL.md` | `artifacts/incident-record.md` | `INC-###` |
| AI Governance | `governance/GOVERNANCE_OPERATING_MODEL.md` | `artifacts/ai-governance-canvas.md` | — |
| AI Change | `governance/AI_CHANGE_CONTROL.md` | `governance/AI_CHANGE_CONTROL.md` §3 (instances: `artifacts/ai-governance-canvas.md` `changes`) | `CHG-###` |
| Authority promotion / demotion | `governance/AUTHORITY_ESCALATION_MODEL.md` | recorded as a Decision (HG-AUTHORITY) + `artifacts/autonomy-assessment.md` update | — |
| Adoption, Role Transition | `change/CHANGE_ADOPTION_MODEL.md`, `change/ROLE_TRANSITION_MODEL.md` | `artifacts/adoption-plan.md` (role transitions section) | — |
| Value Realization | `measurement/VALUE_REALIZATION.md` | `artifacts/value-realization-report.md` | `VRL-###` |
| Benefit Evidence Chain | `measurement/BENEFIT_EVIDENCE_CHAIN.md` | `measurement/BENEFIT_EVIDENCE_CHAIN.md` (instances: `artifacts/value-realization-report.md` `benefit_chain`) | — |
| Evolution | `methodology/08-measurement-evolution.md` | — | — |

## 2. Method rules and vocabularies

| Concept | Canonical source |
|---|---|
| Canonical transformation chain | `STANDARD.md` §2 |
| Core invariants (INV-01…INV-15) | `STANDARD.md` §3 |
| System model dimensions | `STANDARD.md` §4 |
| Intervention challenge order | `STANDARD.md` §5 (questions: `DECISION_MODEL.md` §1) |
| Autonomy levels L0–L5 (labels, authority per level) | `diagnostics/AUTONOMY_SUITABILITY.md` §2 (labels restated in `STANDARD.md` §6, `PUBLIC_API.md` §7) |
| Autonomy challenge questions | `DECISION_MODEL.md` §3 |
| Human decision gates (`HG-*`) | `STANDARD.md` §8 |
| Materiality | `STANDARD.md` §16 |
| Diagnostic dimensions | `diagnostics/DIAGNOSTIC_DIMENSIONS.md` |
| Value states | `measurement/VALUE_REALIZATION.md` §2 |
| Application profiles | `APPLICATION_PROFILES.md` |
| Lifecycle phases and exit conditions | `EXECUTION_MODEL.md` §1, §2 |
| Minimum valid path | `EXECUTION_MODEL.md` §6 |
| Trace record, missing links | `TRACEABILITY.md` §4 |
| Agent statuses | `PUBLIC_API.md` §8 |
| Agent output block | `AGENT_OUTPUT_STANDARD.md` |
| Evidence labels | `AGENTS.md` §3 |
| Engagement workspace (where instances live) | `artifacts/_ARTIFACT_CONTRACT.md` |

## 3. Precedence

The Semantics source of a concept is normative whenever the concept is used, even when its module is not otherwise activated; the module's procedures remain activation-dependent.

If another document conflicts with a canonical source, the canonical source wins subject to `NORMATIVE_INDEX.md`. Within one precedence tier, the canonical source named here wins.
