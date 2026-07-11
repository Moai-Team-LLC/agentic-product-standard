# The Agentic Product Standard v3.0

*The canonical standard for building modern agentic products.*

---

## Philosophy of the standard

**An agentic product is not "a product with AI." It is a product where part of the process is dynamically directed by an LLM within a deterministic architecture with explicit trust boundaries.**

The standard is built on six principles that converged independently in the production practices of Anthropic, OpenAI, Cognition, Sierra, and LangChain across 2024–2026:

1. **Determinism by default, agency by necessity** — every degree of autonomy must be earned, not granted upfront.
2. **Architecture beats framework** — patterns outlive libraries.
3. **Harness > model** — 98% of reliability lives in the code around the LLM, not in the LLM itself.
4. **Context engineering is the core engineering discipline** — what enters the context window determines everything.
5. **Eval-driven development is non-negotiable** — no measurement, no improvement; no trace review, no understanding.
6. **Security is a structural property, not a guardrail** — an agent's safety comes from architecture (identity, least privilege, isolation, pinned tool definitions), not from filters bolted onto the edges. Content filters top out near ~97% accuracy, so ~3% of injection attacks succeed by design — a property you mitigate structurally, not a number you tune.

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

**The 2026 consensus has settled on orchestrator-subagent, not peer-to-peer.** Anthropic's research system, the Claude Code Task tool, and Cognition's 2026 follow-up ("Multi-Agents: What's Actually Working") converge on a single lead that spawns isolated subagents and consumes their summaries. Peer-to-peer agent buses, shared scratchpads, and free-form agent "debates" remain research curiosities — they multiply context, compound errors, and resist evaluation. If you reach for multi-agent, reach for an orchestrator.

### Canon 4. Harness architecture

The harness is everything that surrounds the LLM loop. **In a production agent, the harness is 98% of the code.** A minimal harness contains eight layers:

```
╔═════════════════════════════════════════════╗
║  8. Security & Identity  (CROSS-CUTTING)    ║ ← threat model · injection defense · agent identity · least-privilege scoped tokens · pinned tool defs · sandboxing
╠═════════════════════════════════════════════╣
║ ┌─────────────────────────────────────────┐ ║
║ │  7. Observability & Tracing             │ ║ ← log EVERYTHING
║ ├─────────────────────────────────────────┤ ║
║ │  6. Evaluation Layer (CI gates)         │ ║ ← block regressions
║ ├─────────────────────────────────────────┤ ║
║ │  5. Human-in-the-Loop (notify/ask/review)│║ ← approval gates
║ ├─────────────────────────────────────────┤ ║
║ │  4. Guardrails (input/output validation)│ ║ ← defense in depth
║ ├─────────────────────────────────────────┤ ║
║ │  3. Durable Execution (Workflow+Activity)│ ║ ← pause/resume/retry
║ ├─────────────────────────────────────────┤ ║
║ │  2. Context & Memory Management         │ ║ ← write/select/compress/isolate
║ ├─────────────────────────────────────────┤ ║
║ │  1. Agent Loop (gather → act → verify)  │ ║ ← the "agent" proper
║ └─────────────────────────────────────────┘ ║
╚═════════════════════════════════════════════╝
              ↕ MCP / function calling
       ┌──────────────────────────┐
       │   Tools & Resources      │
       └──────────────────────────┘
```

**Layer 8 is cross-cutting, not a stage you bolt on at the end.** Identity, least privilege, and isolation constrain every layer beneath them; injection defense spans both input and output (layer 4) but cannot live there alone. A guardrail is one tactic inside Security & Identity — not a substitute for it. See Principle 6 and Part II · Layer 8.

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

The reference implementation of this layer (together with Layer 9) is **AgenticGateway** — one OpenAI-compatible key on a Bifrost data plane: eval-sourced tiered routing, a key vault, prompt + semantic caching, and per-run cost circuit breakers, with every call emitting hash-not-text evidence. The `SCORECARD.md` *Model & provider* section gates this; `examples/agenticgateway-case-study.md` maps each gate to a module.

### Layer 2: Tool integration — **MCP by default**

