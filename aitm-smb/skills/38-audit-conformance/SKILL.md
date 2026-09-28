---
name: 38-audit-conformance
description: "Audits an engagement's conformance to AITM-SMB: the core chain and minimum valid path, every CONFORMANCE core item including cause versus symptom, non-AI alternatives, AI justification, system effects (INV-09) and observable, reducible AI authority (INV-07), the STANDARD invariants, claimed profile content, human-gate Decisions, evidence separation, component-only applications, and waivers; then writes the conformance declaration. Use at any phase, via skill 10, and before an engagement claims conformance. Produces the conformance section of artifacts/transformation-intent.md and findings; the result is not approval of any gated decision. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: framework-operations
phase: "any"
human_gate: false
---

# Skill 38: Audit AITM-SMB Conformance

## Purpose

Test whether an engagement is a conforming AITM-SMB application, semantically rather than documentarily, and record the result where every later session finds it. Invoked by [`skills/10-audit-aitm-engagement/SKILL.md`](../10-audit-aitm-engagement/SKILL.md).

## Required inputs

- the engagement workspace (all instance files);
- the approved profile Decision; without one, evaluate as [`CONFORMANCE.md`](../../CONFORMANCE.md) §3 prescribes (no profile: Compact; add-ons only: Standard plus those add-ons).

## Normative sources

- [`CONFORMANCE.md`](../../CONFORMANCE.md)
- [`STANDARD.md`](../../STANDARD.md) (§2 chain, §3 invariants, §8 gates, §14 conformance)
- [`EXECUTION_MODEL.md`](../../EXECUTION_MODEL.md) §6 (minimum valid path)
- [`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md), [`MINIMUM_ARTIFACT_SET.md`](../../MINIMUM_ARTIFACT_SET.md)
- [`TRACEABILITY.md`](../../TRACEABILITY.md)

## Produces

- [`artifacts/transformation-intent.md`](../../artifacts/transformation-intent.md) — the `conformance` declaration ([`CONFORMANCE.md`](../../CONFORMANCE.md) §5);
- `findings`: one per failed check, naming the requirement and the IDs concerned.

## Procedure

1. Check the core chain ([`STANDARD.md`](../../STANDARD.md) §2) and the minimum valid path ([`EXECUTION_MODEL.md`](../../EXECUTION_MODEL.md) §6); report missing links per [`TRACEABILITY.md`](../../TRACEABILITY.md) §4. Trace integrity: `python3 tools/validate.py --engagement <workspace>`.
2. Check every [`CONFORMANCE.md`](../../CONFORMANCE.md) §1 item (1–14), including cause versus symptom, non-AI interventions, AI justification, system effects (INV-09), and how AI authority is observed and reduced (INV-07); aid: [`rubrics/CONFORMANCE_CHECKLIST.md`](../../rubrics/CONFORMANCE_CHECKLIST.md).
3. Check the remaining [`STANDARD.md`](../../STANDARD.md) §3 invariants.
4. Flag an application that is only a component listed in [`CONFORMANCE.md`](../../CONFORMANCE.md) §2 as non-conforming.
5. Check each claimed profile's content ([`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md); artifact mapping [`MINIMUM_ARTIFACT_SET.md`](../../MINIMUM_ARTIFACT_SET.md)), or its recorded waiver ([`CONFORMANCE.md`](../../CONFORMANCE.md) §3).
6. Check every gated item used downstream is listed in an approved DEC with `gate`, `subject_ids`, and a named `approved_by`; report the gates of proposed gate Decisions in `open_gates`; and check that no agent crossed a gate or self-approved.
7. Check evidence and assumption separation (agent inference labeled `[HYPOTHESIS]`; every Assumption owned by a named business role, [`AGENTS.md`](../../AGENTS.md) §3), and artifact proportionality and merge rules ([`CONFORMANCE.md`](../../CONFORMANCE.md) §4).
8. List each waiver with the [`CONFORMANCE.md`](../../CONFORMANCE.md) §6 fields; a waived MUST goes in `unresolved_exceptions`.
9. Write the declaration ([`CONFORMANCE.md`](../../CONFORMANCE.md) §5): `framework_version`, `profiles`, `validated_at`, `validated_by` (this skill), `unresolved_exceptions`.
10. Stop with `BLOCKED` when the workspace cannot be read.

## MUST NOT

- present a conformance result as approval of any gated decision ([`CONFORMANCE.md`](../../CONFORMANCE.md) §5);
- waive a requirement; only an approved human Decision can ([`CONFORMANCE.md`](../../CONFORMANCE.md) §6);
- change audited records; report findings instead.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
