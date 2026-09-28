---
name: 40-handle-incident
description: "Records and triages an incident of an AI-enabled or transformed capability: class and severity, impact and affected state, containment and recovery, root cause and corrective action, and the feedback updates it requires (policy, evaluation dataset, workflow, knowledge, permissions, authority, observability, training, Capability Target State or Target Operating Architecture). Applies immediate authority demotion when a demotion trigger fires; restoring authority is a promotion handed to skill 34 (HG-AUTHORITY). Use in Phase 7 or 8 whenever an alert, report, or review reveals an incident. Produces an INC record per artifacts/incident-record.md. Part of AITM-SMB; paths are relative to the AITM-SMB root."
metadata:
  framework: AITM-SMB
  version: "1.1.0"
  minimum_framework_version: "1.1.0"
  status: active
  category: execution-governance
  phase: "7-8"
  human_gate: "false"
---

# Skill 40: Handle Incident

## Purpose

Treat incidents as transformation governance, not only IT support: contain them, reduce AI authority at once when evidence requires, and feed what was learned back into the system. Runs whenever an incident occurs in a pilot, rollout, or operation ([`skills/INDEX.md`](../INDEX.md) §3).

## Required inputs

- the alert or report, with operation traces ([`operations/OBSERVABILITY_MODEL.md`](../../operations/OBSERVABILITY_MODEL.md) §4) and Evidence;
- the affected Capability and Initiative, and incident ownership ([`artifacts/operating-model.md`](../../artifacts/operating-model.md));
- where AI is involved: the Autonomy Assessment (`current_level`, Authority Ceiling) and the AI Governance Canvas.

## Normative sources

- [`operations/INCIDENT_MODEL.md`](../../operations/INCIDENT_MODEL.md)
- [`governance/AUTHORITY_ESCALATION_MODEL.md`](../../governance/AUTHORITY_ESCALATION_MODEL.md) (§4 demotion)
- [`operations/OBSERVABILITY_MODEL.md`](../../operations/OBSERVABILITY_MODEL.md)
- [`STANDARD.md`](../../STANDARD.md) §16 (materiality)

## Produces

- [`artifacts/incident-record.md`](../../artifacts/incident-record.md) — INC record, opened at detection and updated until `closed`.

## Procedure

1. Open an INC-### record at detection: Capability, Initiative, class ([`operations/INCIDENT_MODEL.md`](../../operations/INCIDENT_MODEL.md) §2), severity (§3), `detected_at`, impact, `affected_state`, `trace_ids`. When materiality is unclear, treat the incident as material.
2. Contain it and record `containment`; notify the incident owner.
3. Check the demotion triggers ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../../governance/AUTHORITY_ESCALATION_MODEL.md) §4). If one fires, reduce authority at once, acting for the operating owner, down to pausing the AI component (L0) where needed; record it in `authority_change`. No gate applies. Hand off to [`skills/34-manage-authority-promotion/SKILL.md`](../34-manage-authority-promotion/SKILL.md) to record the new level in the Autonomy Assessment and the Decision made afterwards.
4. Recover and record `recovery`; then establish root cause and corrective action from Evidence, labeling an unconfirmed cause `[HYPOTHESIS]`. Append new Evidence to [`artifacts/evidence-register.md`](../../artifacts/evidence-register.md) and list it in `evidence_ids`.
5. For a material incident, record each update made under [`operations/INCIDENT_MODEL.md`](../../operations/INCIDENT_MODEL.md) §4 in `feedback_updates`; hand a new evaluation case to [`skills/27-build-eval-dataset/SKILL.md`](../27-build-eval-dataset/SKILL.md) and record its ID in `eval_case_added`. Changes to AI components follow [`governance/AI_CHANGE_CONTROL.md`](../../governance/AI_CHANGE_CONTROL.md).
6. Set `status: closed` only when root cause and corrective action are stated.
7. Validate against the Validation of [`artifacts/incident-record.md`](../../artifacts/incident-record.md).
8. Restoring reduced authority is a promotion: do not restore it here; hand off to [`skills/34-manage-authority-promotion/SKILL.md`](../34-manage-authority-promotion/SKILL.md), which records the `HG-AUTHORITY` Decision (listing the AUT-### and stating level and scope).
9. Stop with `INSUFFICIENT_EVIDENCE` when the cause cannot be established without invented facts (keep the incident open; record Evidence Debt), or `BLOCKED` when a required input is missing.

## MUST NOT

- wait for a gate or an approval before reducing authority when a demotion trigger fires;
- restore authority without an approved `HG-AUTHORITY` Decision;
- close, downgrade, or omit an incident to avoid its consequences;
- copy personal or confidential content into the record ([`evidence/EVIDENCE_STANDARD.md`](../../evidence/EVIDENCE_STANDARD.md) §8).

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
