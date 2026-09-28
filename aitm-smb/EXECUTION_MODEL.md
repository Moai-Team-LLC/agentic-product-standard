# AITM-SMB Execution Model

**Version:** 1.1.0

AITM-SMB is sequential in dependency but iterative in execution.

---

## 1. Canonical lifecycle

| Phase | Phase file | Orchestrator skill |
|---|---|---|
| 0 Frame | [`methodology/00-intent.md`](methodology/00-intent.md) | [`skills/01-discover-transformation/SKILL.md`](skills/01-discover-transformation/SKILL.md) |
| 1 Observe | [`methodology/01-current-system.md`](methodology/01-current-system.md) | [`skills/02-map-current-system/SKILL.md`](skills/02-map-current-system/SKILL.md) |
| 2 Diagnose | [`methodology/02-capability-diagnosis.md`](methodology/02-capability-diagnosis.md) | [`skills/03-diagnose-capabilities/SKILL.md`](skills/03-diagnose-capabilities/SKILL.md) |
| 3 Design Interventions | [`methodology/03-intervention-design.md`](methodology/03-intervention-design.md) | [`skills/04-design-interventions/SKILL.md`](skills/04-design-interventions/SKILL.md) |
| 4 Decide | [`methodology/04-prioritization.md`](methodology/04-prioritization.md) | [`skills/05-prioritize-initiatives/SKILL.md`](skills/05-prioritize-initiatives/SKILL.md) |
| 5 Design Target System | [`methodology/05-target-system-design.md`](methodology/05-target-system-design.md) | [`skills/06-design-target-system/SKILL.md`](skills/06-design-target-system/SKILL.md) |
| 6 Design Transition | [`methodology/06-roadmap.md`](methodology/06-roadmap.md) | [`skills/07-build-roadmap/SKILL.md`](skills/07-build-roadmap/SKILL.md) |
| 7 Operationalize | [`methodology/07-operating-model-governance.md`](methodology/07-operating-model-governance.md) | [`skills/08-design-operating-model/SKILL.md`](skills/08-design-operating-model/SKILL.md) |
| 8 Measure & Evolve | [`methodology/08-measurement-evolution.md`](methodology/08-measurement-evolution.md) | [`skills/09-measure-evolution/SKILL.md`](skills/09-measure-evolution/SKILL.md) |

These are the only phase names. The 12 steps of [`METHOD_FLOW.md`](METHOD_FLOW.md) §1 map onto these phases.

Profile selection ([`skills/36-select-application-profile/SKILL.md`](skills/36-select-application-profile/SKILL.md)) and context bundling ([`skills/37-build-context-bundle/SKILL.md`](skills/37-build-context-bundle/SKILL.md)) run before any orchestrator step that needs them. [`skills/10-audit-aitm-engagement/SKILL.md`](skills/10-audit-aitm-engagement/SKILL.md) audits at any phase. [`skills/40-handle-incident/SKILL.md`](skills/40-handle-incident/SKILL.md) runs whenever an incident occurs in a pilot, rollout, or operation (Phases 7–8).

Pilots, experiments and rollout have no separate phase:

```text
Phase 6  designs Experiments and Pilots where material uncertainty remains (INV-11),
         each with a pre-registered evaluation plan
Phase 7  runs and evaluates pilots, decides promotion, plans and executes rollout,
         and changes AI authority
Phase 8  evaluates post-rollout effect and value
```

Modules: [`execution/EXPERIMENT_MODEL.md`](execution/EXPERIMENT_MODEL.md), [`execution/PILOT_MODEL.md`](execution/PILOT_MODEL.md), [`evaluation/EVALUATION_SYSTEM.md`](evaluation/EVALUATION_SYSTEM.md), [`execution/ROLLOUT_MODEL.md`](execution/ROLLOUT_MODEL.md), [`governance/AUTHORITY_ESCALATION_MODEL.md`](governance/AUTHORITY_ESCALATION_MODEL.md).

