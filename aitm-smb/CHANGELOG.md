# Changelog

All notable changes to AITM-SMB. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [`VERSIONING.md`](VERSIONING.md). Each release's full notes and migration guide live in [`releases/`](releases/).

## [Unreleased]

## [1.1.0] — 2026-09-28

**Consolidation & open-source release.** The first public release of AITM-SMB. It is a MINOR release: no object in the Public Methodology API changes meaning, and no stable identifier is repurposed ([`PUBLIC_API.md`](PUBLIC_API.md) §9). An independent review of the internal 1.0.0 found definitions restated in several files, self-audit claims the shipped tree did not support, and execution steps no phase ran. This release gives every rule and record shape one owner, wires the full lifecycle into the skills, and adds what a public project needs. Full notes and the 1.0 → 1.1 migration table: [`releases/1.1.0.md`](releases/1.1.0.md).

### Added
- **Human decision gate identifiers.** [`STANDARD.md`](STANDARD.md) §8 is now a table of nine gates, `HG-OUTCOME` … `HG-VALUE`. An approval is a Decision (`DEC-###`) with `gate`, `subject_ids`, and `approved_by`. Reducing AI authority never needs a gate ([ADR-0003](decisions/ADR-0003-human-gate-identifiers.md)).
- **Materiality** is defined once ([`STANDARD.md`](STANDARD.md) §16). When it is unclear, the item is material, and agents MUST NOT classify an item as immaterial to avoid a gate.
- **Agent status definitions** with a precedence order ([`PUBLIC_API.md`](PUBLIC_API.md) §8). The `aitm_output` handoff block is a MUST at every skill handoff and gains `status_reason`, `findings`, `open_gates`, and `trace.other_ids` ([`AGENT_OUTPUT_STANDARD.md`](AGENT_OUTPUT_STANDARD.md)).
- **Authority definitions for L0–L5** ([`diagnostics/AUTONOMY_SUITABILITY.md`](diagnostics/AUTONOMY_SUITABILITY.md) §2), assessed per action class. The ladder is an *authority* ladder, not a maturity or architecture ladder.
- **Record contracts:** every record shape is defined once and named in [`CANONICAL_CONCEPTS.md`](CANONICAL_CONCEPTS.md) ([ADR-0004](decisions/ADR-0004-single-record-contracts.md)). New in this release: a State record (`CORE_MODEL.md` §3) for CURRENT, TRANSITION, and TARGET states; a Risk record (`RSK-###`); and [`artifacts/evidence-register.md`](artifacts/evidence-register.md) for Evidence, Evidence Debt, and Uncertainty.
- **Identifiers:** [`ontology/ONTOLOGY.md`](ontology/ONTOLOGY.md) is the complete registry. New: `ATI` Transformation Intent, `ROL` Rollout Plan, `VRL` Value Realization. Prefixes outside the stable list in PUBLIC_API §3 are reserved.
- **Skill 40 `handle-incident`.** It records and triages incidents, demotes authority immediately when a trigger fires, and stops at `HG-AUTHORITY` before authority is restored.
- **Skills as agent skills:** every skill has `description`, `phase`, `human_gate`, and `gates` frontmatter, and the same body sections. A root [`SKILL.md`](SKILL.md) makes the whole folder installable as one Claude Code / Agent Skills skill named `aitm-smb`. [`skills/INDEX.md`](skills/INDEX.md) is a router with invocation rules.
- **Economics before budget:** each material candidate carries an economic hypothesis ([`economics/TRANSFORMATION_ECONOMICS.md`](economics/TRANSFORMATION_ECONOMICS.md) §5) before `HG-BUDGET`.
- **Public-project files:** MIT [`LICENSE`](LICENSE), [`QUICKSTART.md`](QUICKSTART.md), a fictional worked Compact engagement ([`examples/compact-scenario-b/`](examples/compact-scenario-b/README.md)), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), [`SECURITY.md`](SECURITY.md), [`CITATION.cff`](CITATION.cff), ADRs 0003–0005 with an index and a template, issue and PR templates, and an informative [crosswalk to the Agentic Product Standard](docs/crosswalk-agentic-product-standard.md).
- **Tooling:** [`tools/validate.py`](tools/validate.py) checks framework integrity. With `--engagement DIR` it checks an engagement's trace: IDs defined once, the minimum valid path, core links, and gate Decisions behind approved records. [`tools/build_dist.py`](tools/build_dist.py) builds the Core and Full distributions. CI runs both and publishes releases on `aitm-smb-vX.Y.Z` tags. Both are Python standard library only.

