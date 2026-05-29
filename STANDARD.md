# The Agentic Product Standard v1.0

*The canonical standard for building modern agentic products.*

> **Russian original:** [`docs/STANDARD.ru.md`](docs/STANDARD.ru.md)

---

## Philosophy of the standard

**An agentic product is not "a product with AI." It is a product where part of the process is dynamically directed by an LLM within a deterministic architecture with explicit trust boundaries.**

The standard is built on five principles that converged independently in the production practices of Anthropic, OpenAI, Cognition, Sierra, and LangChain across 2024–2026:

1. **Determinism by default, agency by necessity** — every degree of autonomy must be earned, not granted upfront.
2. **Architecture beats framework** — patterns outlive libraries.
3. **Harness > model** — 98% of reliability lives in the code around the LLM, not in the LLM itself.
4. **Context engineering is the core engineering discipline** — what enters the context window determines everything.
5. **Eval-driven development is non-negotiable** — no measurement, no improvement; no trace review, no understanding.

---

## Part I. The architectural canon

### Canon 1. The Autonomy Ladder

Every agentic product is built incrementally up this ladder. **Climb to the next level only once the previous one has proven value on evals.**

| Level | Description | When to use |
|---|---|---|
| **L0. Single LLM call** | One prompt, one response | Classification, extraction, summarization |
| **L1. Augmented LLM** | + retrieval, + tools, + memory | Q&A over documents, simple assistants |
| **L2. Workflow** | Deterministic code orchestrates LLM steps | Known execution path; predictability required |
| **L3. Orchestrator-Worker** | LLM decomposes dynamically, but the graph is bounded | Parallelizable tasks (research, breadth-first) |
| **L4. Autonomous Agent Loop** | The LLM chooses the next step until termination | The path cannot be enumerated; cost and compounding errors are tolerable |

**Escalation rule:** do not climb to L+1 until L delivers ≥90% pass rate on a curated eval set.

### Canon 2. The five composition patterns

This is the vocabulary of the industry. Every agentic product is assembled from these like Lego:

1. **Prompt Chaining** — sequential decomposition (outline → draft → polish)
2. **Routing** — classifier + dispatcher to a specialist
3. **Parallelization** — fan-out of independent subtasks + aggregation
4. **Orchestrator-Workers** — central planner + dynamic workers
5. **Evaluator-Optimizer** — generator + critic in a loop until acceptance

**Meta-principle:** first try to solve the task by composing these patterns in deterministic code. A full agent loop is the last resort.

### Canon 3. Single vs. Multi-Agent — the resolved question

| Task type | Architecture | Why |
|---|---|---|
| **Breadth-first, parallelizable** (research, exploration, multi-source synthesis) | Multi-agent (orchestrator + isolated sub-agents) | Isolated context windows; parallelism; ~90% lift at Anthropic |
| **Depth-first, coherent** (coding, long-form writing, stateful editing) | Single-agent | Shared context is critical; sub-agents create a "telephone game" |

**Sub-agents return synthesis, not transcript.** Never pass a sub-agent's raw output up to the parent.

### Canon 4. Harness architecture

The harness is everything that surrounds the LLM loop. **In a production agent, the harness is 98% of the code.** A minimal harness contains seven layers:

```
┌─────────────────────────────────────────────┐
│  7. Observability & Tracing                 │ ← log EVERYTHING
├─────────────────────────────────────────────┤
│  6. Evaluation Layer (CI gates)             │ ← block regressions
├─────────────────────────────────────────────┤
│  5. Human-in-the-Loop (notify/ask/review)   │ ← approval gates
├─────────────────────────────────────────────┤
│  4. Guardrails (input/output validation)    │ ← defense in depth
├─────────────────────────────────────────────┤
│  3. Durable Execution (Workflow + Activity) │ ← pause/resume/retry
├─────────────────────────────────────────────┤
│  2. Context & Memory Management             │ ← write/select/compress/isolate
├─────────────────────────────────────────────┤
│  1. Agent Loop (gather → act → verify)      │ ← the "agent" proper
└─────────────────────────────────────────────┘
              ↕ MCP / function calling
       ┌──────────────────────────┐
       │   Tools & Resources      │
       └──────────────────────────┘
```

### Canon 5. The Cycle of Trust

