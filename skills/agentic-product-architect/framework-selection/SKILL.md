---
name: framework-selection
description: Choose the right agentic framework — LangGraph, OpenAI Agents SDK, Claude Agent SDK, CrewAI, Pydantic AI, AutoGen/AG2, LlamaIndex Workflows, Semantic Kernel, Mastra, DSPy, mcp-agent — based on the team's dominant constraint, not hype. Use whenever the user asks "which framework should I use," compares any two of these, hits limits with their current framework, or is starting a new project and needs to pick the stack.
---

# Framework Selection

The single best piece of advice from Anthropic's "Building Effective Agents," and it's worth a million dollars: **"Start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code."**

HumanLayer's Dex Horthy independently observed: in production customer-facing agents, most teams roll the stack themselves rather than committing to a heavy framework. The framework is a convenience, not a requirement.

That said, when you do choose, do it by constraint, not by hype.

## Step 0: do you need a framework at all?

For v1 / proof-of-concept, often **no**. The model provider's SDK plus your own code handles the 5 patterns cleanly:

- Prompt chaining = a Python function calling the LLM twice
- Routing = a switch statement after a classifier call
- Parallelization = `asyncio.gather`
- Orchestrator-workers = a function spawning sub-tasks
- Evaluator-optimizer = a while loop

If you can express your design in 100 lines of vanilla code, do that. You'll understand it better, debug it faster, and have fewer dependencies. Frameworks earn their place when you have:

- Long-running workflows that need durable execution
- Multi-agent coordination with complex state
- Need for production observability with deep integration
- A team that benefits from shared vocabulary and structure
- Cross-cutting concerns (HITL, checkpointing) you'd otherwise rebuild

## The decision matrix (constraint-driven)

Find your **dominant constraint** — the one you'd sacrifice others to get. Pick on that. Don't compromise across all dimensions; you'll end up with the worst of all worlds.

| Dominant constraint | Framework | Why |
|---|---|---|
| Maximum control, complex stateful workflows, multi-vendor | **LangGraph** | Graph-based; Postgres checkpointing; HITL primitives; time-travel debugging; used at Uber, Klarna, LinkedIn, JP Morgan, BlackRock |
| Anthropic-native, especially coding/computer-use | **Claude Agent SDK** | The harness powering Claude Code; hooks, skills, subagents, MCP, computer use, compaction — all first-class |
| OpenAI-native, opinionated lightweight SDK | **OpenAI Agents SDK** | Clean handoffs, guardrails, tracing built in; tight integration with Responses API |
| Multi-agent with explicit roles, fastest prototype | **CrewAI** | Role-based orchestration in ~20 LOC; lowest barrier to entry |
| Type safety, FastAPI ergonomics, structured outputs | **Pydantic AI** | Typed signatures, 25+ providers, Temporal integration; built by the Pydantic team |
| Document-heavy, RAG is the core job | **LlamaIndex Workflows** | First-class RAG primitives; event-driven workflow runtime |
| .NET / Azure enterprise | **Semantic Kernel** | C# / Python / Java parity; Azure-native |
| TypeScript full-stack | **Mastra** | TS-native; fits Next.js stacks |
| Programmatic prompt optimization | **DSPy** | Compile prompts and weights against a metric; can layer on top of other frameworks |
| MCP-native + Temporal | **mcp-agent (lastmile-ai)** | Anthropic's effective-agent patterns + MCP + Temporal first-class |
| Conversation-first multi-agent research | **AutoGen / AG2** | Was the standard; AG2 is the community fork; Microsoft has moved on to Microsoft Agent Framework |

## Profiles by framework

### LangGraph

**Use when:** complex stateful workflows, want control without rebuilding the substrate, multi-vendor LLMs, deep observability via LangSmith.

**Strengths:**
- Graph-based; every node and edge is explicit
- Postgres checkpointing for free durability
- Time-travel debugging — replay from any state
- HITL primitives (interrupt, command, send)
- Production deployments at Uber, Klarna, LinkedIn, JP Morgan
- Model-agnostic

**Trade-offs:**
- Medium learning curve (graph mental model)
- Tightest integration with LangSmith pulls toward LangChain ecosystem
- Verbose for simple cases

**Heuristic:** if your design has > 5 distinct nodes / states and stateful transitions, LangGraph pays for itself. If it's a 3-step chain, it's overkill.

### Claude Agent SDK

**Use when:** building agents on Claude, especially coding / computer-use / file-system-heavy work. Anthropic-native.

**Strengths:**
- The agent loop that powers Claude Code, exposed for arbitrary agents
- Hooks (pre/post tool use), skills, subagents, MCP integration, computer use, automatic compaction
- "Give your agents a computer" design philosophy
- Loop: gather context → take action → verify work → repeat

**Trade-offs:**
- Tied to Claude models
- Newer than LangGraph; smaller ecosystem
- Less mature for non-coding use cases

**Heuristic:** if you're building a coding agent, file-system agent, or computer-use agent on Claude, this is the default.

### OpenAI Agents SDK

**Use when:** building on OpenAI, want a clean opinionated SDK, value handoffs and guardrails as first-class concepts.

**Strengths:**
- Handoffs (peer agents transfer ownership) and `agent.asTool()` (manager calls specialist) as first-class patterns
- Guardrails built in
- Tracing built in
- Tight integration with Responses API and Agent Builder

