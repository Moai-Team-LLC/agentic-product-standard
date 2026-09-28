# Agentic Autonomy Suitability

## 1. Purpose

AITM-SMB separates:

```text
AI usefulness
from
AI authority
```

A task may be a strong AI fit but a poor autonomy fit.

---

## 2. Autonomy ladder

```text
L0 — No AI
L1 — Suggest
L2 — Draft
L3 — Execute with explicit approval
L4 — Execute within bounded policy
L5 — Pursue bounded objective and escalate exceptions
```

This file is the only place where the authority of each level is defined:

| Level | Authority |
|---|---|
| L0 | No AI component in the decision or action path. |
| L1 | AI produces recommendations or insights; a human decides and performs the action. |
| L2 | AI produces a draft work product; a human reviews, edits if needed, and releases it; nothing takes effect without human release. |
| L3 | AI prepares a specific action; the system executes it only after a human approves that action. |
| L4 | AI executes actions without per-action approval inside an explicit, written policy (action types, limits, scope); out-of-policy cases escalate; actions are observable and reversible or recoverable. |
| L5 | AI plans and executes multi-step work toward an approved, bounded objective within bounded permissions, budget, and time; exceptions escalate; humans supervise outcomes, not each step. |

The level is assessed per action class of a Capability, not per system.

These are authority levels. They are not maturity levels ([`maturity/MATURITY_MODEL.md`](../maturity/MATURITY_MODEL.md) uses M0–M5) and not software-architecture levels. Where another ladder is in use, such as the Agentic Product Standard's architecture levels, write `AITM-L3` versus `APS-L3` (crosswalk: [`docs/crosswalk-agentic-product-standard.md`](../docs/crosswalk-agentic-product-standard.md)).

Any level above L0 is granted only through `HG-AUTHORITY` ([`STANDARD.md`](../STANDARD.md) §8). The currently approved level of an action class is its Autonomy Assessment `current_level`; the Authority Ceiling (§6) bounds it.

Expanding the scope in which an approved level operates (more users, cases, or volume) with the same action class, level, and ceiling is rollout ([`execution/ROLLOUT_MODEL.md`](../execution/ROLLOUT_MODEL.md), `HG-PROMOTION`), not an authority increase.

Profile selection classifies AI authority from these levels ([`APPLICATION_PROFILES.md`](../APPLICATION_PROFILES.md) §2).

---

## 3. Autonomy dimensions

Evaluate:

```text
Action Reversibility
Financial Impact
Customer Impact
Legal Impact
Security Impact
Safety Impact
Decision Ambiguity
Policy Clarity
Observability
Verification Quality
Exception Detectability
Recovery Quality
Identity / Permission Precision
```

Rate each dimension `low | medium | high` with a short note; mark a dimension that does not apply `not_relevant`, with the reason in the note. Each dimension has one field in the record (§7).

---

## 4. Autonomy-positive conditions

Higher autonomy is more defensible when:

```text
actions are reversible
impact is bounded
policy is explicit
exceptions are detectable
outputs are observable
quality can be evaluated
recovery is reliable
permissions are narrow
```

---

## 5. Autonomy-negative conditions

Lower autonomy is preferred when:

```text
actions are irreversible
financial commitment is material
legal rights are affected
safety risk exists
identity or permissions are ambiguous
evaluation is weak
failure may remain invisible
exceptions are common
```

---

## 6. Authority ceiling

An Authority Ceiling is the highest autonomy level, with its prohibited actions, approval requirements, escalation conditions, and accountable owner, approved for an action class of a Capability.

Each Capability in which AI is used or proposed SHOULD have one. Where an `AI_*` Intervention is selected, an approved Authority Ceiling is required in every profile ([`APPLICATION_PROFILES.md`](../APPLICATION_PROFILES.md)).

Rules:

- Setting or raising a ceiling is an authority increase: `HG-AUTHORITY` ([`STANDARD.md`](../STANDARD.md) §8). Lowering it is a demotion and needs no gate. An L0 ceiling grants nothing and needs no gate.
- Every Decision closing `HG-AUTHORITY` lists the `AUT-###` in `subject_ids` (a `PLT-###` or `ROL-###` MAY be listed as context) and states the new level and its scope in `statement`. One Decision MAY both set the ceiling and raise `current_level` when its statement says both. Grants follow [`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md) §3.
- In Phase 3 the ceiling is proposed; `HG-AUTHORITY` is needed only for an `AI_*` candidate proposed for selection. An `AI_*` Intervention is not selected (Phase 4) before its ceiling is approved.
- No technical implementation, pilot, rollout stage, or promotion may exceed the approved ceiling.
- A recommended or operating level above the ceiling requires re-assessing the ceiling first.

Record: the ceiling fields of the Autonomy Assessment ([`artifacts/autonomy-assessment.md`](../artifacts/autonomy-assessment.md)).

---

## 7. Autonomy assessment

One assessment per `AI_*` Intervention and action class. It records the §3 dimensions, the recommended level, the Authority Ceiling (§6), and, after promotion or demotion reviews ([`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md)), the level in operation.

Record contract: [`artifacts/autonomy-assessment.md`](../artifacts/autonomy-assessment.md).
