# Pilot Model

## 1. Purpose

A Pilot is a bounded operational test of a transformation hypothesis under real or production-representative conditions.

A pilot is not:

```text
demo
prototype
proof that the model can respond
```

It must test business-system behavior.

Pilots are designed in Phase 6 with a pre-registered evaluation, and run, evaluated and decided in Phase 7 ([`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §1).

---

## 2. Pilot record

Record contract: [`artifacts/pilot-plan.md`](../artifacts/pilot-plan.md) (`PLT-###`).

A pilot states the Initiative and Hypotheses it tests, its type (§3) and autonomy level, its scope (§4), baseline and comparison, metrics, risks and guardrails, rollback, success and stop criteria, evidence plan, and owner.

Its evaluations are pre-registered in the Evaluation Plan ([`artifacts/evaluation-plan.md`](../artifacts/evaluation-plan.md), [`evaluation/EVALUATION_SYSTEM.md`](../evaluation/EVALUATION_SYSTEM.md)) before the pilot runs.

---

## 3. Pilot types

### Shadow Pilot

`pilot_type: shadow`

New behavior runs without controlling production action.

Use for:

```text
quality evaluation
recommendation quality
routing accuracy
prediction
policy compliance
```

### Assisted Pilot

`pilot_type: assisted`

AI or new system assists humans while humans retain authority.

### Controlled Execution Pilot

`pilot_type: controlled_execution`

System executes within a small bounded domain with explicit approval or policy.

### Limited Autonomous Pilot

`pilot_type: limited_autonomous`

Agentic execution is allowed within narrow permissions and strong observability.

### Authority in pilots

The pilot type does not set authority; the pilot's autonomy level does ([`diagnostics/AUTONOMY_SUITABILITY.md`](../diagnostics/AUTONOMY_SUITABILITY.md) §2).

A pilot MUST NOT exceed the approved Authority Ceiling ([`diagnostics/AUTONOMY_SUITABILITY.md`](../diagnostics/AUTONOMY_SUITABILITY.md) §6). Running a pilot above the currently approved level (AUT `current_level`) is an authority increase: it needs the pilot-grant criteria of [`governance/AUTHORITY_ESCALATION_MODEL.md`](../governance/AUTHORITY_ESCALATION_MODEL.md) §3 (a) and `HG-AUTHORITY` ([`STANDARD.md`](../STANDARD.md) §8) before the pilot starts.

---

## 4. Pilot scope

A pilot SHOULD constrain some combination of:

```text
users
customers
transactions
geography
workflow type
risk class
time window
autonomy level
```

---

## 5. Pilot validity

A pilot is invalid if:

```text
success criteria are defined after results
baseline is absent without acknowledged evidence debt
production behavior differs materially from test behavior
participants can bypass the intended workflow without measurement
or only AI-quality metrics are observed
```

---

## 6. Pilot result

```text
PROMOTE
REVISE
REPEAT
STOP
INSUFFICIENT_EVIDENCE
```

These are result values, not agent statuses ([`PUBLIC_API.md`](../PUBLIC_API.md) §8). The result is recorded as `pilot_result` in the Evaluation Plan.

PROMOTE is a recommendation. Promoting a material pilot to rollout requires `HG-PROMOTION` ([`STANDARD.md`](../STANDARD.md) §8); Governed: Execution Gate D ([`execution/EXECUTION_GATE_MODEL.md`](EXECUTION_GATE_MODEL.md)).

Unmet success criteria never yield PROMOTE. The owner MAY still promote, but only through the `HG-PROMOTION` Decision, which then records the waiver ([`execution/EXECUTION_GATE_MODEL.md`](EXECUTION_GATE_MODEL.md) §4).
