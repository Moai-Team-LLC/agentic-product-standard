# ADR-0004 — One Record Contract per Record Shape

## Status

Accepted

## Date

2026-09-27

## Context

In 1.0.0 several record shapes were written out in more than one file, with diverging field names. For example, the cause record in `diagnostics/ROOT_CAUSE_ANALYSIS.md` (`hypothesis_id`, `gap_id`, `alternative_causes`, `validation_method`) and the Hypothesis record in the Decision & Assumption Log (`related_gap_ids`, `test`) described the same object differently. Core objects were restated in artifact contracts: `artifacts/capability-map.md` repeated the Capability record of `CORE_MODEL.md` §2 with `current_state_ref` where the core model had `current_state_id`. Instance metadata blocks were repeated in individual contracts.

`CANONICAL_CONCEPTS.md` named where each concept's meaning lived, but not which file owned its field names. Agents could not tell which names to emit, a validator could not check records, and the duplicate-definition audit had to compare copies (`MAINTENANCE.md` §4 calls this dangerous duplication).

## Decision

1. **Each record shape is defined exactly once.** `CANONICAL_CONCEPTS.md` names where, in a new "Record contract" column.
2. **Modules own meaning and rules; the record contract owns field names.** Files that hold instances reference the record contract and MAY add fields only where they say so explicitly ("extends <record> with: …"). The rule is stated in `artifacts/_ARTIFACT_CONTRACT.md`, `MAINTENANCE.md` §3, and `CANONICAL_CONCEPTS.md`.
3. **Where the record contract sits.** The binding table is `CANONICAL_CONCEPTS.md` §1; it follows this reasoning:
   - Six primary objects of `PUBLIC_API.md` §1 (Outcome, Capability, State, Gap, Intervention, Initiative) keep their record in `CORE_MODEL.md`, inside the Canonical Core; artifact contracts hold instances and extend them only explicitly.
   - Decisions, Assumptions, Hypotheses, and Risks keep one record each in `artifacts/decision-assumption-log.md`; the Hypothesis record is the superset of the two 1.0.0 shapes. The Risk record (`RSK-###`) is new in 1.1.0: the Governed profile's explicit risk ownership needs an owner, controls, and a link to the Decision that accepts a material Risk under `HG-RISK`.
   - A record that many skills append to a shared list, or that has no artifact of its own, keeps its record in its module: for example Metric (`METRICS.md` §6), Evidence (`evidence/EVIDENCE_STANDARD.md` §3), Evaluation (`evaluation/EVALUATION_SYSTEM.md` §4), AI Change (`governance/AI_CHANGE_CONTROL.md` §3), Transformation Slice, and Experiment. The artifact that holds the instances points to it.
   - Otherwise the artifact contract that holds the record is its record contract, for example the Autonomy Assessment, the Pilot Plan, and the Incident Record; the module keeps meaning and rules.
4. **Uniform artifact contracts.** Every canonical contract has the same frontmatter and body shape; instance metadata is defined only in `artifacts/_ARTIFACT_CONTRACT.md`; instances live in an engagement workspace outside the AITM root.
5. **Field renames** that align a field with its canonical record are allowed in a MINOR release (`VERSIONING.md` §9). Each one is listed in the migration table of the release notes (`releases/<version>.md`, linked from `CHANGELOG.md`): record, old name, new name. No alias fields are kept; the table is the compatibility path.

## Consequences

- One place to read and change each field name. Agents emit one shape per record, and `tools/validate.py --engagement` reads trace links by these names.
- Artifact contracts became shorter: they point to the record contract and add only explicit extension fields.
- Some 1.0.0 field names changed. Engagements written under 1.0.0 migrate with the `CHANGELOG.md` table; record meanings and stable identifiers are unchanged (`PUBLIC_API.md` §9).
- Contributors change field names only in the record contract named in `CANONICAL_CONCEPTS.md` (`CONTRIBUTING.md`).

## Alternatives

- **Keep parallel copies and audit their parity.** The 1.0.0 approach. Rejected: copies drift between audits, and agents still meet two shapes.
- **Keep 1.x alias fields beside the renamed ones.** Rejected: agents would have to handle both names in every record; a migration table gives the same compatibility at lower cost.
- **Move every record into its module and let artifacts only point.** Rejected: artifact contracts are what producing skills and engagement files are organized around; where an artifact exists, keeping the record there puts the field names where instances are written.
