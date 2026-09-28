# AITM-SMB Module Catalog

Registry ([`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md)): it enumerates modules and the other top-level directories and defines no semantics. Precedence of everything listed here: [`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md).

## 1. Canonical Core

Always normative, whatever the profile.

File list: [`MANIFEST.md`](MANIFEST.md) `canonical_core` (readable copy: [`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md) §Canonical Core). This catalog does not repeat it.

---

## 2. Always active with the Core

Whatever the profile:

```text
methodology/                       phase files 00–08; refine EXECUTION_MODEL.md and MUST agree with it
canonical concept sources          the Semantics source named in CANONICAL_CONCEPTS.md for every
                                   concept in use (CANONICAL_CONCEPTS.md §3); in every engagement
                                   at least:
  METRICS.md                         Metric
  evidence/EVIDENCE_STANDARD.md      Evidence, Evidence Debt, Assumption
  diagnostics/ROOT_CAUSE_ANALYSIS.md Cause / Hypothesis
  design/INTERVENTION_PATTERNS.md    intervention families
  design/LOCAL_OPTIMIZATION_GUARD.md system-effect check (INV-09)
AGENT_DIAGNOSTIC_PROTOCOL.md       whenever an agent diagnoses
```

A concept source is normative for its definitions; its further procedures follow the module activation in §3.

---

## 3. Modules

A module becomes normative for an engagement when a selected profile requires it or a documented Decision activates it ([`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md) §Modules). A profile activates the owning module of each artifact contract it requires (mapping: [`MINIMUM_ARTIFACT_SET.md`](MINIMUM_ARTIFACT_SET.md); owners: [`artifacts/INDEX.md`](artifacts/INDEX.md)) and the module files named in its [`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) section. The lists below are derived from those files; on conflict they win. Rows labeled Compact apply to every application, since Compact is the floor ([`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) §3).

### 3.1 Diagnostics Module

Use to understand why current capabilities fail.

```text
diagnostics/
evidence/
economics/
```

Agent procedure: [`AGENT_DIAGNOSTIC_PROTOCOL.md`](AGENT_DIAGNOSTIC_PROTOCOL.md), active whenever an agent diagnoses (§2).

Activated by:

```text
Compact    diagnostics/CAPABILITY_DISCOVERY.md, diagnostics/DIAGNOSTIC_MODEL.md,
           diagnostics/DIAGNOSTIC_DIMENSIONS.md (Capability Map, Capability Diagnosis);
           evidence/UNCERTAINTY_MODEL.md where uncertainty is recorded;
           diagnostics/AI_SUITABILITY.md and diagnostics/AUTONOMY_SUITABILITY.md where an
           AI_* candidate is proposed for selection (Governance minimum);
           economics/TRANSFORMATION_ECONOMICS.md §5 for each material candidate before
           HG-BUDGET; in full where cost or economic effect informs a decision
Governed   diagnostics/AUTONOMY_SUITABILITY.md §6 for every Capability in which AI is used
```

Core questions:

```text
What is happening?
Which capability is constrained?
Why?
How confident are we?
```

---

### 3.2 Transformation Design Module

Use to define the future business system.

```text
design/
transition/
portfolio/
```

Activated by:

```text
Compact    design/TARGET_STATE_DESIGN.md (Capability Target State)
Standard   design/ in full (Capability Network, System Constraint, System Effect Assessment,
           Decision Rights, Target Operating Architecture, information and application design);
           transition/ (Transition States, sequencing)
Portfolio  portfolio/; design/CAPABILITY_NETWORK.md and transition/TRANSFORMATION_SEQUENCING.md
           (cross-capability dependency analysis)
```

Core questions:

```text
What should change?
How do capabilities interact?
What is the system constraint?
What should the Target Operating Architecture be?
How do we transition?
```

---

### 3.3 Execution Module

Use to turn design into operational change.

```text
execution/
evaluation/
```

Activated by:

```text
Standard   execution/EXECUTION_PRINCIPLES.md, execution/DELIVERY_SLICE.md;
           where a pilot or experiment is required: execution/EXPERIMENT_MODEL.md,
           execution/PILOT_MODEL.md, evaluation/EVALUATION_SYSTEM.md,
           evaluation/AI_EVALS.md (AI components);
           where rolling out: execution/ROLLOUT_MODEL.md
Governed   execution/EXECUTION_GATE_MODEL.md (GAT records; in every profile its §4 waiver content applies when unmet pilot criteria are waived at HG-PROMOTION);
           evaluation/EVALUATION_DATASET.md (AI components)
```

Core questions:

```text
What should we test?
How do we know it works?
When may we scale?
```

---

### 3.4 Operations & Governance Module

Use for production operation and authority control.

