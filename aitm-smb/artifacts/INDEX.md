# AITM-SMB Artifact Registry

Registry (`NORMATIVE_INDEX.md`): enumerates artifact contracts and defines no semantics. Contract shape, instance metadata and the engagement workspace: `artifacts/_ARTIFACT_CONTRACT.md`. Where each record shape is defined: `CANONICAL_CONCEPTS.md`.

Columns: role and the records the contract holds (ID prefixes: `ontology/ONTOLOGY.md`); owning module (semantics); producing skills by number (`skills/INDEX.md`), the same set as the contract's `produced_by` (`artifacts/_ARTIFACT_CONTRACT.md` §2); profiles that require it (`APPLICATION_PROFILES.md`, mapping `MINIMUM_ARTIFACT_SET.md`). "Compact" means every application.

## Contract

| File | Role |
|---|---|
| `artifacts/_ARTIFACT_CONTRACT.md` | shape of every contract; instance metadata; engagement workspace; merge rule |

## Canonical artifact contracts

| Artifact | Role and records | Owning module | Produced by | Required by |
|---|---|---|---|---|
| `artifacts/transformation-intent.md` | outcome framing: ATI; Outcome (OUT) instances; conformance declaration | `methodology/00-intent.md`; Outcome `CORE_MODEL.md` §1 | 01; 38 (conformance) | Compact |
| `artifacts/decision-assumption-log.md` | decisions, assumptions, hypotheses, risks: DEC, ASM, HYP, RSK | `DECISION_MODEL.md`; `evidence/EVIDENCE_STANDARD.md`; `diagnostics/ROOT_CAUSE_ANALYSIS.md`; Risk `ontology/ONTOLOGY.md` | 01, 03, 05, 06, 07, 08, 09, 12, 16, 36; any skill recording a gate Decision or Assumption | Compact |
| `artifacts/evidence-register.md` | evidence inventory: Evidence (EVD), Evidence Debt, and material Uncertainty (UNC) instances | `evidence/EVIDENCE_STANDARD.md`; `evidence/UNCERTAINTY_MODEL.md` | 02, 11, 12, 16; any skill MAY append | Compact |
| `artifacts/business-system-map.md` | current system: business-system entities | `ontology/ONTOLOGY.md` | 02 | Standard |
| `artifacts/capability-map.md` | stable organizational abilities: Capability (CAP) and CURRENT State (STA) instances | Core: `CORE_MODEL.md` §2–§3; discovery `diagnostics/CAPABILITY_DISCOVERY.md` | 02, 11 | Compact |
| `artifacts/capability-diagnosis.md` | gaps and causes: Gap (GAP) instances; causes as HYP in the log | `diagnostics/DIAGNOSTIC_MODEL.md`; Gap `CORE_MODEL.md` §4 | 03, 12 | Compact |
| `artifacts/diagnostic-record.md` | atomic diagnosis record: DIA | `diagnostics/DIAGNOSTIC_MODEL.md` | 03, 12, 16 | optional |
| `artifacts/intervention-map.md` | all intervention candidates: Intervention (INT) instances | `design/INTERVENTION_PATTERNS.md`; Intervention `CORE_MODEL.md` §6 | 04, 05 (status) | Compact |
| `artifacts/ai-suitability-assessment.md` | AI fit: AIS | `diagnostics/AI_SUITABILITY.md` | 04, 13 | optional; where AI is proposed, the usual home of the AI justification (`CONFORMANCE.md` §1 item 7) |
| `artifacts/autonomy-assessment.md` | AI authority fit: AUT, incl. Authority Ceiling | `diagnostics/AUTONOMY_SUITABILITY.md` | 04, 08, 09, 14, 34 | Compact, when an `AI_*` Intervention is selected; Governed: every Capability in which AI is used |
| `artifacts/prioritization-matrix.md` | initiative selection: select, defer, reject, investigate | `methodology/04-prioritization.md`; Portfolio: `portfolio/PORTFOLIO_PRIORITIZATION.md` | 05 | Standard; Portfolio |
| `artifacts/transformation-roadmap.md` | transition sequencing: Initiative (INI) instances | Core: `CORE_MODEL.md` §7 | 05 (INI at selection), 07 | Compact |
| `artifacts/capability-target-state.md` | future state of one Capability: TARGET State (STA) | `design/TARGET_STATE_DESIGN.md`; Core: `CORE_MODEL.md` §3, §12 | 06, 15 | Compact |
| `artifacts/capability-network.md` | inter-capability dependencies: CPN, DEP | `design/CAPABILITY_NETWORK.md` | 06, 17 | Standard; Portfolio |
| `artifacts/system-constraint.md` | current limiting condition: CST | `design/CONSTRAINT_ANALYSIS.md` | 06, 18 | Standard |
| `artifacts/system-effect-assessment.md` | INV-09 system effects (upstream, downstream, shared-resource, incentive, Constraint Migration): SFX | `design/LOCAL_OPTIMIZATION_GUARD.md` | 06, 19, 24 | Compact (short system-effect check); Standard (full) |
| `artifacts/target-operating-architecture.md` | integrated system-level target: TOA | `design/TARGET_OPERATING_ARCHITECTURE.md` | 06, 20 | Standard |
| `artifacts/decision-rights-map.md` | target authority: BDS | `design/DECISION_RIGHTS_ARCHITECTURE.md` | 06, 23 | Standard |
| `artifacts/transition-state.md` | operable intermediate state: TRANSITION State (STA) | `transition/TRANSITION_STATE_MODEL.md` | 07, 21 | Standard |
| `artifacts/transformation-portfolio.md` | multi-initiative coordination: PTF | `portfolio/TRANSFORMATION_PORTFOLIO.md` | 07, 22 | Portfolio |
| `artifacts/pilot-plan.md` | bounded operational validation: PLT | `execution/PILOT_MODEL.md` | 07, 25 | Standard, where a pilot is required |
| `artifacts/evaluation-plan.md` | evaluation contract: EVL plans and results; evaluation datasets | `evaluation/EVALUATION_SYSTEM.md`; `evaluation/EVALUATION_DATASET.md` | 07, 08, 09, 26 (plan), 27 (datasets), 32 (results) | Standard, where a pilot is required; Governed: datasets for AI components |
| `artifacts/execution-gate.md` | execution gate decisions: GAT | `execution/EXECUTION_GATE_MODEL.md` | 07, 08, 09, 25 (Gate C), 32 (Gate D), 33 (Gate G), 35 (Gate E) | Governed |
| `artifacts/operating-model.md` | operational ownership | `methodology/07-operating-model-governance.md` | 08 | Standard |
| `artifacts/observability-plan.md` | operating evidence | `operations/OBSERVABILITY_MODEL.md` | 08, 28 | Standard |
| `artifacts/adoption-plan.md` | human behavior transition; role transitions | `change/CHANGE_ADOPTION_MODEL.md`; `change/ROLE_TRANSITION_MODEL.md` | 08, 30 | Standard |
| `artifacts/ai-governance-canvas.md` | AI controls; AI Change (CHG) instances | `governance/GOVERNANCE_OPERATING_MODEL.md`; changes: `governance/AI_CHANGE_CONTROL.md` | 08, 31, 34 (changes) | Compact, when an `AI_*` Intervention is selected (Governance minimum fields); Governed (complete) |
| `artifacts/rollout-plan.md` | controlled expansion: ROL | `execution/ROLLOUT_MODEL.md` | 08, 29 | Standard, where rolling out |
| `artifacts/incident-record.md` | AI-enabled operations incidents: INC | `operations/INCIDENT_MODEL.md` | 40 | Governed |
| `artifacts/transformation-scorecard.md` | effect measurement: Metric (MET) instances; effect conclusion | `METRICS.md` | 01, 09; any skill MAY append Metric records | Compact |
| `artifacts/value-realization-report.md` | realized business value: VRL; value conclusion; benefit chain | `measurement/VALUE_REALIZATION.md`; `measurement/BENEFIT_EVIDENCE_CHAIN.md` | 09, 33 | Standard; Measured (completes it; also with Compact + Measured) |

Records whose contract is a module and that have no designated host artifact (Transformation Slice SLC, Experiment EXP): `CANONICAL_CONCEPTS.md` §1. Their instances MAY sit in any engagement file under the merge rule (`artifacts/_ARTIFACT_CONTRACT.md` §7).

## Deprecated redirects

Kept through 1.x (`PUBLIC_API.md` §9); `removal_target: 2.0.0` (`VERSIONING.md` §5).

| Deprecated | Replacement | Removal target |
|---|---|---|
| `artifacts/target-architecture.md` | `artifacts/capability-target-state.md` + `artifacts/target-operating-architecture.md` | 2.0.0 |
| `artifacts/ai-opportunity-map.md` | `artifacts/intervention-map.md` + `artifacts/ai-suitability-assessment.md` | 2.0.0 |

## Artifact rule

Skills MUST NOT produce non-canonical or deprecated artifacts. Transient findings go through `AGENT_OUTPUT_STANDARD.md`.
