---
name: 13-assess-ai-suitability
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: diagnostic-specialist
---

# Skill: Assess AI Suitability

## Required inputs

- validated or testable Gap
- intervention candidates

## Produces

- `artifacts/ai-suitability-assessment.md`

## Procedure

1. Evaluate elimination, simplification, standardization, and deterministic automation first.
2. Assess semantic load, variability, judgment, knowledge intensity, probabilistic tolerance, verification, recoverability, context readiness, risk, and economics.
3. Classify AI fit A–E.
4. Record non-AI alternative and rationale.

## Mandatory controls

- Separate evidence from inference.
- Preserve stable AITM identifiers.
- Do not silently widen scope.
- Surface uncertainty.
- Do not recommend AI before simpler intervention classes are considered.

## Stop conditions

Stop when proceeding would require invented business facts or when a human gate is reached.

## Handoff

Use `AGENT_OUTPUT_STANDARD.md`.