### Changed
- **Lifecycle wiring.** Pilots are designed in Phase 6 and run, evaluated, promoted (`HG-PROMOTION`), and rolled out in Phase 7. Value is assessed in Phase 8. Orchestrators now invoke skills 25–35, which no orchestrator called in 1.0.0. [`EXECUTION_MODEL.md`](EXECUTION_MODEL.md) maps the 12 METHOD_FLOW steps to the 9 phases. Every phase file uses one heading set, with exit conditions that agree with EXECUTION_MODEL §2.
- **One source per rule:** the canonical chain ([`STANDARD.md`](STANDARD.md) §2), the minimum valid path ([`EXECUTION_MODEL.md`](EXECUTION_MODEL.md) §6), the gate list, the autonomy labels, the value states ([`measurement/VALUE_REALIZATION.md`](measurement/VALUE_REALIZATION.md) §2), and the intervention families ([`design/INTERVENTION_PATTERNS.md`](design/INTERVENTION_PATTERNS.md) now defines all 18 PUBLIC_API §6 families) are each stated once. Everything else points to them.
- **Normative precedence** ranks every Canonical Core file. An approved human decision may waive SHOULD and profile requirements; waiving a MUST makes the application non-conforming for that requirement ([`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md)).
- **Profiles.** [`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) is canonical, and [`MINIMUM_ARTIFACT_SET.md`](MINIMUM_ARTIFACT_SET.md) maps it to artifact contracts. Compact defines its governance minimum and a system-effect check (INV-09). Standard adds the pilot, evaluation, rollout, and value-realization artifacts it relies on. Governed covers material legal exposure, high AI authority, and irreversible actions. Profile selection is recorded as a Decision.
- **Conformance** tests INV-09 and INV-07 explicitly. The declaration key is `conformance` and is kept in the Transformation Intent.
- **Human gate flags** on skills now match STANDARD §8: 01, 05–09, 14, 20, 22, 23, 25, 29, 31–34, and 40 are gated.
- **Execution gates:** Gate D requires the pre-registered success criteria or a recorded waiver. Gate E points to the rollout gates in [`execution/ROLLOUT_MODEL.md`](execution/ROLLOUT_MODEL.md) §3.
- **Informative modules:** maturity levels are renamed `M0`–`M5` and are not targets. Evaluation layers use names instead of `L1`–`L8`. The reference architecture names no vendor.
- **Field names** are aligned to the record contracts, for example `current_state_ref` → `current_state_id`, the `aitm_output.trace` keys → `*_ids`, and `aitm_conformance` → `conformance`. See the migration table in [`releases/1.1.0.md`](releases/1.1.0.md).
- **Paths** that carried the deprecated AI-first framing were renamed. Skill numbers, not slugs, are the stable identifiers:

  | 1.0.0 | 1.1.0 |
  |---|---|
  | `skills/04-map-ai-opportunities/` | `skills/04-design-interventions/` |
  | `skills/06-design-target-architecture/` | `skills/06-design-target-system/` |
  | `methodology/03-ai-opportunities.md` | `methodology/03-intervention-design.md` |
  | `methodology/05-target-architecture.md` | `methodology/05-target-system-design.md` |
  | `evals/` | `rubrics/` (informative quality rubrics; distinct from `evaluation/`) |
  | `RELEASE_NOTES_1.0.md`, `RC_CHECKLIST.md`, `RELEASE_CANDIDATE.md` | `releases/1.0.0.md`, `releases/1.0.0-release-checklist.md`, `releases/0.7.0-release-candidate.md` |

### Deprecated
- `artifacts/target-architecture.md` and `artifacts/ai-opportunity-map.md` remain redirect stubs, now with `removal_target: 2.0.0`.

### Removed
- `governance/GOVERNANCE.md`, an unreferenced duplicate of the AI Governance Canvas. Its unique content (stop conditions, cost limit, outcome link) was merged into [`artifacts/ai-governance-canvas.md`](artifacts/ai-governance-canvas.md).
- The value state `BASELINED`. A measured baseline is now the condition for leaving `HYPOTHESIZED`.

### Fixed
- The 1.0.0 README and release docs pointed to Core and Full distributions that did not exist. They are now defined in [`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md) and built by `tools/build_dist.py`.
- The 1.0.0 audits claimed an automated integrity audit, but no tooling shipped. They are kept as historical records with a provenance note; the reproducible checks are `tools/validate.py` and skill 39 ([`audits/1.1_RELEASE_AUDIT.md`](audits/1.1_RELEASE_AUDIT.md)).
- Terminology leaks of the deprecated "AI opportunity" framing were removed from active files. `skills/INDEX.md` described five classes as "four".

## [1.0.0] — Stable Methodology

- froze the first stable AITM-SMB Public Methodology API;
- rewrote Canonical Core into a compact normative specification;
- froze 15 core invariants;
- finalized Outcome → Capability → Gap → Intervention → Initiative → Metric → Evidence trace;
- finalized Capability Target State vs Target Operating Architecture separation;
- normalized all 39 active skills to framework 1.0.0;
- normalized canonical artifact metadata to framework 1.0.0;
- removed deprecated terminology from active methodology surfaces;
- retained deprecated artifacts only as compatibility redirects;
- added Public API compatibility promise for the 1.x line;
- added final release audit;
- generated separate Core and Full distributions (internal pre-publication packaging; published distributions start with 1.1.0, built by `tools/build_dist.py`).

## [0.7.0] — Pre-1.0 Consolidation

- separated Capability Target State from Target Operating Architecture;
- deprecated ambiguous `target-architecture` artifact;
- replaced AI-centric opportunity artifact with general Intervention Map;
- converted phase skills 01–10 into orchestrators over specialist skills;
- added canonical Skill Registry and Artifact Registry;
- added Canonical Concept Registry with one authoritative source per concept;
- rewrote Glossary as informative references rather than duplicate definitions;
- reduced MANIFEST to a true Canonical Core;
- normalized active skill framework compatibility to 0.7.0;
- added 1.0 Release Candidate contract and checklist;
- added automated pre-1.0 integrity audit.

## [0.6.0] — Methodology Hardening

- defined canonical normative precedence;
- defined compact Canonical Core;
- added one-page Canonical Method Flow;
- added proportional Application Profiles;
- added Minimum Artifact Set and artifact-merging rules;
- added Module Catalog;
- added semantic versioning policy;
- added Extension Model for domain/regulatory/technology specializations;
- added canonical Glossary;
- added profile-selection method;
- added AI Agent Context Policy;
- added standard machine-readable Agent Output contract;
- added repository maintenance and documentation-drift rules;
- strengthened Conformance for profiles and artifact proportionality;
- added four methodology-hardening agent skills;
- established anti-bureaucracy rule: activate only modules that improve a decision, control a risk, or produce needed evidence.

## [0.5.0] — Execution & Governance

- added execution principles and vertical transformation slices;
- added Experiment, Pilot, Rollout, and Execution Gate models;
- added layered business/AI evaluation system;
- added AI evaluation and evaluation-dataset standards;
- added business-system observability;
- added AI-enabled incident model;
- added governance operating model and AI change control;
- added authority promotion/demotion model;
- added change adoption and role transition models;
- added value realization and benefit evidence chain;
- added eight execution/governance artifacts;
- added eleven execution agent skills;
- upgraded Phases 6–8 for pilot, rollout, governance, evaluation, and value realization;
- added execution-readiness and pilot-quality rubrics.

## [0.4.0] — Transformation Design

- added system transformation model;
- added capability-network semantics and dependency types;
- added system-constraint analysis and Constraint Migration;
- added Target Operating Architecture;
- added local-optimization guard;
- added Decision Rights Architecture;
- added Information & Knowledge Architecture;
- added Application Boundary Design;
- added Transition State Model;
- added transformation sequencing;
- added Transformation Portfolio and portfolio prioritization;
- added six system-level artifacts;
- added eight transformation-design agent skills;
- upgraded Phase 5 and Phase 6 methodology contracts;
- added system-design evaluation rubric.

## [0.3.0] — Diagnostic intelligence

- added formal diagnostic chain from Observation to Intervention;
- added 12 diagnostic dimensions;
- added capability discovery method;
- added root-cause reasoning and competing-hypothesis discipline;
- added AI suitability classification A–E;
- added separate agentic autonomy assessment L0–L5;
- added target-state design method;
- added intervention pattern library;
- added evidence and uncertainty standards;
- added transformation economics model;
- added agent diagnostic protocol;
- added six specialist diagnostic skills;
- added diagnostic, AI suitability, and autonomy artifacts;
- upgraded Phase 2 and Phase 3 methodology contracts.

## [0.2.0] — Core mechanics

- defined canonical transformation chain;
- defined primary entities: Outcome, Capability, State, Gap, Intervention, Initiative, Metric, Evidence;
- added stable identifiers and traceability rules;
- added execution model with phase entry/exit criteria and re-entry loops;
- added explicit intervention decision model and autonomy ladder;
- added conformance profiles;
- added metrics hierarchy;
- upgraded core artifact contracts from placeholders to semantic contracts;
- upgraded all agent skills to concrete bounded procedures;
- added conformance checklist.

## [0.1.1] — Methodology boundary correction

- removed project/example-oriented structure from the core;
- added explicit domain-neutral scope;
- added abstract validation scenarios;
- clarified that real projects are external implementations, not normative examples.

## [0.1.0] — Skeleton

- established framework purpose and invariants;
- defined core ontology;
- defined 9-phase lifecycle;
- created artifact contracts;
- created agent operating protocol;
- created skill structure;
- added logical reference architecture;
- added maturity and governance skeletons;
- added evaluation and anti-pattern baseline.

[Unreleased]: https://github.com/Moai-Team-LLC/agentic-product-standard/compare/aitm-smb-v1.1.0...HEAD
[1.1.0]: https://github.com/Moai-Team-LLC/agentic-product-standard/releases/tag/aitm-smb-v1.1.0
