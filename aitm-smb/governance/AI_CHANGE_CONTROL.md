# AI Change Control

## 1. Purpose

AI system behavior can change even when business code does not.

Change control SHOULD consider:

```text
model
provider
prompt
system instruction
retrieval logic
knowledge corpus
toolset
permission scope
evaluation rubric
workflow
memory behavior
```

---

## 2. Change classes

### Low

Small reversible change with low business impact.

Default handling (SHOULD): owner approval; spot-check after release.

### Medium

Change that may affect quality, cost, or workflow behavior.

Default handling (SHOULD): re-run the affected evaluations before release; owner approval.

### High

Change affecting:

```text
authority
critical customer behavior
financial decisions
security
data access
legal exposure
high-risk process
```

Default handling (SHOULD): evaluation before release, staged rollout ([`execution/ROLLOUT_MODEL.md`](../execution/ROLLOUT_MODEL.md)), and explicit human approval.

An authority increase follows [`governance/AUTHORITY_ESCALATION_MODEL.md`](AUTHORITY_ESCALATION_MODEL.md) and requires `HG-AUTHORITY`; accepting material risk requires `HG-RISK` ([`STANDARD.md`](../STANDARD.md) §8).

The governance owner MAY set stricter handling per Capability.

---

## 3. Change record

```yaml
ai_change:
  id: CHG-###
  capability_id:
  component:                # a §1 item
  class: low | medium | high   # §2
  reason:
  expected_effect:
  evaluation_required:
  evaluation_ids: []        # EVL-### run for this change
  rollout_required:
  approval_required:
  approver:                 # human who approves the change
  decision_id:              # DEC-### when a STANDARD.md §8 gate applies
  rollback:
  evidence_ids: []
  owner:
  status: proposed | approved | rejected | released | rolled_back
```

Instances: the `changes` section of [`artifacts/ai-governance-canvas.md`](../artifacts/ai-governance-canvas.md).

---

## 4. Rule

A model upgrade is not automatically a low-risk change.
