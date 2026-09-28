---
name: NN-slug                         # equals the directory name
description: "<one line, double-quoted, <= 1024 characters: what the skill does, when to use it, what it produces>. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active                        # draft | active | deprecated
category: orchestrator | diagnostic-specialist | design-specialist | execution-governance | framework-operations
phase: "N"                            # orchestrators: their phase; specialists: the phase(s) they serve, e.g. "2" or "6-7"
human_gate: true | false              # true: the output requires a STANDARD.md §8 approval before downstream use
gates: [HG-...]                       # present only when human_gate is true
---

# Skill NN: <Title>

Conventions for paths, `Produces`, the engagement workspace, and frontmatter: `skills/INDEX.md` §4. Keep a skill short (typically 25–60 lines) and add no methodology semantics.

## Purpose

One or two sentences: the bounded operation and why it exists.

## Required inputs

- upstream records the skill reads, by artifact, and whether they must be approved;
- relevant Evidence.

Orchestrators point to the Required inputs of their phase file instead of listing them.

## Normative sources

- the module or core files that define the concepts used (`CANONICAL_CONCEPTS.md`); orchestrators: their phase file.

## Produces

- the artifact contract(s) the output conforms to, with the records created or updated: exactly the contracts whose `produced_by` lists this skill (`artifacts/_ARTIFACT_CONTRACT.md` §2);
- or: no persistent artifact; results go to `findings` in the handoff.

Appends that any skill MAY make (`skills/INDEX.md` §4) are not listed.

## Specialist skills

Orchestrators only: each specialist with the condition under which it runs.

## Procedure

1. Numbered steps that apply the normative sources by reference (`<file>` §n); do not restate definitions, dimension lists, or class lists.
2. Validate the output against the Validation of its artifact contract.
3. Stop with `INSUFFICIENT_EVIDENCE` when proceeding would require invented business facts (record Evidence Debt), or with `BLOCKED` when a required input is missing.

## Human gates

Gated skills only: Stop with status `HUMAN_DECISION_REQUIRED` at `HG-…`; the approval is recorded as a DEC with `gate:` set (`artifacts/decision-assumption-log.md`).

## MUST NOT

- invent business facts or present inference as Evidence;
- widen scope silently;
- renumber or reuse stable IDs;
- select AI before simpler intervention families are considered;
- grant or increase AI authority from technical capability;
- claim `COMPLETE` while a required validation or gate is open.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