---

## 2. Phase gates

| Phase | Exit condition | Typical human gates | Execution gate (Governed) |
|---|---|---|---|
| 0 Frame | Outcome records (OUT) with owner, Metric (MET), baseline or known baseline gap, target and horizon; constraints recorded; profiles selected (DEC); Outcomes and profile Decision approved | `HG-OUTCOME` | — |
| 1 Observe | each relevant Capability (CAP) has a CURRENT State (STA) backed by Evidence (EVD) or by Assumptions (ASM) a named business owner stated or accepted ([`AGENTS.md`](AGENTS.md) §3); Business System Map where the profile requires it | — | — |
| 2 Diagnose | material Gaps (GAP) and their cause Hypotheses (HYP) explicit; a Gap proceeds only when intervention-ready (cause validated, or accepted as testable by a Decision of the Capability or Outcome owner); otherwise its Evidence Debt is recorded | — | — |
| 3 Design Interventions | each intervention-ready Gap has candidate Interventions (INT) with a `type` from [`PUBLIC_API.md`](PUBLIC_API.md) §6 and simpler alternatives considered; where AI is proposed: AI need justified, verification plausible, authority assumptions explicit; each `AI_*` candidate proposed for selection has a proposed Authority Ceiling | `HG-AUTHORITY` | — |
| 4 Decide | selected Initiatives recorded as INI records linked to Outcomes, Capabilities, Gaps, Interventions and Metrics; expected system effects (INV-09) recorded per selected Initiative (SFX); rejected and deferred candidates carry a rationale; material selection approved; no `AI_*` Intervention selected before its Authority Ceiling is approved; material budget approved by a Decision that cites each material Initiative's economic hypothesis (`economic_hypothesis`, [`economics/TRANSFORMATION_ECONOMICS.md`](economics/TRANSFORMATION_ECONOMICS.md) §5); Portfolio: no Initiative selected while a [`portfolio/PORTFOLIO_PRIORITIZATION.md`](portfolio/PORTFOLIO_PRIORITIZATION.md) §5 stop condition holds, unless an approved Decision of the portfolio owner records the override and its reason | `HG-INITIATIVE`, `HG-BUDGET` | A |
| 5 Design Target System | Capability Target States (STA, type TARGET) for selected Capabilities; the design outputs the profile requires (from Standard: a coherent Target Operating Architecture); dependencies, material authority and system effects (INV-09; SFX refined at system level) explicit; system-level metrics exist; Target Operating Architecture approved (Compact: Capability Target States) | `HG-TOA`, `HG-DECISION-RIGHTS` | B |
| 6 Design Transition | every material Initiative has owner, bounded scope, dependency context, evidence plan, decision gates, rollback/recovery and success metrics; Transition States operable where the profile requires them; planned AI authority increases sit behind an `HG-AUTHORITY` decision gate naming its AUT-###; required pilots and experiments designed with pre-registered evaluation; transformation WIP bounded (Portfolio) | `HG-BUDGET` | C |
| 7 Operationalize | ownership explicit; observability active; failure path and support model defined; role changes explicit; adoption defined (training, support, feedback, adoption metrics); governance controls executable; where piloted: pilot evaluated and promotion decided; where rolling out: rollout gates ([`execution/ROLLOUT_MODEL.md`](execution/ROLLOUT_MODEL.md) §3) verified before each stage | `HG-AUTHORITY`, `HG-DECISION-RIGHTS`, `HG-RISK`, `HG-PROMOTION` | D, E, F |
| 8 Measure & Evolve | effect evaluated against baseline; value state recorded with Evidence where the profile requires a Value Realization Report; diagnosis, target, roadmap and authority updated from Evidence | `HG-VALUE`, `HG-AUTHORITY` | G |

Rules:

