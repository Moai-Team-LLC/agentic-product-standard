---
name: 18-identify-system-constraint
description: "Identifies the current System Constraint, the condition that most limits the business system from improving a target Outcome: lists material bottlenecks, applies the constraint test, separates local bottlenecks from the system constraint, and predicts the likely Constraint Migration and how to monitor it. Use in Phase 5 under the Standard profile or above, invoked by skill 06, or when evidence suggests the constraint has moved. Produces a System Constraint record. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: design-specialist
phase: "5"
human_gate: false
---

# Skill 18: Identify System Constraint

## Purpose

Find the one condition that limits the target Outcome, so that investment goes to the limiting part of the system first. Invoked by [`skills/06-design-target-system/SKILL.md`](../06-design-target-system/SKILL.md).

## Required inputs

- approved Outcomes and their Metrics;
- Capability Network, where it exists;
- diagnostic Evidence (Capability Diagnosis, Diagnostic Records, Evidence Register).

## Normative sources

- [`design/CONSTRAINT_ANALYSIS.md`](../../design/CONSTRAINT_ANALYSIS.md)

## Produces

- [`artifacts/system-constraint.md`](../../artifacts/system-constraint.md) — System Constraint (`CST-###`)

## Procedure

1. List material bottlenecks and limiting conditions for the target Outcome.
2. Apply the constraint test ([`design/CONSTRAINT_ANALYSIS.md`](../../design/CONSTRAINT_ANALYSIS.md) §3) to each; separate local bottlenecks (§4); check the false constraint patterns (§7).
3. Record the System Constraint (`system_constraint` record) with its `type` (§2), the constraint-test result in `why_system_limiting`, `evidence_ids`, and `confidence` ([`artifacts/_ARTIFACT_CONTRACT.md`](../../artifacts/_ARTIFACT_CONTRACT.md) §5); record material uncertainty as `UNC-###` in the Evidence Register.
4. Predict the likely Constraint Migration (§5) in `likely_next_constraint`, with `monitoring_metric_ids`; link the `intervention_ids` that relax it.
5. When the constraint changes a Phase 4 priority (§6), report it in `risks` and `decisions_needed` (`HG-INITIATIVE`).
6. When the constraint has moved, record a new `CST-###` and mark the old one `status: superseded`. Validate against the contract's Validation.
7. Stop with `INSUFFICIENT_EVIDENCE` when the constraint test cannot be run without invented facts (record Evidence Debt); with `HUMAN_DECISION_REQUIRED` when any [`STANDARD.md`](../../STANDARD.md) §8 gate is reached.

## MUST NOT

- label every bottleneck a System Constraint;
- optimize a local metric instead of the target Outcome;
- hide likely Constraint Migration;
- invent business facts, present inference as Evidence, or hide uncertainty;
- widen scope silently, or renumber or reuse stable IDs.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
