# AITM-SMB Skill Registry

Skills are procedures that execute the methodology. They define no methodology semantics; modules and record contracts do (`NORMATIVE_INDEX.md`, `CANONICAL_CONCEPTS.md`).

Each skill lives at `skills/<directory>/SKILL.md`. Shape of a skill: `skills/_SKILL_TEMPLATE.md`.

---

## 1. Skill classes

AITM-SMB skills are divided into five classes. The frontmatter `category` names the kind of work.

| Class | Numbers | `category` |
|---|---|---|
| A. Phase Orchestrators | 01–10 | `orchestrator` |
| B. Diagnostic & Capability-Design Specialists | 11–16 | `diagnostic-specialist` (15: `design-specialist`) |
| C. System & Transformation Design | 17–24 | `design-specialist` |
| D. Execution & Governance | 25–35, 40 | `execution-governance` |
| E. Framework Operations | 36–39 | `framework-operations` |

An orchestrator runs one phase: it coordinates specialist skills and artifacts and MUST NOT redefine methodology semantics. A specialist skill owns the detailed procedure for its concept.

If an orchestrator and a specialist conflict, the specialist procedure plus the normative methodology source wins.

---

## 2. Router

Phase: `EXECUTION_MODEL.md` §1. Human gates: `STANDARD.md` §8. Produces: artifact contracts in `artifacts/` (§4).

