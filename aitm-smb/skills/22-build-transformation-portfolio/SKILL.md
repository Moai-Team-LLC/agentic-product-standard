---
name: 22-build-transformation-portfolio
description: "Builds the Transformation Portfolio for several Initiatives: categorizes them, maps dependencies, shared enablers and resource contention, applies the portfolio criteria and dominance rule, measures change saturation, sets the WIP limit, and applies the portfolio stop condition before any Initiative is added. Use in Phase 6 when the Portfolio profile is active or several Initiatives compete for the same people, enablers, or constraint. Produces a PTF record per artifacts/transformation-portfolio.md and stops for Initiative and budget approval. Part of AITM-SMB; paths are relative to the AITM-SMB root."
metadata:
  framework: AITM-SMB
  version: "1.1.0"
  minimum_framework_version: "1.1.0"
  status: active
  category: design-specialist
  phase: "6"
  human_gate: "true"
  gates: "HG-INITIATIVE, HG-BUDGET"
---

# Skill 22: Build Transformation Portfolio

## Purpose

Coordinate several Initiatives toward system-level Outcomes and keep transformation WIP within what the organization can absorb. Invoked by [`skills/07-build-roadmap/SKILL.md`](../07-build-roadmap/SKILL.md) when the Portfolio profile is active.

## Required inputs

- selected Initiatives (INI records, [`artifacts/transformation-roadmap.md`](../../artifacts/transformation-roadmap.md)) and their approved selection Decisions;
- Prioritization Matrix with the portfolio-level criteria assessed in Phase 4 ([`artifacts/prioritization-matrix.md`](../../artifacts/prioritization-matrix.md));
- Capability Network and System Constraint ([`artifacts/capability-network.md`](../../artifacts/capability-network.md), [`artifacts/system-constraint.md`](../../artifacts/system-constraint.md));
- Transition States, where they exist.

## Normative sources

- [`portfolio/TRANSFORMATION_PORTFOLIO.md`](../../portfolio/TRANSFORMATION_PORTFOLIO.md)
- [`portfolio/PORTFOLIO_PRIORITIZATION.md`](../../portfolio/PORTFOLIO_PRIORITIZATION.md)
- [`transition/TRANSFORMATION_SEQUENCING.md`](../../transition/TRANSFORMATION_SEQUENCING.md) (§4 dependency types, §5 portfolio sequencing)

## Produces

- [`artifacts/transformation-portfolio.md`](../../artifacts/transformation-portfolio.md) — PTF record, created or updated.

## Procedure

1. Categorize each Initiative ([`portfolio/TRANSFORMATION_PORTFOLIO.md`](../../portfolio/TRANSFORMATION_PORTFOLIO.md) §3) in `initiative_categories`; every enabler links a business Outcome (§4).
2. Map dependencies between Initiatives and on shared enablers ([`transition/TRANSFORMATION_SEQUENCING.md`](../../transition/TRANSFORMATION_SEQUENCING.md) §4), resource contention, and shared risks; record material shared risks as Risk records (RSK-###, [`artifacts/decision-assumption-log.md`](../../artifacts/decision-assumption-log.md)).
3. Apply the portfolio-level criteria and the dominance rule ([`portfolio/PORTFOLIO_PRIORITIZATION.md`](../../portfolio/PORTFOLIO_PRIORITIZATION.md) §2, §3).
4. Record change saturation ([`portfolio/PORTFOLIO_PRIORITIZATION.md`](../../portfolio/PORTFOLIO_PRIORITIZATION.md) §4) in `change_capacity` and set `wip_limit` ([`portfolio/TRANSFORMATION_PORTFOLIO.md`](../../portfolio/TRANSFORMATION_PORTFOLIO.md) §5).
5. Before adding or activating an Initiative, check the portfolio stop condition ([`portfolio/PORTFOLIO_PRIORITIZATION.md`](../../portfolio/PORTFOLIO_PRIORITIZATION.md) §5); while one holds, the Initiative waits unless an approved Decision by the portfolio owner records the override and its reason.
6. Sequence around Outcome leverage, constraint, dependencies, risk, and learning ([`transition/TRANSFORMATION_SEQUENCING.md`](../../transition/TRANSFORMATION_SEQUENCING.md) §5).
7. Validate against the Validation of [`artifacts/transformation-portfolio.md`](../../artifacts/transformation-portfolio.md); review aid: [`rubrics/SYSTEM_DESIGN_RUBRIC.md`](../../rubrics/SYSTEM_DESIGN_RUBRIC.md) (Portfolio).
8. Stop with `INSUFFICIENT_EVIDENCE` when proceeding would require invented business facts (record Evidence Debt), `HUMAN_DECISION_REQUIRED` while a required selection Decision is still proposed (gate in `open_gates`), or `BLOCKED` when a required input is missing.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-INITIATIVE` when the portfolio adds or activates a material Initiative not covered by an approved selection Decision, and at `HG-BUDGET` when it commits material budget; record the gate as a DEC with `gate:` set and `status: proposed` ([`AGENTS.md`](../../AGENTS.md) §4), listing the `INI-###` or `PTF-###` in `subject_ids`; the named human's approval updates it to `approved`.

A stop-condition override is not a [`STANDARD.md`](../../STANDARD.md) §8 gate: it needs an approved Decision whose `approved_by` is the portfolio owner ([`portfolio/PORTFOLIO_PRIORITIZATION.md`](../../portfolio/PORTFOLIO_PRIORITIZATION.md) §5). Propose it in `decisions_needed`; the Initiative waits until it is approved.

## MUST NOT

- add an Initiative while a stop condition holds without an approved override Decision;
- exceed the WIP limit, or schedule an Initiative only because it is easy, visible, uses AI, or is liked;
- record an approval the named human has not explicitly given;
- invent business facts; renumber or reuse stable IDs.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