- A phase is complete only when its exit condition holds and no gate triggered in it remains open. Exception: Phase 3 MAY exit while `HG-AUTHORITY` for a proposed Authority Ceiling is open; the `AI_*` Intervention is not selected until the ceiling is approved.
- Typical gates are a reading aid. A [`STANDARD.md`](STANDARD.md) §8 gate applies whenever its trigger occurs, in any phase.
- "Decision gates" are the Initiative `decision_gates` ([`CORE_MODEL.md`](CORE_MODEL.md) §7). Execution Gate records (GAT, [`execution/EXECUTION_GATE_MODEL.md`](execution/EXECUTION_GATE_MODEL.md)) are required under the Governed profile; other profiles MAY use them. They are kept per Initiative: Gate A at selection (Phase 4; readiness itself is the Phase 2 exit, and Gate A records that the Initiative's Gaps meet it), Gate B after `HG-TOA` (Phase 5), Gates C–G from Phase 6 (producers: [`artifacts/INDEX.md`](artifacts/INDEX.md)).
- Phases 5 to 7 produce only the outputs the active profile requires ([`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md)). In Compact, Capability Target States stand in for the Target Operating Architecture, and the Phase 7 content (operating owner, observability signal, support path, role changes, failure or rollback path, adoption) MAY sit on the Initiative as `operation:` ([`artifacts/transformation-roadmap.md`](artifacts/transformation-roadmap.md)) instead of separate plans.
- Phase files refine these exit conditions and MUST agree with them.

---

## 3. Iteration

Later Evidence MAY invalidate earlier assumptions.

Examples:

```text
AI assessment reveals deterministic rule is sufficient
→ return to Intervention Design

Target design reveals unavailable knowledge
→ return to Diagnosis / Intervention

Pilot disproves causal hypothesis
→ return to Diagnosis

Refined system effect or System Constraint changes a priority
→ return to Decide (HG-INITIATIVE)

Rollout creates new System Constraint
→ revise Target / Portfolio
```

Iteration is expected.

Silent semantic drift is not.

On re-entry, a revised record keeps its ID; a replaced record keeps its ID and gets `status: superseded` ([`ontology/ONTOLOGY.md`](ontology/ONTOLOGY.md)).

---

## 4. Human gates

Gates and their identifiers: [`STANDARD.md`](STANDARD.md) §8.

Agents MUST stop when a required human gate remains open, including a required upstream gate that is still open. They list it in `open_gates`, which holds the gates of all proposed gate Decisions relevant to the handoff ([`AGENT_OUTPUT_STANDARD.md`](AGENT_OUTPUT_STANDARD.md)), and report `HUMAN_DECISION_REQUIRED` unless `BLOCKED` or `INSUFFICIENT_EVIDENCE` takes precedence ([`PUBLIC_API.md`](PUBLIC_API.md) §8). An open gate alone is never `BLOCKED`; that status is for missing inputs and unresolved normative conflicts. Procedure: [`AGENTS.md`](AGENTS.md) §4.

---

## 5. Evidence gates

The correct result MAY be:

```text
INSUFFICIENT_EVIDENCE
```

when proceeding would require invented business facts ([`PUBLIC_API.md`](PUBLIC_API.md) §8), including a State, Gap or Outcome baseline resting only on agent inference ([`AGENTS.md`](AGENTS.md) §3). Record what is missing as Evidence Debt ([`evidence/EVIDENCE_STANDARD.md`](evidence/EVIDENCE_STANDARD.md) §5).

---

## 6. Minimum valid path

Every application, including Compact, MUST preserve:

```text
Outcome
→ Capability
→ Gap
→ Intervention
→ Initiative
→ Target State
→ Metric
→ Evidence
```

Target State here is the Capability Target State (STA, type TARGET). The order follows [`STANDARD.md`](STANDARD.md) §2.

No profile may skip these semantic layers. Artifacts may be merged; semantic layers may not.

This path is the floor, not the full conformance test: [`CONFORMANCE.md`](CONFORMANCE.md) §1 adds Current State, Cause, authority and system-effect requirements.