- **MCP (Model Context Protocol)** — the agent ↔ tool standard, donated to the Linux Foundation's Agentic AI Foundation (Dec 2025). Target the **stable 2025-11-25 spec** today (async tasks, elicitation, extensions) and branch for the **2026-07-28 release candidate** (stateless core, MCP Apps / server-rendered UI, hardened OAuth 2.1 / OIDC). Prefer **remote Streamable HTTP + OAuth 2.1 with Resource Indicators**, externalize session state, and use **elicitation** for human-in-the-loop rather than a side channel.
- **A2A (Agent2Agent)** — the agent ↔ agent standard, now at the **Linux Foundation** (since June 2025): 150+ supporting orgs (AWS, Cisco, Google, IBM, Microsoft, Salesforce, SAP, ServiceNow), 22,000+ stars by April 2026. Reach for A2A **only when crossing a vendor / framework / org boundary** — inside one system, tightly-coupled subagents should share context or call functions directly.
- **Do not write custom integrations** where an MCP server already exists. Do not write tool-only code where the tool should be reusable — wrap it in MCP. **Treat community MCP servers as untrusted supply chain** — see Layer 8.

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

**The 40% rule:** keep context-window usage below 40% of the limit. Degradation past that point is non-linear — this is **harness-engineering doctrine, not a hedge.** Chroma's "context rot" research and Databricks' retrieval studies show accuracy degrading well before the window is full (from ~32k tokens). Bigger windows do **not** repeal the rule: *"no matter how big context windows get, you always get better results if you use less of them"* (Horthy). The frontier technique is **just-in-time retrieval** — Claude Code's glob + grep + read over precomputed vector RAG — pulling context on demand instead of front-loading it.

### Layer 4: Memory

Choose by the dominant requirement:

| Vendor | Strength | When to choose |
|---|---|---|
| **Mem0** | General-purpose, largest community | Default; personalization |
| **Zep** | Temporal knowledge graph; SOC2/HIPAA | Evolving facts (finance, healthcare) |
| **Letta (MemGPT)** | Tiered self-editing memory | Long-horizon agents (500+ interactions) |
| **LangMem** | LangChain-native | Already on LangGraph |
| **Files in repo** | Versioned markdown | When memory must be human-editable |

