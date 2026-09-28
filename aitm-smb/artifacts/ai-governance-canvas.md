---
artifact_type: ai-governance-canvas
framework_version: 1.1.0
status: canonical
owner_module: governance/GOVERNANCE_OPERATING_MODEL.md
produced_by: [08-design-operating-model, 09-measure-evolution, 31-operationalize-governance, 34-manage-authority-promotion]
---

# AI Governance Canvas

## Purpose

Define authority, control, accountability, cost boundaries, and failure handling for an AI-enabled Capability, and log the changes made to its AI components ([`governance/GOVERNANCE_OPERATING_MODEL.md`](../governance/GOVERNANCE_OPERATING_MODEL.md)). One canvas per AI-enabled Capability, where the profile requires it.

## Record

Record contract for `changes`: AI Change [`governance/AI_CHANGE_CONTROL.md`](../governance/AI_CHANGE_CONTROL.md) §3.

```yaml
governance:
  capability_id:            # CAP-###
  outcome_ids: []           # OUT-### the Capability serves
  owner:                    # accountable owner
  risk_owner:               # named risk owner (Governed)
  risk_ids: []              # RSK-### (artifacts/decision-assumption-log.md) for this Capability's AI use
  authority_ceiling_ids: [] # AUT-### whose Authority Ceiling bounds this Capability, one per action class
  ai_role:
  human_role:
  data_access:
  tool_access:
  permissions:
  prohibited_actions:
  approval_required:
  escalation_conditions:
  stop_conditions:          # when execution must stop
  evaluation_method:
  audit_evidence:           # what is logged and retained
  failure_mode:
  recovery_path:
  cost_limit:               # cost boundary

changes: []                 # AI Change records (CHG-###)
```

Required fields by profile ([`APPLICATION_PROFILES.md`](../APPLICATION_PROFILES.md)), where AI is used: Compact — the Governance minimum `owner`, `permissions`, `prohibited_actions`, `approval_required`, `escalation_conditions`, `recovery_path`; Standard — all fields except `risk_owner` and `risk_ids`; Governed — all fields, with a named risk owner. The link fields `capability_id`, `outcome_ids`, and `authority_ceiling_ids` are always filled.

## Rules

The canvas MUST NOT permit what a referenced Authority Ceiling prohibits or leaves to approval ([`diagnostics/AUTONOMY_SUITABILITY.md`](../diagnostics/AUTONOMY_SUITABILITY.md) §6). Authority changes follow [`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md).

## Required questions

1. What may AI see?
2. What may AI infer?
3. What may AI recommend?
4. What may AI change?
5. What requires human approval?
6. What triggers escalation?
7. When must execution stop?
8. What is logged, and what evidence must be retained?
9. How is output quality evaluated?
10. Who owns failure?
11. How can the action be reversed or recovered?
12. What is the cost boundary?

## Validation

- [ ] linked to one Capability, its Outcomes, and the Authority Ceilings that bound it
- [ ] the fields the active profile requires are filled (Required fields above): Compact — the six Governance minimum fields; Standard — every field except `risk_owner` and `risk_ids`; Governed — every field
- [ ] owner is named; Governed: a risk owner is named, and material AI risks are Risk records (`RSK-###`) listed in `risk_ids`
- [ ] permissions, prohibited actions, approval, escalation, and recovery path are explicit and within the ceilings
- [ ] every AI Change has a class ([`governance/AI_CHANGE_CONTROL.md`](../governance/AI_CHANGE_CONTROL.md) §2), and a High change that increases authority has an `HG-AUTHORITY` Decision
