# Which agent architecture should you actually build?

*From [The Agentic Product Standard](../../STANDARD.md). One page, from "we want an agent" to a named architecture **and the license it owes**.*

The viral version of this question stops at the architecture. That is the easy half: picking a shape is a whiteboard decision, and every shape works in a demo. The half that decides whether the thing survives production is **what the shape owes** — which failure modes it invites, what permission tier it needs, what its eval plan has to cover, and which license it must hold before it runs without a human watching. This tree carries both columns to every leaf.

It is **derived from** the [10-question checklist](../../README.md#-the-10-question-checklist), which stays the single source of truth. A CI check fails if the canon changes and this page does not.

---

## The tree

```mermaid
flowchart TD
    Q1["<b>Q1.</b> What is the minimum autonomy level<br/>(L0–L4) that solves this?"]
    Q1 -->|"L0–L1: fixed steps,<br/>model does one bounded job"| A["<b>A · Deterministic pipeline</b><br/>or a single LLM call"]
    Q1 -->|"L2+: the path varies<br/>with the input"| Q2

    Q2["<b>Q2.</b> Can it be solved by composing the<br/>5 patterns, without a full agent loop?"]
    Q2 -->|"Yes — chaining, routing,<br/>parallelization, evaluator,<br/>orchestrator"| B["<b>B · Workflow composition</b><br/>fixed topology, no open-ended loop"]
    Q2 -->|"No — the agent must decide<br/>its own next step"| Q3

    Q3["<b>Q3.</b> Breadth-first (parallelizable)<br/>or depth-first (coherent)?"]
    Q3 -->|"Depth-first: one coherent<br/>artifact or thread"| Q4
    Q3 -->|"Breadth-first: independent<br/>subtasks, genuinely parallel"| Q5

    Q4["<b>Q4.</b> Does it run unattended —<br/>finding its own work, looping<br/>without a human each turn?"]
    Q4 -->|No| C["<b>C · Single agent, L2</b><br/>human approves each external action"]
    Q4 -->|Yes| D["<b>D · Single unattended agent, L3+</b>"]

    Q5["<b>Q5.</b> Does every extra node clear<br/>its <i>own</i> verification bar?"]
    Q5 -->|"No — cannot verify a node<br/>independently yet"| C
    Q5 -->|Yes| Q6

    Q6["<b>Q6.</b> Does it run unattended?"]
    Q6 -->|No| E["<b>E · Graph, L2</b><br/>orchestrator + subagents,<br/>human approves external actions"]
    Q6 -->|Yes| F["<b>F · Unattended graph, L3+</b>"]

    A --> LA["No license.<br/>DoD 1–15 · 24"]
    B --> LB["No license.<br/>DoD 1–15 · 24"]
    C --> LC["No license.<br/>DoD 1–15 · 24"]
    D --> LD["<b>Loop License</b> — six gates<br/>DoD 16–19 + oversight plan"]
    E --> LE["No license, but the<br/><b>weakest-link bound</b> already applies<br/>DoD 1–15 · 24"]
    F --> LF["<b>Loop License</b> per unattended node<br/><b>+ Graph License</b><br/>DoD 16–19 · 25"]

    classDef leaf fill:#e8f0fe,stroke:#3367d6,stroke-width:2px,color:#111
    classDef lic fill:#fff4e5,stroke:#d97757,stroke-width:2px,color:#111
    class A,B,C,D,E,F leaf
    class LA,LB,LC,LD,LE,LF lic
```

---

## The leaves — architecture **and** what it owes

| Leaf | Architecture | License required | Checklist | DoD |
|---|---|---|---|---|
| **A** | Deterministic pipeline, or a single LLM call inside fixed steps | None | — | 1–15 · 24 |
| **B** | Workflow composition — the [five patterns](../../STANDARD.md#canon-2-the-five-composition-patterns) with a fixed topology and no open-ended loop | None | — | 1–15 · 24 |
| **C** | Single agent, L2 — the agent decides its next step; a human approves every external action | None | — | 1–15 · 24 |
| **D** | Single agent running **unattended** at L3+ | **Loop License** | [`loop-license/CHECKLIST.md`](../loop-license/CHECKLIST.md) | + 16–19, + oversight plan |
| **E** | Graph of agents at L2 — orchestrator plus subagents, human approves external actions | None — but the **weakest-link bound** already governs any path you later promote | [`graph-license/CHECKLIST.md`](../graph-license/CHECKLIST.md) (as a design aid) | 1–15 · 24 |
| **F** | Graph of agents running **unattended** at L3+ | **Loop License per unattended node** *and* a **Graph License** for the composition | [`graph-license/CHECKLIST.md`](../graph-license/CHECKLIST.md) | + 16–19 · 25 |

**Leaf F is the one people get wrong.** A graph of licensed loops is *not* a licensed graph — the risks that hurt are the ones no single node owns (Part IV, *License Composition*; anti-pattern 19).

---

## The governance column, per leaf

The four questions the architecture genre skips. Answer them at the same whiteboard, not after the incident.

| Leaf | Failure modes to name first | Permission tier | Eval plan must cover | License |
|---|---|---|---|---|
| **A** | Bad parse, schema drift, silent fallback | Read-mostly; writes behind code | Unit + schema; a handful of end-to-end cases | — |
| **B** | Wrong branch taken; a stage passing junk downstream | Per-stage least privilege | Per-stage cases **and** the composed path | — |
| **C** | Wrong tool, wrong target, context exhaustion | Every external action approved by a human | ≥50 cases per named failure mode; judges calibrated | — |
| **D** | Runaway loop, unbounded spend, hijack via "find work" | Blast radius declared and enforced below the model | The above **plus** injection cases on the find-work path | **Loop License** |
| **E** | Handoff loses context; a node acting on another's unverified output | Per-node least privilege; external actions human-approved | Per-node **plus** end-to-end graph tasks | — |
| **F** | Everything in D and E, plus: fan-out multiplying spend past per-node caps; unverified aggregation at fan-in; an uncalibrated node lending a path autonomy it never earned; a kill switch that never met an in-flight branch | Blast radius = union of node radii **plus** the shared state store | Graph-level golden tasks; **poisoned-state** scenarios; per-edge judge decorrelation | **Loop + Graph License** |

---

## The loop-vs-graph branch, in our terms

Q5 is the branch the market argues about. Reasons to add a node, stated as things you must be able to *show*, not prefer:

- **Specialty handoff** — a subtask needs a materially different skill, and you can name the boundary.
- **Genuine fan-out** — subtasks are independent, and parallelism buys wall-clock you actually need.
- **Per-step model or toolset** — a step wants a different model tier or a tool surface the others must not hold.
- **Auditable routing** — you need to see *which* path a request took, as a first-class record.
- **Failure isolation** — one subtask failing must not take the others with it.
- **A dedicated reviewer** — verification wants its own contract, decorrelated from the producer.

> **The exit criterion: every extra node must clear its own verification bar.** If you cannot say how a node is independently verified — deterministically where possible, by a calibrated and decorrelated judge otherwise — it is not a node yet. Adding it converts an evaluable system into an unevaluable one, which is anti-pattern 1 (multi-agent before a single-agent baseline) wearing a topology.

---

## Derivation from the canon

This tree asks a subset of the [10-question checklist](../../README.md#-the-10-question-checklist) as branch conditions; the rest are carried in the governance column above, because they shape *how* you build the leaf rather than *which* leaf you land on. The canon is the single source of truth — this page is a surface over it, and CI fails if they drift apart.

| Canon question | Where it lives here |
|---|---|
| `What is the minimum autonomy level (L0–L4) that solves this?` | **Q1** — the root branch |
| `Can it be solved by composing the 5 patterns without a full agent loop?` | **Q2** |
| `Is the task breadth-first (parallelizable) or depth-first (coherent)?` | **Q3** |
| `What are the 3 failure modes that would lose user trust first?` | Governance column — *Failure modes to name first* |
| `Where are the permission boundaries? What MUST the agent NOT do?` | Governance column — *Permission tier*; the blast radius at leaves D and F |
| `Which constraint dominates framework choice?` | Deliberately **not** a branch — this tree binds topology, not runtime (Layer 7 decides the framework) |
| `Where does state live? (in-context = anti-pattern for long-running)` | Governance column; the shared state store is part of the blast radius at leaf F |
| `Who validates outputs at each stage? (assertion / LLM judge / human review)` | **Q5** — the verification bar every extra node must clear |
| `Where do traces live, with what retention?` | Governance column — *Eval plan*; DoD 12 at every leaf |
| `Eval set: how many examples, who labels, how does it grow?` | Governance column — *Eval plan*; DoD 10, 22 |

---

## Regenerating the social export

The Mermaid block above is the primary artifact — diffable, and it renders natively on GitHub. For a raster/vector export to attach to a release:

```bash
npx -y @mermaid-js/mermaid-cli -i templates/decision-tree/README.md -o decision-tree.svg
```

*The export is a derivative. When the tree changes, regenerate it — never edit the SVG.*
