---
name: 12-separate-symptoms-gaps-causes
description: "Converts raw observations about a business into evidenced Observations and Symptoms, links them to Outcomes, Capabilities and CURRENT States, forms Gaps between current and required behavior, and generates competing cause Hypotheses classified by cause class and confidence. Use in Phase 2 (diagnosis), usually invoked by skill 03, before root causes are validated (skill 16) and before any solution is considered. Produces Diagnostic Records, Gap records in the Capability Diagnosis, cause Hypotheses in the Decision and Assumption Log, and Evidence Register entries. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: diagnostic-specialist
phase: "2"
human_gate: false
---

# Skill 12: Separate Symptoms, Gaps, and Causes

## Purpose

Keep observations, symptoms, Gaps, and cause Hypotheses distinct, so that diagnosis does not jump from a pain point to a solution. Invoked by [`skills/03-diagnose-capabilities/SKILL.md`](../03-diagnose-capabilities/SKILL.md).

## Required inputs

- observations and their Evidence;
- Capability Map with CURRENT States;
- approved Outcomes.

## Normative sources

- [`diagnostics/DIAGNOSTIC_MODEL.md`](../../diagnostics/DIAGNOSTIC_MODEL.md)
- [`diagnostics/DIAGNOSTIC_DIMENSIONS.md`](../../diagnostics/DIAGNOSTIC_DIMENSIONS.md)
- [`diagnostics/ROOT_CAUSE_ANALYSIS.md`](../../diagnostics/ROOT_CAUSE_ANALYSIS.md) §3 (cause classes)
- [`AGENT_DIAGNOSTIC_PROTOCOL.md`](../../AGENT_DIAGNOSTIC_PROTOCOL.md)

## Produces

- [`artifacts/diagnostic-record.md`](../../artifacts/diagnostic-record.md) — Diagnostic Records (`DIA-###`) with Observations and Symptoms, Standard and above
- [`artifacts/capability-diagnosis.md`](../../artifacts/capability-diagnosis.md) — Gap records (`GAP-###`); in Compact without a Diagnostic Record, also their `observations` and `symptoms`
- [`artifacts/decision-assumption-log.md`](../../artifacts/decision-assumption-log.md) — cause Hypotheses (`HYP-###`, `kind: cause`, `status: hypothesized`)
- [`artifacts/evidence-register.md`](../../artifacts/evidence-register.md) — Evidence and Evidence Debt

## Procedure

1. Follow [`AGENT_DIAGNOSTIC_PROTOCOL.md`](../../AGENT_DIAGNOSTIC_PROTOCOL.md) §2, steps 1–9.
2. Record Observations, each citing Evidence, and the Symptoms they support in a Diagnostic Record ([`diagnostics/DIAGNOSTIC_MODEL.md`](../../diagnostics/DIAGNOSTIC_MODEL.md) §2); in Compact they MAY sit on the Gap instead ([`artifacts/capability-diagnosis.md`](../../artifacts/capability-diagnosis.md)).
3. Link each Symptom to the affected Outcomes, Capabilities, and CURRENT States.
4. Inspect the diagnostic dimensions relevant to the boundary ([`diagnostics/DIAGNOSTIC_DIMENSIONS.md`](../../diagnostics/DIAGNOSTIC_DIMENSIONS.md)); form a Gap for each material difference between current and required behavior, with its business impact.
5. Generate competing cause Hypotheses ([`AGENT_DIAGNOSTIC_PROTOCOL.md`](../../AGENT_DIAGNOSTIC_PROTOCOL.md) §3) and record each as a Hypothesis record (`HYP-###`, `kind: cause`) with `cause_class`, `confidence` ([`diagnostics/DIAGNOSTIC_MODEL.md`](../../diagnostics/DIAGNOSTIC_MODEL.md) §5), and `alternative_hypothesis_ids`; list them in the Gap's `hypothesis_ids` and set `cause_status: hypothesized`.
6. Record missing Evidence as Evidence Debt; validate against the Validation of each produced contract.
7. Hand the Hypotheses to skill 16. Stop with `INSUFFICIENT_EVIDENCE` when a Gap or Hypothesis would require invented business facts; with `HUMAN_DECISION_REQUIRED` when any [`STANDARD.md`](../../STANDARD.md) §8 gate is reached.

## MUST NOT

- invent business facts, present inference as Evidence, or hide uncertainty;
- diagnose "lack of AI" as a cause, or propose a solution;
- mark a Hypothesis `validated` (skill 16 tests it);
- widen scope silently, or renumber or reuse stable IDs;
- recommend AI before simpler intervention families are considered.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
