---
name: 17-map-capability-network
description: "Maps the smallest set of dependencies between business Capabilities needed to reason about the transformation: relation type and direction, criticality, failure and capacity effects, and shared capabilities. Use in Phase 5 under the Standard profile or above, invoked by skill 06, or when a change to one Capability may shift work, information or constraints to another. Produces a Capability Network with Capability Dependency records. Part of AITM-SMB; paths are relative to the AITM-SMB root."
metadata:
  framework: AITM-SMB
  version: "1.1.0"
  minimum_framework_version: "1.1.0"
  status: active
  category: design-specialist
  phase: "5"
  human_gate: "false"
---

# Skill 17: Map Capability Network

## Purpose

Show how the Capabilities in scope depend on one another, so that constraint analysis and system-effect checks see beyond one Capability. Invoked by [`skills/06-design-target-system/SKILL.md`](../06-design-target-system/SKILL.md).

## Required inputs

- Capability Map with CURRENT States;
- approved Outcomes and selected Initiatives;
- Business System Map and current-state Evidence, where they exist.

## Normative sources

- [`design/CAPABILITY_NETWORK.md`](../../design/CAPABILITY_NETWORK.md)

## Produces

- [`artifacts/capability-network.md`](../../artifacts/capability-network.md) — Capability Network (`CPN-###`) with Capability Dependency records (`DEP-###`)

## Procedure

1. Bound the network to Capabilities relevant to the target Outcomes and selected Initiatives ([`design/CAPABILITY_NETWORK.md`](../../design/CAPABILITY_NETWORK.md) §7); list them in the CPN `capability_ids`.
2. For each Capability, answer the dependency questions (§5).
3. Record each dependency once as a `DEP-###` with `source_capability_id`, one §2 `relation`, and `target_capability_id`, in the §2 direction convention; add its `criticality` (§4), `failure_effect`, `capacity_effect`, and `evidence_ids`.
4. Mark shared capabilities (§6).
5. Validate against the [`artifacts/capability-network.md`](../../artifacts/capability-network.md) Validation.
6. Stop with `INSUFFICIENT_EVIDENCE` when a dependency would have to be invented (record it as an Assumption or Evidence Debt instead); with `HUMAN_DECISION_REQUIRED` when any [`STANDARD.md`](../../STANDARD.md) §8 gate is reached.

## MUST NOT

- map the whole company, or widen scope silently;
- hide dependency effects on the target Outcomes;
- invent business facts, present inference as Evidence, or hide uncertainty;
- renumber or reuse stable IDs.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
