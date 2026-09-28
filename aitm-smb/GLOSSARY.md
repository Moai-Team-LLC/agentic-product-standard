# AITM-SMB Glossary

This glossary is informative.

Canonical semantics are defined in the sources named by [`CANONICAL_CONCEPTS.md`](CANONICAL_CONCEPTS.md); the Canonical source column below matches it.

| Term | Short meaning | Canonical source |
|---|---|---|
| Outcome | Measurable business result that matters independently of AI | [`CORE_MODEL.md`](CORE_MODEL.md) |
| Capability | Stable organizational ability | [`CORE_MODEL.md`](CORE_MODEL.md) |
| State | How a Capability operates at a point in time (CURRENT, TRANSITION, TARGET) | [`CORE_MODEL.md`](CORE_MODEL.md) |
| Current State | How a Capability operates now | [`CORE_MODEL.md`](CORE_MODEL.md) |
| Capability Target State | Required future behavior of one Capability | [`CORE_MODEL.md`](CORE_MODEL.md) |
| Gap | Material difference between current and required behavior | [`CORE_MODEL.md`](CORE_MODEL.md) |
| Cause / Hypothesis | Condition explaining a Gap; a Hypothesis until validated | [`diagnostics/ROOT_CAUSE_ANALYSIS.md`](diagnostics/ROOT_CAUSE_ANALYSIS.md) |
| Intervention | Design choice intended to close a Gap | [`CORE_MODEL.md`](CORE_MODEL.md) |
| Intervention family | Kind of Intervention (`ELIMINATE` … `FEEDBACK`) | [`design/INTERVENTION_PATTERNS.md`](design/INTERVENTION_PATTERNS.md) |
| Initiative | Executable package implementing Interventions | [`CORE_MODEL.md`](CORE_MODEL.md) |
| System Constraint | Main current limiter of a target Outcome | [`design/CONSTRAINT_ANALYSIS.md`](design/CONSTRAINT_ANALYSIS.md) |
| Constraint Migration | Movement of the limiting condition after change | [`design/CONSTRAINT_ANALYSIS.md`](design/CONSTRAINT_ANALYSIS.md) |
| Target Operating Architecture | Integrated future operating system | [`design/TARGET_OPERATING_ARCHITECTURE.md`](design/TARGET_OPERATING_ARCHITECTURE.md) |
| AI Suitability | Whether probabilistic intelligence adds structural value | [`diagnostics/AI_SUITABILITY.md`](diagnostics/AI_SUITABILITY.md) |
| Autonomy | Authority granted to AI to act (levels L0–L5) | [`diagnostics/AUTONOMY_SUITABILITY.md`](diagnostics/AUTONOMY_SUITABILITY.md) |
| Authority Ceiling | Maximum approved AI autonomy | [`diagnostics/AUTONOMY_SUITABILITY.md`](diagnostics/AUTONOMY_SUITABILITY.md) |
| Human Gate | Point where explicit human approval is required (`HG-*`) | [`STANDARD.md`](STANDARD.md) |
| Materiality | Whether being wrong about an item could change an approved Outcome or create exposure the Outcome owner would decide personally | [`STANDARD.md`](STANDARD.md) |
| Risk | Potential failure with impact and likelihood; accepting a material Risk requires `HG-RISK` | [`ontology/ONTOLOGY.md`](ontology/ONTOLOGY.md) |
| Evidence | Source supporting a claim | [`evidence/EVIDENCE_STANDARD.md`](evidence/EVIDENCE_STANDARD.md) |
| Evidence Debt | Known evidence gap affecting a decision | [`evidence/EVIDENCE_STANDARD.md`](evidence/EVIDENCE_STANDARD.md) |
| Evidence Register | Engagement record of Evidence, Evidence Debt, and material Uncertainties | [`artifacts/evidence-register.md`](artifacts/evidence-register.md) |
| Pilot | Bounded operational test of a transformation hypothesis | [`execution/PILOT_MODEL.md`](execution/PILOT_MODEL.md) |
| Rollout | Controlled expansion of validated change | [`execution/ROLLOUT_MODEL.md`](execution/ROLLOUT_MODEL.md) |
| Value Realization | Observed and sustained business value | [`measurement/VALUE_REALIZATION.md`](measurement/VALUE_REALIZATION.md) |
| Engagement workspace | Location outside the AITM-SMB root where an engagement's artifact instances are written | [`artifacts/_ARTIFACT_CONTRACT.md`](artifacts/_ARTIFACT_CONTRACT.md) |
