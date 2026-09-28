# Execution Gate Model

## 1. Purpose

Execution gates prevent uncontrolled progression from idea to production autonomy.

They are evidence checkpoints on an Initiative. They do not replace the human decision gates ([`STANDARD.md`](../STANDARD.md) §8); where passing a gate needs such an approval, the gate names it (§2).

Execution Gate records (`GAT-###`) are required under the Governed profile; other profiles MAY use them or carry gates in the Initiative `decision_gates` ([`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2).

---

## 2. Standard gates

### Gate A — Diagnosis Ready

Gap and cause are sufficiently understood: the Initiative's Gaps meet the Phase 2 readiness condition ([`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2). Recorded at selection.

### Gate B — Design Approved

Intervention and Target State approved.

### Gate C — Pilot Ready

Pilot scope, evidence, guardrails, metrics, and rollback defined.

### Gate D — Pilot Passed

Pre-defined success criteria met. Unmet criteria never yield `pilot_result` PROMOTE; the owner MAY still promote, but only through the `HG-PROMOTION` Decision, which then records the waiver (§4).

### Gate E — Rollout Ready

Rollout gates in [`execution/ROLLOUT_MODEL.md`](ROLLOUT_MODEL.md) §3 verified.

### Gate F — Operational

Target scope runs under approved operating model.

### Gate G — Value Confirmed

Value conclusion `VALUE_CONFIRMED`, with value state REALIZED or SUSTAINED ([`measurement/VALUE_REALIZATION.md`](../measurement/VALUE_REALIZATION.md) §2, §6).

### Gate map

| Gate | Human gate needed to pass ([`STANDARD.md`](../STANDARD.md) §8) |
|---|---|
| A | — |
| B | `HG-TOA`; `HG-DECISION-RIGHTS` where Decision Rights change |
| C | `HG-AUTHORITY` where the pilot runs above the currently approved level (AUT `current_level`); `HG-RISK` where material risk is accepted |
| D | `HG-PROMOTION` for a material pilot |
| E | `HG-AUTHORITY` where the rollout stage raises the autonomy level; `HG-RISK` where material risk is accepted |
| F | — |
| G | `HG-VALUE` |

A gate passes only when every human gate that applies to it is approved. The phase in which each gate typically falls: [`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2; records are kept per Initiative once it exists (Gate A at selection, Gate B after `HG-TOA`). Gate E is checked before each rollout stage. Any other [`STANDARD.md`](../STANDARD.md) §8 gate applies whenever its trigger occurs. Named custom gates MAY be added; they follow §3 and §4.

---

## 3. Gate record

Record contract: [`artifacts/execution-gate.md`](../artifacts/execution-gate.md) (`GAT-###`).

The approver is a human. An agent records the evidence provided and proposes a status; it does not pass or waive a gate.

---

## 4. Waiver

A gate MAY be waived only by an explicit human decision with:

```text
reason
risk
owner
expiration or review trigger
```

The waiver is a Decision (`DEC-###`, [`artifacts/decision-assumption-log.md`](../artifacts/decision-assumption-log.md)) referenced by the gate record. Unmet pilot success criteria are waived in the `HG-PROMOTION` Decision, in every profile; under Governed, the Gate D record references it.
