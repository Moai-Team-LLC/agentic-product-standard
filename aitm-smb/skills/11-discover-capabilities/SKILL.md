---
name: 11-discover-capabilities
description: "Discovers the stable business Capabilities that materially affect the approved Outcomes, normalizes their boundaries with the granularity test, assigns CAP identifiers, and records each Capability's CURRENT State with evidence and confidence. Use in Phase 1 (current-system mapping), usually invoked by skill 02, or whenever a Capability in scope is missing from the Capability Map. Produces Capability and CURRENT State records in the Capability Map and Evidence Register entries. Part of AITM-SMB; paths are relative to the AITM-SMB root."
metadata:
  framework: AITM-SMB
  version: "1.1.0"
  minimum_framework_version: "1.1.0"
  status: active
  category: diagnostic-specialist
  phase: "1"
  human_gate: "false"
---

# Skill 11: Discover Business Capabilities

## Purpose

Identify the stable organizational abilities that produce the approved Outcomes and describe how each operates today, so that Gaps can be diagnosed against a CURRENT State. Invoked by [`skills/02-map-current-system/SKILL.md`](../02-map-current-system/SKILL.md).

## Required inputs

- approved Outcomes (Transformation Intent, `HG-OUTCOME` closed);
- value-stream and process Evidence (Evidence Register, interviews, system data).

## Normative sources

- [`diagnostics/CAPABILITY_DISCOVERY.md`](../../diagnostics/CAPABILITY_DISCOVERY.md) (granularity test §4)
- [`CORE_MODEL.md`](../../CORE_MODEL.md) §2 (Capability), §3 (State)

## Produces

- [`artifacts/capability-map.md`](../../artifacts/capability-map.md) — Capability records (`CAP-###`) and their CURRENT States (`STA-###`, `type: CURRENT`)
- [`artifacts/evidence-register.md`](../../artifacts/evidence-register.md) — Evidence and Evidence Debt

## Procedure

1. Start from each approved Outcome and follow the discovery sequence ([`diagnostics/CAPABILITY_DISCOVERY.md`](../../diagnostics/CAPABILITY_DISCOVERY.md) §2).
2. Name and bound candidates (§3); apply the granularity test (§4); decompose only per §5.
3. Assign a new `CAP-###` when a candidate is accepted (§7); record `outcome_ids`, `value_stream_ids`, owner, `evidence_ids`, and the Capability Map extensions `dependencies` (§6), `confidence`, `boundary_notes`.
4. For each Capability in scope, record one CURRENT State across the relevant dimensions ([`CORE_MODEL.md`](../../CORE_MODEL.md) §3) and set `current_state_id`.
5. Back each State with `evidence_ids`, or with `assumption_ids` of Assumptions a named business owner stated or accepted (`[ASSUMPTION]`, [`AGENTS.md`](../../AGENTS.md) §3); label agent inference `[HYPOTHESIS]`: it does not satisfy the phase exit. Record missing Evidence as Evidence Debt.
6. Validate against the [`artifacts/capability-map.md`](../../artifacts/capability-map.md) Validation.
7. Stop with `INSUFFICIENT_EVIDENCE` when a Capability or State would require invented business facts or rest only on agent inference; with `HUMAN_DECISION_REQUIRED` (gate in `open_gates`) while `HG-OUTCOME` is open or when any [`STANDARD.md`](../../STANDARD.md) §8 gate is reached.

## MUST NOT

- invent business facts, present inference as Evidence, or hide uncertainty;
- put a target-state solution into a CURRENT State;
- widen scope beyond the approved Outcomes silently, or renumber or reuse stable IDs;
- recommend AI or any other intervention (that is Phase 3).

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
