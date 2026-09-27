---
name: 11-discover-capabilities
version: 1.0.0
minimum_framework_version: 1.0.0
framework: AITM-SMB
status: active
category: diagnostic-specialist
---

# Skill: Discover Business Capabilities

## Required inputs

- approved Outcome scope
- value-stream/process evidence

## Produces

- `artifacts/capability-map.md`

## Procedure

1. Start from each approved Outcome.
2. Identify value streams materially affecting that Outcome.
3. Extract stable organizational abilities from activities.
4. Normalize capability boundaries using the granularity test.
5. Remove tool names, department names, and task-level artifacts where they do not represent stable abilities.
6. Assign stable CAP identifiers and record evidence/confidence.

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
