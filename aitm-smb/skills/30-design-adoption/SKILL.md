---
name: 30-design-adoption
description: "Designs the Adoption Plan for a transformation: one role transition per affected role (task dispositions, removed and new tasks, decision-right, skill and metric changes), behavior changes across the adoption dimensions including manager behavior and exception handling, training, incentives, trust and workflow-fit risks, communication, support, feedback channel and adoption metrics, with resistance treated as evidence. Use in Phase 7 before a pilot or rollout changes how people work. Produces adoption and role-transition records per artifacts/adoption-plan.md. Part of AITM-SMB; paths are relative to the AITM-SMB root."
metadata:
  framework: AITM-SMB
  version: "1.1.0"
  minimum_framework_version: "1.1.0"
  status: active
  category: execution-governance
  phase: "7"
  human_gate: "false"
---

# Skill 30: Design Change Adoption

## Purpose

Make the human side of the transformation explicit before rollout: which roles change, what they need, and how adoption is observed. Invoked by [`skills/08-design-operating-model/SKILL.md`](../08-design-operating-model/SKILL.md).

## Required inputs

- role changes implied by the Target Operating Architecture role model, the Capability Target States, and Transition State `role_changes`, where they exist;
- Decision Rights Map, where it exists;
- Pilot Plan or Rollout Plan, where piloting or rolling out;
- Metric records.

## Normative sources

- [`change/CHANGE_ADOPTION_MODEL.md`](../../change/CHANGE_ADOPTION_MODEL.md)
- [`change/ROLE_TRANSITION_MODEL.md`](../../change/ROLE_TRANSITION_MODEL.md)

## Produces

- [`artifacts/adoption-plan.md`](../../artifacts/adoption-plan.md) — `adoption` record and `role_transitions` (one per affected role), created or updated.

## Procedure

1. For each affected role, record a role transition ([`change/ROLE_TRANSITION_MODEL.md`](../../change/ROLE_TRANSITION_MODEL.md) §3): current and target responsibilities, a disposition per affected task in `task_dispositions` (§2), removed and new tasks (§4), decision-right, skill, and performance-metric changes, risks.
2. Check `decision_right_changes` against the Decision Rights Map ([`change/ROLE_TRANSITION_MODEL.md`](../../change/ROLE_TRANSITION_MODEL.md) §5).
3. Address every adoption dimension the change touches ([`change/CHANGE_ADOPTION_MODEL.md`](../../change/CHANGE_ADOPTION_MODEL.md) §2), including manager behavior and exception handling; record `trust_risks` and `workflow_fit_risks`.
4. Define `training_required`, `incentive_changes`, communication, support model, and `feedback_channel`.
5. Define adoption metrics (§4) as Metric records alongside, not in place of, Outcome metrics.
6. Treat observed resistance as evidence (§5); where it indicates workflow degradation or an incorrect target-state design, report it in `findings` for redesign.
7. Validate against the Validation of [`artifacts/adoption-plan.md`](../../artifacts/adoption-plan.md).
8. Stop with `INSUFFICIENT_EVIDENCE` when proceeding would require invented business facts, `BLOCKED` when a required input is missing, or `HUMAN_DECISION_REQUIRED` at `HG-DECISION-RIGHTS` when a role transition changes material Decision Rights not yet approved.

## MUST NOT

- leave role redesign implicit;
- treat all resistance as a people problem;
- use adoption metrics as evidence of business value.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
