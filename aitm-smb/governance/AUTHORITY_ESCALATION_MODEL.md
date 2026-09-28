# Authority Escalation Model

## 1. Purpose

AITM-SMB increases AI authority only after demonstrated evidence, and reduces it as soon as evidence requires.

Authority is set per action class of a Capability. Levels and the authority each grants: `diagnostics/AUTONOMY_SUITABILITY.md` §2.

---

## 2. Authority promotion path

```text
L1 — Suggest
→ L2 — Draft
→ L3 — Execute with explicit approval
→ L4 — Execute within bounded policy
→ L5 — Pursue bounded objective and escalate exceptions
```

The path starts from L0 (No AI); granting L1 is the first promotion.

Authority SHOULD NOT jump directly to the maximum technically possible level (`transition/TRANSITION_STATE_MODEL.md` §7).

A promotion MUST NOT exceed the approved Authority Ceiling (`diagnostics/AUTONOMY_SUITABILITY.md` §6; `maximum_allowed_level` in `artifacts/autonomy-assessment.md`). A higher level requires re-assessing the ceiling first.

---

## 3. Promotion criteria

Before increasing authority verify:

```text
task quality stable
failure modes understood
observability sufficient
policy enforcement sufficient
recovery tested
permissions bounded
incident rate acceptable
business value demonstrated
```

Evidence comes from Evaluation records (`EVL-###`), incident history (`INC-###`), and operating signals.

A promotion also requires:

```text
target level within the approved Authority Ceiling (maximum_allowed_level)
AND a Decision closing HG-AUTHORITY (STANDARD.md §8) that names the Autonomy Assessment (AUT-###) and the new level
```

Until that Decision is approved, a promotion is a proposal and the level in operation does not change.

Where AI Change Control applies (Governed), the promotion is also an AI Change of class High (`governance/AI_CHANGE_CONTROL.md` §2).

---

## 4. Demotion

Authority MUST be reducible.

Triggers may include:

```text
quality degradation
unexpected cost
new failure class
policy change or policy violation
knowledge drift
model/provider change
security incident
AUTHORITY, POLICY, TOOL_ACTION or STATE_INTEGRITY incident (operations/INCIDENT_MODEL.md §2)
a promotion criterion (§3) no longer met
```

Demotion needs no human gate (`STANDARD.md` §8). When a trigger fires, the operating owner, or an agent acting for the owner under incident handling, MAY reduce authority immediately, down to pausing the AI component (L0).

Restoring authority after a demotion is a promotion (§3) and requires `HG-AUTHORITY`.

---

## 5. Rule

Autonomy is a revocable operating privilege, not a permanent maturity achievement.

---

## 6. Record

A promotion or demotion is recorded as:

```text
the level in operation, the recommendation and the reason in the Autonomy Assessment (artifacts/autonomy-assessment.md)
a Decision (DEC-###): for a promotion, the HG-AUTHORITY approval; for a demotion, a record made afterwards (SHOULD)
an AI Change record (CHG-###, artifacts/ai-governance-canvas.md) where AI Change Control applies
```
