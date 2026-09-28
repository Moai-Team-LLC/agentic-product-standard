---
name: 36-select-application-profile
description: "Selects the engagement's Application Profiles: a base profile (Compact or Standard) and each add-on (Governed, Portfolio, Measured) evaluated independently, by answering the PROFILE_SELECTION questions against the APPLICATION_PROFILES use-when lists, defaulting to Standard + Measured where an answer is unknown, and records the selection, rationale and change triggers as a Decision that HG-OUTCOME confirms. Use at the start of an engagement (Phase 0, via skill 01), whenever no approved profile Decision exists, at the Phase 1 exit re-check, and when new evidence changes an answer. Produces a DEC record in artifacts/decision-assumption-log.md. Part of AITM-SMB; paths are relative to the AITM-SMB root."
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

Fix how much methodology the engagement needs, by complexity and risk rather than company size, and persist the choice so every later session loads the same profiles. Invoked by `skills/01-discover-transformation/SKILL.md`, or directly when no profile Decision exists (`AGENT_CONTEXT_POLICY.md`).

## Required inputs

- business context and transformation scope as the Outcome owner states them;
- what is known about the selection dimensions (`APPLICATION_PROFILES.md` §2);
- the current profile Decision, when re-checking.

## Normative sources

- `PROFILE_SELECTION.md`
- `APPLICATION_PROFILES.md`
- `STANDARD.md` §16 (materiality)

## Produces

- `artifacts/decision-assumption-log.md` — one Decision: `statement` names the selected profiles, `rationale` answers each question, `review_trigger` states what would change them, `status: proposed` until approved; a change supersedes the previous Decision.

## Procedure

1. Assess every selection dimension (`APPLICATION_PROFILES.md` §2), including business criticality and regulatory exposure; label unknowns `[OPEN]`.
2. Base profile: answer `PROFILE_SELECTION.md` §2; Compact only when every Compact use-when condition holds, otherwise Standard.
3. Add-ons: answer each §3 question independently of the base and of each other (Governed, including high AI authority and irreversible actions; Portfolio; Measured).
4. Where an answer is unknown at Phase 0, apply the default Standard + Measured (§4).
5. Record the Decision (§5) and return its DEC-### for the Transformation Intent `profile_decision_id` (skill 01).
6. Until `HG-OUTCOME` confirms it, the selection is provisional; say so in `status_reason`.
7. Re-check at the Phase 1 exit and whenever new Evidence changes an answer (§6); a change is a new Decision that supersedes the previous one.
8. Validate against the Validation of `artifacts/decision-assumption-log.md`; stop with `BLOCKED` when no Outcome owner can state the business context.

## MUST NOT

- leave out an add-on whose use-when condition holds, or pick a base profile to reduce work;
- classify an item as immaterial to avoid a profile or a gate;
- activate modules the selected profiles do not require without a Decision (`APPLICATION_PROFILES.md` §9);
- record the `HG-OUTCOME` approval itself.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