| No. | Directory | Purpose | Phase | Human gates | Produces |
|---|---|---|---|---|---|
| 01 | `01-discover-transformation` | frame Outcomes, owner, constraints; select profiles | 0 | HG-OUTCOME | transformation-intent, decision-assumption-log, transformation-scorecard (baseline Metrics) |
| 02 | `02-map-current-system` | map Capabilities, their CURRENT States, and the current business system | 1 | — | business-system-map, capability-map, evidence-register |
| 03 | `03-diagnose-capabilities` | turn symptoms into Gaps and tested cause Hypotheses | 2 | — | capability-diagnosis, diagnostic-record, decision-assumption-log |
| 04 | `04-design-interventions` | design intervention candidates across all families; AI only where justified | 3 | — | intervention-map, ai-suitability-assessment, autonomy-assessment |
| 05 | `05-prioritize-initiatives` | select, defer, reject, or investigate candidates; create Initiatives | 4 | HG-INITIATIVE, HG-BUDGET | prioritization-matrix, transformation-roadmap, intervention-map (status), decision-assumption-log |
| 06 | `06-design-target-system` | design Capability Target States and, from Standard, the Target Operating Architecture | 5 | HG-TOA, HG-DECISION-RIGHTS | capability-target-state, capability-network, system-constraint, system-effect-assessment, target-operating-architecture, decision-rights-map, decision-assumption-log |
| 07 | `07-build-roadmap` | sequence Initiatives through operable states, slices, gates, and pilots | 6 | HG-BUDGET | transformation-roadmap, transition-state, transformation-portfolio, pilot-plan, evaluation-plan, execution-gate (incl. C), decision-assumption-log |
| 08 | `08-design-operating-model` | make the system operable and governed; evaluate pilots; roll out | 7 | HG-DECISION-RIGHTS, HG-AUTHORITY, HG-RISK, HG-PROMOTION | operating-model, observability-plan, adoption-plan, ai-governance-canvas, rollout-plan, evaluation-plan (results), execution-gate (D, E, F), autonomy-assessment, decision-assumption-log |
| 09 | `09-measure-evolution` | measure effect and value; evolve design and authority from evidence | 8 | HG-VALUE, HG-AUTHORITY | transformation-scorecard, value-realization-report, evaluation-plan (results), execution-gate (G), autonomy-assessment, decision-assumption-log |
| 10 | `10-audit-aitm-engagement` | audit an engagement's conformance | any | — | findings (skill 38 writes the conformance declaration) |
| 11 | `11-discover-capabilities` | discover Capabilities for approved Outcomes and record their CURRENT States | 1 | — | capability-map, evidence-register |
| 12 | `12-separate-symptoms-gaps-causes` | separate observations, symptoms, Gaps, and competing cause Hypotheses | 2 | — | capability-diagnosis, diagnostic-record, decision-assumption-log, evidence-register |
| 13 | `13-assess-ai-suitability` | assess and classify AI fit of an `AI_*` candidate against non-AI alternatives | 3 | — | ai-suitability-assessment |
| 14 | `14-assess-autonomy` | recommend autonomy levels and propose the Authority Ceiling per action class | 3 | HG-AUTHORITY | autonomy-assessment |
| 15 | `15-design-target-state` | design one Capability Target State | 5 | — | capability-target-state |
| 16 | `16-validate-root-cause` | test cause Hypotheses against evidence and set their status | 2 | — | diagnostic-record, decision-assumption-log, evidence-register |
| 17 | `17-map-capability-network` | map the Outcome-relevant dependencies between Capabilities | 5 | — | capability-network |
| 18 | `18-identify-system-constraint` | identify the System Constraint and its likely migration | 5 | — | system-constraint |
| 19 | `19-assess-system-effects` | answer the system-effect questions for a selected Initiative | 5 | — | system-effect-assessment |
| 20 | `20-design-target-operating-architecture` | integrate Capability Target States into one Target Operating Architecture | 5 | HG-TOA | target-operating-architecture |
| 21 | `21-design-transition-states` | design independently operable Transition States | 6 | — | transition-state |
| 22 | `22-build-transformation-portfolio` | build the portfolio and bound transformation WIP | 6 | HG-INITIATIVE, HG-BUDGET | transformation-portfolio |
| 23 | `23-design-decision-rights` | design current and target authority for material decisions | 5 | HG-DECISION-RIGHTS | decision-rights-map |
| 24 | `24-audit-local-optimization` | audit an Initiative or TOA for local optimization | 5 | — | system-effect-assessment |
| 25 | `25-design-pilot` | design a bounded pilot with pre-defined success and stop criteria | 6 | HG-RISK, HG-AUTHORITY | pilot-plan, execution-gate (C) |
| 26 | `26-design-evaluation` | pre-register evaluations; add new ones when needed (results: 32, 09) | 6-8 | — | evaluation-plan (plan) |
| 27 | `27-build-eval-dataset` | build the evaluation dataset for an AI component | 6 | — | evaluation-plan (datasets) |
| 28 | `28-design-observability` | make AI and automated work observable | 7 | — | observability-plan |
| 29 | `29-plan-rollout` | plan a staged rollout after an approved promotion | 7 | HG-AUTHORITY, HG-RISK | rollout-plan |
| 30 | `30-design-adoption` | plan adoption, role transitions, training, and support | 7 | — | adoption-plan |
| 31 | `31-operationalize-governance` | make AI governance executable | 7 | HG-RISK, HG-AUTHORITY | ai-governance-canvas |
| 32 | `32-evaluate-pilot` | evaluate a pilot against its pre-registered criteria | 7 | HG-PROMOTION | evaluation-plan (results), execution-gate (D) |
| 33 | `33-assess-value-realization` | assess value state and value conclusion | 8 | HG-VALUE | value-realization-report, execution-gate (G) |
| 34 | `34-manage-authority-promotion` | promote, retain, or demote AI authority from evidence | 7-8 | HG-AUTHORITY | autonomy-assessment, ai-governance-canvas (changes) |
| 35 | `35-audit-operational-readiness` | verify rollout gates before each rollout stage | 7 | — | execution-gate (E) |
| 36 | `36-select-application-profile` | select the Application Profiles and record the Decision | 0 | — | decision-assumption-log |
| 37 | `37-build-context-bundle` | build the bounded context for a skill | any | — | none (loaded files in the handoff) |
| 38 | `38-audit-conformance` | audit conformance; write the conformance declaration | any | — | transformation-intent (`conformance`) |
| 39 | `39-audit-framework-integrity` | check the AITM-SMB repository's integrity before a release | maintenance | — | none (findings) |
| 40 | `40-handle-incident` | record and triage incidents; demote authority when a trigger fires | 7-8 | HG-AUTHORITY | incident-record |

