# AITM-SMB Application Profiles

**Version:** 1.1.0

Canonical source for profile content (`CANONICAL_CONCEPTS.md` §2). Artifact mapping: `MINIMUM_ARTIFACT_SET.md` (subordinate to this file). Requirement status: claiming a profile requires the content listed for it, unless waived (`CONFORMANCE.md` §3, §6).

## 1. Purpose

AITM-SMB scales by complexity and risk, not by bureaucracy.

Company size alone does not determine methodology depth.

A 20-person business running a regulated, high-impact process may require more governance than a 300-person business with low-risk, reversible work.

A phase produces only the outputs its active profiles require; everything else is optional (INV-15, `EXECUTION_MODEL.md` §2).

---

## 2. Profile selection dimensions

Select a profile using:

```text
business criticality
number of capabilities affected
number of systems affected
AI authority
financial impact
customer impact
data sensitivity
regulatory exposure
irreversibility
organizational change load
```

Procedure: `PROFILE_SELECTION.md` (skill `skills/36-select-application-profile/SKILL.md`). Materiality: `STANDARD.md` §16.

---

## 3. Profile A — Compact

Use when:

```text
one or two capabilities
low or moderate risk
limited system change
low AI authority
high reversibility
small number of affected roles
```

Minimum content:

```text
Transformation Intent (with Outcome records)
Capability Map (with CURRENT States)
Capability Diagnosis (Gaps, Cause Hypotheses)
Intervention Map
Capability Target State
Transformation Roadmap (Initiative records)
system-effect check
Governance minimum
Transformation Scorecard (Metric records)
Evidence Register
Decision & Assumption Log
```

System-effect check: the `design/LOCAL_OPTIMIZATION_GUARD.md` §2 questions answered for each selected Initiative (INV-09). A short System Effect Assessment suffices.

Governance minimum: when any `AI_*` Intervention is selected,

```text
an Autonomy Assessment with an approved Authority Ceiling (HG-AUTHORITY)
AI Governance Canvas fields: owner, permissions, prohibited_actions,
  approval_required, escalation_conditions, recovery_path
```

When no `AI_*` Intervention is selected, the Governance minimum is empty.

Compact is the floor: every application provides this content.

Recommended for many small businesses and bounded transformation initiatives.

---

## 4. Profile B — Standard

Use when:

```text
several interdependent capabilities
multiple systems
material process redesign
moderate AI authority
meaningful organizational change
```

Adds:

```text
Business System Map
Capability Network
System Constraint
System Effect Assessment
Prioritization Matrix
Decision Rights Map
Target Operating Architecture
Transition States
Pilot Plan + Evaluation Plan      (where a pilot is required)
Observability Plan
Operating Model
Adoption Plan
Rollout Plan                      (where rolling out)
Value Realization Report          (value state + Evidence)
```

Standard is the default base profile. Standard + Measured is the recommended default for meaningful SMB transformation (`PROFILE_SELECTION.md` §4).

---

## 5. Profile C — Governed

Use when:

```text
high customer or financial impact
sensitive data
material security exposure
material legal exposure
regulated process
high AI authority
irreversible actions
```

Adds:

```text
complete AI Governance Canvas with a named risk owner
approved Authority Ceiling for every Capability in which AI is used
AI Change Control (CHG records)
incident handling (INC records)
Evaluation Dataset for AI components
Execution Gate records (GAT)
Operational Readiness Audit (recorded on Gate E)
explicit risk ownership (RSK records with named owners;
  HG-RISK Decisions for accepted material Risks)
```

Sources: Authority Ceiling `diagnostics/AUTONOMY_SUITABILITY.md` §6; AI Change Control `governance/AI_CHANGE_CONTROL.md`; incident handling `operations/INCIDENT_MODEL.md` (skill `skills/40-handle-incident/SKILL.md`); Evaluation Dataset `evaluation/EVALUATION_DATASET.md`; Execution Gates `execution/EXECUTION_GATE_MODEL.md`; Operational Readiness Audit `skills/35-audit-operational-readiness/SKILL.md`; Risk `ontology/ONTOLOGY.md` (record: `artifacts/decision-assumption-log.md`).

The AI Governance Canvas, Authority Ceiling, AI Change Control and Evaluation Dataset items apply where AI is used.

Without Governed, Initiative `decision_gates` carry the gates; GAT records MAY be used (`EXECUTION_MODEL.md` §2).

---

## 6. Profile D — Portfolio

Use when transformation spans:

```text
multiple value streams
many capabilities
several transformation initiatives
shared enablers
resource contention
organizational change saturation
```

Adds:

```text
Transformation Portfolio
Portfolio Prioritization
shared-enabler model
change saturation controls (WIP limit)
cross-capability dependency analysis
```

Sources: `portfolio/TRANSFORMATION_PORTFOLIO.md` (enabler initiatives, WIP rule); `portfolio/PORTFOLIO_PRIORITIZATION.md` (criteria, change saturation, stop condition); `design/CAPABILITY_NETWORK.md`, `transition/TRANSFORMATION_SEQUENCING.md` (dependencies).

---

## 7. Profile E — Measured

Use when realized value must be explicitly demonstrated.

Adds, completing the Value Realization Report:

```text
Benefit Evidence Chain
attribution confidence (with competing explanations)
sustained-value review
```

Sources: `measurement/BENEFIT_EVIDENCE_CHAIN.md`; `measurement/VALUE_REALIZATION.md` §4, §5.

With Compact + Measured, the Value Realization Report is required too.

Measured is usually combined with Standard, Governed, or Portfolio.

---

## 8. Profiles are composable

Base profile: Compact or Standard. Add-ons: Governed, Portfolio, Measured; each adds to the base.

Examples:

```text
Standard + Measured
Compact + Governed
Standard + Governed + Measured
Standard + Portfolio + Governed + Measured
```

Default when uncertain: Standard + Measured.

The selected profiles are recorded as a Decision (skill 36, `artifacts/decision-assumption-log.md`) and confirmed with HG-OUTCOME. Until then they are provisional (`AGENT_CONTEXT_POLICY.md`).

An application that declares no profile is evaluated as Compact.

---

## 9. Anti-bureaucracy rule

Do not activate a module merely because it exists.

Every artifact and control SHOULD answer:

```text
What decision does this improve?
What risk does this control?
What evidence does this produce?
```

If none, omit it.

Modules each profile activates: `MODULE_CATALOG.md`.