Every agent action passes through an explicit trust check:

```
gather context → propose action → check permissions →
verify preconditions → execute → verify outcome →
log trace → update memory
```

**Never let the model bypass a permission boundary.** Permissions are enforced by code, not by prompt. The Replit incident of 2025 (an agent wiped the database of 1,200+ companies, ignoring a "code freeze" instruction in its prompt) is the canonical proof of this principle.

---

## Part II. The technology stack

### Layer 1: Model and provider

- **Multi-provider from the start.** Locking into a single model API is a strategic mistake. Use a framework or an abstraction (Pydantic AI supports 25+ providers; LangGraph is model-agnostic).
- **Tiered routing.** Small model for routing/classification, flagship for reasoning. Per-agent model assignment.
- **Prompt caching is mandatory** for stable parts (system prompt, tool schemas).

### Layer 2: Tool integration — **MCP by default**

- **MCP (Model Context Protocol)** — the agent ↔ tool standard. By early 2026: 10,000+ servers, 177,000+ tools.
- **A2A (Agent2Agent)** — the agent ↔ agent standard (Google → Linux Foundation).
- **Do not write custom integrations** where an MCP server already exists. Do not write tool-only code where the tool should be reusable — wrap it in MCP.

**Tool design rules:**
- <20 active tools per agent (above that — RAG-MCP to select the relevant subset, +3.2× accuracy on correct tool selection)
- Tool names and descriptions are designed as prompts
- Structured outputs by default (Pydantic-validated)
- Formats from the training distribution: Markdown diffs, JSON, NL — not custom DSLs

### Layer 3: Context engineering — four operations

| Operation | When to apply | Implementation |
|---|---|---|
| **Write** | State that must be preserved | Scratchpad, files (CLAUDE.md, AGENTS.md), memory store |
| **Select** | Relevant context for the current step | RAG for documents, RAG for tool descriptions, RAG for memory |
| **Compress** | Long conversation history | Multi-layer compaction (drop low-value → summarize) |
| **Isolate** | Sub-tasks with independent contexts | Sub-agents with their own windows |

**The 40% rule:** keep context-window usage below 40% of the limit. Degradation past that point is non-linear.

### Layer 4: Memory

Choose by the dominant requirement:

| Vendor | Strength | When to choose |
|---|---|---|
| **Mem0** | General-purpose, largest community | Default; personalization |
| **Zep** | Temporal knowledge graph; SOC2/HIPAA | Evolving facts (finance, healthcare) |
| **Letta (MemGPT)** | Tiered self-editing memory | Long-horizon agents (500+ interactions) |
| **LangMem** | LangChain-native | Already on LangGraph |
| **Files in repo** | Versioned markdown | When memory must be human-editable |

### Layer 5: Durable execution — **mandatory**

Stateless agents lose everything on a crash. The minimal standard:

- **Agent loop** = Workflow (deterministic, replayable from the event log)
- **LLM calls and tool invocations** = Activities (non-deterministic, retryable)
- **State** = a first-class object; the agent must be a pure function (state, event) → new_state

Options:
- **Temporal** — the industry standard; first-party integrations with the OpenAI SDK, Pydantic AI, mcp-agent
- **Inngest / Restate** — operationally simpler; for TypeScript teams
- **LangGraph checkpointer** (Postgres) — built in if you're already on LangGraph

### Layer 6: Observability & Evals

**Do not launch to production without observability.** The minimal set:

| Tool | When to choose |
|---|---|
| **LangSmith** | Deep integration with LangGraph |
| **Langfuse** | OSS / self-hosted; vendor-neutral |
| **Braintrust** | Eval-driven CI/CD deploy gating |
| **Arize Phoenix** | OpenTelemetry-native, ML monitoring lineage |

**Instrument via OpenInference / OpenLLMetry** — so you can swap vendors later without re-instrumenting.

### Layer 7: Framework selection

The deciding factor is the **dominant constraint**, not the hype:

