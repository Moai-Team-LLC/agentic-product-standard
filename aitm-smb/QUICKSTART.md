# Quickstart: your first Compact engagement

A step-by-step path through one Compact engagement, for a human facilitator (owner, operator, or consultant) and for an AI agent. The path is the same for both. An agent runs it through [`SKILL.md`](SKILL.md) and stops at every human gate until the named human decides.

This guide is informative ([`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md), tier 13). It points to the rules and does not restate them; on any conflict, the linked files govern.

## Before you start

### Prerequisites

- **An accountable Outcome owner** who decides personally about the result and can approve the human decision gates (IDs `HG-*`, [`STANDARD.md`](STANDARD.md) §8).
- **Time:** typically 4–8 weeks of part-time work to reach an approved roadmap for one or two Capabilities. Running a pilot and measuring its effect take as long as the evidence period needs.
- **Access** to the people who do the work, and to system data (exports, logs, tickets, reports) that can serve as Evidence.
- **A workspace** outside this folder (below).

### Is Compact the right profile?

Compact fits only when every "Use when" condition in [`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) §3 holds. If one fails, the base is Standard; where you do not know yet, the default is Standard + Measured, and a Governed condition you cannot answer counts as holding unless the Outcome owner records otherwise ([`PROFILE_SELECTION.md`](PROFILE_SELECTION.md) §4). A profile can change later; see [Escalating](#escalating-to-standard-or-governed).

### Lay out the engagement workspace

Instances go into a workspace outside the AITM-SMB folder, never into [`artifacts/`](artifacts/), which holds contracts only ([`artifacts/_ARTIFACT_CONTRACT.md`](artifacts/_ARTIFACT_CONTRACT.md) §6). A common layout is one file per contract, named by artifact type. Merged files are allowed as long as every record keeps its ID and its record type stays identifiable ([`CONFORMANCE.md`](CONFORMANCE.md) §4, [`MINIMUM_ARTIFACT_SET.md`](MINIMUM_ARTIFACT_SET.md) §3). Instance metadata: [`artifacts/_ARTIFACT_CONTRACT.md`](artifacts/_ARTIFACT_CONTRACT.md) §4.

```text
engagement/                        outside the AITM-SMB folder
  transformation-intent.md         Transformation Intent, Outcomes (OUT), conformance declaration
  decision-assumption-log.md       Decisions (DEC), Assumptions (ASM), Hypotheses (HYP), Risks (RSK)
  evidence-register.md             Evidence (EVD), Evidence Debt
  capability-map.md                Capabilities (CAP) and their CURRENT States (STA)
  capability-diagnosis.md          Gaps (GAP), with observations and symptoms on the Gap, unless
                                   you keep a separate diagnostic-record.md (DIA; optional in Compact)
  intervention-map.md              Interventions (INT)
  transformation-roadmap.md        Initiatives (INI) with economic_hypothesis and operation (incl. adoption);
                                   slices (SLC) and experiments (EXP) unless a pilot plan holds them
  capability-target-state.md       TARGET States (STA)
  system-effect-assessment.md      system-effect check per Initiative proposed for selection (SFX)
  transformation-scorecard.md      Metrics (MET), observations, effect conclusion
  ai-suitability-assessment.md     only for AI_* candidates (AIS)
  autonomy-assessment.md           only for AI_* candidates proposed for selection: Authority Ceiling (AUT)
  ai-governance-canvas.md          only when an AI_* Intervention is selected
  pilot-plan.md, evaluation-plan.md    only if you pilot (PLT, EVL)
```

The Compact content and its contracts: [`MINIMUM_ARTIFACT_SET.md`](MINIMUM_ARTIFACT_SET.md) §2.1.

## The path, phase by phase

Each phase lists what to do, the skills to run, the contracts its records follow, the human gate to stop at, and when it is done. Run the orchestrator of the phase; it invokes its specialists. "Done when" summarizes the phase row of [`EXECUTION_MODEL.md`](EXECUTION_MODEL.md) §2, which governs; the phase files in [`methodology/`](methodology/) refine it. Any gate applies whenever its trigger occurs, not only where listed.

### Phase 0 — Frame

- **Do:** with the owner, name the business problem and why it matters now. Write Outcomes with owner, baseline (or the known baseline gap), target, and horizon. Record a Metric for each Outcome; an unmeasured baseline is `MISSING:<reason>` with an Evidence Debt item. List constraints and non-goals. Select the profile and record it as a Decision. Optionally record materiality thresholds ([`STANDARD.md`](STANDARD.md) §16).
- **Skills:** 36 [`skills/36-select-application-profile/SKILL.md`](skills/36-select-application-profile/SKILL.md) → 37 [`skills/37-build-context-bundle/SKILL.md`](skills/37-build-context-bundle/SKILL.md) → 01 [`skills/01-discover-transformation/SKILL.md`](skills/01-discover-transformation/SKILL.md).
- **Contracts:** [`artifacts/transformation-intent.md`](artifacts/transformation-intent.md), [`artifacts/decision-assumption-log.md`](artifacts/decision-assumption-log.md), [`artifacts/evidence-register.md`](artifacts/evidence-register.md), [`artifacts/transformation-scorecard.md`](artifacts/transformation-scorecard.md) (baseline Metrics).
- **Stop at:** `HG-OUTCOME`. It approves the Outcomes and confirms the profile Decision.
- **Done when:** each Outcome has an owner, a baseline or known baseline gap, a target, and a horizon; constraints are recorded; a Decision closing `HG-OUTCOME` lists the approved Outcome IDs and the profile Decision.

### Phase 1 — Observe

- **Do:** interview the people who do the work and pull system data. Discover the Capabilities that serve the approved Outcomes ([`diagnostics/CAPABILITY_DISCOVERY.md`](diagnostics/CAPABILITY_DISCOVERY.md), including its granularity test). Describe each relevant Capability's CURRENT State on the [`STANDARD.md`](STANDARD.md) §4 dimensions that matter. Record Evidence, assumptions, and workarounds. At the exit, re-check the profile ([`PROFILE_SELECTION.md`](PROFILE_SELECTION.md) §6).
- **Skills:** 02 [`skills/02-map-current-system/SKILL.md`](skills/02-map-current-system/SKILL.md) → 11 [`skills/11-discover-capabilities/SKILL.md`](skills/11-discover-capabilities/SKILL.md).
- **Contracts:** [`artifacts/capability-map.md`](artifacts/capability-map.md), [`artifacts/evidence-register.md`](artifacts/evidence-register.md). No Business System Map in Compact.
- **Stop at:** no typical gate.
- **Done when:** each relevant Capability has a CURRENT State backed by Evidence or by Assumptions (ASM) that a named business owner stated or accepted. Agent inference alone is a `[HYPOTHESIS]` and does not count ([`AGENTS.md`](AGENTS.md) §3).

### Phase 2 — Diagnose

- **Do:** separate observations, symptoms, Gaps, and competing cause Hypotheses. Look for evidence for and against each Hypothesis, then set each Gap's cause status. Accepting a cause as testable before it is validated takes a Decision by the Capability or Outcome owner; an agent only proposes it. Never jump from a symptom to a solution.
- **Skills:** 03 [`skills/03-diagnose-capabilities/SKILL.md`](skills/03-diagnose-capabilities/SKILL.md) → 12 [`skills/12-separate-symptoms-gaps-causes/SKILL.md`](skills/12-separate-symptoms-gaps-causes/SKILL.md), 16 [`skills/16-validate-root-cause/SKILL.md`](skills/16-validate-root-cause/SKILL.md).
- **Contracts:** [`artifacts/capability-diagnosis.md`](artifacts/capability-diagnosis.md) (Gaps; in Compact also Observations and Symptoms on the Gap, or a separate [`artifacts/diagnostic-record.md`](artifacts/diagnostic-record.md)); Hypotheses in [`artifacts/decision-assumption-log.md`](artifacts/decision-assumption-log.md); [`artifacts/evidence-register.md`](artifacts/evidence-register.md).
- **Stop at:** no typical gate.
- **Done when:** material Gaps have explicit cause Hypotheses. A Gap moves on only when it is intervention-ready ([`diagnostics/DIAGNOSTIC_MODEL.md`](diagnostics/DIAGNOSTIC_MODEL.md) §6); the others carry Evidence Debt.

### Phase 3 — Design Interventions

- **Do:** for each intervention-ready Gap, generate several candidates across the families in [`design/INTERVENTION_PATTERNS.md`](design/INTERVENTION_PATTERNS.md), challenging the simpler ones first ([`DECISION_MODEL.md`](DECISION_MODEL.md) §1). For each `AI_*` candidate, assess AI suitability; for each one you propose for selection, assess autonomy per action class and propose an Authority Ceiling. Record rejected candidates with their rationale.
- **Skills:** 04 [`skills/04-design-interventions/SKILL.md`](skills/04-design-interventions/SKILL.md) → 13 [`skills/13-assess-ai-suitability/SKILL.md`](skills/13-assess-ai-suitability/SKILL.md) for `AI_*` candidates, and 14 [`skills/14-assess-autonomy/SKILL.md`](skills/14-assess-autonomy/SKILL.md) for those proposed for selection.
- **Contracts:** [`artifacts/intervention-map.md`](artifacts/intervention-map.md); for `AI_*` candidates [`artifacts/ai-suitability-assessment.md`](artifacts/ai-suitability-assessment.md), and for those proposed for selection [`artifacts/autonomy-assessment.md`](artifacts/autonomy-assessment.md).
- **Stop at:** `HG-AUTHORITY` for each proposed Authority Ceiling above L0; its Decision lists the `AUT-###` in `subject_ids` and states the level and scope. The phase may exit while this gate is open, but the `AI_*` candidate cannot be selected in phase 4 until its ceiling is approved.
- **Done when:** every intervention-ready Gap has candidate Interventions with a type and simpler alternatives considered; every `AI_*` candidate has a justified AI need, a plausible way to verify its output, and explicit authority assumptions; each one proposed for selection has a proposed Authority Ceiling.

### Phase 4 — Decide

- **Do:** decide per candidate: select, defer, reject, or investigate, each with written rationale; `investigate` keeps the Intervention a candidate and records an Evidence Debt item naming what must be learned. Create an Initiative (`status: proposed`) for each candidate proposed for selection, linked to its Outcomes, Capabilities, Interventions, and success Metrics. Before `HG-INITIATIVE` decides, answer the system-effect questions ([`design/LOCAL_OPTIMIZATION_GUARD.md`](design/LOCAL_OPTIMIZATION_GUARD.md) §2) for each Initiative, so that system effects are weighed, not only local ones (INV-09, a core invariant in [`STANDARD.md`](STANDARD.md) §3); a short record suffices. Before `HG-BUDGET`, record an economic hypothesis on each material Initiative (`economic_hypothesis`, [`economics/TRANSFORMATION_ECONOMICS.md`](economics/TRANSFORMATION_ECONOMICS.md) §5). Compact needs no Prioritization Matrix; the rationale sits in the Intervention Map and the selection Decision.
- **Skills:** 05 [`skills/05-prioritize-initiatives/SKILL.md`](skills/05-prioritize-initiatives/SKILL.md) → 19 [`skills/19-assess-system-effects/SKILL.md`](skills/19-assess-system-effects/SKILL.md) for each Initiative proposed for selection.
- **Contracts:** [`artifacts/transformation-roadmap.md`](artifacts/transformation-roadmap.md) (Initiatives), [`artifacts/system-effect-assessment.md`](artifacts/system-effect-assessment.md), [`artifacts/intervention-map.md`](artifacts/intervention-map.md) (status), [`artifacts/decision-assumption-log.md`](artifacts/decision-assumption-log.md), [`artifacts/transformation-scorecard.md`](artifacts/transformation-scorecard.md) (success Metrics).
- **Stop at:** `HG-INITIATIVE`; `HG-BUDGET` where material budget is committed.
- **Done when:** every selected Initiative traces to Outcomes, Capabilities, Interventions (and through them Gaps) and Metrics, and has its system-effect record; no `AI_*` Intervention is selected before its ceiling is approved; rejected and deferred candidates carry a rationale; the approvals are recorded, and the `HG-BUDGET` Decision cites each material Initiative's economic hypothesis.

### Phase 5 — Design Target System

- **Do:** design one Capability Target State per selected Capability, with any AI authority set per action class inside the approved ceiling. Refine each selected Initiative's system-effect record at system level; if a refined effect changes a priority, the selection returns to `HG-INITIATIVE`. Check that system-level Metrics exist, not only local ones (INV-09). Compact has no Target Operating Architecture; the Capability Target States stand in for it.
- **Skills:** 06 [`skills/06-design-target-system/SKILL.md`](skills/06-design-target-system/SKILL.md) → 15 [`skills/15-design-target-state/SKILL.md`](skills/15-design-target-state/SKILL.md); 19 [`skills/19-assess-system-effects/SKILL.md`](skills/19-assess-system-effects/SKILL.md) refines each system-effect record, and 24 [`skills/24-audit-local-optimization/SKILL.md`](skills/24-audit-local-optimization/SKILL.md) audits it.
- **Contracts:** [`artifacts/capability-target-state.md`](artifacts/capability-target-state.md), [`artifacts/system-effect-assessment.md`](artifacts/system-effect-assessment.md).
- **Stop at:** `HG-TOA`, which in Compact approves the Capability Target States; `HG-DECISION-RIGHTS` if material Decision Rights change.
- **Done when:** the selected Capabilities have approved TARGET States; dependencies, authority, and system effects are explicit; system-level Metrics exist.

### Phase 6 — Design Transition

- **Do:** sequence the Initiatives. Give each one an owner, bounded scope, dependencies, an evidence plan, decision gates, rollback or recovery, and success Metrics. Cut vertical Transformation Slices ([`execution/DELIVERY_SLICE.md`](execution/DELIVERY_SLICE.md)) and record them, like any experiment, in the roadmap unless a pilot plan holds them. Where material uncertainty remains, design an experiment or a small pilot with pre-registered success and stop criteria (INV-11). Compact does not require a pilot, but a pilot you run is still a Pilot record ([`execution/PILOT_MODEL.md`](execution/PILOT_MODEL.md)). Put any planned increase of AI authority behind a `decision_gates` entry `{gate: HG-AUTHORITY, subject_ids: [AUT-###]}`.
- **Skills:** 07 [`skills/07-build-roadmap/SKILL.md`](skills/07-build-roadmap/SKILL.md) → 25 [`skills/25-design-pilot/SKILL.md`](skills/25-design-pilot/SKILL.md) and 26 [`skills/26-design-evaluation/SKILL.md`](skills/26-design-evaluation/SKILL.md) if you pilot; 27 [`skills/27-build-eval-dataset/SKILL.md`](skills/27-build-eval-dataset/SKILL.md) for an AI component.
- **Contracts:** [`artifacts/transformation-roadmap.md`](artifacts/transformation-roadmap.md); if you pilot, [`artifacts/pilot-plan.md`](artifacts/pilot-plan.md) and [`artifacts/evaluation-plan.md`](artifacts/evaluation-plan.md).
- **Stop at:** `HG-BUDGET`. Before a pilot that grants AI authority or accepts material risk runs: `HG-AUTHORITY` or `HG-RISK`.
- **Done when:** every material Initiative is execution-ready as listed above, and any pilot has its evaluation registered before it starts.

### Phase 7 — Operationalize

- **Do:** make ownership, support, role changes, and adoption explicit, and observability active before any AI or automated work runs. Compact requires no Operating Model, Observability Plan, or Adoption Plan: the operating owner, observability signal, support path, role changes, failure or rollback path, and adoption (training, support, feedback, adoption metrics) can sit on the Initiative as `operation:` ([`artifacts/transformation-roadmap.md`](artifacts/transformation-roadmap.md)); the exit condition still holds. Where AI is used, fill the Governance-minimum fields of the AI Governance Canvas ([`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) §3) within the approved ceiling before the AI runs. Before a pilot runs above the currently approved level, grant that level through `HG-AUTHORITY`. Run the pilot, if any, and evaluate it against its pre-registered criteria; unmet criteria never yield a `pilot_result` of `PROMOTE`, and promoting anyway takes an `HG-PROMOTION` Decision that records the waiver. Where you roll out, do it in stages (Compact requires no Rollout Plan). Change AI authority only by approved promotion or by demotion, and handle incidents as they occur.
- **Skills:** 08 [`skills/08-design-operating-model/SKILL.md`](skills/08-design-operating-model/SKILL.md) → 28 [`skills/28-design-observability/SKILL.md`](skills/28-design-observability/SKILL.md) before any AI or automated work runs; 30 [`skills/30-design-adoption/SKILL.md`](skills/30-design-adoption/SKILL.md) for role changes; 31 [`skills/31-operationalize-governance/SKILL.md`](skills/31-operationalize-governance/SKILL.md) where AI is used; 32 [`skills/32-evaluate-pilot/SKILL.md`](skills/32-evaluate-pilot/SKILL.md) after a pilot; 29 [`skills/29-plan-rollout/SKILL.md`](skills/29-plan-rollout/SKILL.md) and 35 [`skills/35-audit-operational-readiness/SKILL.md`](skills/35-audit-operational-readiness/SKILL.md) for a rollout; 34 [`skills/34-manage-authority-promotion/SKILL.md`](skills/34-manage-authority-promotion/SKILL.md) for every authority change, including before a pilot or rollout stage runs above the approved level; 40 [`skills/40-handle-incident/SKILL.md`](skills/40-handle-incident/SKILL.md) for incidents.
- **Contracts:** [`artifacts/transformation-roadmap.md`](artifacts/transformation-roadmap.md) (`operation:`); [`artifacts/ai-governance-canvas.md`](artifacts/ai-governance-canvas.md) where AI is used; results in [`artifacts/evaluation-plan.md`](artifacts/evaluation-plan.md) if you piloted; updates to [`artifacts/autonomy-assessment.md`](artifacts/autonomy-assessment.md).
- **Stop at:** `HG-PROMOTION` before a material pilot goes to rollout; `HG-AUTHORITY`, `HG-RISK`, `HG-DECISION-RIGHTS` when their triggers occur. Demotion needs no gate.
- **Done when:** ownership, observability, the failure path and support, role changes, adoption, and governance controls are explicit and working; where you piloted, the pilot is evaluated and its promotion decided; where you roll out, the rollout gates ([`execution/ROLLOUT_MODEL.md`](execution/ROLLOUT_MODEL.md) §3) are verified before each stage.

### Phase 8 — Measure & Evolve

- **Do:** after the evidence period, read each Metric against its baseline and record the observations and the effect conclusion, negative results included. Update the diagnosis, target, roadmap, and AI authority from what the Evidence shows.
- **Skills:** 09 [`skills/09-measure-evolution/SKILL.md`](skills/09-measure-evolution/SKILL.md) → 34 for authority from evidence; 33 [`skills/33-assess-value-realization/SKILL.md`](skills/33-assess-value-realization/SKILL.md) only when Measured is added (Compact + Measured requires the Value Realization Report).
- **Contracts:** [`artifacts/transformation-scorecard.md`](artifacts/transformation-scorecard.md); with Measured, [`artifacts/value-realization-report.md`](artifacts/value-realization-report.md).
- **Stop at:** `HG-VALUE` before value is declared realized; `HG-AUTHORITY` before authority is increased or restored.
- **Done when:** the effect is evaluated against the baseline; with Measured, the value state is recorded with Evidence; the diagnosis, target, roadmap, and AI authority are updated from Evidence.

### Close: audit and validate

- Run 10 [`skills/10-audit-aitm-engagement/SKILL.md`](skills/10-audit-aitm-engagement/SKILL.md); its specialist 38 [`skills/38-audit-conformance/SKILL.md`](skills/38-audit-conformance/SKILL.md) writes the conformance declaration into the Transformation Intent ([`CONFORMANCE.md`](CONFORMANCE.md) §5).
- Check the trace from the AITM-SMB folder: `python3 tools/validate.py --engagement <path-to-workspace>`.
- A conformance result is not approval of any gated decision.

## Escalating to Standard or Governed

Escalate when a Compact "Use when" condition stops holding: for example a third Capability, Capabilities that depend on each other across several systems, sensitive data, irreversible actions, or high AI authority.

1. Re-run skill 36 and record a new profile Decision that supersedes the old one; confirm it with `HG-OUTCOME` ([`PROFILE_SELECTION.md`](PROFILE_SELECTION.md) §5–§6).
2. Add the content the new profile requires ([`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) §4–§5; contracts in [`MINIMUM_ARTIFACT_SET.md`](MINIMUM_ARTIFACT_SET.md) §2.2–§2.3), starting at the earliest phase it belongs to.
3. Return to an earlier phase where the new content changes a decision ([`EXECUTION_MODEL.md`](EXECUTION_MODEL.md) §3). Existing records keep their IDs.

## Common mistakes

The full catalogue is [`rubrics/ANTI_PATTERNS.md`](rubrics/ANTI_PATTERNS.md). First engagements most often:

- start from a tool or a vendor offer (Tool-first transformation); a means is not an Outcome ([`CORE_MODEL.md`](CORE_MODEL.md) §1);
- accept the first plausible explanation as the validated cause (INV-03);
- skip the non-AI candidates, or treat a strong AI fit as permission to act (INV-05, INV-06; Autonomous-by-default);
- count an artifact marked approved, a proposed gate Decision, or an agent's word as a gate approval; only an approved Decision naming the human counts ([`AGENTS.md`](AGENTS.md) §4);
- write engagement instances into the AITM-SMB folder;
- change success criteria after seeing results, or declare value at deployment (INV-12);
- produce Standard artifacts "just in case" (Framework bureaucracy, INV-15).

## Worked example

[`examples/compact-scenario-b/README.md`](examples/compact-scenario-b/README.md) is a finished, fictional Compact engagement built on Abstract Scenario B ([`validation/ABSTRACT_SCENARIOS.md`](validation/ABSTRACT_SCENARIOS.md)). It shows a workspace layout, the IDs, the gate Decisions, and the handoffs a complete run produces. Check it with `python3 tools/validate.py --engagement examples/compact-scenario-b`.

## For agents

The same path is the "First run" section of [`SKILL.md`](SKILL.md). Install the AITM-SMB folder intact, as one skill through that root `SKILL.md` ([Using it with Claude Code](README.md#using-it-with-claude-code)); single skills copied out of it lose their references. Load context as [`AGENT_CONTEXT_POLICY.md`](AGENT_CONTEXT_POLICY.md) defines, never the whole folder, and write engagement instances only into the workspace outside the folder (its Engagement workspace section). Every skill ends with the `aitm_output` block ([`AGENT_OUTPUT_STANDARD.md`](AGENT_OUTPUT_STANDARD.md)); an open gate is recorded as a proposed Decision and appears in `open_gates` with status `HUMAN_DECISION_REQUIRED`.