The reference implementation of this layer is **[AgenticMind](https://github.com/Moai-Team-LLC/AgenticMind)** — citation-enforced knowledge & memory served headlessly over MCP, self-hostable on Postgres + pgvector. Bring-your-own (Mem0 / Zep / Letta / files) stays fine (Principle 2); this is the paved road, not a mandate. See the [`reference-stack`](skills/agentic-product-architect/reference-stack/SKILL.md) skill.

### Layer 5: Durable execution — **mandatory**

Stateless agents lose everything on a crash. The minimal standard:

- **Agent loop** = Workflow (deterministic, replayable from the event log)
- **LLM calls and tool invocations** = Activities (non-deterministic, retryable)
- **State** = a first-class object; the agent must be a pure function (state, event) → new_state

Options:
- **Temporal** — the industry standard; first-party integrations with the OpenAI SDK, Pydantic AI, mcp-agent
- **Inngest / Restate** — operationally simpler; for TypeScript teams
- **LangGraph checkpointer** (Postgres) — built in if you're already on LangGraph

**Fleet operations — when you run many long-lived agents.** Everything above is single-agent durability: one loop pauses, resumes, retries. Operating a *fleet* of scheduled, long-lived agents adds a Day-2 surface the layers above stop short of: the agent as a versioned **deployable manifest** (resources, schedule, runtime, env) distinct from its Agent Contract; **coordinated scheduling** — a lock so a cron fires once across replicas, with misfire handling — backed by a **durable backlog** that survives restarts; per-agent lifecycle (deploy / start / stop / restart) and graceful termination; and **fleet observability** — per-agent health plus an append-only operational audit, layered on the per-run traces of Layer 6. Keep it lean: a runner is a function with limits, not a platform, until a real fleet exists. The `SCORECARD.md` *Fleet operations* section gates this; `examples/agenticops-case-study.md` maps each gate to a reference implementation.

### Layer 6: Observability & Evals

**Do not launch to production without observability.** The minimal set:

| Tool | When to choose |
|---|---|
| **LangSmith** | Deep integration with LangGraph |
| **Langfuse** | OSS / self-hosted; vendor-neutral |
| **Braintrust** | Eval-driven CI/CD deploy gating |
| **Arize Phoenix** | OpenTelemetry-native, ML monitoring lineage |

**Instrument on the OpenTelemetry GenAI semantic conventions** (Semantic Conventions ≥1.40.0) — so you can swap vendors later without re-instrumenting. Emit the standard agent-lifecycle spans (`create_agent`, `invoke_agent`, `execute_tool`, `invoke_workflow`), the `gen_ai.client.operation.duration` metric, and `gen_ai.client.token.usage`; keep payloads opt-in for PII. Datadog, Honeycomb, New Relic, Grafana and the major frameworks emit these natively. (OTel GenAI is still "Development" status — adopt now via `OTEL_SEMCONV_STABILITY_OPT_IN` and expect attribute churn.)

**Distinguish LLM observability from agent observability.** LLM observability is per-call (tokens, latency, cost); **agent observability** is trajectory-, multi-turn-, and session-level (did the agent take a sane path?). You need both. Run **online / production evals**: evaluators on completed threads, with failing live traces routed back into the offline eval set.

The reference implementation of this layer is **[AgenticPerformance (APL)](https://github.com/Moai-Team-LLC/AgenticPerformance)** — OTel traces → per-agent golden-set evals with a CI gate, a named failure taxonomy, and a governed improvement loop. Bring your own (LangSmith / Langfuse / Braintrust / Phoenix) is fine (Principle 2); this is the paved road, not a mandate. See the [`reference-stack`](skills/agentic-product-architect/reference-stack/SKILL.md) skill.

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
| .NET / enterprise Microsoft stack | **Microsoft Agent Framework (1.0 GA)** |

**2026 framework reality (verify before quoting — this layer ages fastest):**
- **Microsoft Agent Framework 1.0 went GA (April 2026)** and supersedes both AutoGen and Semantic Kernel, which are now in maintenance mode. Reframe any "AutoGen" reference as **AG2** (the community fork) or **MAF**.
- The vendor SDKs — **OpenAI Agents SDK, Google ADK, Claude Agent SDK** — are all production-grade as of 2026.
- **LangGraph** is the stateful-workflow default; **Pydantic AI** is the type-safe pick; **CrewAI** is fastest for role-based prototyping.
- Treat **MCP-native vs. adapter** as a portability hedge: an MCP-native tool layer ports across harnesses; framework-specific tool wrappers do not.

**Anthropic's million-dollar advice:** *"Start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code."*

### Layer 8: Security & Identity — **cross-cutting**

Security is Principle 6 and the 8th harness layer. It is the largest gap in most agentic products. Anchor the discipline on the **OWASP Top 10 for Agentic Applications (2026 edition)** — ASI01 *Agent Goal Hijack* through ASI10 *Rogue Agents* — which names agent-specific risks (delegated-identity abuse, cross-agent prompt injection, runtime tool composition) that no single "guardrails" layer covers.

**The lethal trifecta (Willison).** An agent that simultaneously has (1) access to **private data**, (2) exposure to **untrusted content**, and (3) the ability to **communicate externally** can be turned into an exfiltration tool by prompt injection. Run this as a structural check on **every** deployment; if all three are present, break one leg (gate egress, quarantine untrusted input, or scope data) before shipping.

**MCP supply-chain controls.** Community MCP servers are an untrusted supply chain — subject to *tool poisoning*, *rug pulls* (a server mutates tool descriptions after approval), full schema poisoning, and confused-deputy attacks. Therefore:
- **Pin tool definitions by cryptographic hash; alert on any change** (per the OWASP MCP Security Cheat Sheet).
- **Version-pin and signature-check** community servers; install only from an **allow-listed registry**.
- Use **OAuth 2.1 + Resource Indicators**; never pass tokens through; never over-scope.

**Agent identity & least privilege.** Each agent gets a distinct, scoped, least-privilege identity; tokens are short-lived and audience-bound; tool execution is sandboxed. Identity is derived from auth, never asserted by the model.

> **Runnable:** [`templates/security/`](templates/security/README.md) ships a red-team kit — a lethal-trifecta gate, indirect-prompt-injection test cases, and an MCP tool-definition hash-pinning / rug-pull detector.

The reference implementation for red-teaming this layer is **[AgenticAssurance (AAL)](https://github.com/Moai-Team-LLC/AgenticAssurance)** — an OWASP-Agentic / MITRE-ATLAS attack library plus a toxic-flow graph that finds lethal-trifecta / RCE composition paths single-prompt scanners miss, emitting SARIF for CI code-scanning. It operationalizes the lethal-trifecta check above; framework-neutral, not a runtime guardrail (Principle 2). See the [`reference-stack`](skills/agentic-product-architect/reference-stack/SKILL.md) skill.

### Layer 9: Cost & FinOps — **cross-cutting**

Agentic systems are expensive in a way chat never was. Anthropic reports agents use **~4× the tokens of chat, and multi-agent systems ~15×**; Gartner puts agentic tasks at **5–30× the tokens** of a standard chatbot; the FinOps Foundation's *State of FinOps 2026* finds **98% of orgs now manage AI spend** (up from 31% two years prior). Token usage alone explains ~80% of cost variance; tool-call count and model choice are the other two factors.

Make cost a first-class engineering constraint, not a month-end surprise:
- **Per-run token / cost ceilings enforced in code** — a circuit breaker that halts a runaway autonomous session. (Most published multi-agent architectures leave this gap open; close it.)
- **Prompt / KV caching** on stable prefixes (system prompt, tool schemas): up to ~90% cost and ~85% latency reduction on long prompts.
- **Model routing / cascades** — small model for routing & classification, flagship for reasoning.
- **Measure cost-per-outcome, not just total spend** — wire cost into the same traces as Layer 6.
- **The multi-agent economics rule:** only pay the 15× when the task value justifies it. If a single agent clears the bar, the orchestra is waste.

The reference implementation of this layer (together with Layer 1) is **[AgenticGateway](https://github.com/Moai-Team-LLC/AgenticGateway)** — per-run/tenant cost ceilings enforced in code, prompt + semantic caching, and eval-sourced routing behind one OpenAI-compatible key. Bring your own gateway (LiteLLM / Portkey / raw Bifrost) is fine (Principle 2); this is the paved road, not a mandate. See the [`reference-stack`](skills/agentic-product-architect/reference-stack/SKILL.md) skill.

---

## Part III. Production readiness — Definition of Done

An agentic product is **not production-ready** until all 19 items are satisfied (items 16–19 bind only at L3+ unattended operation):

### Context and state
- [ ] **1.** Context utilization < 40% in a typical cycle
- [ ] **2.** State is externalized (does not live only in the context window)
- [ ] **3.** Compaction pipeline tested on long-running scenarios

### Tools and permissions
- [ ] **4.** All destructive actions require explicit human approval
- [ ] **5.** Permissions enforced by code, not by prompt
- [ ] **6.** Tool execution sandboxed (containers / OAuth scopes / least privilege)
- [ ] **(if multi-tenant)** Tenant isolation enforced below the LLM (row-level security / repository layer); `tenant_id` derived from auth, never from the model; retrieval, memory, cache, traces, and sub-agents all tenant-scoped; a code-asserted cross-tenant leakage eval runs in CI — see the `tenant-isolation` skill

### Reliability
- [ ] **7.** Durable execution: pause/resume/retry works across a killed process
- [ ] **8.** Structured outputs validated by schema; assertions on the critical path
- [ ] **9.** Guardrails (minimum: PII, jailbreak, schema validation) on input and output

### Evals and observability
- [ ] **10.** Eval set ≥50 examples per top-priority failure mode
- [ ] **11.** LLM judges calibrated against human labels (TPR/TNR tracked)
- [ ] **12.** CI blocks deploy on eval regression; 100% of production traces logged

### Security & identity
- [ ] **13.** Lethal-trifecta check performed and documented (private data × untrusted content × external comms — at least one leg broken if all three are present)
- [ ] **14.** MCP tool definitions pinned by hash with change alerts; servers installed only from an allow-listed registry; OAuth 2.1 scoped tokens, no token passthrough

### Cost
- [ ] **15.** Per-run token / cost ceiling enforced **in code** (circuit breaker on runaway sessions); cost-per-task tracked in traces

### Unattended operation (L3+) — the Loop License
- [ ] **16.** **Loop License** satisfied for any L3+ unattended system: eval pass-rate threshold, regression gate, declared blast radius, cost cap, kill switch, and escalation path — all six declared, enforced in code, and tested (Part IV; [`CHECKLIST`](templates/loop-license/CHECKLIST.md))
- [ ] **17.** Stop conditions declared in the Agent Contract and enforced by the runner: max iterations, token/time/spend budgets, timeout, escalation after N consecutive failures (Part IV)
- [ ] **18.** Independent verification: the producing model does not grade its own work; deterministic checks first; any LLM judge is calibrated (item 11) and decorrelated from the writer (Part IV)
- [ ] **19.** Loop economics: cost per run and cost per *verified* outcome tracked in traces; per-run and per-window cost caps declared (Part IV · Layer 9)

> **Score yourself.** [`SCORECARD.md`](SCORECARD.md) turns this DoD into a Yes/No maturity self-assessment (M0–M3, mapped to the Autonomy Ladder) — run it with the team against a real deployment each release.

---

## Part IV. The Loop License — earning unattended operation (L3+)

The Autonomy Ladder (Canon 1) and the Cycle of Trust (Canon 5) hold that autonomy is *earned*, not granted. This Part makes that concrete for the hardest case: an agent that runs **unattended** — finding its own work and looping without a human in each turn (L3 orchestrator-worker and L4 autonomous). The market calls this *loop engineering*; done without discipline it produces **a factory with no quality control**. The **Loop License** is the standard's answer: the conditions a system MUST satisfy *before* it may run unattended, and MUST keep satisfying to stay there.

Everything in this Part binds at **L3+**. Below L3 (a single call, or a workflow with a human in the loop) it is recommended, not required.

### The Loop License

> **MUST — no unattended (L3+) operation without all six of these declared, enforced in code, and tested:**
> 1. **Eval pass-rate threshold** — a named minimum pass rate on a representative eval set, measured before promotion (Canon 1 · Part V). Below it, the loop does not run unattended.
> 2. **Regression gate** — CI blocks promotion when the eval pass rate drops against the recorded baseline (DoD 12). A loop that can silently regress has no license.
> 3. **Declared blast radius** — the maximum scope one unattended run can affect (files, records, spend, external calls, tenants), written down and enforced below the model, never asserted by it.
> 4. **Cost cap** — a per-run and per-window token/spend ceiling, enforced in code, that halts the loop (Layer 9 · DoD 15).
> 5. **Kill switch** — an out-of-band control that stops the loop mid-flight without a redeploy, reachable by a human who is not the agent.
> 6. **Escalation path** — a named human (or higher-authority system) the loop hands to on repeated failure, on hitting a stop condition, or on any action outside the declared blast radius.

These are not six nice-to-haves; they are one license. Missing any single gate caps the system at L2 (human-in-the-loop), regardless of how good the model is. The one-page [`templates/loop-license/CHECKLIST.md`](templates/loop-license/CHECKLIST.md) is the artifact to run against a real deployment, with the team in the room.

### Independent verification

The most common way a loop launders a wrong answer into a shipped one is **self-verification**: the same model that produced the work also declares it correct.

> **MUST, at L3+:**
> - **Self-check by the producing model does not count as verification.** A model grading its own output shares its own blind spots and failure correlations; a pass tells you nothing new.
> - **Deterministic-first.** Verify with a deterministic check — tests, schema, assertion, type-check, invariant, diff against a known-good — wherever the property admits one. Reach for an LLM judge only for properties that genuinely require judgment.
> - **The judge has its own eval.** An LLM judge is itself an agent under this standard: calibrated against human labels, TPR/TNR tracked (DoD 11). An uncalibrated judge is not verification — it is a second opinion of unknown quality.
> - **The checker is decorrelated from the writer.** A different model, or a materially different prompt and context; no shared scratchpad; and it sees the *artifact*, not the writer's reasoning about why the artifact is fine.

**Writer / Checker, done right (reference pattern).** A Writer produces the artifact under its Agent Contract. A Checker — a separate agent with its own contract, its own eval, and a deterministic layer in front of its judgment — receives only the artifact and the acceptance criteria, and returns a *hard-to-vary* verdict (each criterion names the single probe that falsifies it). The Writer never sees the Checker's internals; the Checker never sees the Writer's chain of thought. Disagreement escalates — it is not averaged away.

### Stop conditions & fail paths

An unattended loop with no declared way to stop is the defining L4 anti-pattern.

> **MUST — every L3+ agent spec declares, and the runner enforces:**
> - **Max iterations** — a hard turn/step ceiling per run.
> - **Budgets** — token, wall-clock, and spend ceilings (the cost cap of the Loop License).
> - **Timeout** — a maximum run duration after which the loop is cancelled, not left hanging.
> - **Escalation after N failures** — a named threshold of consecutive failed attempts (verification failures, tool errors, guardrail trips) that hands to the escalation path instead of retrying forever.

These are **mandatory sections of the Agent Contract** (`AGENT_STANDARD.md`), declared at design time, not discovered in production. This is DoD item 17.

### The ingestion boundary — "find work" is untrusted input

An L4 loop that selects its own work reads that work from somewhere — a queue, an inbox, a repo, a webhook, a scraped page. **Every one of those is untrusted input.** Treating the find-work step as trusted is how a loop gets hijacked into doing the attacker's work instead of yours (OWASP **LLM01 Prompt Injection**; agentic **ASI01** *Goal Hijack*).

> **MUST, at L3+:**
> - **Injection tests live in the eval suite.** The find-work path is fuzzed with indirect-injection payloads as part of the standing eval set (Layer 8 · DoD 13), not tested once by hand.
> - **Instructions and data are separated.** Ingested content is data; it is never concatenated into the instruction channel where it can rewrite the agent's goal (Layer 8 · indirect prompt injection).
> - **Least privilege on triggers.** What can enqueue work for the loop — and what that work is allowed to reach — is scoped and allow-listed. A trigger is a capability, not an open door.

**Threat checklist:** `[ ]` find-work source classified as untrusted · `[ ]` indirect-injection cases in the eval suite · `[ ]` instruction/data channels separated, verified under a poisoned input · `[ ]` trigger sources allow-listed and least-privileged · `[ ]` egress from a triggered run gated (lethal-trifecta check, Layer 8).

### The instruction supply chain

Skills, prompts, system instructions, tool descriptions and trigger rules are **executable artifacts that steer the loop** — and therefore a supply chain, subject to the same discipline as code dependencies (OWASP **LLM03 Supply Chain**; **AIUC-1** control expectations). A "factory with no QC" is usually a factory whose *instructions* were never version-controlled or evaluated.

> **MUST, at L3+:**
> - **Versioned** — every skill/prompt/instruction artifact carries a version; what shipped is knowable.
> - **Provenance** — who authored it, from what source, and why (the change's intent) is recorded.
> - **Evaluated before deploy** — an instruction change is promoted through the same eval gate as a code change (Part V), never hot-edited into a live loop.
> - **Regression-tested on update** — updating an instruction re-runs its evals; a prompt change that drops the pass rate is a regression (DoD 12), not a tweak.
> - **Trigger-collision audited** — where many skills/agents share a trigger space, overlapping or ambiguous activation is audited; two artifacts silently competing for one trigger is a supply-chain defect.

This is the direct answer to "a factory with no QC": the instructions *are* the tooling on the line, and they get inspected like it.

### Economics of the loop

A loop makes cost a first-class risk: it can spend without a human noticing. Layer 9 sets the cost controls; this Part sets what a licensed loop MUST *know* about its own economics.

> **MUST:**
> - **Measure cost per run** — token and spend, attributed per unattended run, in the same traces as Layer 6.
> - **Measure cost per *verified* outcome** — spend divided by outcomes that passed independent verification, not raw completions. A loop that is cheap per call but rarely produces a verified result is expensive, and only this metric shows it.
> - **Declare cost caps** — the per-run and per-window ceilings of the Loop License, stated up front.

The standard fixes **what** to measure and declare, not **how**: the reference implementations of enforcement and measurement are the model/cost plane (Layer 9 · AgenticGateway) and the observability plane (Layer 6 · AgenticPerformance). This is DoD item 19.

### Architecture-phase declarations

Two properties decide whether a loop is operable, and both MUST be **declared during design, not reconstructed after an incident**:

> **MUST — the Agent Contract declares, at architecture time:**
> - **The memory model** — what the loop persists, for how long (retention), where it came from (provenance), and whether a past run can be **replayed** from it. *"Where does the state live on step 7?"* must have an answer on the whiteboard, not in a post-mortem.
> - **The determinism map** — which steps are deterministic (pure functions, tools, checks) and which are model-driven, so durability, replay, and verification attach to the right steps (Layer 5). A loop whose determinism boundary is unknown cannot be made durable or independently verified.

These are **mandatory sections of the Agent Contract**, alongside the stop conditions above.

### Glossary bridge — the loop-engineering lexicon

Teams arrive with the market's vocabulary. This standard already holds the concepts under its own names; here is the bridge, so clients are met, not re-educated.

| Market term (loop engineering) | This standard |
|---|---|
| Loop / loop engineering | Unattended operation at **L3–L4** on the Autonomy Ladder (Canon 1), governed by the **Loop License** (this Part) |
| Intent debt | Acceptance criteria that are not *hard-to-vary* — the gap the **Cycle of Trust** (Canon 5) and eval discipline (Part V) close |
| Writer / Checker | **Independent verification** (this Part): a decorrelated producer and verifier, each an agent under its own contract |
| State / working memory | **Memory** (Layer 4) + the **memory-model** architecture-phase declaration |
| Find work | The **ingestion boundary** (this Part) — untrusted input, OWASP LLM01 |
| Blast radius / kill switch | Loop License gates 3 and 5 (this Part) |
| Factory with no QC | A loop missing **independent verification** and running an unmanaged **instruction supply chain** |

---

## Part V. Eval discipline (per Husain/Shankar)

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
6. **Evaluate the trajectory, not only the final answer.** For agents, score the path — multi-turn, session-level: tool selection, recovery, policy adherence — not just the last message. A right answer reached by a reckless path is a latent incident.
7. **Track reliability with `pass^k`, not just `pass@1`.** `pass^k` (does it succeed on *all* k attempts) exposes the consistency that a single run hides — the metric that matters for anything autonomous.
8. **Run online evals.** Evaluators on completed production threads, with failing live traces routed back into the offline set (closes the loop with Layer 6).

*Reference benchmarks (as orientation, never as ground truth — see anti-pattern 12): τ-bench / τ²-bench (policy adherence, dual-control), SWE-bench Verified, GAIA, TerminalBench, WebArena. LLM-as-judge agrees with humans ~85% of the time but carries position / verbosity / self-preference bias — keep judges binary and calibrated.*

> **Runnable:** [`templates/ci/eval-gate.yml`](templates/ci/eval-gate.yml) is a copy-paste CI workflow that blocks a merge when the eval pass-rate drops below the ≥90% gate (DoD item 12).

---

## Part VI. The canon from thought leaders

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
9. **Anthropic — "Effective Context Engineering for AI Agents"** (Sept 2025) — just-in-time retrieval, the consensus definition of context engineering

### Specs, protocols & security canon (2025–2026)
- **OWASP — Top 10 for Agentic Applications (2026 edition)** + *Agentic AI Threats and Mitigations* + the **MCP Security Cheat Sheet** — the threat model for Layer 8
- **Simon Willison — "The lethal trifecta"** (June 2025) — the deployment check every agent must pass
- **OpenTelemetry — GenAI semantic conventions** — the vendor-neutral observability standard (Layer 6)
- **MCP specification** (2025-11-25 stable; 2026-07-28 RC) and the **A2A specification** (Linux Foundation) — the interop protocols
- **GEPA** (reflective prompt evolution, ICLR 2026) + **DSPy** — programmatic optimization, the bridge before any weight update

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

## Part VII. A 12-week build roadmap

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

## Part VIII. Anti-patterns

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
13. **Trusting community MCP servers without pinning or scanning.** Tool descriptions can mutate after you approve them (rug pull). Pin by hash; alert on change.
14. **Deploying the lethal trifecta with no mitigation.** Private data + untrusted content + external comms = an exfiltration channel. Break one leg.
15. **Token passthrough / over-scoped OAuth.** Forwarding a user's token, or minting broad scopes "to be safe," is a confused-deputy waiting to happen.
16. **No budget ceiling on autonomous sessions.** Without a per-run cost circuit breaker, one bad loop is an unbounded invoice.
17. **Peer-to-peer multi-agent buses.** Free-form agent debates multiply context and resist evaluation. Use an orchestrator with isolated subagents.

---

## Part IX. Compact decision checklist

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
□ Does the deployment hit the lethal trifecta? If so, which leg do we break?
□ Are MCP tool definitions pinned, and servers installed from an allow-list?
□ What is the per-run token/cost ceiling, and where in the code is it enforced?
```

---

## Part X. Emerging & deferred

Tracked deliberately, but **not** yet promoted to first-class standard surface — naming what we refuse to over-specify is part of the discipline. Reach for these only when the dominant constraint demands it.

- **Inter-agent protocols (A2A) in depth.** The decision rule lives in Layer 2: internal function calls / shared context for tightly-coupled subagents; A2A only across vendor / framework / org boundaries. A full protocol playbook is deferred until cross-org agent deployments are common in practice.
- **Model adaptation (RL / fine-tuning / programmatic optimization).** Decision ladder: prompt → context-engineer → **programmatic optimization (DSPy / GEPA)** → RL or fine-tune *only* when a verifiable reward and a rollout budget exist. **Engineer the harness first** remains the right 2026 default; GEPA/DSPy is the named bridge before any weight update.
- **Agent experience (AX).** Ambient / event-driven agents, the agent-inbox UX, and notify / ask / review trust calibration extend the existing Human-in-the-Loop layer — see Harrison Chase's ambient-agents work. Extend HITL; do not duplicate it.
- **Orchestration topologies beyond orchestrator-worker** (blackboard, hierarchical, market-based, swarm) — documented as map, but 2026 evidence favors orchestrator-subagent for reliability (Canon 3).
- **Agentic / Graph RAG.** Claude Code abandoned precomputed vector RAG for grep-style agentic retrieval (Layer 3); GraphRAG earns its keep on genuinely multi-hop questions.
- **Computer-use & voice agents.** First-class in the Claude Agent SDK (computer use) and benchmarked by τ-Voice (full-duplex voice) — emerging deployment patterns, not yet core.
- **Curated-context formats (`llms.txt`, OKF).** `llms.txt` (a single-file navigation pointer) and **OKF** — Google Cloud's Open Knowledge Format, v0.1, a git-distributed bundle of Markdown concept files cross-linked into a graph — standardize the *knowledge an agent consumes*, upstream of the agent system this standard governs. Treat them as the **supply side of context engineering** (Layer 3 · Select / just-in-time retrieval): adopt as a source, don't mandate a v0.1 spec. Details in the `context-engineering` skill. *(Aptly, this repo is already that shape — Markdown concepts + frontmatter + an index.)*

---

## Closing

The standard is not dogma. It is a **tilt of the field** toward the practices that, across 2024–2026, converged independently at Anthropic, OpenAI, Cognition, Sierra, LangChain, and among leading practitioners.

**The single most important rule of the standard:**

> *"Architecture is what remains when the model improves. The model is the variable, the harness is the constant. Invest proportionally."*

---

*v3.0 · assembled from production practices as of June 2026*