| Constraint | Framework |
|---|---|
| Maximum control, complex stateful workflows, multi-vendor | **LangGraph** |
| Anthropic-native, especially coding/computer-use | **Claude Agent SDK** |
| OpenAI-native, opinionated SDK | **OpenAI Agents SDK** |
| Multi-agent with explicit roles, fastest prototype | **CrewAI** |
| Type-safety, FastAPI ergonomics, structured outputs | **Pydantic AI** |
| Document-heavy, RAG at the core | **LlamaIndex Workflows** |
| TypeScript full-stack | **Mastra** |
| Programmatic prompt optimization | **DSPy** |
| MCP-native + Temporal | **mcp-agent (lastmile-ai)** |

**Anthropic's million-dollar advice:** *"Start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code."*

---

## Part III. Production readiness — Definition of Done

An agentic product is **not production-ready** until all 12 items are satisfied:

### Context and state
- [ ] **1.** Context utilization < 40% in a typical cycle
- [ ] **2.** State is externalized (does not live only in the context window)
- [ ] **3.** Compaction pipeline tested on long-running scenarios

### Tools and permissions
- [ ] **4.** All destructive actions require explicit human approval
- [ ] **5.** Permissions enforced by code, not by prompt
- [ ] **6.** Tool execution sandboxed (containers / OAuth scopes / least privilege)

### Reliability
- [ ] **7.** Durable execution: pause/resume/retry works across a killed process
- [ ] **8.** Structured outputs validated by schema; assertions on the critical path
- [ ] **9.** Guardrails (minimum: PII, jailbreak, schema validation) on input and output

### Evals and observability
- [ ] **10.** Eval set ≥50 examples per top-priority failure mode
- [ ] **11.** LLM judges calibrated against human labels (TPR/TNR tracked)
- [ ] **12.** CI blocks deploy on eval regression; 100% of production traces logged

---

## Part IV. Eval discipline (per Husain/Shankar)

This discipline matters more than the choice of framework.

### The three-level eval pyramid

```
       ▲
      ╱ ╲     Level 3: Human Review
     ╱   ╲    (on major changes, ~20-50 traces)
    ╱─────╲
   ╱       ╲   Level 2: LLM-as-Judge
  ╱         ╲  (on cadence, binary output, calibrated)
 ╱───────────╲
╱             ╲ Level 1: Code Assertions
─────────────── (on every change, cheap)
```

### Eval rules

1. **Error analysis first.** Read 20–50 production traces by hand before building any infrastructure.
2. **Binary outputs.** An LLM judge always returns true/false. Likert scales break alignment.
3. **Calibrate every judge.** A minimum of 100 human-labeled examples per judge; track TPR/TNR every release.
4. **Product-specific evals.** Generic "helpfulness" does not catch real failures. Evals are built around observed failure modes ("missed human handoff," "wrong tool selection").
5. **The eval set grows from production.** Every new failure mode becomes a permanent regression test.

---

## Part V. The canon from thought leaders

A minimal reading list. **These sources are not references — they are the operational base:**

### Must-read (in order)
1. **Anthropic — "Building Effective Agents"** (Schluntz & Zhang, Dec 2024) — the vocabulary of patterns
2. **OpenAI — "A Practical Guide to Building Agents"** (PDF, 2025) — a production-oriented view
3. **HumanLayer — "12 Factor Agents"** (Dex Horthy) — the most prescriptive practical methodology
4. **Anthropic — "How we built our multi-agent research system"** (Hadfield, Zhang et al.) — multi-agent case study
5. **Cognition — "Don't Build Multi-Agents"** (Walden Yan, June 2025) — the opposing view
6. **LangChain — "Context Engineering for Agents"** (Lance Martin) — write/select/compress/isolate
7. **Hamel Husain — "A Field Guide to Rapidly Improving AI Products"** + "Your AI Product Needs Evals" — eval discipline
8. **Anthropic — "Building agents with the Claude Agent SDK"** (Sept 2025) — a guide to harness design

### Reference exemplars for studying architecture
- **Claude Code** — harness design, 5-layer compaction, 7-mode permissions (arXiv:2604.14228)
- **Cognition Devin** — single-threaded coding agent, RPI framework
- **Anthropic Research feature** — orchestrator-worker with a separate citation pass
- **OpenAI Codex Harness** — agent self-validation, progressive disclosure via docs/
- **Sierra** — Agent Development Life Cycle, multi-model constellation, outcome-based pricing

