---
name: 10-audit-aitm-engagement
description: "Cross-phase orchestrator. Audits an AITM-SMB engagement at any point for semantic traceability, conformance with the selected profiles, evidence discipline, human decision gates and AI authority boundaries, by running the conformance audit (skill 38). Use before a phase exit, before a human gate decision, or when conformance is claimed. Returns findings and the decisions a human must take; skill 38 writes the conformance declaration into the Transformation Intent. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: orchestrator
phase: "any"
human_gate: false
---

# Skill 10: Orchestrate Conformance Audit

## Purpose

Audit semantic traceability, selected-profile conformance, evidence discipline, human gates, and authority boundaries of an engagement, at any phase.

## Required inputs

- the engagement's instances in the engagement workspace, as far as they exist;
- the approved profile Decision (`AGENT_CONTEXT_POLICY.md`); an engagement that declares no profile is evaluated as Compact (`CONFORMANCE.md` §3).

## Normative sources

- `CONFORMANCE.md`
- `TRACEABILITY.md`

## Produces

- findings in the handoff (`findings`, with the IDs each concerns); no artifact of its own

The conformance declaration is written by skill 38 (its `## Produces`).

## Specialist skills

- `skills/38-audit-conformance/SKILL.md` — always

## Procedure

1. Load the active profiles and `CONFORMANCE.md`.
2. Fix the audit scope: the whole engagement, or named phases or artifacts; record it in `status_reason`.
3. Invoke skill 38 for that scope; review aids: `rubrics/CONFORMANCE_CHECKLIST.md`, `rubrics/EVALUATION_RUBRIC.md`.
4. Report each finding with the IDs it concerns; put findings that need a human decision in `decisions_needed`, with the gate where one applies.
5. Report an item that cannot be judged from the records as a finding, never as passed; stop with `BLOCKED` when there are no engagement records to audit.

## MUST NOT

- approve, waive, or close any gate: a conformance result is not approval (`CONFORMANCE.md` §5);
- change engagement records other than the conformance declaration;
- create a second definition of any concept owned by a specialist skill or normative module.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
