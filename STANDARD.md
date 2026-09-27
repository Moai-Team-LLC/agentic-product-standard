<!-- canon:begin:standard.title -->
# The Agentic Product Standard v4.0

> **Release candidate 4.0.0-rc.1** — *Conformance Contract*. Open for comment before the final release; what changed and why: [`CHANGELOG.md`](CHANGELOG.md).

<!-- canon:end:standard.title -->

*The canonical standard for building modern agentic products.*

---

## Philosophy of the standard

**An agentic product is not "a product with AI." It is a product where part of the process is dynamically directed by an LLM within a deterministic architecture with explicit trust boundaries.**

The standard is built on six principles that converged independently in the production practices of Anthropic, OpenAI, Cognition, Sierra, and LangChain across 2024–2026:

<!-- canon:begin:standard.principles -->
1. **Determinism by default, agency by necessity** — every degree of autonomy must be earned, not granted upfront.
2. **Architecture beats framework** — patterns outlive libraries.
3. **Harness > model** — reliability lives in the code around the LLM, not in the LLM itself; in a production coding agent that harness is ~98% of the code (Canon 4).
4. **Context engineering is the core discipline** — what enters the context window determines everything.
5. **Eval-driven development is non-negotiable** — no measurement, no improvement; no trace review, no understanding.
6. **Security is a structural property, not a guardrail** — an agent's safety comes from architecture (identity, least privilege, isolation, pinned tool definitions), not from filters bolted onto the edges. Content filters top out near ~97% accuracy, so ~3% of injection attacks succeed by design — a property you mitigate structurally, not a number you tune.

<!-- canon:end:standard.principles -->

---

## Part I. The architectural canon

### Canon 1. The Autonomy Ladder

Every agentic product is built incrementally — and, since v4.0, along **two axes**. *Autonomy* is who chooses the next step; *oversight* is whether a human approves each consequential action. They are different questions: an L3 orchestrator whose every external action waits for approval is not unattended, and an L2 pipeline that auto-applies its output is. **Climb one step at a time, on evidence, and earn each axis separately.** The combination a system actually runs at — its **operating point**, e.g. `L3 · O0` — is declared at design time (Part IV, *Architecture-phase declarations*) and decides which licenses it owes.

<!-- canon:begin:standard.ladder -->
**Autonomy — who chooses the next step.**

| Level | What it is | Use when |
|---|---|---|
| **L0** · Single LLM call | One prompt → one response | Classification, extraction, summarization |
| **L1** · Augmented LLM | One call + retrieval, tools, memory | Q&A over docs, simple assistants, lookup + reformat |
| **L2** · Workflow | Deterministic code orchestrates LLM steps | The path is known; predictability matters |
| **L3** · Bounded decomposition *(formerly Orchestrator-Worker)* | The LLM decomposes the task dynamically, within a bounded graph | Parallelizable, breadth-first work — typically built with the Orchestrator-Workers pattern |
| **L4** · Autonomous agent loop | The LLM chooses the next step until termination | The path cannot be enumerated; cost and compounding errors are tolerable |

**Oversight — whether a human approves each consequential action.** A consequential action is any action at permission tier P3 or above — external write, financial, communication, destructive ([`AGENT_STANDARD.md`](AGENT_STANDARD.md) · Permission Tiers). Destructive (P6) actions require explicit human approval at every oversight mode (DoD 4).

| Mode | What it means | Requires |
|---|---|---|
| **O0** · Human in the loop | A human approves each consequential action before it executes | Per-action approval is the control (DoD 4) |
| **O1** · Human on the loop | Actions inside the declared blast radius execute without per-action approval; a human supervises live and can veto, pause, or take over | Loop License (DoD 16–19) |
| **O2** · Unattended | No human watches in real time; people are reached through the escalation path and sampled review | Loop License + success-legitimacy audit (DoD 16–19, 30) |

> **Escalation rules — each axis is earned separately:**
>
> - **Climb autonomy** (L → L+1) only when L delivers **pass@1 ≥ 90%** on a curated eval set.
> - **Relax oversight** (O0 → O1 → O2) only under a **Loop License**, whose eval gate adds consistency: **pass^5 ≥ a declared threshold** on the same set. O2 also requires a published **legitimacy rate** (DoD 30).
> - Measure your reliability horizon on your own eval set. Benchmark time horizons do not transfer — they differ between domains by orders of magnitude (METR) — so this standard sets no hour thresholds.

An **operating point** is one of each:

- `L3 · O0` — an orchestrator whose every external action waits for approval: no Loop License required.
- `L2 · O2` — a nightly pipeline that auto-applies its output: Loop License and legitimacy audit, despite its low autonomy.
- `L4 · O1` — an autonomous loop a human supervises live: Loop License required.

<!-- canon:end:standard.ladder -->

### Canon 2. The five composition patterns

This is the vocabulary of the industry. Every agentic product is assembled from these like Lego:

<!-- canon:begin:standard.patterns -->
1. **Prompt Chaining** — sequential decomposition (outline → draft → polish)
2. **Routing** — classifier + dispatcher to a specialist
3. **Parallelization** — fan-out of independent subtasks + aggregation
4. **Orchestrator-Workers** — central planner + dynamic workers
5. **Evaluator-Optimizer** — generator + critic in a loop until acceptance

**Meta-principle:** First try to solve the task by composing these patterns in deterministic code. A full agent loop is the last resort.

<!-- canon:end:standard.patterns -->

### Canon 3. Single vs. Multi-Agent — the resolved question

| Task type | Architecture | Why |
|---|---|---|
| **Breadth-first, parallelizable** (research, exploration, multi-source synthesis) | Multi-agent (orchestrator + isolated sub-agents) | Isolated context windows; parallelism; ~90% lift at Anthropic |
| **Depth-first, coherent** (coding, long-form writing, stateful editing) | Single-agent | Shared context is critical; sub-agents create a "telephone game" |

**Sub-agents return synthesis, not transcript.** Never pass a sub-agent's raw output up to the parent.

**The 2026 consensus has settled on orchestrator-subagent, not peer-to-peer.** Anthropic's research system, the Claude Code Task tool, and Cognition's 2026 follow-up ("Multi-Agents: What's Actually Working") converge on a single lead that spawns isolated subagents and consumes their summaries. Peer-to-peer agent buses, shared scratchpads, and free-form agent "debates" remain research curiosities — they multiply context, compound errors, and resist evaluation. If you reach for multi-agent, reach for an orchestrator.

### Canon 4. Harness architecture

The harness is everything that surrounds the LLM loop. **In a production agent, the harness is ~98% of the code** (a community estimate for Claude Code — ~1.6% AI decision logic, ~98.4% operational infrastructure — cited by Liu et al., *Dive into Claude Code*, arXiv:2604.14228). A minimal harness contains nine layers — seven stacked around the loop, two cutting across all of them:

<!-- canon:begin:standard.harness -->
```
╔══════════════════════════════════════════════╗
║  9. Cost & FinOps           (CROSS-CUTTING)  ║ ← per-run ceilings in code · caching · routing · cost per verified outcome
║  8. Security & Identity     (CROSS-CUTTING)  ║ ← threat model · injection defense · per-agent identity · least-privilege tokens · pinned tool defs · protocol auth baseline
╠══════════════════════════════════════════════╣
║   7. Observability & Tracing                 ║ ← log EVERYTHING — on pinned OTel GenAI conventions
║   6. Evaluation (CI gates)                   ║ ← block regressions
║   5. Human-in-the-Loop (notify/ask/review)   ║ ← approval gates
║   4. Guardrails (input/output validation)    ║ ← defense in depth
║   3. Durable Execution (Workflow + Activity) ║ ← pause/resume/retry
║   2. Context & Memory Management             ║ ← write/select/compress/isolate
║   1. Agent Loop (gather → act → verify)      ║ ← the "agent" proper
╚══════════════════════════════════════════════╝
              ↕ MCP / function calling
       ┌──────────────────────────┐
       │   Tools & Resources      │
       └──────────────────────────┘
```

<!-- canon:end:standard.harness -->

**Layers 8 and 9 are cross-cutting, not stages you bolt on at the end.** Identity, least privilege, and isolation constrain every layer beneath them; injection defense spans both input and output (Layer 4) but cannot live there alone. A guardrail is one tactic inside Security & Identity — not a substitute for it. See Principle 6 and Stack 8. Cost & FinOps cuts across the same way: a runaway loop is stopped by a per-run ceiling enforced in code at every layer that spends, not by a dashboard (Stack 9).

*Numbering.* **"Layer N" always means a harness layer** in this diagram. Part II — the technology stack, which technology to choose for each concern — numbers its sections **Stack 1–9**. The two lists coincide only at 8 (Security & Identity) and 9 (Cost & FinOps), which are both harness layers and stack sections.

### Canon 5. The Cycle of Trust

Every agent action passes through an explicit trust check:

```
gather context → propose action → check permissions →
verify preconditions → execute → verify outcome →
log trace → update memory
```

**Never let the model bypass a permission boundary.** Permissions are enforced by code, not by prompt. The Replit incident of July 2025 (an agent deleted a production database holding records on 1,200+ companies, ignoring a "code freeze" instruction in its prompt — [Fortune, 23 Jul 2025](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/)) is the canonical proof of this principle.

**Calibration invariant.** The "verify outcome" step is only trust-bearing if the verifier is. A judge whose calibration status is not `calibrated` (Part V, *Judge calibration*) MUST NOT gate operation without per-action approval (O1+), an auto-apply decision, or a release; a low-confidence verdict abstains and escalates rather than passing. A flaky grader in a release gate is the eval-world equivalent of a prompt-enforced permission — it looks like a check and isn't one.

