---
name: 28-design-observability
description: "Designs the Observability Plan for a transformed Capability: signals per observability layer including decision signals, the operation-trace fields captured, trace depth proportional to authority, risk, impact and irreversibility, answers to the minimum observable questions, alerts that open incidents, review cadence and owner, and a dark-automation check whose findings block rollout. Use in Phase 7 before AI-enabled or automated work runs in a pilot or rollout stage. Produces the observability record per artifacts/observability-plan.md. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: execution-governance
phase: "7"
human_gate: false
---

# Skill 28: Design Observability

## Purpose

Make a transformed Capability observable as a business system, not only as technology, in proportion to the authority and risk involved. Invoked by [`skills/08-design-operating-model/SKILL.md`](../08-design-operating-model/SKILL.md).

## Required inputs

- Capability Target State or Target Operating Architecture;
- Pilot Plan or Rollout Plan, where piloting or rolling out;
- Autonomy Assessments (levels, Authority Ceilings) and the AI Governance Canvas draft, where AI is used;
- Metric records.

## Normative sources

- [`operations/OBSERVABILITY_MODEL.md`](../../operations/OBSERVABILITY_MODEL.md)
- [`operations/INCIDENT_MODEL.md`](../../operations/INCIDENT_MODEL.md) (§2 classes, for alerts)

## Produces

- [`artifacts/observability-plan.md`](../../artifacts/observability-plan.md) — one plan per transformed Capability, created or updated.

## Procedure

1. Identify signals for each relevant layer ([`operations/OBSERVABILITY_MODEL.md`](../../operations/OBSERVABILITY_MODEL.md) §2), including decision signals.
2. Choose the operation-trace fields to capture (§4) and set `trace_depth` from authority, risk, financial and customer impact, irreversibility, and regulatory significance (§5), with the reason.
3. Verify the minimum observable questions (§3) can be answered for production AI-enabled work.
4. Check for dark-automation patterns (§6); each one found is a blocking gap for rollout, reported in `findings` and `risks`.
5. Define alerts, which alerts open an Incident (§7), review cadence, and owner.
6. Validate against the Validation of [`artifacts/observability-plan.md`](../../artifacts/observability-plan.md).
7. Stop with `INSUFFICIENT_EVIDENCE` when proceeding would require invented business facts, or `BLOCKED` when a required input is missing.

## MUST NOT

- leave a state-changing AI or agent action unlogged;
- instrument low-risk interactions beyond what proportionality justifies ([`operations/OBSERVABILITY_MODEL.md`](../../operations/OBSERVABILITY_MODEL.md) §5);
- treat technical monitoring alone as business observability.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
