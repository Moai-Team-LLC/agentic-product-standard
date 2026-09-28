# Decision Rights Architecture

## 1. Purpose

AI transformation changes not only tasks but who is allowed to decide.

Decision Rights Architecture makes this explicit for operational business decisions (`BDS-###`). Engagement decisions about the transformation itself are `DEC-###` (`DECISION_MODEL.md`).

---

## 2. Decision record

Business Decision records (`BDS-###`): record contract `artifacts/decision-rights-map.md`.

Each record names the accountable decision owner, the current and target authority model (§3), and, where AI takes part, the Autonomy Assessment whose Authority Ceiling bounds it.

---

## 3. Authority models

Each authority model corresponds to one autonomy level (`diagnostics/AUTONOMY_SUITABILITY.md` §2):

| Authority model | Autonomy level |
|---|---|
| `HUMAN` | L0 — No AI |
| `HUMAN_WITH_AI` (AI informs the human's work) | L1 — Suggest |
| `AI_RECOMMENDS_HUMAN_DECIDES` | L1 — Suggest |
| `AI_DRAFTS_HUMAN_APPROVES` | L2 — Draft |
| `AI_EXECUTES_WITH_APPROVAL` | L3 — Execute with explicit approval |
| `AI_EXECUTES_WITHIN_POLICY` | L4 — Execute within bounded policy |
| `AGENT_PURSUES_BOUNDED_OBJECTIVE` | L5 — Pursue bounded objective and escalate exceptions |

The authority of each level is defined only in `diagnostics/AUTONOMY_SUITABILITY.md` §2; the model names do not change it.

Rules:

- The level of a target authority model MUST NOT exceed the approved Authority Ceiling (`maximum_allowed_level` in `artifacts/autonomy-assessment.md`) for that Capability and action class.
- Changing a material Decision Right requires `HG-DECISION-RIGHTS`; a change that raises AI authority also requires `HG-AUTHORITY` (`STANDARD.md` §8). Lowering AI authority needs no gate.
- Every decision keeps a human decision owner, also at L4 and L5: the role accountable for outcomes and exceptions.

---

## 4. Decision decomposition

Large decisions often contain smaller decisions.

Example:

```text
"approve proposal"
```

may decompose into:

```text
validate completeness
calculate price
check margin
check legal terms
approve exception
send commitment
```

Some sub-decisions may be automated while others remain human. Each sub-decision is its own record, linked to the compound decision.

---

## 5. Principle

Do not automate the label of a decision.

Decompose the actual authority structure.