**Trade-offs:**
- Tightest OpenAI coupling
- Smaller ecosystem than LangChain
- Less control than LangGraph for complex flows

**Heuristic:** for OpenAI-only projects, this is more ergonomic than LangGraph and more structured than vanilla function calling. Default for OpenAI-native shops.

### CrewAI

**Use when:** multi-agent prototypes where work decomposes naturally into named roles, fastest possible time to demo.

**Strengths:**
- Role-based orchestration in ~20 lines
- Strong community; lots of examples
- Easy to communicate the design ("we have a Researcher, a Writer, a Reviewer")

**Trade-offs:**
- Abstractions hide details that matter at scale
- Harder to debug than explicit graphs
- Production deployments less common than LangGraph

**Heuristic:** great for proving the multi-agent concept; switch to LangGraph or rolled-your-own once you need fine-grained control. Many teams use CrewAI to validate, then rebuild.

### Pydantic AI

**Use when:** type safety matters, you're already on Pydantic / FastAPI, structured outputs are the norm, Python team.

**Strengths:**
- Type-safe signatures everywhere
- 25+ provider support — true model agnosticism
- Temporal integration first-class
- Familiar to anyone using Pydantic / FastAPI

**Trade-offs:**
- Less developed multi-agent story
- Smaller community than LangChain ecosystem

**Heuristic:** if your team already uses Pydantic for API validation and you want agents that fit naturally into that codebase, this is the cleanest option.

### LlamaIndex Workflows

**Use when:** retrieval is the core job (Q&A over documents, knowledge agents).

**Strengths:**
- Event-driven workflow runtime
- First-class RAG primitives, advanced retrieval patterns
- Mature ingestion / indexing

**Trade-offs:**
- Less production tooling than LangGraph
- Strongest as retrieval-first; weaker for general agents

**Heuristic:** if "RAG" appears more in your design than "agent," start here.

### DSPy

**Use when:** you want to programmatically optimize prompts (and weights) against a metric, not hand-tune.

**Strengths:**
- Compile prompts against eval metrics
- Demonstrated lifting program quality dramatically (e.g., 33% → 82% on GSM8K with GPT-3.5 in the ICLR 2024 paper)
- Composable with other frameworks (layer on top)

**Trade-offs:**
- Steep learning curve
- Metric design becomes the new prompt-engineering
- Most valuable when you have good evals

**Heuristic:** consider once you have a working baseline and a solid eval set. DSPy + good evals can replace manual prompt tuning.

### mcp-agent

**Use when:** MCP-native architecture is a strategic commitment, want Anthropic's "Building Effective Agents" patterns implemented natively.

**Strengths:**
- Implements the 5 patterns from Anthropic's guide
- MCP-first design
- Temporal integration

**Trade-offs:**
- Newer, smaller community
- Less mature than LangGraph

**Heuristic:** for teams going all-in on MCP, this aligns the framework with the standard.

## What to look for when comparing frameworks

Beyond the dominant constraint, check these before committing:

1. **Production deployments at known companies.** Demos prove ideas; production proves robustness.
2. **Active maintenance.** Last 6 months of commits, issue response times, releases.
3. **Documentation quality.** Especially examples close to your use case.
4. **Observability integration.** OpenInference / OpenLLMetry support, or first-class tracing.
5. **Escape hatch.** Can you drop down to raw SDK calls when the abstraction doesn't fit?
6. **Lock-in.** What changes if you swap models? Swap memory? Swap orchestrator?

> **On model lock-in specifically:** the *framework* question is separate from the *provider* question. To swap models or providers without touching agent code, put every call behind one OpenAI-compatible endpoint. The family's reference implementation of that plane is **[AgenticGateway](https://github.com/Moai-Team-LLC/AgenticGateway)** — provider swap becomes config, not code, with eval-sourced routing and per-run/tenant cost ceilings (harness Layers 1 + 9). Vendor-neutral: keep LiteLLM / Portkey / raw Bifrost if you already run one (Principle 2). See the [`reference-stack`](../reference-stack/SKILL.md) skill.

## Framework misuse patterns

| Pattern | Why it's wrong | Fix |
|---|---|---|
| Picked the most popular framework | Popularity ≠ fit | Re-evaluate against dominant constraint |
| Picked the framework with most features | More features = more concepts to learn = more bugs | Pick the simplest framework that satisfies the constraint |
| Picked the framework matching the model vendor | Sometimes right, often wrong | Decide model coupling deliberately |
| Adopted framework abstractions before understanding raw APIs | Debugging becomes reverse-engineering | Build a small version in raw SDK first |
| Rebuilt the framework's primitives because "it's too opinionated" | Likely using the wrong framework | Switch frameworks or commit to building from scratch |

## The "build it twice" rule

For non-trivial agentic products: **build v0 in raw SDK calls** to understand the shape. Then either keep raw code or pick a framework that maps to what you built. Frameworks chosen before understanding usually fight the design.

## Output of this skill

When the conversation completes, the user should have:

1. A named dominant constraint
2. A framework choice (or a deliberate decision to use raw SDK)
3. Awareness of the trade-offs they accepted
4. A plan for the escape hatch if the framework doesn't fit later
5. If multiple frameworks were viable, a documented reason for the pick
