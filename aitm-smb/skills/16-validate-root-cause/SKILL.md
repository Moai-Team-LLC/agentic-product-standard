---
name: 16-validate-root-cause
description: "Tests the cause Hypotheses of a Gap against supporting and falsifying evidence, competing explanations, the counterfactual challenge and the intervention trap test, then sets each Hypothesis's confidence and status (validated or rejected), proposes acceptance as testable to the Capability or Outcome owner, or defines the cheapest useful validation test. Use in Phase 2, invoked by skill 03, before a Gap is declared ready for intervention design. Produces updated Hypothesis records in the Decision and Assumption Log, Diagnostic Record updates and Evidence Register entries. Part of AITM-SMB; paths are relative to the AITM-SMB root."
metadata:
  framework: AITM-SMB
  version: "1.1.0"
  minimum_framework_version: "1.1.0"
  status: active
  category: diagnostic-specialist
  phase: "2"
  human_gate: "false"
---

# Skill 16: Validate Root Cause

## Purpose

Establish whether a Gap's cause is supported well enough for intervention design, resisting premature closure. Invoked by [`skills/03-diagnose-capabilities/SKILL.md`](../03-diagnose-capabilities/SKILL.md).

## Required inputs

- a Gap with its cause Hypotheses (skill 12);
- available Evidence (Evidence Register, Diagnostic Records).

## Normative sources

- [`diagnostics/ROOT_CAUSE_ANALYSIS.md`](../../diagnostics/ROOT_CAUSE_ANALYSIS.md)
- [`AGENT_DIAGNOSTIC_PROTOCOL.md`](../../AGENT_DIAGNOSTIC_PROTOCOL.md) §3–§4
- [`diagnostics/DIAGNOSTIC_MODEL.md`](../../diagnostics/DIAGNOSTIC_MODEL.md) §5–§6

## Produces

- [`artifacts/decision-assumption-log.md`](../../artifacts/decision-assumption-log.md) — Hypothesis records (`HYP-###`): `evidence_for`, `evidence_against`, `alternative_hypothesis_ids`, `test`, `confidence`, `status`
- [`artifacts/diagnostic-record.md`](../../artifacts/diagnostic-record.md) — updated `hypothesis_ids`, `evidence_debt`, `next_action`, where Diagnostic Records exist
- [`artifacts/evidence-register.md`](../../artifacts/evidence-register.md) — Evidence and Evidence Debt

## Procedure

1. For each cause Hypothesis, apply the evidence test ([`diagnostics/ROOT_CAUSE_ANALYSIS.md`](../../diagnostics/ROOT_CAUSE_ANALYSIS.md) §4): cite supporting and falsifying Evidence in `evidence_for` and `evidence_against`.
2. Ensure competing Hypotheses exist and are linked ([`AGENT_DIAGNOSTIC_PROTOCOL.md`](../../AGENT_DIAGNOSTIC_PROTOCOL.md) §3); add missing ones.
3. Apply the counterfactual challenge ([`AGENT_DIAGNOSTIC_PROTOCOL.md`](../../AGENT_DIAGNOSTIC_PROTOCOL.md) §4) and the intervention trap test ([`diagnostics/ROOT_CAUSE_ANALYSIS.md`](../../diagnostics/ROOT_CAUSE_ANALYSIS.md) §5).
4. Set `confidence` ([`diagnostics/DIAGNOSTIC_MODEL.md`](../../diagnostics/DIAGNOSTIC_MODEL.md) §5) and `status` ([`diagnostics/ROOT_CAUSE_ANALYSIS.md`](../../diagnostics/ROOT_CAUSE_ANALYSIS.md) §7). `accepted_as_testable` needs an approved Decision of the Capability or Outcome owner listing the `HYP-###` in `subject_ids`: propose it in `decisions_needed`.
5. Where Evidence is insufficient, define the cheapest useful validation method in `test`; record Evidence Debt.
6. Return each Gap's resulting `cause_status` and intervention readiness ([`diagnostics/DIAGNOSTIC_MODEL.md`](../../diagnostics/DIAGNOSTIC_MODEL.md) §6) in `findings`; validate against the Validation of each produced contract; review aid: [`rubrics/DIAGNOSTIC_QUALITY_RUBRIC.md`](../../rubrics/DIAGNOSTIC_QUALITY_RUBRIC.md).
7. Stop with `INSUFFICIENT_EVIDENCE` when a status would require invented business facts; with `HUMAN_DECISION_REQUIRED` when any [`STANDARD.md`](../../STANDARD.md) §8 gate is reached.

## MUST NOT

- mark a Hypothesis `validated` without Evidence in `evidence_for`;
- set a Hypothesis, or a Gap's `cause_status`, to `accepted_as_testable` without that owner's approved Decision;
- infer a root cause from one statement without labeling it `[HYPOTHESIS]`;
- invent business facts, present inference as Evidence, or hide uncertainty;
- widen scope silently, or renumber or reuse stable IDs;
- recommend AI before simpler intervention families are considered.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