"Human gates" lists the gates a skill's output requires (`human_gate: true`); the closing Decisions go to the decision-assumption-log once the named human gives them. Every skill still stops at any other gate whose trigger occurs. Each skill's frontmatter and `## Produces` are authoritative; report any drift from this table (skill 39).

---

## 3. Invocation

```text
entry        01, then 02 … 09 in phase order; iterate per EXECUTION_MODEL.md §3
before       36 (profiles) and 37 (context bundle) run before any orchestrator step
             that needs them (AGENT_CONTEXT_POLICY.md); re-run 36 when profiles change
             (PROFILE_SELECTION.md §6)
any time     10 audits an engagement at any phase
on incident  40 whenever an incident occurs in operation (operations/INCIDENT_MODEL.md)
maintenance  39 checks the AITM-SMB repository before a release (MAINTENANCE.md);
             it is not an engagement skill
```

Orchestrators and the specialists they invoke (conditions in each orchestrator):

```text
01 discover transformation   Phase 0   36, 37
02 map current system        Phase 1   11
03 diagnose capabilities     Phase 2   12, 16
04 design interventions      Phase 3   13, 14 (AI_* candidates)
05 prioritize initiatives    Phase 4   none (modules: its Normative sources)
06 design target system      Phase 5   15, 17, 18, 19, 24, 23, 20 (24 again after 20)
07 build roadmap             Phase 6   21, 22, 25, 26, 27
08 design operating model    Phase 7   28, 30, 31, 32, 29, 35, 34
09 measure evolution         Phase 8   26, 33, 34
10 audit engagement          any       38
```

A specialist MAY also run on its own for a bounded task. It then verifies its own inputs and stops at its own gates.

A first Compact engagement, step by step: `QUICKSTART.md`.

---

## 4. Conventions

Paths: every path in a skill is relative to the AITM root, the directory containing `MANIFEST.md` (`AGENT_CONTEXT_POLICY.md`). Skills are not self-contained: they need the whole AITM root. Install it as one skill through the root `SKILL.md`; do not copy single skills out.

Context: every skill assumes the Core bundle and the active profiles are loaded (`AGENT_CONTEXT_POLICY.md`).

Produces: names each artifact contract (`artifacts/<name>.md`) the skill writes to, and the records it creates or updates; the contracts named are exactly those whose `produced_by` lists the skill (`artifacts/_ARTIFACT_CONTRACT.md` §2). Engagement instances go to the engagement workspace (`artifacts/_ARTIFACT_CONTRACT.md` §6), never into the AITM root. Any skill MAY also append Evidence, Evidence Debt, and Uncertainties to the Evidence Register; Decisions (including gate approvals), Assumptions, and Risks to the Decision & Assumption Log; and Metric records to the Transformation Scorecard `metrics` list. Such appends are not listed in `## Produces`.

Frontmatter (shape: `skills/_SKILL_TEMPLATE.md`):

```text
name                        equals the directory name
description                 one line: what it does, when to use it, what it produces
version                     skill version
minimum_framework_version   oldest AITM-SMB version the skill works with
framework                   AITM-SMB
status                      draft | active | deprecated
category                    §1
phase                       orchestrators: their phase; specialists: the phase(s) they serve
human_gate                  true | false
gates                       only when human_gate is true: the STANDARD.md §8 gate IDs
```

`human_gate: true` means the skill's output requires a `STANDARD.md` §8 approval before downstream use; `gates` names those gates. The skill then stops with `HUMAN_DECISION_REQUIRED` until a Decision closing each gate is recorded. `human_gate: false` does not exempt a skill from any gate whose trigger occurs.

Handoff: every skill emits the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.

---

## 5. Stability

Skill numbers (01–40 in 1.1.0) are the stable identifiers for the 1.x line. Directory slugs and titles are not; 1.1.0 renamed `04-map-ai-opportunities` to `04-design-interventions` and `06-design-target-architecture` to `06-design-target-system`.

New 1.x skills use new numbers (1.1.0 added 40); a number is never repurposed. Extension skills: `EXTENSION_MODEL.md`.
