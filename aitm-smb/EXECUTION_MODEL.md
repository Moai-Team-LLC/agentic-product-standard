# AITM-SMB Execution Model

**Version:** 1.0.0

AITM-SMB is sequential in dependency but iterative in execution.

---

## 1. Canonical lifecycle

```text
0 Frame
1 Observe
2 Diagnose
3 Design Interventions
4 Decide
5 Design Target System
6 Design Transition
7 Operationalize
8 Measure & Evolve
```

The detailed phase files live under `methodology/`.

---

## 2. Phase gates

| Phase | Exit condition |
|---:|---|
| 0 Intent | Outcome, owner, baseline/known baseline gap, target, horizon, constraints |
| 1 Current System | relevant Current State and Capabilities evidence-backed |
| 2 Diagnosis | material Gaps and Causes explicit |
| 3 Intervention | alternatives considered; AI justified where used |
| 4 Prioritization | material Initiative selection approved |
| 5 Target Design | Capability Target States + coherent Target Operating Architecture |
| 6 Transition | operable Transition States, dependencies, evidence gates |
| 7 Operations | ownership, governance, observability, adoption, recovery |
| 8 Measurement | effect evaluated and architecture updated from Evidence |

---

## 3. Iteration

Later Evidence MAY invalidate earlier assumptions.

Examples:

```text
AI assessment reveals deterministic rule is sufficient
→ return to Intervention Design

Target design reveals unavailable knowledge
→ return to Diagnosis / Intervention

Pilot disproves causal hypothesis
→ return to Diagnosis

Rollout creates new System Constraint
→ revise Target / Portfolio
```

Iteration is expected.

Silent semantic drift is not.

---

## 4. Human gates

See `STANDARD.md`.

Agents MUST stop when a required human gate remains open.

---

## 5. Evidence gates

The correct result MAY be:

```text
INSUFFICIENT_EVIDENCE
```

when proceeding would require invented business facts.

---

## 6. Minimum valid path

Even a Compact application preserves:

```text
Outcome
→ Capability
→ Gap
→ Intervention
→ Initiative
→ Target State
→ Metric
→ Evidence
```

Artifacts may be merged; semantic layers may not.
