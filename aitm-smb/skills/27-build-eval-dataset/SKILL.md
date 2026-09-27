---
name: 27-build-eval-dataset
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: execution-governance
---

# Skill: Build Evaluation Dataset

## Required inputs

- AI task definition
- historical cases
- failure patterns
- policy constraints

## Produces

- no persistent artifact required; return findings through `AGENT_OUTPUT_STANDARD.md`

## Procedure

1. Collect representative common cases.
2. Add edge, rare, ambiguous, high-impact, and policy-sensitive cases.
3. Define expected and unacceptable behavior.
4. Record source and risk class.
5. Check for evaluation leakage.

## Execution controls

- Evidence gates must be explicit.
- Success criteria must not be rewritten after results are known.
- Technical deployment does not equal transformation success.
- Business effect, operating effect, and AI quality must remain separate.
- Human approval is required for material authority increases.
- Failed pilots may be stopped.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