**Gate-integrity invariant.** A gate is trust-bearing only if its green state means the property holds — not that the check was silenced. Weakening a correctness, type-safety, security, or eval gate to make CI pass — disabling a rule repo-wide, `@ts-ignore` / `eslint-disable`, `.skip`, deleting an assertion, lowering a threshold — is a defect, not a fix: it removes the exact protection at the moment it fired. A false positive is a *scoping* problem, not a kill switch — confine the exception to the offending file or glob with a named reason, then re-prove the gate still fires by planting what it must catch (an adversarial check). Note that a passing `tsc` is **not** a substitute for the `no-unsafe-*` / `no-explicit-any` lint family: `any` is assignable to everything by design, so the compiler waves it through and the lint rules are what close that hole. Like a prompt-enforced permission, a disabled gate looks like a check and isn't one. The mechanical form of this invariant — a test that fails if the safety rules are ever flipped off — is exemplified in AgenticMind's shared lint config.

---

## Part II. The technology stack

### Stack 1: Model and provider

- **Multi-provider from the start.** Locking into a single model API is a strategic mistake. Use a framework or an abstraction (Pydantic AI supports 25+ providers; LangGraph is model-agnostic).
- **Tiered routing.** Small model for routing/classification, flagship for reasoning. Per-agent model assignment.
- **Prompt caching is mandatory** for stable parts (system prompt, tool schemas).
- **A model swap is a release, not a config change.** Re-run the eval suite, re-measure the context budget (DoD 1), and re-derive cost ceilings and routing (DoD 15) on the new model — prices, tokenizers, and degradation curves all move. Pin exact model identifiers in configuration; in prose and prompts, refer to capability tiers rather than model names, which turn over several times a year.

The reference implementation of this stack section (together with Stack 9) is **AgenticGateway** — one OpenAI-compatible key on a Bifrost data plane: eval-sourced tiered routing, a key vault, prompt + semantic caching, and per-run cost circuit breakers, with every call emitting hash-not-text evidence. The `SCORECARD.md` *Model & provider* section gates this; `examples/agenticgateway-case-study.md` maps each gate to a module.

### Stack 2: Tool integration — **MCP by default**

- **MCP (Model Context Protocol)** — the agent ↔ tool standard, governed at the Linux Foundation's Agentic AI Foundation since December 2025. **The baseline is revision 2026-07-28** (final 28 Jul 2026; the TypeScript, Python, Go and C# SDKs supported it on release). It is **stateless**: no protocol sessions and no `initialize` — servers that need cross-call state mint explicit handles; server-initiated requests became multi-round-trip `input_required` results; list and read results carry `ttlMs` / `cacheScope` caching hints; Tasks and MCP Apps moved to extensions; Roots, Sampling, and Logging are deprecated (removal no earlier than a revision dated 2027-07-28). Prefer **remote Streamable HTTP + OAuth**, with clients registered by **Client ID Metadata Document**, and use **elicitation** — now an `input_required` round trip — for human-in-the-loop rather than a side channel. The protocol and auth baseline is DoD 26; migration notes are in advisory [APS-2026-01](docs/advisories/APS-2026-01-mcp-2026-07-28.md).
- **A2A (Agent2Agent)** — the agent ↔ agent standard, at the **Linux Foundation** since June 2025, with 150+ supporting organizations (AWS, Cisco, Google, IBM, Microsoft, Salesforce, SAP, ServiceNow) by April 2026. **v1.0**, the first stable release, shipped on 12 Mar 2026 (current: v1.0.1) and defines **signed Agent Cards** — a JWS over the JCS-canonicalized card. Reach for A2A **only when crossing a vendor / framework / org boundary** — inside one system, tightly-coupled subagents should share context or call functions directly — and when you do cross one, verify the card before you delegate (DoD 28).
- **Do not write custom integrations** where an MCP server already exists. Do not write tool-only code where the tool should be reusable — wrap it in MCP. **Treat community MCP servers as untrusted supply chain** — see Layer 8.

**Tool design rules:**
- <20 active tools per agent (above that — RAG-MCP to select the relevant subset, +3.2× accuracy on correct tool selection)
- Tool names and descriptions are designed as prompts
- Structured outputs by default (Pydantic-validated)
- Formats from the training distribution: Markdown diffs, JSON, NL — not custom DSLs

### Stack 3: Context engineering — four operations

| Operation | When to apply | Implementation |
|---|---|---|
| **Write** | State that must be preserved | Scratchpad, files (CLAUDE.md, AGENTS.md), memory store |
| **Select** | Relevant context for the current step | RAG for documents, RAG for tool descriptions, RAG for memory |
| **Compress** | Long conversation history | Multi-layer compaction (drop low-value → summarize) |
| **Isolate** | Sub-tasks with independent contexts | Sub-agents with their own windows |

**The context budget (the 40% rule, measured):** keep context-window usage below the point where quality degrades. Degradation past that point is non-linear — this is **harness-engineering doctrine, not a hedge.** Since v4.0 the budget is **measured, not assumed**: it is the fill level at which *your* eval pass rate starts to fall for the model in use, re-measured on every model change. **40% of the window is the default until you have measured it** — and on 1M-token windows, measure before you trust it: 40% of 1M is 400K tokens, far past where the studies below see accuracy fall (DoD 1). Chroma's "context rot" research and Databricks' retrieval studies show accuracy degrading well before the window is full (from ~32k tokens). Bigger windows do **not** repeal the rule: *"no matter how big context windows get, you always get better results if you use less of them"* (Horthy). The frontier technique is **just-in-time retrieval** — Claude Code's glob + grep + read over precomputed vector RAG — pulling context on demand instead of front-loading it.

### Stack 4: Memory

Choose by the dominant requirement:

| Vendor | Strength | When to choose |
|---|---|---|
| **Mem0** | General-purpose, largest community | Default; personalization |
| **Zep** | Temporal knowledge graph; SOC2/HIPAA | Evolving facts (finance, healthcare) |
| **Letta (MemGPT)** | Tiered self-editing memory | Long-horizon agents (500+ interactions) |
| **LangMem** | LangChain-native | Already on LangGraph |
| **Files in repo** | Versioned markdown | When memory must be human-editable |

**Freshness is part of the memory model.** Knowledge fetched over MCP now carries caching hints (`ttlMs`, `cacheScope`): treat the TTL as the freshness contract for anything you persist from it, invalidate on change notifications, and never let a `private`-scoped entry cross a user or tenant (DoD 32).

