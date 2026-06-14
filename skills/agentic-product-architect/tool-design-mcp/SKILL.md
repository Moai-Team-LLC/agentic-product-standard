---
name: tool-design-mcp
description: Design tools for agents — function/tool definitions, MCP (Model Context Protocol) servers, tool routing when there are many tools, structured outputs, and the rules of thumb that prevent tool selection failures. Use whenever the user is adding tools/functions to an agent, integrating external systems, building or consuming MCP servers, hitting "the agent picks the wrong tool" failures, designing function signatures, choosing between MCP and direct function calling, or wondering how many tools is too many.
---

# Tool Design and MCP

In 2026 the tool-integration question has a clear answer: **MCP by default**. The ecosystem now exceeds 10,000 active servers and 177,000 registered tools. Adoption by Anthropic, OpenAI, Google, and the broader community makes it the de facto standard.

## The two protocols

**MCP (Model Context Protocol)** — agent ↔ tool
- Anthropic, Nov 2024
- JSON-RPC 2.0
- Servers expose tools, resources, prompts
- One server per integration; any MCP-aware client can use it

**A2A (Agent2Agent)** — agent ↔ agent
- Google, April 2025; donated to Linux Foundation June 2025
- Agents publish "Agent Cards" (capability metadata)
- Tasks exchanged via HTTP/JSON

They're **complementary, not competing.** MCP gives an agent its tools; A2A lets specialized agents delegate to each other across vendor boundaries.

## The NxM collapse

Before MCP: every model × every tool = a custom integration. N × M problem.

After MCP: one MCP server per tool, any MCP-aware client can consume it. N + M.

**Practical implication:** if you write custom function-calling code for a tool that already has an MCP server, you're choosing technical debt. Search for an existing server first.

## Tool design as prompt engineering

The single most important rule from Anthropic's "Building Effective Agents": **treat tool definitions like prompts**. Name them, describe them, give examples, document edge cases. Anthropic dedicates an appendix to "prompt-engineering your tools" for a reason.

### Required elements of a tool definition

1. **Name** — descriptive, namespaced, action-oriented. `search_docs` not `tool_3`.
2. **Description** — what it does, when to use it, when NOT to use it
3. **Parameters** — with types, descriptions, examples, required/optional flags
4. **Return value** — schema of what the agent gets back
5. **Side effects** — does this mutate state? trigger an external action? expensive?
6. **Examples** — 1–2 in the description showing correct invocation

### Anti-patterns in tool design

- **Verb-only names** (`get`, `run`, `do`) — model can't disambiguate
- **Overloaded tools** that do five things based on a `mode` parameter — split them
- **Custom DSL parameters** — use formats the model has seen in training (Markdown diffs, JSON, natural language) over invented syntax
- **No examples in description** — Anthropic empirically shows 1–2 examples in tool descriptions reduce selection errors substantially
- **Hidden side effects** — if it costs money, mutates state, or sends notifications, say so in the description

### Description as prompt — example

```json
{
  "name": "search_internal_docs",
  "description": "Search the company's internal documentation by semantic similarity. Use this when the user asks about company policies, internal tools, or anything that wouldn't be in public knowledge. Do NOT use this for general programming or knowledge questions — use web_search for those. Returns the top 5 matching document chunks with source URLs.",
  "parameters": {
    "query": {
      "type": "string",
      "description": "Natural language search query. Best results with full questions ('what is our refund policy for enterprise customers') rather than keywords ('refund policy').",
      "examples": ["what's our policy on remote work?", "how do I deploy to staging?"]
    },
    "max_results": {
      "type": "integer",
      "description": "Maximum chunks to return (1-10). Default 5.",
      "default": 5
    }
  }
}
```

## The <20 tool rule

Empirical guidance from HumanLayer's Dex Horthy: **keep active tools per agent below 20, ideally below 10**. Above that, tool descriptions overlap and the model selects badly.

When you legitimately have many tools:

### Option A: Routing

Classify the request, dispatch to a specialist sub-agent that only sees the relevant tools.

```
input → classifier → 
  ├─ research_agent (5 tools: search, fetch, extract, summarize, cite)
  ├─ data_agent (4 tools: query_db, run_sql, plot, export)
  └─ comms_agent (3 tools: send_email, schedule_meeting, draft_doc)
```

