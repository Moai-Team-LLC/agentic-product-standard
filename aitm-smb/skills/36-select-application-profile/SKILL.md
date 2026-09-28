---
name: 36-select-application-profile
description: "Selects the engagement's Application Profiles: a base profile (Compact or Standard) and each add-on (Governed, Portfolio, Measured) evaluated independently, by answering the PROFILE_SELECTION questions against the APPLICATION_PROFILES use-when lists, applying the PROFILE_SELECTION defaults where an answer is unknown (Standard base, a Governed condition treated as holding, Measured added, Portfolio re-checked at the Phase 1 exit), and records the selection, rationale and change triggers as a proposed Decision approved together with HG-OUTCOME. Use at the start of an engagement (Phase 0, via skill 01), whenever no approved profile Decision exists, at the Phase 1 exit re-check, and when new evidence changes an answer. Produces a DEC record in artifacts/decision-assumption-log.md. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: framework-operations
phase: "0"
human_gate: false
---

# Skill 36: Select Application Profile

## Purpose

Fix how much methodology the engagement needs, by complexity and risk rather than company size, and persist the choice so every later session loads the same profiles. Invoked by [`skills/01-discover-transformation/SKILL.md`](../01-discover-transformation/SKILL.md), or directly when no profile Decision exists ([`AGENT_CONTEXT_POLICY.md`](../../AGENT_CONTEXT_POLICY.md)).

## Required inputs

- business context and transformation scope as the Outcome owner states them;
- what is known about the selection dimensions ([`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md) §2);
- the current profile Decision, when re-checking.

## Normative sources

- [`PROFILE_SELECTION.md`](../../PROFILE_SELECTION.md)
- [`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md)
- [`STANDARD.md`](../../STANDARD.md) §16 (materiality)

## Produces

- [`artifacts/decision-assumption-log.md`](../../artifacts/decision-assumption-log.md) — one Decision: `statement` names the selected profiles, `rationale` answers each question, `review_trigger` states what would change them, `status: proposed` until approved together with `HG-OUTCOME` ([`PROFILE_SELECTION.md`](../../PROFILE_SELECTION.md) §5); a change supersedes the previous Decision.

## Procedure

1. Assess every selection dimension ([`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md) §2), including business criticality and regulatory exposure; label unknowns `[OPEN]`.
2. Base profile: answer [`PROFILE_SELECTION.md`](../../PROFILE_SELECTION.md) §2; Compact only when every Compact use-when condition holds, otherwise Standard.
3. Add-ons: answer each §3 question independently of the base and of each other (Governed, including high AI authority as [`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md) §2 classifies it, and irreversible actions; Portfolio; Measured).
4. Where an answer is unknown at Phase 0, apply §4 exactly: base Standard; a Governed condition treated as holding ([`STANDARD.md`](../../STANDARD.md) §16) unless the Outcome owner records otherwise in this Decision; Measured added; Portfolio not added, re-checked at the Phase 1 exit (§6). Mark each unknown answer in `rationale`. Always record the base explicitly ([`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md) §8).
5. Record the Decision (§5) and return its DEC-### for the Transformation Intent `profile_decision_id` (skill 01).
6. Until approved with `HG-OUTCOME` (skill 01 lists this DEC in the `HG-OUTCOME` Decision's `subject_ids`, or approves it in a separate DEC), the selection is provisional; say so in `status_reason`.
7. Re-check at the Phase 1 exit and whenever new Evidence changes an answer (§6); a change is a new Decision that supersedes the previous one.
8. Validate against the Validation of [`artifacts/decision-assumption-log.md`](../../artifacts/decision-assumption-log.md); stop with `BLOCKED` when no Outcome owner can state the business context.

## MUST NOT

- leave out an add-on whose use-when condition holds, or pick a base profile to reduce work;
- classify an item as immaterial to avoid a profile or a gate;
- activate modules the selected profiles do not require without a Decision ([`APPLICATION_PROFILES.md`](../../APPLICATION_PROFILES.md) §9);
- record the `HG-OUTCOME` approval itself.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
