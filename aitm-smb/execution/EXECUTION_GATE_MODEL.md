# Execution Gate Model

## 1. Purpose

Execution gates prevent uncontrolled progression from idea to production autonomy.

They are evidence checkpoints on an Initiative. They do not replace the human decision gates (`STANDARD.md` §8); where passing a gate needs such an approval, the gate names it (§2).

Execution Gate records (`GAT-###`) are required under the Governed profile; other profiles MAY use them or carry gates in the Initiative `decision_gates` (`EXECUTION_MODEL.md` §2).

---

## 2. Standard gates

### Gate A — Diagnosis Ready

Gap and cause are sufficiently understood.

### Gate B — Design Approved

Intervention and Target State approved.

### Gate C — Pilot Ready

Pilot scope, evidence, guardrails, metrics, and rollback defined.

### Gate D — Pilot Passed

Pre-defined success criteria met; otherwise promotion requires a recorded waiver (§4).

### Gate E — Rollout Ready

Rollout gates in `execution/ROLLOUT_MODEL.md` §3 verified.

### Gate F — Operational

Target scope runs under approved operating model.

### Gate G — Value Confirmed

Value conclusion `VALUE_CONFIRMED`, with value state REALIZED or SUSTAINED (`measurement/VALUE_REALIZATION.md` §2, §6).

### Gate map

| Gate | Human gate needed to pass (`STANDARD.md` §8) |
|---|---|
| A | — |
| B | `HG-TOA`; `HG-DECISION-RIGHTS` where Decision Rights change |
| C | `HG-AUTHORITY` where the pilot runs above the approved autonomy level; `HG-RISK` where material risk is accepted |
| D | `HG-PROMOTION` for a material pilot |
| E | `HG-AUTHORITY` where the rollout stage raises the autonomy level; `HG-RISK` where material risk is accepted |
| F | — |
| G | `HG-VALUE` |

The phase in which each gate typically falls: `EXECUTION_MODEL.md` §2. Gate E is checked before each rollout stage. Any other `STANDARD.md` §8 gate applies whenever its trigger occurs. Named custom gates MAY be added; they follow §3 and §4.

---

## 3. Gate record

Record contract: `artifacts/execution-gate.md` (`GAT-###`).

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

The waiver is a Decision (`DEC-###`, `artifacts/decision-assumption-log.md`) referenced by the gate record.