### Option B: RAG-MCP

RAG over tool descriptions. For each turn, retrieve only the relevant subset of tools to expose. The RAG-MCP paper (arXiv:2505.03275) reports: **+3.2× tool selection accuracy (43% vs 13.6%) with ~50% fewer prompt tokens.**

```
input → retrieve_relevant_tools(input, k=8) → expose only those to agent
```

### Option C: Hierarchical tools

A few "meta-tools" that internally route to many specific ones. The agent sees `database_action(operation, params)`; behind it, your code routes to one of 30 specific DB tools. Trade-off: less LLM control, more deterministic dispatch.

## Structured outputs as the default

Both OpenAI and Anthropic now support schema-enforced JSON outputs. **Default to structured outputs for any tool result the agent needs to reason about.**

Why:
- Eliminates a class of parsing errors
- Downstream code can validate before consuming
- Easier to log, trace, eval

```python
# Pydantic AI style
class SearchResult(BaseModel):
    query: str
    matches: list[Match]
    confidence: float

result: SearchResult = await agent.run(...)
```

Treat ad-hoc text-parsing as legacy.

## MCP server design — when you're building one

If your tool surface is something other agents (yours or third-party) will want, expose it via MCP rather than burying it in function-calling code.

Principles:

- **One concern per server.** A "Stripe MCP server" exposes Stripe operations. Don't combine Stripe + Slack + email into one mega-server.
- **OAuth scopes mapped to tool exposure.** A user with read-only credentials sees read-only tools. Don't expose tools the credentials can't execute.
- **Resources for data, tools for actions, prompts for templates.** MCP has all three primitives; use them correctly.
- **Versioning and discoverability.** Servers should advertise their version and capabilities.
- **Logging and instrumentation.** Treat the MCP server like any other production service.

## Permission model — non-negotiable

The Replit incident is the canonical lesson: prompts don't enforce permissions. **The agent cannot have credentials that bypass the permission boundary.**

Pattern:

```
agent invokes destructive_tool(params)
  → tool server requires approval token
  → token only issued by separate "approval service"
  → approval service requires human signoff for high-blast-radius actions
  → agent literally cannot get the token without human in the loop
```

This is the difference between "the agent asks permission" (prompt-level, bypassable) and "the agent must obtain a permission token" (code-level, enforced).

### Secure write actions (the write path)

"Require approval" is necessary but underspecified. The operational pattern — **read-only by default; writes are elevated, scoped, time-bounded, and confirmed out-of-band (the agent never sees the confirmation secret); destructive changes get a dry-run first** — is its own companion doc: [`SECURE-WRITE-ACTIONS.md`](SECURE-WRITE-ACTIONS.md). Read it whenever an agent or MCP server you're designing can mutate state (P3+).

## Sandboxing

Tool execution surfaces are attack surfaces. Minimum:

- **Code execution** in containers, never in the agent's host environment
- **File operations** in scoped working directories
- **Network access** through allow-listed domains
- **Secrets** never in context window; injected at tool boundary

OpenAI's sandbox agents and Claude Code's permission modes are reference implementations.

## Diagnosing tool failures

When the user reports "the agent picks the wrong tool" or "the tools don't work":

| Symptom | Likely cause | Fix |
|---|---|---|
| Picks wrong tool | Vague descriptions, overlapping tools | Rewrite descriptions; consolidate or split tools |
| Picks no tool when it should | "When to use" missing from description | Add explicit triggers and counter-examples |
| Calls tools in wrong order | No precondition documentation | Document tool dependencies in description |
| Tool call malformed | Schema mismatch, ambiguous params | Switch to structured outputs; add examples |
| Loops calling same tool | No verification step in harness | Add verification in agent loop (layer 1) |
| Tool selection slows down with more tools | >20 tools active | Apply routing or RAG-MCP |

## Output of this skill

When this conversation completes, the user should have:

1. A tool inventory with each tool's name, description, parameters, return schema
2. Selection strategy: direct exposure (<20), routing, or RAG-MCP
3. Permission model: what cannot be called without approval; how approval is enforced
4. MCP server identification: which tools should be MCP-exposed for reuse
5. Sandbox plan for any execution surface (code, file, network)
6. Structured output schemas for tool results
