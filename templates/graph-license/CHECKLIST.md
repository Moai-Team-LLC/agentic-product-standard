# The Graph License — one-page checklist

*From [The Agentic Product Standard](../../STANDARD.md), Part IV (*License Composition*). Run this against a real deployment, with the team in the room, before a **graph of agents** runs unattended (Autonomy Ladder L3+). Every box is binary — a half-met control is a No.*

**This checklist assumes the [Loop License](../loop-license/CHECKLIST.md), it does not replace it.** Each unattended node holds its own; this page asks the question the per-node licenses cannot answer: *is the composition licensed?* A graph of licensed loops is **not** licensed by virtue of the wiring.

## 1. Per-node inventory

One row per node. A node with no license is not disqualifying on its own — it is what the weakest-link bound (§3) is for.

| Node | What it does | Autonomy level | Loop License? | Judge calibrated? | Blast radius |
|---|---|---|---|---|---|
| | | L_ | Yes / No / n/a (deterministic) | Yes / No / n/a | |

- [ ] Every node in the running topology appears in this table — including deterministic steps and any node added "temporarily".
- [ ] Every node marked *deterministic* genuinely is: no model call anywhere on its path.

## 2. The six gates at graph scope

- [ ] **1. Graph-level eval threshold.** A named pass rate on **end-to-end golden tasks for the graph**, not the union of per-node suites. State the number and the set. *(Nodes that each pass in isolation routinely fail in composition — that gap is the reason this gate exists.)*
- [ ] **2. Regression gate** on the graph-level set, blocking promotion in CI.
- [ ] **3. Declared blast radius** = the **union** of every node's radius **plus the shared state store**. Written down; enforced below the model.
- [ ] **4. Cost caps — per-node *and* aggregate.** Fan-out multiplies burn; per-node caps alone do not bound a graph.
- [ ] **5. Kill switch that halts *all* nodes**, verified against **in-flight parallel branches** — not only against nodes waiting to start. Record the test below.
- [ ] **6. One escalation path, one named owner** for the graph as a whole. *(If each node escalates to its own owner, the graph has no owner.)*

## 3. Path analysis — the weakest-link bound

For **every path that ends in an external action** (a write, a send, a payment, a deploy, a public post):

| Path (node → node → action) | Nodes on it | Weakest link (min licensed level) | Declared level | OK? |
|---|---|---|---|---|
| | | L_ | L_ | declared ≤ weakest |

- [ ] Every external action in the system is traced to at least one path in this table.
- [ ] **No path declares an autonomy level above its weakest link.** An unlicensed node — or one gated by an uncalibrated judge — anywhere on the path caps that path at **L2** (propose-approve).

## 4. Shared state — provenance

- [ ] Every shared-state field carries **writer provenance**: producing node, timestamp, verification status.
- [ ] Verification status is one of `verified_by: <check|judge>` or `unverified` — no implicit third state, no absent field read as "fine".
- [ ] Consumers **can filter on verification status** (it is queryable, not merely present).
- [ ] **No action node triggers an external action from an `unverified` field.** Asserted by a test, not by convention.

## 5. Fan-in points

One row per merge point where parallel branches join.

| Merge point | Branches in | Verification point or pass-through? | Method (deterministic check / calibrated judge) or rationale |
|---|---|---|---|
| | | | |

- [ ] Every fan-in is declared **either** a verification point **or** an explicit pass-through with written rationale. Undeclared merges are the finding.
- [ ] **No unverified aggregation sits upstream of an external action.** *(Merging does not add correctness; aggregating parallel outputs and treating the result as validated is self-verification wearing a topology.)*

## 6. Edges

- [ ] Inter-node handoffs are treated as **ingestion boundaries** — a node's output is untrusted input downstream.
- [ ] The graph eval suite contains **poisoned-state scenarios**: a compromised or hallucinating node writing to shared state, asserting that downstream nodes do not act on it.
- [ ] **Reviewer nodes are judges** — calibrated, bias-tested, and decorrelated **from each producer they review** (per edge, not once per graph).

## 7. Topology enforcement

| Edge class | Route | **Enforced** (code/runtime constrains it) or **declared** (SOP / skill / prompt) |
|---|---|---|
| | | |

- [ ] Every edge class is marked.
- [ ] **No declared-only edge is counted as a control** in this license or any node's. A topology that exists only in prose is documentation, not a guardrail (Principle 6; the graph-scale form of DoD 5, *permissions enforced by code, not by prompt*).

## 8. Kill-switch test record

| Date | Who ran it | Nodes running at trigger | In-flight parallel branches? | All halted within | Result |
|---|---|---|---|---|---|
| | | | Yes / No | \_\_ s | Pass / Fail |

- [ ] Tested this release, with parallel branches genuinely in flight.

## 9. Escalation owner

- [ ] **Named human (or higher-authority system):** ______________________
- [ ] Reachable out-of-band, through a channel no node in the graph can write to.

---

**Scoring.** All boxes Yes → the graph is licensed for unattended L3+ operation, this release. The first No is your next piece of work. Re-run every release; the score should only ratchet up.

*Definition of Done item 25 maps to this checklist; items 16–19 map to the [Loop License](../loop-license/CHECKLIST.md) each node still owes. The reference implementations of enforcement and measurement are the [AgenticProduct family](../../ECOSYSTEM.md) — paved road, not a mandate (Principle 2).*