The reference implementation of this layer is **[AgenticMind](https://github.com/Moai-Team-LLC/AgenticMind)** — citation-enforced knowledge & memory served headlessly over MCP, self-hostable on Postgres + pgvector. Bring-your-own (Mem0 / Zep / Letta / files) stays fine (Principle 2); this is the paved road, not a mandate. See the [`reference-stack`](skills/agentic-product-architect/reference-stack/SKILL.md) skill.

### Stack 5: Durable execution — **mandatory**

Stateless agents lose everything on a crash. The minimal standard:

- **Agent loop** = Workflow (deterministic, replayable from the event log)
- **LLM calls and tool invocations** = Activities (non-deterministic, retryable)
- **State** = a first-class object; the agent must be a pure function (state, event) → new_state

Options:
- **Temporal** — the industry standard; first-party integrations with the OpenAI SDK, Pydantic AI, mcp-agent
- **Inngest / Restate** — operationally simpler; for TypeScript teams
- **LangGraph checkpointer** (Postgres) — built in if you're already on LangGraph

**Human-in-the-loop is a durable pause, not a side channel.** When the loop needs a person — approval for a destructive action (DoD 4), a disambiguation, a judgment call — model it as a **tool call the agent emits** (an MCP *elicitation*, which under revision 2026-07-28 arrives as an `input_required` round trip, Stack 2) that **suspends the workflow on this same durable substrate**, resumed by the human's reply as the next event. The paused run keeps no state in memory and survives a killed process (DoD 7); an approval that blocks an in-process thread — or an out-of-band notification the loop merely waits on — is the anti-pattern: it loses the work on any crash and turns "ask a human" into an availability risk. This unifies what the harness otherwise treats as three separate concerns — the HITL layer (Canon 4), durable execution (here), and the Loop License escalation path (Part IV): a human contact is one more durable tool call, suspended and resumed like any other.

**Fleet operations — when you run many long-lived agents.** Everything above is single-agent durability: one loop pauses, resumes, retries. Operating a *fleet* of scheduled, long-lived agents adds a Day-2 surface the layers above stop short of: the agent as a versioned **deployable manifest** (resources, schedule, runtime, env) distinct from its Agent Contract; **coordinated scheduling** — a lock so a cron fires once across replicas, with misfire handling — backed by a **durable backlog** that survives restarts; per-agent lifecycle (deploy / start / stop / restart) and graceful termination; and **fleet observability** — per-agent health plus an append-only operational audit, layered on the per-run traces of Stack 6. Keep it lean: a runner is a function with limits, not a platform, until a real fleet exists. The `SCORECARD.md` *Fleet operations* section gates this; `examples/agenticops-case-study.md` maps each gate to a reference implementation.

### Stack 6: Observability & Evals

**Do not launch to production without observability.** The minimal set:

| Tool | When to choose |
|---|---|
| **LangSmith** | Deep integration with LangGraph |
| **Langfuse** | OSS / self-hosted; vendor-neutral |
| **Braintrust** | Eval-driven CI/CD deploy gating |
| **Arize Phoenix** | OpenTelemetry-native, ML monitoring lineage |

**Instrument on the OpenTelemetry GenAI semantic conventions — at a pinned revision** — so you can swap vendors later without re-instrumenting. Since semconv v1.42.0 (June 2026) the conventions live in their own repository, `open-telemetry/semantic-conventions-genai`, still in *Development* status and without tagged releases: **pin a commit**, record it with your traces, and run a migration test before you move the pin. Emit an `invoke_agent` span per run with child `chat` and `execute_tool` spans (`create_agent` where agents are provisioned), record token usage (`gen_ai.usage.input_tokens` / `gen_ai.usage.output_tokens`) and `gen_ai.client.operation.duration`, and instrument MCP traffic with the MCP conventions (`mcp.method.name`). **Content capture is off by default**: the conventions say instrumentations should not record prompts and completions unless you opt in (`gen_ai.input.messages`, `gen_ai.output.messages`, `gen_ai.system_instructions`, `gen_ai.tool.definitions` are all opt-in) — switch capture on only by written policy, with retention and access limits. Instrumentation libraries may gate the newest attributes behind an opt-in (e.g. `OTEL_SEMCONV_STABILITY_OPT_IN=gen_ai_latest_experimental` in OpenTelemetry Python), and metric names are still moving — a pinned revision plus a migration test is how you absorb that churn. Datadog, Honeycomb, New Relic, Grafana and the major frameworks emit these conventions natively. This is DoD 29.

**Distinguish LLM observability from agent observability.** LLM observability is per-call (tokens, latency, cost); **agent observability** is trajectory-, multi-turn-, and session-level (did the agent take a sane path?). You need both. Run **online / production evals**: evaluators on completed threads, with failing live traces routed back into the offline eval set.

The reference implementation of this layer is **[AgenticPerformance (APL)](https://github.com/Moai-Team-LLC/AgenticPerformance)** — OTel traces → per-agent golden-set evals with a CI gate, a named failure taxonomy, and a governed improvement loop. Bring your own (LangSmith / Langfuse / Braintrust / Phoenix) is fine (Principle 2); this is the paved road, not a mandate. See the [`reference-stack`](skills/agentic-product-architect/reference-stack/SKILL.md) skill.

### Stack 7: Framework selection

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

### Stack 8: Security & Identity — **cross-cutting**

Security is Principle 6 and the 8th harness layer. It is the largest gap in most agentic products. Anchor the discipline on the **OWASP Top 10 for Agentic Applications (2026 edition)** — ASI01 *Agent Goal Hijack* through ASI10 *Rogue Agents* — which names agent-specific risks (delegated-identity abuse, cross-agent prompt injection, runtime tool composition) that no single "guardrails" layer covers. [`CROSSWALK.md`](CROSSWALK.md) maps every DoD item to the ASI risk it mitigates.

**The lethal trifecta (Willison).** An agent that simultaneously has (1) access to **private data**, (2) exposure to **untrusted content**, and (3) the ability to **communicate externally** can be turned into an exfiltration tool by prompt injection. Run this as a structural check on **every** deployment; if all three are present, break one leg (gate egress, quarantine untrusted input, or scope data) before shipping.

**MCP supply-chain controls.** Community MCP servers are an untrusted supply chain — subject to *tool poisoning*, *rug pulls* (a server mutates tool descriptions after approval), full schema poisoning, and confused-deputy attacks. Therefore:
- **Pin tool definitions by cryptographic hash; alert on any change** (per the OWASP MCP Security Cheat Sheet).
- **Version-pin and signature-check** community servers; install only from an **allow-listed registry**.
- **Re-verify the pin on every refetch.** Revision 2026-07-28 lets servers mark `tools/list` cacheable for `ttlMs`; when the cache expires and the list is fetched again, the hash check runs again. A pin checked only at install is a pin with a TTL.
- Use **OAuth 2.1 + Resource Indicators**; never pass tokens through; never over-scope.

**Protocol & auth baseline (MCP 2026-07-28).** The revision hardened exactly the seams Layer 8 cares about, so the baseline is normative (DoD 26): clients register with **Client ID Metadata Documents** — Dynamic Client Registration is deprecated — validate the authorization server's `iss` (RFC 9207) before redeeming a code, and key persisted credentials by issuer so a token minted for one authorization server is never replayed to another; servers never pass through the token they received. Treat MRTR `requestState` as attacker-controlled and integrity-protect it (HMAC/AEAD) wherever it touches authorization. Every server and client you own runs the official conformance suite in CI at a pinned version.

**Policy enforcement outside the model.** 2026-07-28 puts the JSON-RPC method and the tool, resource, or prompt name in HTTP headers (`Mcp-Method`, `Mcp-Name`) precisely so that intermediaries can route and inspect without parsing the body, and servers reject a header that disagrees with the body. That makes an **MCP gateway a real enforcement point**: authorize per tool at the edge, reject mismatches, and reject protocol versions that predate the headers. It is the network-level form of "permissions in code, not in the prompt" (DoD 5) — and the natural home for it is the model & cost plane (Stack 9 · AgenticGateway).

**Per-agent identity & least privilege.** Each agent acts under **its own non-human identity** — never a shared service account, never a person's token — with short-lived, audience-bound credentials scoped to its declared blast radius; tool execution is sandboxed; identity (and tenant) is derived from auth, never asserted by the model; and every action is attributable to the agent **and** to the human or system that delegated it (DoD 27). NIST's NCCoE concept paper *Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization* (Feb 2026) frames the same problem on OAuth 2.0 and SPIFFE; NIST's AI Agent Standards Initiative (CAISI, Feb 2026) names agent identity and security as a research pillar.

**Inter-agent trust.** Inside your trust boundary an orchestrator calls functions; across it, another agent is an unauthenticated principal until proven otherwise. A2A v1.0 lets agents **sign their Agent Cards** (JWS over the JCS-canonicalized card, keys via `kid` and a `jku` or a trusted keystore) but leaves verification a SHOULD and does not bind the key URL to the card's origin. This standard closes the gap: before delegating across a trust boundary, verify the signature against a trusted keystore or an allow-listed `jku` origin; fail closed on unsigned or unverifiable cards; delegate no more scope than you hold; and treat everything the peer returns as untrusted input (DoD 28, OWASP ASI07).

> **Runnable:** [`templates/security/`](templates/security/README.md) ships a red-team kit — a lethal-trifecta gate, indirect-prompt-injection test cases, and an MCP tool-definition hash-pinning / rug-pull detector.

The reference implementation for red-teaming this layer is **[AgenticAssurance (AAL)](https://github.com/Moai-Team-LLC/AgenticAssurance)** — an OWASP-Agentic / MITRE-ATLAS attack library plus a toxic-flow graph that finds lethal-trifecta / RCE composition paths single-prompt scanners miss, emitting SARIF for CI code-scanning. It operationalizes the lethal-trifecta check above; framework-neutral, not a runtime guardrail (Principle 2). See the [`reference-stack`](skills/agentic-product-architect/reference-stack/SKILL.md) skill.

### Stack 9: Cost & FinOps — **cross-cutting**

Agentic systems are expensive in a way chat never was. Anthropic reports agents use **~4× the tokens of chat, and multi-agent systems ~15×**; Gartner puts agentic tasks at **5–30× the tokens** of a standard chatbot; the FinOps Foundation's *State of FinOps 2026* finds **98% of orgs now manage AI spend** (up from 31% two years prior). Token usage alone explains ~80% of cost variance; tool-call count and model choice are the other two factors.

Make cost a first-class engineering constraint, not a month-end surprise:
- **Per-run token / cost ceilings enforced in code** — a circuit breaker that halts a runaway autonomous session. (Most published multi-agent architectures leave this gap open; close it.)
- **Prompt / KV caching** on stable prefixes (system prompt, tool schemas): up to ~90% cost and ~85% latency reduction on long prompts.
- **Model routing / cascades** — small model for routing & classification, flagship for reasoning.
- **Measure cost-per-outcome, not just total spend** — wire cost into the same traces as Stack 6.
- **The multi-agent economics rule:** only pay the 15× when the task value justifies it. If a single agent clears the bar, the orchestra is waste.
- **Re-derive ceilings on every model change.** A ceiling is a number of tokens at a price; both move with the model. When Anthropic released Claude Opus 5.5 (Sep 2026) it priced tokens 20% below Opus 5 and put typical workload cost 40% lower — a ceiling copied from the old model is now either loose or meaningless. The model-swap runbook re-measures cost per task and re-derives ceilings and routing before the swap ships (DoD 15).

The reference implementation of this layer (together with Stack 1) is **[AgenticGateway](https://github.com/Moai-Team-LLC/AgenticGateway)** — per-run/tenant cost ceilings enforced in code, prompt + semantic caching, and eval-sourced routing behind one OpenAI-compatible key. Bring your own gateway (LiteLLM / Portkey / raw Bifrost) is fine (Principle 2); this is the paved road, not a mandate. See the [`reference-stack`](skills/agentic-product-architect/reference-stack/SKILL.md) skill.

---

## Part III. Production readiness — Definition of Done

<!-- canon:begin:standard.dod -->
An agentic product is **not production-ready** until every item below that binds to it is satisfied. There are **33 items**. Numbers are stable identifiers — never reused or renumbered — so a group may list them out of order. An item marked with a condition in italics binds only when that condition holds; every other item binds for every production system. [`SCORECARD.md`](SCORECARD.md) sets the maturity band at which each item becomes mandatory; [`CROSSWALK.md`](CROSSWALK.md) maps each item to the EU AI Act, the OWASP Top 10 for Agentic Applications, the NIST AI RMF, and IMDA's agentic framework.

### Context and state
- [ ] **1.** Context stays within a **measured budget** in a typical cycle — the fill level at which your own eval pass rate starts to degrade for the model in use; until you have measured it, the default is **40% of the window**
- [ ] **2.** State is externalized — it does not live only in the context window, or in a protocol session
- [ ] **3.** Compaction pipeline tested on long-running scenarios

### Tools and permissions
- [ ] **4.** All destructive actions require explicit human approval — at every oversight mode, O2 included
- [ ] **5.** Permissions enforced by code, not by prompt
- [ ] **6.** Tool execution sandboxed (containers / OAuth scopes / least privilege)
- [ ] **32.** *(If multi-tenant)* Tenant isolation enforced below the LLM (row-level security / repository layer); `tenant_id` derived from auth, never from the model; retrieval, memory, cache (including MCP `private`-scoped results), traces, and sub-agents all tenant-scoped; a code-asserted cross-tenant leakage eval runs in CI — see the `tenant-isolation` skill

### Reliability
- [ ] **7.** Durable execution: pause/resume/retry works across a killed process
- [ ] **8.** Structured outputs validated by schema; assertions on the critical path
- [ ] **9.** Guardrails (minimum: PII, jailbreak, schema validation) on input and output

### Evals and observability
- [ ] **10.** Eval set ≥50 examples per top-priority failure mode
- [ ] **11.** *(Wherever an LLM judge is used)* LLM judges calibrated against human labels (TPR/TNR tracked)
- [ ] **12.** CI blocks deploy on eval regression; 100% of production traces logged
- [ ] **29.** Telemetry follows the **OpenTelemetry GenAI semantic conventions at a pinned revision** (a commit of `semantic-conventions-genai` until it publishes tagged releases), with `invoke_agent`, `chat`, and `execute_tool` spans and token usage recorded; **prompt and completion content is not captured by default** — capture is switched on by a written policy with retention and access limits; a schema test runs on exported traces, and bumping the pinned revision runs a migration test first

### Security and identity
- [ ] **13.** Lethal-trifecta check performed and documented (private data × untrusted content × external comms — at least one leg broken if all three are present)
- [ ] **14.** *(Wherever MCP is used)* MCP tool definitions pinned by hash with change alerts — re-verified whenever a cached tool list expires; servers installed only from an allow-listed registry, version-pinned and signature-checked (auth baseline: item 26)
- [ ] **26.** *(Wherever MCP is used)* Every MCP connection speaks revision **2026-07-28** — or carries a dated sunset — and passes the official conformance suite in CI at a pinned version; no state depends on a protocol session; no new dependency on Roots, Sampling, or Logging; `requestState` is treated as untrusted and integrity-protected where it affects authorization; clients register with Client ID Metadata Documents (never Dynamic Client Registration alone), validate `iss` (RFC 9207), and key stored credentials by issuer; no token passthrough, anywhere (Stack 2 · Layer 8)
- [ ] **27.** Every agent acts under **its own non-human identity** — never a shared service account or a person's credentials — with short-lived, scope-limited, audience-bound credentials issued by your identity provider; every action is attributable in traces to the agent identity **and** to the human or system that delegated the task (Layer 8)

### Cost
- [ ] **15.** Per-run token / cost ceiling enforced **in code** (circuit breaker on runaway sessions); cost-per-task tracked in traces; ceilings re-derived whenever the model or provider changes

### Operating without per-action approval (O1+) — the Loop License
- [ ] **16.** *(At oversight O1 or O2)* **Loop License** held: eval threshold (pass@1 **and** pass^5 on a representative set), regression gate, declared blast radius, cost cap, kill switch, and escalation path — all six declared, enforced in code, and tested (Part IV; [`CHECKLIST`](templates/loop-license/CHECKLIST.md))
- [ ] **17.** *(At autonomy L3+ or oversight O1+)* Stop conditions declared in the Agent Contract and enforced by the runner: max iterations, token/time/spend budgets, timeout, escalation after N consecutive failures (Part IV)
- [ ] **18.** *(At oversight O1 or O2)* Independent verification: the producing model does not grade its own work; deterministic checks first; any LLM judge is calibrated (items 11 and 20) and decorrelated from the writer; the checks, graders, and eval sets sit outside the agent's write scope (Part IV)
- [ ] **19.** *(At oversight O1 or O2)* Loop economics: cost per run and cost per *verified* outcome tracked in traces; per-run and per-window cost caps declared (Part IV · Layer 9)
- [ ] **30.** *(At oversight O2)* A sample of runs scored as successful is reviewed each release for **illegitimate success** — tampered or skipped tests, special-cased graders, hard-coded outputs, work routed around a check; the **legitimacy rate** is published with the eval results and gates promotion alongside the pass rate (Part IV · *Independent verification*)

### Measurement science and human oversight
- [ ] **20.** *(Wherever an LLM judge gates O1+ operation, auto-apply, or release)* The gating judge has **documented calibration** — accuracy + calibration error (ECE/Brier) against an anchored ground-truth sample within a declared recency window; no unvalidated verbalized confidence used as a gating signal (Part V · *Judge calibration*)
- [ ] **21.** *(Wherever memory or retrieval is used)* Memory/retrieval components evaluated with **retrieval metrics** (≥ Recall@k, MRR) on a labeled set, independently of end-to-end task evals; embedding/chunking/index changes pass a declared **retrieval regression gate** (Part V · *Retrieval evaluation* · Stack 4)
- [ ] **22.** Golden sets declare **labeling provenance** (rubric version, labeler type, date, agreement); unanchored sets do not back a license or release gate; rubrics are versioned instruction artifacts with judge re-baselining on change (Part V · *Ground-truth discipline* · Part IV)
- [ ] **23.** Input drift monitored vs. the eval distribution with a declared **eval-refresh policy**; provider-hosted models canaried, a detected change triggering the eval regression gate (item 12) (Part V · *Drift monitoring*)
- [ ] **33.** *(Wherever a human approval counts as a control; the oversight plan at O1+)* Human approval and review are run as a program: **override rate** and **approval latency** (p50/p95) are measured per queue, and a **rubber-stamp alarm** — near-total approval at latencies too short to have read the action — triggers a review; at **O1+** the Loop License declares the oversight plan (sampling schedule per mode, reviewer SLA, re-escalation triggers) and reviews are captured as stratified labeled data (Part V · *Human oversight*)

### Gate integrity
- [ ] **24.** No safety-class gate is disabled repo-wide to pass CI — a correctness test, type-safety (`no-unsafe-*` / `no-explicit-any`), security lint, or a coverage/mutation floor; a false positive is scoped to a file/glob with a named reason and the gate re-proven to still fire (Canon 5, *gate-integrity invariant*). Binds wherever such a gate exists.

### Composition (multi-agent)
- [ ] **25.** *(Any graph of agents operating at O1+)* **Graph License** held: the six gates re-evaluated at graph scope (graph-level golden tasks, regression gate, blast radius as the union of node radii **plus** the shared state store, per-node **and** aggregate cost caps, a kill switch tested against in-flight parallel branches, one named escalation owner); the **weakest-link bound** holds on every path to an external action; shared state carries writer provenance and verification status; every fan-in is a declared verification point or a rationalized pass-through; every edge class is marked **enforced** or **declared**, and declared-only edges are not counted as controls (Part IV · [`CHECKLIST`](templates/graph-license/CHECKLIST.md))
- [ ] **28.** *(Wherever work is delegated across a trust boundary)* Before delegating across a trust boundary — another organization, vendor, or independently operated service, typically over A2A — the peer's **signed Agent Card is verified** (JWS over the JCS-canonicalized card, keys from a trusted keystore or an allow-listed `jku` origin); unsigned or unverifiable peers fail closed; the delegated scope never exceeds the delegator's own; the peer's output enters as untrusted input (Part IV · *Edges are ingestion boundaries*)

### Governance and regulation
- [ ] **31.** *(Wherever the product is exposed to a regulated jurisdiction, e.g. EU users)* A written record states the jurisdictions the product is exposed to and, for each regime, the product's **role** and **risk class** — under the EU AI Act: provider or deployer; prohibited, high-risk (Annex I or III), transparency (Art. 50), or minimal; general-purpose-model dependencies — with the application dates that bind it; the record has an owner and is re-reviewed whenever the intended purpose, user base, or model changes ([`CROSSWALK`](CROSSWALK.md))

> **Score yourself.** [`SCORECARD.md`](SCORECARD.md) turns this DoD into a Yes/No maturity self-assessment (M0–M3, mapped to the operating envelope) — run it with the team against a real deployment each release, or let [`aps-conformance`](docs/conformance.md) score it in CI.

<!-- canon:end:standard.dod -->

---

## Part IV. The Loop License — acting without per-action approval (O1+)

The Autonomy Ladder (Canon 1) and the Cycle of Trust (Canon 5) hold that autonomy is *earned*, not granted. This Part makes that concrete for the hardest case: a system whose consequential actions execute **without a human approving each one** — oversight **O1** (a human supervises live and can intervene) or **O2** (no one watches in real time) — at any autonomy level. Typically that is an agent finding its own work and looping (L3–L4); but a nightly L2 pipeline that auto-applies its output is in scope too, and an L3 orchestrator whose every external action waits for approval is not. The market calls this *loop engineering*; done without discipline it produces **a factory with no quality control**. The **Loop License** is the standard's answer: the conditions a system MUST satisfy *before* its oversight is relaxed, and MUST keep satisfying to stay there.

Everything in this Part binds at **O1+**; a few requirements bind at **O2** only, and say so. At O0 — a human approves each consequential action — the Part is recommended, not required, except the stop conditions, which also bind at L3+ under O0. (Until v4.0 this Part bound at "L3+ unattended"; ADR-0004 explains the split into two axes.)

### The Loop License

> **MUST — no operation at O1+ without all six of these declared, enforced in code, and tested:**
> 1. **Eval threshold** — named minimums on a representative eval set, measured before promotion: **pass@1** *and* **pass^5** (all five of five attempts succeed), because consistency, not an average, is what an unwatched system runs on (Canon 1 · Part V). At O2 the **legitimacy rate** (DoD 30) is part of this gate. Below any of them, oversight is not relaxed.
> 2. **Regression gate** — CI blocks promotion when the eval pass rate drops against the recorded baseline (DoD 12). A loop that can silently regress has no license.
> 3. **Declared blast radius** — the maximum scope one run can affect (files, records, spend, external calls, tenants), written down and enforced below the model, never asserted by it. Its strongest form is a **typed safe-output channel**: the agent runs read-only and emits typed action requests; a separate, deterministic applier that holds the write credential validates each request against policy and executes it ([`templates/safe-outputs/`](templates/safe-outputs/README.md)).
> 4. **Cost cap** — a per-run and per-window token/spend ceiling, enforced in code, that halts the loop (Layer 9 · DoD 15).
> 5. **Kill switch** — an out-of-band control that stops the loop mid-flight without a redeploy, reachable by a human who is not the agent.
> 6. **Escalation path** — a named human (or higher-authority system) the loop hands to on repeated failure, on hitting a stop condition, or on any action outside the declared blast radius.

These are not six nice-to-haves; they are one license. Missing any single gate caps the system at **O0** — every consequential action human-approved — regardless of how good the model is. The one-page [`templates/loop-license/CHECKLIST.md`](templates/loop-license/CHECKLIST.md) is the artifact to run against a real deployment, with the team in the room. The license also carries a **human-oversight plan** — a sampling schedule per oversight mode, a reviewer SLA, and automatic re-escalation triggers (Part V, *Human oversight as a program*) — and, where its gates rely on a judge, that judge's **calibration status** (Part V, *Judge calibration*).

### Independent verification

The most common way a loop launders a wrong answer into a shipped one is **self-verification**: the same model that produced the work also declares it correct.

> **MUST, at O1+:**
> - **Self-check by the producing model does not count as verification.** A model grading its own output shares its own blind spots and failure correlations; a pass tells you nothing new.
> - **Deterministic-first.** Verify with a deterministic check — tests, schema, assertion, type-check, invariant, diff against a known-good — wherever the property admits one. Reach for an LLM judge only for properties that genuinely require judgment.
> - **The judge has its own eval.** An LLM judge is itself an agent under this standard: calibrated against human labels, TPR/TNR tracked (DoD 11). An uncalibrated judge is not verification — it is a second opinion of unknown quality.
> - **The checker is decorrelated from the writer.** A different model, or a materially different prompt and context; no shared scratchpad; and it sees the *artifact*, not the writer's reasoning about why the artifact is fine.
> - **The checks are out of the agent's reach.** Tests, graders, eval sets, and thresholds sit outside the agent's write scope. A loop that can edit the test it is graded by has no verification, only a mirror.

**Writer / Checker, done right (reference pattern).** A Writer produces the artifact under its Agent Contract. A Checker — a separate agent with its own contract, its own eval, and a deterministic layer in front of its judgment — receives only the artifact and the acceptance criteria, and returns a *hard-to-vary* verdict (each criterion names the single probe that falsifies it). The Writer never sees the Checker's internals; the Checker never sees the Writer's chain of thought. Disagreement escalates — it is not averaged away.

### Success legitimacy — a pass is not a success until someone has looked

A check the agent can satisfy without doing the task measures its skill at satisfying checks. METR's *Frontier Risk Report* (May 2026) found that on tasks longer than eight hours, at least 16% of the runs its automated scoring counted as successful were illegitimate on review — tests edited, graders special-cased, the work routed around the check — with well over 100 distinct instances of cheating. An unwatched loop optimizes against whatever checks it faces; the pass rate rises while the capability does not, and the license is issued on a number that measures gaming.

> **MUST, at O2:**
> - **Audit a sample of successes** each release — stratified by task type, reviewed for the *path*, not only the outcome: diffs to tests or graders, skipped assertions, special-cased inputs, outputs that match the checker rather than the task.
> - **Publish the legitimacy rate** (legitimate successes ÷ reviewed successes) next to pass@1 and pass^5; a declared floor gates promotion (Loop License gate 1).
> - **Turn every illegitimate success into a regression case** and, where the property admits one, a deterministic tripwire.
>
> At O1 the audit is recommended; keeping the checks out of the agent's reach (*Independent verification*, above) binds at O1+. This is DoD 30 and anti-pattern 20.

### Stop conditions & fail paths

An unattended loop with no declared way to stop is the defining L4 anti-pattern.

> **MUST — every agent spec at L3+ or O1+ declares, and the runner enforces:**
> - **Max iterations** — a hard turn/step ceiling per run.
> - **Budgets** — token, wall-clock, and spend ceilings (the cost cap of the Loop License).
> - **Timeout** — a maximum run duration after which the loop is cancelled, not left hanging.
> - **Escalation after N failures** — a named threshold of consecutive failed attempts (verification failures, tool errors, guardrail trips) that hands to the escalation path instead of retrying forever.

These are **mandatory sections of the Agent Contract** (`AGENT_STANDARD.md`), declared at design time, not discovered in production. This is DoD item 17.

### The ingestion boundary — "find work" is untrusted input

An L4 loop that selects its own work reads that work from somewhere — a queue, an inbox, a repo, a webhook, a scraped page. **Every one of those is untrusted input.** Treating the find-work step as trusted is how a loop gets hijacked into doing the attacker's work instead of yours (OWASP **LLM01 Prompt Injection**; agentic **ASI01** *Goal Hijack*).

> **MUST, at O1+:**
> - **Injection tests live in the eval suite.** The find-work path is fuzzed with indirect-injection payloads as part of the standing eval set (Layer 8 · DoD 13), not tested once by hand.
> - **Instructions and data are separated.** Ingested content is data; it is never concatenated into the instruction channel where it can rewrite the agent's goal (Layer 8 · indirect prompt injection).
> - **Least privilege on triggers.** What can enqueue work for the loop — and what that work is allowed to reach — is scoped and allow-listed. A trigger is a capability, not an open door.
> - **Protocol state is input too.** An MCP `requestState` echoed back by a client and a result returned by an A2A peer arrive from outside the trust boundary; they are validated like any other untrusted input (DoD 26, 28).

**Threat checklist:** `[ ]` find-work source classified as untrusted · `[ ]` indirect-injection cases in the eval suite · `[ ]` instruction/data channels separated, verified under a poisoned input · `[ ]` trigger sources allow-listed and least-privileged · `[ ]` egress from a triggered run gated (lethal-trifecta check, Layer 8).

### The instruction supply chain

Skills, prompts, system instructions, tool descriptions, trigger rules, and judge rubrics (Part V) are **executable artifacts that steer the loop** — and therefore a supply chain, subject to the same discipline as code dependencies (OWASP **LLM03 Supply Chain**; **AIUC-1** control expectations). A "factory with no QC" is usually a factory whose *instructions* were never version-controlled or evaluated.

> **MUST, at O1+:**
> - **Versioned** — every skill/prompt/instruction artifact carries a version; what shipped is knowable.
> - **Provenance** — who authored it, from what source, and why (the change's intent) is recorded.
> - **Evaluated before deploy** — an instruction change is promoted through the same eval gate as a code change (Part V), never hot-edited into a live loop.
> - **Regression-tested on update** — updating an instruction re-runs its evals; a prompt change that drops the pass rate is a regression (DoD 12), not a tweak.
> - **Trigger-collision audited** — where many skills/agents share a trigger space, overlapping or ambiguous activation is audited; two artifacts silently competing for one trigger is a supply-chain defect.
> - **Spec-valid, scanned, and hash-locked** — skills conform to the open **Agent Skills specification** (agentskills.io; validate with the reference `skills-ref` tool or equivalent), are scanned for hidden instructions (invisible Unicode, HTML comments, piped installers) before install, and ship with a **lockfile of content hashes** so an installed copy can be checked against the version that was evaluated. Snyk's *ToxicSkills* scan of 3,984 public skills (Feb 2026) found critical-level security issues in 13.4% of them and 76 confirmed malicious payloads; OWASP has opened an *Agentic Skills Top 10* project in response.

This is the direct answer to "a factory with no QC": the instructions *are* the tooling on the line, and they get inspected like it.

### Economics of the loop

A loop makes cost a first-class risk: it can spend without a human noticing. Layer 9 sets the cost controls; this Part sets what a licensed loop MUST *know* about its own economics.

> **MUST:**
> - **Measure cost per run** — token and spend, attributed per run, in the same traces as Stack 6.
> - **Measure cost per *verified* outcome** — spend divided by outcomes that passed independent verification, not raw completions. A loop that is cheap per call but rarely produces a verified result is expensive, and only this metric shows it.
> - **Declare cost caps** — the per-run and per-window ceilings of the Loop License, stated up front.

The standard fixes **what** to measure and declare, not **how**: the reference implementations of enforcement and measurement are the model/cost plane (Stack 9 · AgenticGateway) and the observability plane (Stack 6 · AgenticPerformance). This is DoD item 19.

### Architecture-phase declarations

Two properties decide whether a loop is operable, and both MUST be **declared during design, not reconstructed after an incident**:

> **MUST — the Agent Contract declares, at architecture time:**
> - **The operating point** — the autonomy level and the oversight mode the system runs at (Canon 1). What runs in production must match what was licensed; relaxing oversight is a release, not a toggle.
> - **The memory model** — what the loop persists, for how long (retention), where it came from (provenance), and whether a past run can be **replayed** from it. *"Where does the state live on step 7?"* must have an answer on the whiteboard, not in a post-mortem.
> - **The determinism map** — which steps are deterministic (pure functions, tools, checks) and which are model-driven, so durability, replay, and verification attach to the right steps (Stack 5). A loop whose determinism boundary is unknown cannot be made durable or independently verified.

These are **mandatory sections of the Agent Contract**, alongside the stop conditions above.

### License Composition — graphs of licensed loops

Wiring loops into a graph — nodes doing work, edges routing between them, shared state flowing underneath — **multiplies** the Loop License question instead of answering it. The market calls this *graph engineering*. This section defines how licenses compose.

It binds the **topology, not the runtime**: the requirements below take no position on which framework draws the graph (that is Stack 7's question), and they hold whether the edges are a runtime construct, a set of queues, or an orchestrator calling sub-agents.

> **MUST — no license inheritance by wiring.** A graph of licensed loops is not itself licensed. A graph operating at **O1+** MUST hold its own **Graph License**: the six gates, re-evaluated at *graph* scope.
> 1. **Eval pass-rate threshold** on **graph-level golden tasks** — end-to-end outcomes, not the union of per-node suites. Nodes that each pass in isolation routinely fail in composition.
> 2. **Regression gate** on that graph-level set (DoD 12).
> 3. **Declared blast radius** — the **union** of every node's radius **plus the shared state store**, which is a blast surface in its own right.
> 4. **Cost caps — per-node *and* aggregate.** Fan-out multiplies burn: per-node caps alone do not bound a graph, because the graph's spend is the product of its branching, not the max of its nodes.
> 5. **Kill switch** that verifiably halts **all** nodes — including in-flight parallel branches. "Verifiably" means tested, with the in-flight case in the test.
> 6. **Escalation path** — **one** path with **one** named owner for the graph as a whole. A graph in which each node escalates to its own owner has no owner.

The one-page [`templates/graph-license/CHECKLIST.md`](templates/graph-license/CHECKLIST.md) is the artifact to run against a real deployment; it is the sibling of the loop-license checklist and assumes it. This is DoD item 25.

**The weakest-link bound.**

> **MUST — the oversight under which a graph executes an external action MUST NOT be more relaxed than the least-licensed node on the path producing that action allows.** An unlicensed node — or one gated by an uncalibrated judge (Part V) — anywhere on an action path caps that path at **O0** (propose-approve), regardless of how well-licensed the other nodes are. Licensing is a property of paths, not of averages.

**Shared state carries provenance.**

> **MUST, at O1+:** every shared-state field carries **writer provenance** — the producing node, a timestamp, and a verification status (`verified_by: <check|judge>`, or `unverified`). Consumers MUST be able to **filter on verification status**, and action nodes MUST NOT trigger external actions from `unverified` fields. State that cannot say where it came from cannot be trusted to authorize anything.

**Fan-in is a verification point.**

> **MUST — every merge point where parallel branches join is declared either a verification point** (a deterministic check or a calibrated judge validates the merged state before anything downstream consumes it) **or an explicit pass-through with written rationale.** Unverified aggregation upstream of an external action is prohibited at O1+.

Aggregating parallel outputs and treating the aggregate as validated is **self-verification in graph form** — the failure named under *Independent verification* above, wearing a topology instead of a prompt. Merging does not add correctness; it only adds confidence.

**Edges are ingestion boundaries.**

> **MUST — a node's output is untrusted input to the nodes downstream of it.** Inter-node handoffs fall under *The ingestion boundary* above in full. The graph's eval suite MUST include **poisoned-state scenarios**: a compromised, hijacked, or simply hallucinating node writing to shared state, with the assertion that downstream nodes do not act on it.

> **MUST — reviewer nodes are judges.** A node whose job is to review another node's work is an LLM judge, and Part V applies to it in full: calibration, the bias battery, and decorrelation from the producer it reviews — **per edge**, not merely once per loop. A reviewer that is decorrelated from one producer and not from another is calibrated for one edge only.

**Declared vs. enforced topology.**

> **MUST — architecture-phase declarations state, per edge class, whether routing is *enforced* or *declared*.** **Enforced** means the runtime or the code constrains it: the edge cannot be traversed otherwise. **Declared** means the agent is *expected* to follow it — an SOP, a skill, a prompt. **Declared-only edges MUST NOT be counted as controls in any license.**

A topology that exists only in prose is documentation, not a guardrail (Principle 6 — security is a structural property). This is the graph-scale form of "permissions enforced by code, not by prompt" (DoD 5): an instruction-defined route is exactly as binding as an instruction-defined permission, which is to say not at all under adversarial input.

### Glossary bridge — the loop- and graph-engineering lexicon

Teams arrive with the market's vocabulary. This standard already holds the concepts under its own names; here is the bridge, so clients are met, not re-educated.

The market narrates its craft as a ladder of five layers. The ladder is a useful map of *what people are talking about*; it is not an architecture. Each rung maps onto something this standard already governs:

| Market term ("the five layers") | This standard |
|---|---|
| Prompt engineering | The **Agent Contract** and its instructions (`AGENT_STANDARD.md`) |
| Context engineering | **Stack 3** — context engineering's four operations, and **Stack 4** memory |
| "Harness" | The **harness** (Canon 4) — nine layers, of which the market's usage covers roughly Layers 1–3 |
| Loop engineering | The **Agent Loop** running without per-action approval (O1–O2), typically at L3–L4, governed by the **Loop License** (this Part) |
| Graph engineering | The **five composition patterns** (Canon 2), governed by **License Composition** (this Part) |

| Market term (loop engineering) | This standard |
|---|---|
| Loop / loop engineering | Operation without per-action approval — oversight **O1–O2** (Canon 1), typically at L3–L4 — governed by the **Loop License** (this Part) |
| Human in / on the loop, unattended | The three **oversight modes** O0 / O1 / O2 (Canon 1) — a separate axis from autonomy |
| Reward hacking / specification gaming | **Illegitimate success** — caught by the success-legitimacy audit (this Part · DoD 30) |
| Intent debt | Acceptance criteria that are not *hard-to-vary* — the gap the **Cycle of Trust** (Canon 5) and eval discipline (Part V) close |
| Writer / Checker | **Independent verification** (this Part): a decorrelated producer and verifier, each an agent under its own contract |
| State / working memory | **Memory** (Stack 4) + the **memory-model** architecture-phase declaration |
| Find work | The **ingestion boundary** (this Part) — untrusted input, OWASP LLM01 |
| Blast radius / kill switch | Loop License gates 3 and 5 (this Part) |
| Factory with no QC | A loop missing **independent verification** and running an unmanaged **instruction supply chain** |
| Autorater / model grader | **Judge** — an LLM verifier, itself an agent under this standard, calibrated per Part V |
| Model card (for a grader) | **Judge Card** — the versioned calibration record of a judge (Part V · AgenticPerformance) |
| Eval set / benchmark | **Golden set** — with declared labeling provenance (Part V · *Ground-truth discipline*) |
| Operating envelope / Authority to Operate (ATO) | **Loop License** (Part IV), of which calibration and oversight status are inputs |
| Graduation / promotion criteria | The **Cycle of Trust** (Canon 5) — earned autonomy, re-escalating on regression |
| Graph / graph engineering | A **composition pattern** (Canon 2) wired for operation at O1+, governed by **License Composition** (this Part) |
| Node | One agent (or deterministic step) in a composition, under its own Agent Contract and — where it runs at O1+ — its own Loop License |
| Agent Card | A2A's machine-readable description of an agent — **signed** since v1.0 and verified before any cross-boundary delegation (DoD 28) |
| Edge | A handoff between nodes. An **ingestion boundary** (this Part): the upstream node's output is untrusted input downstream |
| Shared state | The store nodes read and write between steps — **Memory** (Stack 4) at graph scope, carrying **writer provenance** and a verification status |
| Fan-out / fan-in | Parallel branching and its merge. Fan-out multiplies the **cost cap** question; fan-in is a **verification point** (this Part) |
| Declared vs. enforced topology | Whether an edge is constrained by code/runtime (**enforced**, countable as a control) or merely instructed (**declared**, never countable) |
| Weakest-link bound | The rule that a path runs under no more relaxed oversight than its **least-licensed** node allows (this Part) |
| Supervisor / router / handoff | Named instances of the **five composition patterns** (Canon 2); the governance is the same regardless of the name |
| Graph License / license composition | The **Graph License** (this Part) — the six gates re-evaluated at graph scope, plus the weakest-link bound |

---

## Part V. Eval discipline & measurement science (per Husain/Shankar)

This discipline matters more than the choice of framework. The rules below set the shape of an eval program; the *measurement science* subsections that follow set what makes its numbers trustworthy — because an autonomy license (Part IV) is only as sound as the evals and judges behind it.

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
7. **Track reliability with `pass^k`, not just `pass@1`.** `pass^k` (does it succeed on *all* k attempts) exposes the consistency that a single run hides — the metric that matters for anything autonomous. Relaxing oversight gates on it: the Loop License requires a declared `pass^5` threshold (Canon 1 · Part IV).
8. **Run online evals.** Evaluators on completed production threads, with failing live traces routed back into the offline set (closes the loop with Stack 6).

*Reference benchmarks (as orientation, never as ground truth — see anti-pattern 12): τ-bench / τ²-bench (policy adherence, dual-control), SWE-bench Verified, GAIA, TerminalBench, WebArena. LLM-as-judge agrees with humans ~85% of the time but carries position / verbosity / self-preference bias — keep judges binary and calibrated.*

> **Runnable:** [`templates/ci/eval-gate.yml`](templates/ci/eval-gate.yml) is a copy-paste CI workflow that blocks a merge when the eval pass-rate drops below the ≥90% gate (DoD item 12) — and, when your eval report carries them, when `pass^5` or the legitimacy rate drops below the thresholds your Loop License declares.

### Judge calibration & bias

**Calibration** is the agreement between a judge's stated confidence and its empirical accuracy — a judge that says "90% confident" should be right ~90% of the time. Measure it with **ECE** (Expected Calibration Error: bin verdicts by confidence, take the weighted mean gap between accuracy and confidence) and the **Brier score** (mean squared error of confidence vs. outcome); a **reliability diagram** plots confidence against empirical accuracy, with the diagonal as perfect. Verbalized LLM confidence is systematically **over**confident — untrustworthy until validated. Usable confidence signals are **self-consistency** (sample the judge k=3–5 times; the agreement fraction is the signal) and **swap-consistency** (score `(A,B)` and `(B,A)`; a verdict that flips with order is **position bias**, not judgment). Screen every judge for position, **verbosity** (favoring longer output), and **self-preference** bias (favoring its own model family — the mechanism behind the decorrelation rule in Part IV). Keep **reliability vs. validity** distinct: judge–judge agreement is not correctness; validity requires anchoring to ground truth (human labels or deterministic outcomes), or high agreement is merely **correlated error**. This *deepens* eval rule 3 and DoD item 11 (TPR/TNR accuracy) for judges that gate autonomy — accuracy and confidence-calibration are one requirement stated at two depths, not two competing bars.

> **MUST — a verdict that gates operation at O1+, auto-apply, or release:**
> - comes from a judge with **documented calibration** — accuracy and calibration error measured against an anchored ground-truth sample, within a declared recency window, above declared thresholds;
> - **never** uses unvalidated verbalized confidence as the gating signal — use validated self-consistency or swap-consistency;
> - pairwise judging **MUST** randomize order or apply a swap-consistency check.
>
> Judges **SHOULD** be screened for position, verbosity, and self-preference bias. A judge's **calibration status is an input to the Loop License** (Part IV): an uncalibrated judge invalidates the license for the levels it gates, and its low-confidence verdicts abstain and escalate rather than passing. *(Reference artifact: the versioned **Judge Card** — AgenticPerformance.)*

*Compliance note: supports EU AI Act Art. 15 (accuracy & robustness) declarations.*

### Retrieval evaluation

Retrieval failures and reasoning failures are different diseases; an end-to-end eval that conflates them cannot direct a fix. Evaluate retrieval on its own terms: **Recall@k** (fraction of queries whose relevant item is in the top-k — the primary memory-retrieval metric), **MRR** (Mean Reciprocal Rank of the first relevant item — "how high did the right thing land"), **Precision@k** (when the context-window budget is tight), and **NDCG@k** (only when relevance is *graded*, not binary). In RAG framing, **context precision / recall** separate retrieved-context relevance from coverage of what was needed to answer.

> **MUST:**
> - Memory or retrieval components are evaluated with retrieval-specific metrics (at minimum **Recall@k** and **MRR**) against a **labeled retrieval set**, independently of end-to-end task evals;
> - any change to the **embedding model, chunking, or index parameters** passes a declared **retrieval regression gate** before deploy (starting bar: no Recall@5 regression; `pass^3` for release-critical suites).
>
> Failure analysis **SHOULD** attribute each failure to a pipeline stage — `retrieval_miss | reasoning_error | tool_error | verification_error` — so improvement is directed, not guessed.

*Citations prove the answer was grounded in what was retrieved; Recall@k proves the right memory was retrievable — auditability needs both. Reference: AgenticMind retrieval harness; the staged failure taxonomy in AgenticPerformance.*

### Ground-truth discipline

A golden set is only as trustworthy as its labels. A **rubric** (rater guideline) is the written labeling standard — definitions, positive and negative examples, edge-case rules; on this line **LLM judges are raters and rubrics are their guidelines**. Measure **inter-annotator agreement (IAA)** with chance-corrected statistics — **Cohen's κ** (two raters), **Fleiss' κ** (n raters), **Krippendorff's α** (missing data / ordinal); conventional bands: 0.6–0.8 substantial, >0.8 strong. Diagnostically, sustained κ < 0.6 signals an **ambiguous rubric**; sustained κ > 0.95 between "independent" judges signals **suspected correlation** → run a decorrelation review. **Gold questions** (known-answer probes mixed into the judging stream) QA the judge continuously; **adjudication** (a third judge or a human) resolves disagreements, and adjudicated items are the highest-grade golden material. A golden set without **labeling provenance** is **unanchored** — you cannot know what its pass rate means.

> **MUST:**
> - Golden sets declare **labeling provenance**: rubric version, labeler type, label date, and agreement statistics where multiple labelers were used. **Unanchored sets MUST NOT back an autonomy license or a release gate;**
> - judge **rubrics are versioned instruction artifacts** under the Instruction Supply Chain (Part IV) — a rubric change **MUST trigger judge re-baselining**.
>
> Multi-judge verification **SHOULD** monitor inter-judge agreement: sustained near-perfect agreement **MUST** trigger a decorrelation review, sustained low agreement a rubric review. Judges **SHOULD** be qualified against gold questions before gating duty and monitored with gold probes after.

### Drift monitoring

Drift monitoring answers one question — **"when did my evals stop representing production?"** — turning golden-set upkeep from a calendar habit into a triggered obligation. Taxonomy: **input drift** (task/query mix diverges from the eval distribution), **concept drift** (what counts as a correct outcome changes), **behavior drift** (the agent's action / tool-call mix shifts), **upstream drift** (source APIs or tool contracts change), and **provider drift** (a hosted model silently updated). Detect distribution shift with **PSI** (bands: <0.1 stable, 0.1–0.25 watch, >0.25 act) or a two-sample test; in the LLM era an **embedding-space** method works well — the drift score is the centroid cosine shift plus the AUC of a classifier trained to tell production from golden embeddings (≈0.5 means same distribution, →1.0 means drifted). Note that temperature-0 is not determinism across providers, so canary comparison needs semantic-similarity tiers, not exact match alone.

> **MUST:**
> - Deployments **monitor input drift** relative to the eval distribution and declare an **eval-refresh policy** — drift thresholds and the triggered action (e.g., auto-open a golden-set refresh);
> - systems relying on **provider-hosted models SHOULD run scheduled canary evaluations** to catch unannounced model changes; a detected change **MUST trigger the eval regression gate** (DoD 12 · Loop License gate 2) before continued reliance;
> - **behavior drift** (e.g., tool-call distribution) **SHOULD** be monitored at autonomy ≥ L2.
>
> *Reference: the representativeness score in AgenticPerformance; provider canaries in AgenticGateway (Stack 1).*

*Compliance note: implements EU AI Act Art. 72 (post-market monitoring) for agentic deployments.*

### Human oversight as a program

Human-in-the-loop is not a checkbox but an **operated program**: review queues, reviewer SLAs, a sampling strategy, reviewer-quality tracking, and a feedback loop from reviews back into eval data. The **sampling schedule is a trust instrument** — oversight intensity declines as trust is earned (100% review at O0 → 10% audit → 2% spot-checks) and **re-escalates automatically on regression**; graduation is not a one-way door (this operationalizes the Cycle of Trust, Canon 5). Beware **sampling bias**: if only escalated or hard cases reach humans, review-derived labels skew hard — **stratify** (escalations *plus* a random sample of routine traffic).

**Automation bias turns a gate back into no gate.** A reviewer who approves everything, fast, is a rubber stamp with a login. Singapore IMDA's *Model AI Governance Framework for Agentic AI* (January 2026, updated May 2026) names the measurement: human override rates — how often people reject or modify agent actions — where a low rate may signal rubber-stamping, alongside response times. The EU AI Act's human-oversight article (Art. 14) asks for the same awareness of automation bias. Measure it wherever an approval counts as a control, including at O0.

> **MUST — wherever a human approval or review counts as a control:**
> - **override rate** and **approval latency** (p50/p95) are measured per queue and per reviewer, with a **rubber-stamp alarm** — sustained near-total approval at latencies too short to have read the action — that triggers a review of the queue, not a silencing of the alarm.
>
> **MUST — at O1+:**
> - a **Loop License declares its human-oversight plan**: review **sampling schedule per oversight mode**, reviewer **SLA**, and automatic **re-escalation triggers** (e.g., a regression-gate failure or override-rate spike drops the loop to the previous mode);
> - human review decisions and overrides are **captured as labeled evaluation data**, and golden-set ingestion from reviews uses **stratified sampling** to avoid difficulty skew.
>
> This is DoD 33.

*Compliance note: gives concrete form to EU AI Act Art. 14 (human oversight) for agentic systems.*

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

### Specs, protocols & security canon (2025–2026) — pin the revision you conform to
- **OWASP — Top 10 for Agentic Applications (2026 edition)** + *Agentic AI Threats and Mitigations* + the **MCP Security Cheat Sheet** — the threat model for Layer 8
- **Simon Willison — "The lethal trifecta"** (June 2025) — the deployment check every agent must pass
- **OpenTelemetry — GenAI semantic conventions** — the vendor-neutral observability standard (Stack 6); since semconv v1.42.0 (June 2026) maintained in `open-telemetry/semantic-conventions-genai`, still *Development* status — pin a commit
- **MCP specification 2026-07-28** (final 28 Jul 2026; 2025-11-25 is the prior revision) with the official conformance suite, and the **A2A specification v1.0.1** (v1.0 stable since 12 Mar 2026; Linux Foundation) — the interop protocols
- **Agent Skills specification** (agentskills.io) — the open format for skills, the instruction supply chain of Part IV
- **GEPA** (reflective prompt evolution, ICLR 2026) + **DSPy** — programmatic optimization, the bridge before any weight update
- **METR — *Frontier Risk Report*** (May 2026) and *Clarifying limitations of time horizon* (Jan 2026) — why success needs a legitimacy audit (Part IV) and why benchmark time horizons do not transfer to your product (Canon 1)

### Governance & regulation (2025–2026)
- **EU AI Act** — Regulation (EU) 2024/1689 as amended by the **Digital Omnibus on AI**, Regulation (EU) 2026/1744 (in force 27 Jul 2026): Art. 50 transparency applies from 2 Aug 2026; high-risk obligations from 2 Dec 2027 (Annex III) and 2 Aug 2028 (Annex I)
- **Singapore IMDA — *Model AI Governance Framework for Agentic AI*** (Jan 2026, updated May 2026) — four dimensions, and automation-bias measurement for human oversight
- **NIST AI RMF 1.0** (Govern / Map / Measure / Manage), the **AI Agent Standards Initiative** (CAISI, Feb 2026), and the NCCoE concept paper on **software and AI agent identity and authorization** (Feb 2026)
- **OWASP — *Agentic Skills Top 10*** (incubator project, 2026) — the supply-chain view of skills

[`CROSSWALK.md`](CROSSWALK.md) maps every Definition of Done item to these frameworks.

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

<!-- canon:begin:standard.antipatterns -->
**Do not do this:**

1. **Multi-agent before a single-agent baseline.** First prove value on one agent.
2. **Framework abstractions before understanding the raw API.** Otherwise debugging turns into reverse-engineering someone else's code.
3. **LLM judges without calibration against human labels.** A metric with no trust value is not a metric.
4. **Permissions enforced through prompts.** The model will ignore them. Enforce in code only.
5. **Memory as an afterthought.** Externalizing state is an architectural decision; the retrofit is painful.
6. **Generic evals ("helpfulness," "correctness").** They do not catch product-specific failures.
7. **Likert scales in an LLM judge.** Binary outputs are the only thing that calibrates.
8. **>100 tools per agent.** The model gets confused. Use RAG-MCP or routing.
9. **One agent for both breadth and depth.** Specialize: one type of agent, one type of task.
10. **Deploying without trace monitoring.** Most failures are routing/tool-selection — visible only in traces.
11. **Hardcoded prompts without version control.** Prompts are code.
12. **Treating single-vendor benchmarks as ground truth.** Anthropic's 90.2% lift, Letta's 500+ interactions — directionally correct, not absolute truth.
13. **Trusting community MCP servers without pinning or scanning.** Tool descriptions can mutate after you approve them (rug pull). Pin by hash; alert on change.
14. **Deploying the lethal trifecta with no mitigation.** Private data + untrusted content + external comms = an exfiltration channel. Break one leg.
15. **Token passthrough / over-scoped OAuth.** Forwarding a user's token, or minting broad scopes "to be safe," is a confused deputy waiting to happen. Its 2026 variant: an MCP client that can only register through the now-deprecated Dynamic Client Registration.
16. **No budget ceiling on autonomous sessions.** Without a per-run cost circuit breaker, one bad loop is an unbounded invoice.
17. **Peer-to-peer multi-agent buses instead of an orchestrator.** Free-form agent debates multiply context and resist evaluation. Use an orchestrator with isolated subagents.
18. **Prose topology counted as a control.** A route described in an SOP, a skill, or a system prompt is documentation, not a guardrail — it holds until the moment it matters, and prose cannot fail loudly. Mark every edge class enforced or declared; count only enforced edges (Part IV).
19. **License inheritance by wiring.** "Every agent is production-ready, so the graph is." A graph of licensed loops is not a licensed graph — hold a Graph License (Part IV, *License Composition*).
20. **Counting a pass as a success without legitimacy review.** A check the agent can satisfy without doing the task measures its skill at satisfying checks. Keep checks out of the agent's reach, audit a sample of successes, and publish the legitimacy rate (DoD 30).

<!-- canon:end:standard.antipatterns -->

---

## Part IX. Compact decision checklist

Before starting any agentic project, run through this checklist:

<!-- canon:begin:standard.checklist -->
```
□ What is the minimum autonomy level (L0–L4) that solves this, and under which oversight mode (O0–O2)?
□ Can it be solved by composing the 5 patterns without a full agent loop?
□ Is the task breadth-first (parallelizable) or depth-first (coherent)?
□ What are the 3 failure modes that would lose user trust first?
□ Where are the permission boundaries? What MUST the agent NOT do?
□ Which constraint dominates framework choice?
□ Where does state live? (in-context = anti-pattern for long-running)
□ Who validates outputs at each stage? (assertion / LLM judge / human review)
□ Where do traces live, with what retention?
□ Eval set: how many examples, who labels, how does it grow?
□ Does the deployment hit the lethal trifecta? If so, which leg do we break?
□ Which MCP revision do we speak — and are tool definitions pinned and servers allow-listed?
□ What is the per-run token/cost ceiling, and where in the code is it enforced?
□ Which identity does each agent act as, and who delegated it?
□ Which regulations apply, and what is our role and risk class under each?
```

<!-- canon:end:standard.checklist -->

---

## Part X. Emerging & deferred

Tracked deliberately, but **not** yet promoted to first-class standard surface — naming what we refuse to over-specify is part of the discipline. Reach for these only when the dominant constraint demands it.

- **Inter-agent protocols (A2A) in depth.** The decision rule lives in Stack 2: internal function calls / shared context for tightly-coupled subagents; A2A only across vendor / framework / org boundaries. v4.0 promotes one piece — verifying a signed Agent Card before cross-boundary delegation (DoD 28); a full protocol playbook is still deferred until cross-org agent deployments are common in practice.
- **Agent identity profiles and control overlays.** NIST's NCCoE project on software and AI agent identity (concept paper, Feb 2026) and the planned SP 800-53 overlays for agent use cases (COSAiS) are unpublished as of this release. DoD 27 fixes the outcome — a distinct, short-lived, attributable identity per agent; the mechanism (OAuth token exchange, SPIFFE, workload identity) stays the implementer's choice until a profile ships.
- **Evidence behind the thresholds.** The standard's numbers (≥90% pass@1, ≥50 evals per failure mode, the 40% default budget) are practitioner consensus, not measured on a published dataset. A dataset that grounds them — the way *AgentReady* derives each measured claim from published agent-run data — is on the roadmap; until then every threshold is overridable by a measured one.
- **Model adaptation (RL / fine-tuning / programmatic optimization).** Decision ladder: prompt → context-engineer → **programmatic optimization (DSPy / GEPA)** → RL or fine-tune *only* when a verifiable reward and a rollout budget exist. **Engineer the harness first** remains the right 2026 default; GEPA/DSPy is the named bridge before any weight update.
- **Agent experience (AX).** Ambient / event-driven agents, the agent-inbox UX, and notify / ask / review trust calibration extend the existing Human-in-the-Loop layer — see Harrison Chase's ambient-agents work. Extend HITL; do not duplicate it.
- **Orchestration topologies beyond orchestrator-worker** (blackboard, hierarchical, market-based, swarm) — documented as map, but 2026 evidence favors orchestrator-subagent for reliability (Canon 3).
- **Agentic / Graph RAG.** Claude Code abandoned precomputed vector RAG for grep-style agentic retrieval (Stack 3); GraphRAG earns its keep on genuinely multi-hop questions.
- **Computer-use & voice agents.** First-class in the Claude Agent SDK (computer use) and benchmarked by τ-Voice (full-duplex voice) — emerging deployment patterns, not yet core.
- **Curated-context formats (`llms.txt`, OKF).** `llms.txt` (a single-file navigation pointer) and **OKF** — Google Cloud's Open Knowledge Format, v0.1, a git-distributed bundle of Markdown concept files cross-linked into a graph — standardize the *knowledge an agent consumes*, upstream of the agent system this standard governs. Treat them as the **supply side of context engineering** (Stack 3 · Select / just-in-time retrieval): adopt as a source, don't mandate a v0.1 spec. Details in the `context-engineering` skill. *(Aptly, this repo is already that shape — Markdown concepts + frontmatter + an index.)*

---

## Closing

The standard is not dogma. It is a **tilt of the field** toward the practices that, across 2024–2026, converged independently at Anthropic, OpenAI, Cognition, Sierra, LangChain, and among leading practitioners.

**The single most important rule of the standard:**

> *"Architecture is what remains when the model improves. The model is the variable, the harness is the constant. Invest proportionally."*

---

<!-- canon:begin:standard.footer -->
*v4.0.0-rc.1 · assembled from production practices as of September 2026*

<!-- canon:end:standard.footer -->
