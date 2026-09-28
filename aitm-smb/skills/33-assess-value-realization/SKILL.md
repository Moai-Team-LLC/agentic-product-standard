---
name: 33-assess-value-realization
description: "Assesses whether an Initiative created attributable, sustained business value: compares the Outcome metric with baseline and target, traces the benefit chain, nets implementation and operating cost, records attribution confidence with competing explanations, checks sustainability and that governance remains effective, proposes the value state and value conclusion, and updates Execution Gate G. Use in Phase 8 once rollout or operation has produced evidence. Produces a VRL record per artifacts/value-realization-report.md; declaring value REALIZED or SUSTAINED stops for HG-VALUE. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: execution-governance
phase: "8"
human_gate: true
gates: [HG-VALUE]
---

# Skill 33: Assess Value Realization

## Purpose

Separate projected from realized value, so that deployment or adoption is never reported as business value. Invoked by [`skills/09-measure-evolution/SKILL.md`](../09-measure-evolution/SKILL.md).

## Required inputs

- Outcome and Metric records with measured baselines ([`artifacts/transformation-intent.md`](../../artifacts/transformation-intent.md), [`artifacts/transformation-scorecard.md`](../../artifacts/transformation-scorecard.md));
- post-rollout or operating Evidence and EVL results ([`artifacts/evaluation-plan.md`](../../artifacts/evaluation-plan.md));
- cost data and the Initiative's `economic_hypothesis` ([`artifacts/transformation-roadmap.md`](../../artifacts/transformation-roadmap.md); record: [`economics/TRANSFORMATION_ECONOMICS.md`](../../economics/TRANSFORMATION_ECONOMICS.md) §5);
- Incident records (INC-###) and risk and governance evaluations, where they exist.

## Normative sources

- [`measurement/VALUE_REALIZATION.md`](../../measurement/VALUE_REALIZATION.md)
- [`measurement/BENEFIT_EVIDENCE_CHAIN.md`](../../measurement/BENEFIT_EVIDENCE_CHAIN.md)
- [`economics/TRANSFORMATION_ECONOMICS.md`](../../economics/TRANSFORMATION_ECONOMICS.md)
- [`execution/EXECUTION_GATE_MODEL.md`](../../execution/EXECUTION_GATE_MODEL.md) (Gate G)

## Produces

- [`artifacts/value-realization-report.md`](../../artifacts/value-realization-report.md) — VRL record, created or updated;
- [`artifacts/execution-gate.md`](../../artifacts/execution-gate.md) — Gate G record (created by skill 07): `evidence_provided` and a proposed status (Governed).

## Procedure

1. Compare the Outcome metric with baseline and target; without a measured baseline the value state stays HYPOTHESIZED and the gap is recorded as Evidence Debt ([`measurement/VALUE_REALIZATION.md`](../../measurement/VALUE_REALIZATION.md) §2).
2. Trace change, behavior, capability, Outcome, and economic value ([`measurement/BENEFIT_EVIDENCE_CHAIN.md`](../../measurement/BENEFIT_EVIDENCE_CHAIN.md) §2); Measured: record `benefit_chain`, keeping a link without Evidence visible as missing.
3. Estimate the economic effect and net implementation and operating cost into `realized_value` ([`economics/TRANSFORMATION_ECONOMICS.md`](../../economics/TRANSFORMATION_ECONOMICS.md) §2, §4).
4. Record attribution confidence LOW, MEDIUM, or HIGH with competing explanations ([`measurement/VALUE_REALIZATION.md`](../../measurement/VALUE_REALIZATION.md) §4).
5. Assess sustainability over the stated period (§5).
6. Check that governance remains effective: incident history and risk / governance evaluations.
7. Propose `value_state` (§2 entry criteria) and `conclusion` (§6); the scorecard's effect conclusion stays separate.
8. Governed: update Gate G with the evidence provided and a proposed status.
9. Validate against the Validation of [`artifacts/value-realization-report.md`](../../artifacts/value-realization-report.md).
10. Stop with `INSUFFICIENT_EVIDENCE` when value cannot be established without invented facts (conclusion INSUFFICIENT_EVIDENCE; record Evidence Debt), or `BLOCKED` when a required input is missing.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-VALUE` before `value_state` REALIZED or SUSTAINED, or `conclusion` VALUE_CONFIRMED, takes effect; record the gate as a DEC with `gate:` set and `status: proposed` ([`AGENTS.md`](../../AGENTS.md) §4), listing the VRL-### in `subject_ids` ([`measurement/VALUE_REALIZATION.md`](../../measurement/VALUE_REALIZATION.md) §2); the named human's approval updates it to `approved`. Until then the state and conclusion are proposals.

## MUST NOT

- accept deployment, adoption, or AI quality as evidence of value;
- claim value without netting cost or recording competing explanations;
- call a temporary post-launch improvement sustained;
- record an approval the named human has not explicitly given.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
