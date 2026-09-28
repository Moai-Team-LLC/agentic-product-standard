---
name: 31-operationalize-governance
description: "Makes AI governance executable for an AI-enabled Capability: completes the AI Governance Canvas within the approved Authority Ceilings (owner, risk owner, permissions, prohibited actions, approvals, escalation and stop conditions, evaluation, audit evidence, recovery path, cost boundary), assigns AI components to the canonical change-control classes, and defines the authority promotion and demotion path and the incident review loop. Use in Phase 7 wherever AI is used; Compact needs only the Governance minimum fields. Produces the canvas per artifacts/ai-governance-canvas.md and stops where material risk is accepted or AI authority is granted. Part of AITM-SMB; paths are relative to the AITM-SMB root."
version: 1.1.0
minimum_framework_version: 1.1.0
framework: AITM-SMB
status: active
category: execution-governance
phase: "7"
human_gate: true
gates: [HG-RISK, HG-AUTHORITY]
---

# Skill 31: Operationalize Governance

## Purpose

Turn authority decisions into controls that operate: who may do what, who approves, how changes are classed, and how failures and authority changes are handled. Invoked by `skills/08-design-operating-model/SKILL.md`.

## Required inputs

- AI Governance Canvas draft, if any; otherwise start it from the Autonomy Assessments and the Decision Rights Map;
- Autonomy Assessments with approved Authority Ceilings (`artifacts/autonomy-assessment.md`);
- Operating Model draft and Observability Plan, where they exist.

## Normative sources

- `governance/GOVERNANCE_OPERATING_MODEL.md`
- `governance/AI_CHANGE_CONTROL.md`
- `governance/AUTHORITY_ESCALATION_MODEL.md`
- `operations/INCIDENT_MODEL.md`

## Produces

- `artifacts/ai-governance-canvas.md` — `governance` record (Compact: the Governance minimum fields; Governed: complete, with a named risk owner), created or updated.

## Procedure

1. Link the canvas to its Capability, Outcomes, and `authority_ceiling_ids`; answer its Required questions.
2. Set permissions, prohibited actions, approval, escalation, and stop conditions within the referenced Authority Ceilings.
3. Name the owner and, under Governed, the `risk_owner`, with material AI risks recorded as Risk records (RSK-###, `artifacts/decision-assumption-log.md`) listed in `risk_ids`; define evaluation method, audit evidence, recovery path, and the cost boundary (`cost_limit`).
4. Assign each AI component and change type (`governance/AI_CHANGE_CONTROL.md` §1) to the canonical Low, Medium, or High class (§2); define no new classes.
5. State how authority is promoted (`governance/AUTHORITY_ESCALATION_MODEL.md` §3, via skill 34) and demoted (§4), and who may demote at once.
6. Define the incident review loop: incidents recorded as INC-### by `skills/40-handle-incident/SKILL.md`, feedback per `operations/INCIDENT_MODEL.md` §4.
7. Return governance responsibilities, cadence, and review triggers (`governance/GOVERNANCE_OPERATING_MODEL.md` §3, §4, §6) in `findings`; orchestrator 08 writes them into the Operating Model (`artifacts/operating-model.md`).
8. Validate against the Validation of `artifacts/ai-governance-canvas.md`.
9. Stop with `INSUFFICIENT_EVIDENCE` when proceeding would require invented business facts, or `BLOCKED` when a required input is missing.

## Human gates

Stop with status `HUMAN_DECISION_REQUIRED` at `HG-RISK` when the canvas accepts material customer, financial, security, legal, or operational risk, and at `HG-AUTHORITY` when it would grant AI permissions beyond the currently approved authority; the approval is recorded as a DEC with `gate:` set that, for `HG-RISK`, lists the accepted RSK-### in `subject_ids` (`artifacts/decision-assumption-log.md`).

## MUST NOT

- permit what an Authority Ceiling prohibits or leaves to approval;
- define change classes other than the canonical ones, or treat a model upgrade as automatically low-risk;
- record an approval the named human has not explicitly given.

## Handoff

Emit the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.