```text
operations/
governance/
```

Activated by:

```text
Compact    where an AI_* Intervention is selected: governance/GOVERNANCE_OPERATING_MODEL.md
           (Governance minimum fields); governance/AUTHORITY_ESCALATION_MODEL.md when AI
           authority is granted, promoted, or demoted
Standard   operations/OBSERVABILITY_MODEL.md; where AI is used:
           governance/GOVERNANCE_OPERATING_MODEL.md (AI Governance Canvas, all fields
           except risk_owner, risk_ids)
Governed   governance/ in full (incl. governance/AI_CHANGE_CONTROL.md);
           operations/INCIDENT_MODEL.md
```

Core questions:

```text
Who owns the system?
What may AI do?
How are incidents handled?
How does authority change?
```

---

### 3.5 Change Module

Use when human roles and workflows materially change.

```text
change/
```

Activated by:

```text
Standard   change/CHANGE_ADOPTION_MODEL.md, change/ROLE_TRANSITION_MODEL.md (Adoption Plan)
```

Core questions:

```text
What behavior must change?
What new skills and responsibilities appear?
Why might adoption fail?
```

---

### 3.6 Measurement Module

Use to prove effect.

```text
measurement/
```

Activated by:

```text
Standard   measurement/VALUE_REALIZATION.md (value state + Evidence)
Measured   measurement/BENEFIT_EVIDENCE_CHAIN.md; measurement/VALUE_REALIZATION.md §4–§5
           (also with Compact + Measured)
```

Core questions:

```text
Did the business improve?
Was the effect caused by the transformation?
Did it persist?
```

---

## 4. Other directories and files

Not modules. Tiers: [`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md).

| Path | Role | Status |
|---|---|---|
| [`artifacts/`](artifacts/) | artifact contracts; registry [`artifacts/INDEX.md`](artifacts/INDEX.md); instances live in the engagement workspace | normative for the records they own (tier 11) |
| [`skills/`](skills/) | agent procedures; registry [`skills/INDEX.md`](skills/INDEX.md) | normative procedures (tier 12) |
| [`PROFILE_SELECTION.md`](PROFILE_SELECTION.md), [`MINIMUM_ARTIFACT_SET.md`](MINIMUM_ARTIFACT_SET.md) | profile selection order; profile-to-contract map | subordinate to [`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) (tier 8) |
| [`rubrics/`](rubrics/) | framework QA rubrics for judging AITM-SMB outputs and this repository; not the engagement [`evaluation/`](evaluation/) module | informative |
| [`maturity/`](maturity/) | descriptive maturity levels M0–M5; not autonomy levels | informative |
| [`reference-architecture/`](reference-architecture/) | logical reference architecture; not a required stack | informative |
| [`validation/`](validation/) | abstract scenarios for testing the method's generality ([`MAINTENANCE.md`](MAINTENANCE.md)) | informative |
| [`docs/`](docs/) | documentation, e.g. [`docs/crosswalk-agentic-product-standard.md`](docs/crosswalk-agentic-product-standard.md); not an extension | informative |
| [`examples/`](examples/) | fictional worked examples, e.g. [`examples/compact-scenario-b/`](examples/compact-scenario-b/) | informative |
| [`README.md`](README.md), [`QUICKSTART.md`](QUICKSTART.md), [`GLOSSARY.md`](GLOSSARY.md), [`SKILL.md`](SKILL.md) | entry points; [`SKILL.md`](SKILL.md) is the Agent Skills adapter | informative |
| [`tools/`](tools/) | [`tools/validate.py`](tools/validate.py) (integrity), [`tools/build_dist.py`](tools/build_dist.py) (distributions) | framework tooling |
| [`releases/`](releases/) | release notes and release checklists | informative; project record |
| [`audits/`](audits/) | historical audit reports | informative; project record |
| [`decisions/`](decisions/) | maintainer ADRs ([`decisions/README.md`](decisions/README.md)) | framework governance |
| [`VERSIONING.md`](VERSIONING.md), [`EXTENSION_MODEL.md`](EXTENSION_MODEL.md), [`MAINTENANCE.md`](MAINTENANCE.md), [`CONTRIBUTING.md`](CONTRIBUTING.md), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), [`SECURITY.md`](SECURITY.md), [`CHANGELOG.md`](CHANGELOG.md), [`REPO_STRUCTURE.md`](REPO_STRUCTURE.md) (generated file tree, checked by [`tools/validate.py`](tools/validate.py)), `LICENSE`, [`CITATION.cff`](CITATION.cff) | framework governance and project files | not engagement rules |
| `.github/` | standalone CI for after a split ([`MAINTENANCE.md`](MAINTENANCE.md) §6) | project file |
