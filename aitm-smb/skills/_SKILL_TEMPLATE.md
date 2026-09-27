---
name: aitm-skill-name
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: draft
category:
human_gate: false
---

# Skill: <Name>

## Purpose

One bounded AITM-SMB operation.

## Required inputs

- Canonical Core bundle
- selected Application Profile
- relevant upstream approved artifacts
- relevant Evidence

## Produces

- canonical artifact(s) or explicit transient findings

## Procedure

1. verify required context;
2. verify upstream trace;
3. execute only the bounded operation;
4. preserve Fact / Evidence / Assumption / Hypothesis / Decision distinctions;
5. validate the output contract;
6. stop at human gates;
7. hand off using `AGENT_OUTPUT_STANDARD.md`.

## MUST NOT

- invent business facts;
- expand scope silently;
- select AI before simpler alternatives are considered;
- grant authority from technical capability;
- claim `COMPLETE` when required validation is missing.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
