---
name: 24-audit-local-optimization
description: "Audits a selected Initiative or a Target Operating Architecture for local optimization (INV-09): upstream, downstream, shared-resource, incentive and Constraint Migration effects, which role absorbs new exceptions, and whether the change improves the target Outcome or only a local metric. Use in Phase 5, or whenever a local improvement may degrade the wider operating system. Updates the existing SFX record per artifacts/system-effect-assessment.md, or creates one where none exists. Part of AITM-SMB; paths are relative to the AITM-SMB root."
metadata:
  framework: AITM-SMB
  version: "1.1.0"
  minimum_framework_version: "1.1.0"
  status: active
  category: design-specialist
  phase: "5"
  human_gate: "false"
---

# Skill 24: Audit Local Optimization Risk

## Purpose

Challenge a design against the system-effect questions so that a local gain does not degrade the wider system. It audits and completes the System Effect Assessment that [`skills/19-assess-system-effects/SKILL.md`](../19-assess-system-effects/SKILL.md) produces. Invoked by [`skills/06-design-target-system/SKILL.md`](../06-design-target-system/SKILL.md).

## Required inputs

- selected Initiative (INI) or Target Operating Architecture (TOA);
- the existing System Effect Assessment for the same Initiative or TOA, if any;
- Capability Network and System Constraint, where the profile requires them.

## Normative sources

- [`design/LOCAL_OPTIMIZATION_GUARD.md`](../../design/LOCAL_OPTIMIZATION_GUARD.md)
- [`design/CONSTRAINT_ANALYSIS.md`](../../design/CONSTRAINT_ANALYSIS.md) (§5 Constraint Migration)

## Produces

- [`artifacts/system-effect-assessment.md`](../../artifacts/system-effect-assessment.md) — the SFX record for the Initiative (`initiative_id`) or TOA (`toa_id`): updated if it exists, created otherwise.

## Procedure

1. Find the SFX for the same `initiative_id` or `toa_id`; update it, never create a second one ([`design/LOCAL_OPTIMIZATION_GUARD.md`](../../design/LOCAL_OPTIMIZATION_GUARD.md) §4).
2. Answer every §2 question: upstream support, downstream demand and capacity, shared-resource contention, incentive and KPI-gaming risk, likely Constraint Migration ([`design/CONSTRAINT_ANALYSIS.md`](../../design/CONSTRAINT_ANALYSIS.md) §5), and the role that absorbs new exceptions (`operational_risks`).
3. Compare the design with the common failures in §3 (throughput increases, exception-load shifts).
4. Set `system_verdict`: does the change improve the target Outcome or only a local metric; add mitigations or sequencing changes for material negative effects.
5. Report a `local_only` or `degrades_outcome` verdict in `risks`; where it changes a Phase 4 priority, the selection returns to `HG-INITIATIVE` (§5).
6. Validate against the Validation of [`artifacts/system-effect-assessment.md`](../../artifacts/system-effect-assessment.md); review aid: [`rubrics/SYSTEM_DESIGN_RUBRIC.md`](../../rubrics/SYSTEM_DESIGN_RUBRIC.md) (Local optimization).
7. Stop with `INSUFFICIENT_EVIDENCE` when an effect cannot be assessed without invented facts (record Evidence Debt), `HUMAN_DECISION_REQUIRED` when a selection returns to `HG-INITIATIVE` (gate in `open_gates`), or `BLOCKED` when a required input is missing.

## MUST NOT

- create a second SFX for an Initiative or TOA that already has one;
- accept a local KPI improvement as a system improvement;
- skip any of the five INV-09 effects;
- invent business facts; renumber or reuse stable IDs.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