### Lead voices of thoughtful practitioners
- **Harrison Chase** (LangChain) — ambient agents, agent inbox
- **Hamel Husain** (Parlance Labs) — eval methodology
- **Dex Horthy** (HumanLayer) — 12 Factor Agents, harness engineering
- **Andrew Ng** (DeepLearning.AI) — the four agentic design patterns
- **Andrej Karpathy** — context engineering, the LLM-as-OS framing
- **Simon Willison** — practical grounding in LLM tooling
- **Omar Khattab** — DSPy, programmatic prompt optimization
- **Eugene Yan** — patterns for LLM systems & products
- **Bret Taylor** (Sierra) — enterprise agentic operations

---

## Part VI. A 12-week build roadmap

### Phase 1 — Prove value (weeks 0–2)
- Write the workflow as a deterministic pipeline
- Find the **one** point where an LLM is mandatory
- Use the raw model SDK; no framework
- Curated eval set of 20–50 examples **before** writing code
- Enumerate the failure modes that would lose trust — these are your first assertions

**Gate to Phase 2:** ≥90% pass rate on the eval set

### Phase 2 — Structure & routing (weeks 2–6)
- Choose a framework by the dominant constraint
- Wire up observability on day one of writing code
- Routing + structured outputs + guardrail layer
- 100% of production traffic traced
- 30 minutes a week of manual trace review

**Gate to Phase 3:** the router dispatches to >1 specialist; 3 top failure modes identified from traces

### Phase 3 — Harden for production (weeks 6–12)
- Durable execution **before** the first long-running agent in production
- Human-in-the-loop for any action with blast radius
- LLM-as-judge for the top-3 subjective failure modes (calibrated)
- CI gates on eval regression
- Memory layer (if sessions outgrow a single conversation)
- MCP for non-proprietary integrations

**Gate to Phase 4 (multi-agent):** the single-agent demonstrably hits (a) context exhaustion, (b) breadth-first parallelism, and the sub-tasks are **genuinely** independent.

### Phase 4 — Optimize (ongoing)
- Audit context utilization
- Tiered model routing
- The eval set expands from every new production failure
- The harness is your durable advantage; invest here, not in model swaps

---

## Part VII. Anti-patterns

**Do not do this:**

1. **Multi-agent before a single-agent baseline.** First prove value on one agent.
2. **Framework abstractions before understanding the raw API.** Otherwise debugging turns into reverse-engineering someone else's code.
3. **LLM judges without calibration against human labels.** A metric with no trust value is not a metric.
4. **Permissions via prompt.** The model will ignore them. Enforce in code only.
5. **Memory as an afterthought.** Externalizing state is an architectural decision; the retrofit is painful.
6. **Generic evals ("helpfulness," "correctness").** They do not catch product-specific failures.
7. **Likert scales in an LLM judge.** Binary outputs are the only thing that calibrates.
8. **Tool count >100.** The model gets confused. Use RAG-MCP or routing.
9. **One agent for breadth + depth.** Specialize: one type of agent, one type of task.
10. **Deploy without trace monitoring.** Most failures are routing/tool-selection — visible only in traces.
11. **Hardcoded prompts without version control.** Prompts are code.
12. **Trusting single-vendor benchmarks.** Anthropic's 90.2% lift, Letta's 500+ interactions — directionally correct, not absolute truth.

---

## Part VIII. Compact decision checklist

Before starting any agentic project, run through this checklist:

```
□ What is the minimum sufficient level of the autonomy ladder? (L0–L4)
□ Can it be solved by composing the 5 patterns without a full loop?
□ Breadth-first or depth-first? (decides single vs. multi)
□ Which 3 failure modes will lose trust first?
□ Where are the permission boundaries? (what can the agent NOT do?)
□ Which constraint dominates framework choice?
□ Where does state live? (in-context = anti-pattern for long-running)
□ Who validates? (assertion / LLM judge / human review — for which layer?)
□ Trace storage and retention — where, how long?
□ Eval set: how many examples, who labels, how does it grow?
```

---

## Closing

The standard is not dogma. It is a **tilt of the field** toward the practices that, across 2024–2026, converged independently at Anthropic, OpenAI, Cognition, Sierra, LangChain, and among leading practitioners.

**The single most important rule of the standard:**

> *"Architecture is what remains when the model improves. The model is the variable, the harness is the constant. Invest proportionally."*

---

*v1.0 · assembled from production practices as of May 2026*
