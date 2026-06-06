# Agent Standard — Building One Production-Grade Agent

*The operational standard for a single agent: contract, schemas, tools, permissions, durable state, verification, and traceability.*

> Companion to `STANDARD.md` — the product-level canon. This is the **single-agent** track; the `agent-builder` Claude Code skill operationalizes it (this doc ships bundled with that skill, under `skills/agent-builder/`), and the copy-paste artifacts live in `templates/`. Evidence for the load-bearing claims is in the **Evidence & Sources** appendix at the end.

---

## Purpose

This standard defines a production-grade approach to designing, implementing, reviewing, and improving agents and sub-agents inside agentic products.

Use it whenever the task involves:
- creating an AI agent;
- creating a sub-agent;
- designing a multi-agent workflow;
- adding tool use to an agent;
- adding memory, context, permissions, durable execution, evals, or tracing;
- reviewing whether an agentic implementation is production-ready;
- deciding whether a task needs a workflow, a single agent, or multiple agents.

The core principle:

> An agent is not a prompt.
> An agent is a bounded execution unit with a contract, scoped context, tools, permissions, durable state, verification, and traceability.

Default to deterministic software. Add agency only where the path cannot be fully predefined.

A note on terminology used throughout this document: **autonomy levels (L0–L4)** describe *how much* control flow the model owns; **permission tiers (P0–P6)** describe *how dangerous* a tool's side effects are. They are two distinct scales — never conflate them.

---

## Operating Doctrine

### 1. Determinism First, Agency Second

Always start with the least autonomous design that can produce the required value.

Use this autonomy ladder:

| Level | Pattern | Use When |
|---|---|---|
| L0 | Single LLM call | Classification, extraction, summarization |
| L1 | Augmented LLM | One call plus retrieval, tools, or memory |
| L2 | Deterministic workflow | The path is known and reliability matters |
| L3 | Orchestrator-worker | The system must dynamically decompose bounded work |
| L4 | Autonomous agent loop | The path is genuinely open-ended and cannot be enumerated |

**Transition rule:** do not climb to level `L+1` until level `L` reaches **≥90% pass rate on a curated eval set**. Every degree of autonomy must earn its place through evals, not be granted in advance.

Rules:
- Do not use L3 when L2 is enough.
- Do not use L4 unless the task cannot be expressed as a bounded workflow.
- Do not create multi-agent systems before a single-agent or workflow baseline exists.

#### The five composition patterns

Before reaching for a full agent loop, try to assemble the task from the five
industry-standard composition patterns. They are framework-agnostic and most can
be implemented in a few lines of deterministic code:

1. **Prompt chaining** — sequential decomposition (outline → draft → polish).
2. **Routing** — a classifier dispatches the request to a specialist handler/model.
3. **Parallelization** — fan out independent sub-tasks (sectioning, voting), then aggregate.
4. **Orchestrator-workers** — a central LLM plans dynamically and delegates to sub-LLMs whose outputs it synthesizes. Bridges workflow and agent: dynamic decomposition, bounded control.
5. **Evaluator-optimizer** — a generator is paired with a critic that loops until the critic accepts; the cheapest reliability win when "good" is recognizable but not generable in one shot.

Metaprinciple: solve the task by composing these patterns on deterministic code first. A full agent loop is the last resort.

### 2. Harness Over Model

Model choice matters. The harness matters more. In a production coding agent, roughly **98% of the code is harness**, not the model loop — and as model capability converges, harness quality is the durable competitive advantage.

A production agent must be surrounded by these seven harness layers:

```text
┌───────────────────────────────────────────────┐
│ 7. Observability & Tracing      (log everything)│
├───────────────────────────────────────────────┤
│ 6. Evaluation Layer             (CI gates)      │
├───────────────────────────────────────────────┤
│ 5. Human-in-the-Loop            (notify/ask/review)
├───────────────────────────────────────────────┤
│ 4. Guardrails                   (input/output validation, defense in depth)
├───────────────────────────────────────────────┤
│ 3. Durable Execution            (pause / resume / retry)
├───────────────────────────────────────────────┤
│ 2. Context & Memory Management  (write/select/compress/isolate)
├───────────────────────────────────────────────┤
│ 1. Agent Loop                   (gather → act → verify)
└───────────────────────────────────────────────┘
                  ↕ MCP / function calling
          ┌──────────────────────────┐
          │   Tools & Resources      │
          └──────────────────────────┘
```

Never rely on a prompt to enforce security, permissions, or control flow.

### 3. Context Engineering Over Prompt Engineering

The agent's performance depends on what enters the context window.

Treat context as an engineered resource:
- **Write** durable state outside the context window.
- **Select** only the relevant context for the current step.
- **Compress** old or low-value context.
- **Isolate** independent sub-tasks into separate context windows.
- **Closed enumerations over open vocabularies.** For any rule the model has
  shown willingness to satisfy cosmetically (selecting from a category, naming a
  capability, choosing a label), inline the *complete allowed set* in the context
  read at runtime. A pointer to another file leaks the vocabulary under pressure:
  the model fills the gap with plausible-but-invented values that pass a shallow
  check. Any value not in the closed set is a failure, not a creative liberty.

**The 40% rule:** keep context-window utilization below ~40% of the model's limit. Degradation past that threshold is non-linear — recall drops sharply in the "dumb zone." Avoid filling the context window with raw transcripts, large files, irrelevant prior decisions, or unused tool descriptions.

### 4. Cycle of Trust

Every action an agent takes passes through an explicit trust check:

```text
gather context → propose action → check permissions →
verify preconditions → execute → verify outcome →
write trace → update memory
```

Permissions are enforced in **code**, never in the prompt. The model will, given the chance, ignore an instruction it was told to obey. The canonical proof is the July 2025 Replit incident, where an agent deleted the production database of 1,200+ companies despite an explicit "code and action freeze" written into its prompt. Treat every tool surface as an RPC endpoint exposed to untrusted input.

### 5. Eval-Driven Development

No agent is production-ready without evals.

Start with:
- error analysis on 20–50 real traces *before* building any eval infrastructure;
- a curated set of examples for the target use case;
- code assertions for deterministic requirements;
- product-specific failure-mode tests;
- human review for high-impact changes;
- LLM-as-judge only for subjective failure modes, with binary output, calibrated against human labels.

Each production failure becomes a permanent regression test.

### 6. Bitter-Pilled Maintenance

The harness should shrink as models improve. Prescriptive instructions added to
compensate for a model's weakness become dead weight once the weakness is gone —
and every unnecessary rule competes for attention and degrades the rules that
still matter.

Audit instructions, prompts, and contracts on a cadence with one test:

> **"Would a smarter model make this rule unnecessary?"**
> If yes, it is scaffolding, not architecture — remove it.

Tag every rule as **anti-fragile** or **fragile**:

| Class | Keep / Cut | Examples |
|---|---|---|
| **Anti-fragile** | Keep | Verification harnesses, eval sets, data pipelines, tool contracts, specific DO/DON'T examples, routing rules, accumulated failure gotchas |
| **Fragile** | Cut or re-test | Chain-of-thought orchestrators, output-format parsers, retry cascades, numeric "personality" scales, abstract value statements, process descriptions the agent does not actually follow |

Fragile rules that cannot be cut yet (the model still needs them) are flagged for
re-test on the next model upgrade — they are debt, not architecture.

### 7. Security Is Structural

An agent's safety comes from architecture — identity, least privilege, isolation,
pinned tool definitions — not from filters bolted onto the edges. A guardrail is
one tactic, not the discipline. Content filters top out near ~97% accuracy, so
~3% of injection attacks succeed *by design*; you mitigate that structurally.

Three checks belong in every design, not just at review:

- **The lethal trifecta.** If an agent simultaneously has (1) access to private
  data, (2) exposure to untrusted content, and (3) the ability to communicate
  externally, prompt injection can turn it into an exfiltration tool. Break one
  leg — gate egress, quarantine untrusted input, or scope the data — before shipping.
- **The MCP supply chain.** Community MCP servers are untrusted code whose tool
  descriptions can mutate after approval (rug pull). Pin tool definitions by hash,
  alert on change, install only from an allow-listed registry.
- **Agent identity.** Each agent gets a distinct, least-privilege, short-lived,
  audience-bound identity. Identity and tenant are derived from auth, never asserted
  by the model. (Map controls to the OWASP Top 10 for Agentic Applications.)

---

## Skill Activation

When this skill is active, follow this sequence.

### Step 1: Classify the Work

Determine whether the user is asking to:

1. Design a new agent.
2. Implement an agent.
3. Design a multi-agent workflow.
4. Review an existing agent.
5. Add tools to an agent.
6. Add memory/state/context.
7. Add reliability, durable execution, or human-in-the-loop.
8. Add evals/observability.
9. Debug agent behavior.
10. Harden for production.

Then choose the appropriate sub-skill from the orchestrator below.

On uncertain classification, bias toward more verification and less autonomy.
Under-scoping the work (too little control, too much agency granted on a guess) is
the more expensive failure to recover from than over-scoping it.

### Step 2: Choose the Minimal Architecture

Before writing code, answer:

```text
What is the least autonomous architecture that can solve this?
```

Prefer, in order:

```text
deterministic function
→ deterministic workflow with LLM steps
→ single agent with bounded loop
→ orchestrator-worker
→ autonomous multi-agent system
```

### Step 3: Produce or Update the Agent Contract

Every agent must have an explicit contract before implementation.

### Step 4: Implement With Guardrails

All agent execution must go through:
- schema validation;
- permission checks;
- tool allowlists;
- guardrails on input and output;
- durable state persistence;
- trace logging;
- failure handling.

### Step 5: Add Evals Before Claiming Completion

The implementation is incomplete until evals exist.

---

# Orchestrator

## Role

You are the **Agentic Product Agent Standard Orchestrator**.

Your job is to select the right sub-skill and enforce the standard.

You do not create vague prompts.
You create bounded, testable, inspectable agent systems.

## Orchestrator Decision Tree

### If the task is about agent design

Use: `agent-contract-designer`

Output:
- Agent Contract
- Responsibility boundary
- Inputs/outputs
- Tools
- Permission level
- Acceptance criteria
- Failure modes
- Eval plan

### If the task is about implementation

Use: `agent-implementation-architect`

Output:
- File structure
- Schemas
- Runner logic
- Tool interface
- State model
- Trace events
- Tests

### If the task is about multiple agents

Use: `multi-agent-system-architect`

Output:
- Orchestrator-worker design
- Agent map
- Message envelope
- Handoff contracts
- Shared state model
- Conflict resolution
- QA layer

### If the task is about context or memory

Use: `context-engineering-specialist`

Output:
- Context sources
- Selection rules
- Compression rules
- Isolation boundaries
- Memory policy

### If the task is about tools

Use: `tool-permission-architect`

Output:
- Tool contracts
- Permission model
- Approval gates
- Sandbox rules
- Side-effect classification

### If the task is about reliability, durability, or human-in-the-loop

Use: `reliability-durable-execution-architect`

Output:
- Durable execution model (Workflow / Activity)
- Retry, timeout, and idempotency policy
- Resumability design
- Guardrail layer (input/output)
- Human-in-the-loop gates (notify / ask / review)

### If the task is about quality

Use: `eval-observability-engineer`

Output:
- Eval pyramid
- Assertion tests
- LLM-judge specs (calibrated, binary)
- Trace schema
- Review process
- CI gates

### If the task is about production readiness

Use: `production-readiness-reviewer`

Output:
- Risk assessment
- Failure modes
- Missing controls
- Required hardening tasks
- Release checklist

---

# Sub-Skill 1: Agent Contract Designer

## Mission

Design agents as bounded execution units.

## Required Output

Always produce an Agent Contract in this structure:

```md
# Agent Contract: {Agent Name}

## 1. Mission
One sentence describing the agent's purpose.

## 2. Ownership
The result this agent owns completely.

## 3. Non-Ownership
What this agent must not do.

## 4. Inputs
Required and optional inputs.

## 5. Required Context
Minimum context needed to do the job.

## 6. Optional Context
Useful context if available, but not required.

## 7. Tools
Allowed tools and why each is needed.

## 8. Forbidden Actions
Actions the agent must never take.

## 9. Output Schema
Structured output format.

## 10. Acceptance Criteria
How success is verified.

## 11. Failure Modes
Known ways this agent can fail.

## 12. Escalation Rules
When the agent must stop, ask, hand off, or request human approval.

## 13. Logging Requirements
What must be written to trace.
```

## Design Rules

- One agent must own one primary artifact.
- An agent must not own both generation and final approval.
- An agent must not perform external side effects unless explicitly permitted.
- Destructive actions always require human approval.
- The output must be schema-validatable.
- The acceptance criteria must be *hard-to-vary*: a criterion is well-formed only
  if you can name the single probe (Read / Grep / Bash / curl / SELECT / test run)
  that returns yes/no on whether it is met. If you cannot name the falsifying
  test, it is not yet a criterion — it is a wish. Split any criterion that needs
  more than one probe (signals: the word "and", scope words like "all"/"every",
  two independent failure modes).
- The failure modes must be concrete, not generic.
- Every **Forbidden Action** (contract §8) and **Non-Ownership** clause (§3) must
  yield at least one *anti-criterion*: a code assertion that fails if the forbidden
  thing happens (e.g. `expect(trace.events.filter(e => e.type === "email.send")).toHaveLength(0)`).
  Prose forbiddance is not enforcement — the derived assertion is. Anti-criteria
  belong in the Level 1 code-assertion eval layer, never in an LLM judge.

## Anti-Patterns

Avoid:
- "smart assistant" agents;
- agents with broad responsibilities;
- agents that own both planning and execution of high-risk actions;
- agents that receive all available context by default;
- agents that communicate through free-form text only;
- agents without explicit stop conditions.

---

# Sub-Skill 2: Agent Implementation Architect

## Mission

Turn an Agent Contract into production-grade code structure.

## Required File Structure

Use this default structure unless the repository already has a better convention:

```text
/agents
  /_shared
    agent-contract.ts
    agent-runner.ts
    message-envelope.ts
    permissions.ts
    guardrails.ts
    durable.ts
    trace.ts
    eval-runner.ts
    schemas.ts
    errors.ts

  /{agent-name}
    contract.md
    schema.ts
    prompt.ts
    runner.ts
    tools.ts
    state.ts
    evals.ts
    fixtures/
    README.md
```

## Required Runtime Flow

Every agent runner must follow this flow:

```text
load contract
→ validate input (schema + input guardrails)
→ load scoped context
→ initialize/restore durable state
→ execute deterministic steps
→ call LLM only where needed
→ validate structured output (schema + output guardrails)
→ run assertions
→ write trace
→ return artifact or escalation
```

## Required Implementation Properties

The implementation must include:

- typed input schema;
- typed output schema;
- input and output guardrails;
- explicit, externalized agent state;
- tool allowlist;
- permission checks;
- structured errors;
- trace events;
- eval fixtures;
- retry policy;
- timeout policy;
- resumability (durable execution) for any long-running work;
- escalation path.

## Agent Runner Pseudocode

```ts
export async function runAgent(input: AgentInput, runtime: AgentRuntime): Promise<AgentResult> {
  const validatedInput = AgentInputSchema.parse(input)
  await runtime.guardrails.checkInput(validatedInput)

  const contract = await runtime.contracts.load("agent-name")
  const permissions = await runtime.permissions.resolve(validatedInput.actor)

  const context = await runtime.context.select({
    agentId: "agent-name",
    task: validatedInput.task,
    maxContextBudget: runtime.contextBudget, // keep utilization < ~40%
  })

  // State is durable and externalized: restore if a prior run exists, else create.
  const state = await runtime.state.upsert({
    agentId: "agent-name",
    input: validatedInput,
    status: "running",
  })

  await runtime.trace.write({
    type: "agent.started",
    agentId: "agent-name",
    stateId: state.id,
  })

  try {
    const draft = await executeDeterministicPlan({
      input: validatedInput,
      context,
      state,
      runtime,
    })

    const output = AgentOutputSchema.parse(draft)
    await runtime.guardrails.checkOutput(output)

    await runAssertions(output)

    await runtime.trace.write({
      type: "agent.completed",
      agentId: "agent-name",
      stateId: state.id,
      outputSummary: summarizeOutput(output),
    })

    return {
      status: "completed",
      output,
    }
  } catch (error) {
    await runtime.trace.write({
      type: "agent.failed",
      agentId: "agent-name",
      stateId: state.id,
      error: serializeError(error),
    })

    return handleAgentError(error)
  }
}
```

## Code Rules

- Do not parse critical data from free-form text.
- Use structured outputs for all critical agent results.
- Keep prompts versioned (prompts are code; put them under version control).
- Keep schemas close to the agent.
- Keep business logic outside the prompt where possible.
- Never let the model choose tools that are not in the allowlist.
- Never let the model bypass permissions.
- Never treat successful text generation as successful task completion.

---

# Sub-Skill 3: Multi-Agent System Architect

## Mission

Design systems where multiple agents cooperate without losing ownership, context integrity, or auditability.

## When To Use Multi-Agent

This question is settled as a **context-engineering trade-off**. Multi-agent
orchestration can deliver a large quality lift on the right tasks (≈90% on
parallelizable research in one published study) but at multiples of the token
cost (≈15×). Choose deliberately.

Use multi-agent architecture only when the task is:

- breadth-first;
- parallelizable;
- decomposable into independent sub-tasks;
- improved by context isolation;
- too large or diverse for a single context window.

Use single-agent or workflow architecture when the task is:

- depth-first;
- highly stateful;
- dependent on shared context;
- a single coherent artifact;
- a codebase edit requiring continuity;
- a long-form writing task requiring one voice.

Splitting a depth-first, shared-context task across sub-agents creates a "game of telephone": each handoff loses context and the system produces conflicting decisions. When in doubt, stay single-agent.

## Allowed Multi-Agent Patterns

### 1. Orchestrator → Worker

A central orchestrator plans, delegates, and synthesizes.

Use for:
- research;
- analysis;
- product planning;
- broad document processing;
- multi-source synthesis.

### 2. Router → Specialist

A router classifies the task and sends it to the right specialist.

Use for:
- support triage;
- request classification;
- different workflows by user intent.

### 3. Generator → Critic

One agent creates; another evaluates (the evaluator-optimizer pattern).

Use for:
- generated content;
- code review;
- policy review;
- quality review.

### 4. Parallel Workers → Synthesizer

Independent agents investigate different areas; a synthesizer integrates.

Use for:
- market research;
- competitive research;
- technical option analysis;
- risk analysis.

### 5. Handoff

One agent transfers ownership to another.

Use only when the next agent must own the task fully. This is an *ownership* decision: be explicit about who is responsible for the final reply. (Contrast with "agent-as-tool," where the caller keeps ownership and the specialist is a bounded helper.)

## Multi-Agent Rules

- There must be one final owner of the user-facing result.
- Sub-agents must return condensed findings, not raw transcripts.
- Handoffs must use structured contracts.
- Shared state must be explicit.
- Each agent must have a contract.
- Each agent must have scoped context.
- Each agent must have an output schema.
- The orchestrator must verify compatibility between sub-agent outputs.
- The system must detect conflicting outputs.
- The system must have a final QA pass before external action.

## Message Envelope

Agents must communicate through a structured envelope.

```ts
export type AgentMessage = {
  messageType:
    | "task_request"
    | "task_result"
    | "clarification_request"
    | "clarification_response"
    | "critique_request"
    | "critique_result"
    | "handoff_request"
    | "handoff_acceptance"
    | "handoff_rejection"
    | "approval_request"
    | "error_report"

  sender: string
  receiver: string
  runId: string
  taskId: string
  priority: "low" | "normal" | "high" | "urgent"
  payload: unknown
  contextRefs: string[]
  permissions: string[]
  expectedOutput?: unknown
  trace: {
    parentStepId?: string
    correlationId: string
  }
}
```

## Handoff Contract

Every handoff must include:

```json
{
  "handoff_id": "uuid",
  "from_agent": "string",
  "to_agent": "string",
  "task": "string",
  "reason_for_handoff": "string",
  "inputs": {},
  "constraints": {},
  "known_risks": [],
  "expected_output_schema": "string",
  "approval_required": false
}
```

## Conflict Resolution

When agents disagree, do not average answers.

Use this order:
1. Check source evidence.
2. Check agent contracts.
3. Check acceptance criteria.
4. Ask a critic agent.
5. Ask a human if the decision has high blast radius.

---

# Sub-Skill 4: Context Engineering Specialist

## Mission

Design context flows that make agents reliable, cheap, and inspectable.

## Context Types

Use these categories:

| Context Type | Description |
|---|---|
| System Context | Agent rules, policies, contract |
| Task Context | Current task and objective |
| Domain Context | Domain knowledge needed for the task |
| User Context | User-provided data and preferences |
| Tool Context | Tool schemas and usage rules |
| Memory Context | Relevant durable memory |
| Runtime Context | Current execution state and prior steps |

## Context Operations

### Write

Externalize state that must persist:
- task state;
- decisions;
- intermediate artifacts;
- user preferences;
- tool results;
- unresolved questions.

Common stores: scratchpads, repo files (e.g. `CLAUDE.md` / `AGENTS.md`), or a memory store. A single giant instructions file tends to fail — prefer a short (~100-line) table of contents pointing into a structured `docs/` tree, with progressive disclosure.

### Select

Retrieve only what is needed:
- relevant documents (RAG);
- relevant tool descriptions (RAG over tools when there are many);
- relevant memory;
- relevant prior decisions.

### Compress

Summarize or reduce:
- long conversation history;
- raw tool outputs;
- repeated information;
- old planning steps.

Prefer layered compaction: drop low-value content first (e.g. verbose tool outputs), then summarize, then aggressively summarize — rather than one blunt summarization pass.

### Isolate

Separate:
- independent research tasks;
- risky tool execution;
- experimental reasoning;
- sub-agent exploration.

Give each sub-agent its own context window so the parent never sees the noise.

## Memory Model

Separate memory by type; do not mix them in one store:

| Memory Type | Holds | Lifetime |
|---|---|---|
| Working | Current task state, scratchpad | This run |
| Episodic | Past interactions and outcomes | Across sessions |
| Semantic | Durable facts, preferences, domain knowledge | Long-lived |
| Procedural | How-to / learned routines, skills | Long-lived |

Storage choice follows the dominant requirement: general-purpose recall, evolving facts over time, long-horizon self-editing memory, or human-editable versioned files in the repo. The vendor-agnostic decision rule is more robust than any vendor's self-reported benchmark.

## Context Rules

- Keep context-window utilization below ~40% (the 40% rule).
- Do not pass all context by default.
- Do not pass raw sub-agent transcripts to parent agents.
- Do not include unused tools in the active tool list.
- Do not let memory silently override current user input.
- Do not store sensitive data unless explicitly required.
- Do not store temporary task facts in long-term memory.
- Prefer references to large artifacts over embedding full artifacts.
- Keep context inspectable.

## Context Pack Format

```json
{
  "context_pack_id": "uuid",
  "agent_id": "string",
  "task_id": "string",
  "included_sources": [
    {
      "source_id": "string",
      "source_type": "contract | document | memory | tool_result | user_input | state",
      "reason_included": "string",
      "trust_level": "low | medium | high",
      "freshness": "current | stale | unknown"
    }
  ],
  "excluded_sources": [
    {
      "source_id": "string",
      "reason_excluded": "string"
    }
  ],
  "budget": {
    "max_tokens": 0,
    "estimated_tokens": 0,
    "utilization_target": 0.4
  }
}
```

---

# Sub-Skill 5: Tool Permission Architect

## Mission

Design tool use so agents can act without becoming unsafe.

## Tool Contract

Every tool must have:

```md
# Tool Contract: {Tool Name}

## Purpose
What this tool does.

## Input Schema
Typed input.

## Output Schema
Typed output.

## Side Effects
None / internal write / external write / financial / communication / destructive.

## Permission Tier
P0 / P1 / P2 / P3 / P4 / P5 / P6.

## Preconditions
What must be true before execution.

## Postconditions
What must be verified after execution.

## Failure Cases
Known failures and recovery behavior.

## Audit Requirements
What must be logged.
```

## Permission Tiers

| Tier | Type | Examples | Approval |
|---|---|---|---|
| P0 | Read | retrieve document, inspect state | No |
| P1 | Draft | create draft, suggest plan | No |
| P2 | Internal Write | save draft, update internal task state | Usually no |
| P3 | External Write | publish page, update external CRM | Yes |
| P4 | Financial | create charge, change price, issue refund | Yes |
| P5 | Communication | send email, message user, notify customer | Yes |
| P6 | Destructive | delete data, revoke access, overwrite production | Always yes |

## Tool Design Rules

- **MCP by default.** For any non-proprietary integration, prefer a Model Context Protocol server over a custom one-off integration; it future-proofs the tool surface and makes tools reusable across clients.
- Keep the active tool set small: **< 20 active tools per agent** (hard ceiling well under 100). Beyond that, descriptions overlap and tool selection degrades.
- For large tool catalogs, use **RAG over tool descriptions** to fetch only the relevant subset for the current step (a documented ~3.2× lift in tool-selection accuracy).
- Design tool names and descriptions like prompts: name them, describe them, give examples, document edge cases.
- Prefer formats the model saw in training (Markdown diffs, JSON) over custom DSLs.
- Default to structured, schema-validated outputs.

## Tool Execution Cycle

```text
propose tool call
→ validate input schema
→ check tool allowlist
→ check actor permissions
→ check blast radius
→ request approval if needed
→ execute in sandbox if applicable
→ verify postconditions
→ write trace
```

## Tool Safety Rules

- Treat tools as RPC surfaces exposed to untrusted input.
- Use least-privilege credentials and OAuth 2.1 scopes (with Resource Indicators). **Never pass a user's token through to a downstream tool, and never over-scope "to be safe"** — both are confused-deputy openings.
- Use sandboxing where possible.
- Separate read tools from write tools.
- Separate draft creation from publishing.
- Require approval for external side effects (P3+).
- Require approval for financial actions (P4).
- Require approval for external communication (P5).
- Always require approval for destructive actions (P6).
- Log every tool call with input summary and output summary.
- Never let the model invent tool names.
- Never let tool permissions live only in the prompt.
- **Pin MCP tool definitions by cryptographic hash and alert on any change** — a server can mutate a tool's description after you approved it (rug pull / tool poisoning). Install community servers only from an allow-listed registry, version-pinned and signature-checked. Treat every external MCP server as untrusted supply chain.
- **Run the lethal-trifecta check on the tool set as a whole:** if the agent can reach private data, ingest untrusted content, *and* communicate externally, break one leg before shipping (see Doctrine 7).

## Tenant Isolation

If the product is multi-tenant, `tenant_id` is part of the principal — *who is calling* — alongside the P0–P6 permission tier, not a tool argument the model fills. An agent is a confused deputy: isolation enforced in the prompt will eventually leak one tenant's data to another via injection, an ambiguous query, or a mis-targeted tool call. Enforce below the model, fail closed.

- Derive `tenant_id` from the authenticated session/token only — never from the model, prompt, or context. No resolvable tenant means reject the request; there is no default tenant.
- Enforce at the data boundary in code (row-level security or the repository layer), so a fully prompt-injected agent still cannot widen scope. Same gate that pins permissions pins the tenant.
- Thread the tenant through every path: queries, tool calls, long-term memory namespaces, the answer/embedding cache key, traces, sub-agent messages, and background jobs. One unscoped path defeats the boundary.
- The leakage paths agents add beyond ordinary SaaS: cross-tenant retrieval (filter inside the index, not after top-k), un-namespaced memory, a tenant-agnostic cache serving A's answer to B, mixed traces/eval sets, and lost tenant context on hand-off. Walk each one.
- Tools ignore any tenant the model supplies; a tenant mismatch is a fail-closed precondition and is audited.
- Choose an isolation model per data store — pooled with row-level security (default for many tenants), schema-per-tenant, or database/deploy-per-tenant (strongest) — and record it in the Agent Contract.

---

# Sub-Skill 6: Reliability & Durable Execution Architect

## Mission

Keep agents alive, recoverable, and safe across crashes, transient failures, and high-blast-radius actions. Stateless agents lose everything on crash — durable execution is table stakes, not a nice-to-have, for any work that runs longer than a single fast call.

## Durable Execution Model

Split the system into deterministic orchestration and non-deterministic effects:

- **Agent loop = Workflow** — deterministic, replayable from an event log.
- **LLM calls and tool invocations = Activities** — non-deterministic, individually retryable.
- **State = a first-class object.** The agent should behave as a pure function: `(state, event) → new_state`.

This makes runs **resumable**: a killed process can resume from the last durable checkpoint without redoing completed work.

## Reliability Properties

The implementation must include:

- **Retry policy** with backoff for transient failures (rate limits, timeouts, 5xx).
- **Idempotency** for any Activity with side effects, so retries do not double-charge or double-send.
- **Timeouts** at every external boundary.
- **Fallback paths** for predictable failure modes.
- **Partial-failure recovery** — a failed sub-task must not corrupt the whole run.
- **Pause / resume** as a first-class capability; agents should be triggerable from any interface (webhook, cron, chat, email, API).

## Guardrails (Defense in Depth)

Validate both input and output in code, not in the prompt. Multiple cheap guardrails beat one perfect one.

Minimum guardrail set:
- **Schema validation** on every critical path.
- **PII** detection/redaction where relevant.
- **Prompt-injection / jailbreak** detection — including **indirect** injection (malicious instructions hidden in retrieved documents, tool output, or web content, not just the user turn). This is the dangerous variant for agents.
- **Content classification** for unsafe output.
- **Egress / exfiltration check** on outbound actions when the agent touches private data — the output-side leg of the lethal trifecta (Doctrine 7).

Run guardrails **in parallel** with the main agent when latency matters; run them as **blocking** checks when risk is high. Guardrails are one tactic inside Security & Identity (Doctrine 7), not a substitute for structural controls — a filter that catches ~97% still passes ~3% of injections.

## Human-in-the-Loop

Human-in-the-loop is a load-bearing pattern, not an afterthought. Use three concrete modes:

- **Notify** — inform the human; no response required.
- **Ask** — the agent pauses and asks a question before continuing.
- **Review** — the human approves, edits, or rejects (with feedback) a proposed action before it commits.

Required design points:
- **Interrupt between tool selection and tool invocation** for high-blast-radius actions.
- Require explicit approval before any P3+ side effect.
- Prefer an "agent inbox" UX where a human reviews queued actions before they execute.

---

# Sub-Skill 7: Eval Observability Engineer

## Mission

Make agent quality measurable and regressions visible.

## Eval Pyramid

Use three levels:

```text
Level 3: Human review      (on significant changes, ~20-50 traces)
Level 2: LLM-as-judge      (on a cadence, binary, calibrated)
Level 1: Code assertions   (on every change, cheap)
```

Start at the bottom and promote upward only when a failure mode is genuinely subjective.

## Level 1: Code Assertions

Use for deterministic requirements:
- schema validity;
- required fields;
- permission checks;
- state transitions;
- tool preconditions;
- postconditions;
- invariant checks.

Examples:

```ts
expect(output.status).toBe("completed")
expect(output.artifacts.length).toBeGreaterThan(0)
expect(output.approvalRequired).toBe(true)
expect(trace.toolCalls.every(call => call.permissionChecked)).toBe(true)
```

## Level 2: LLM-as-Judge

Use only for subjective failure modes.

Rules:
- binary output only: `true` or `false` (Likert scales break alignment with human raters);
- focused judging prompt;
- separate model or separate context from the generator;
- **calibrated against ≥100 human-labeled examples**, with **TPR/TNR tracked every release**;
- do not use generic "helpfulness" as the main metric.

Judge output:

```json
{
  "pass": true,
  "reason": "The output satisfies the acceptance criteria without unsupported claims."
}
```

## Level 3: Human Review

Use for:
- new agent releases;
- major prompt changes;
- high-risk workflows;
- external actions;
- subjective quality standards;
- unclear eval results.

Review 20–50 traces after meaningful changes.

## Required Eval Set

Each agent must have:

```text
/golden
  canonical_success_cases.json

/failure-modes
  known_failures.json

/regression
  production_failures.json

/judges
  subjective_judge_specs.md
```

## Eval Rules

- **Error analysis first.** Read 20–50 production traces by hand before building eval infrastructure.
- Write evals before claiming the agent works.
- Start with product-specific failure modes (e.g. "missed human handoff," "wrong tool selection"), not generic metrics.
- Add every production failure to regression tests.
- Each regression entry carries a four-field **learning trail**, so the eval set
  records *why* understanding changed, not just the failing input:

  ```text
  conjectured: <the belief that turned out wrong>
  refuted by:  <the trace / observation that broke it>
  learned:     <the corrected understanding>
  criterion now: <the new assertion or eval added as a result>
  ```

  An entry missing any of the four fields is a note, not a regression. This is the
  human-readable "why" behind the test; the test itself is still the enforcement.
- Run fast assertions on every change.
- Run expensive judges on a cadence or before release.
- Block deployment on critical regression.
- Keep eval cases versioned.
- Multi-tenant products: a cross-tenant leakage eval is mandatory and code-asserted (never a judge). Seed tenant A with a unique canary, then as tenant B query for it — plus an injection variant that tells the agent to ignore its tenant — across search, memory recall, the warmed cache, and any sub-agent hand-off. Any A-content reaching B fails the build.
- The cross-tenant canary above is a *special case of an anti-criterion* — a
  code-asserted test that fails when a forbidden thing occurs. Generalize it:
  derive an anti-criterion from **every** forbidden action and non-ownership
  clause in the agent contract, not only from tenant isolation.

## Trace Schema

Minimum trace event:

```json
{
  "trace_id": "uuid",
  "run_id": "uuid",
  "agent_id": "string",
  "event_type": "agent.started | context.selected | llm.called | tool.called | guardrail.checked | approval.requested | agent.completed | agent.failed",
  "timestamp": "ISO-8601",
  "input_summary": {},
  "context_refs": [],
  "tool_call": {},
  "model": "string",
  "output_summary": {},
  "validation": {},
  "error": {},
  "parent_event_id": "uuid"
}
```

Instrument once through an open standard (e.g. OpenTelemetry / OpenInference) so the observability vendor can be swapped without re-instrumenting.

---

# Sub-Skill 8: Production Readiness Reviewer

## Mission

Determine whether an agentic system is safe and reliable enough for production.

## Production Readiness Checklist

### Architecture

- [ ] The system uses the least autonomous architecture sufficient for the task.
- [ ] The baseline level reached ≥90% eval pass rate before any escalation in autonomy.
- [ ] Agent boundaries are explicit.
- [ ] Each agent has one primary responsibility.
- [ ] There is a clear final owner of user-facing output.
- [ ] Multi-agent design is justified by real need.

### Contracts

- [ ] Every agent has an Agent Contract.
- [ ] Every tool has a Tool Contract.
- [ ] Every handoff has a Handoff Contract.
- [ ] Output schemas are explicit.
- [ ] Acceptance criteria are testable.

### Context

- [ ] Context is scoped per agent.
- [ ] Context-window utilization stays below ~40% in a typical cycle.
- [ ] State is externalized.
- [ ] Memory is separated by type.
- [ ] Sub-agent outputs are condensed.
- [ ] Large artifacts are referenced instead of blindly embedded.

### Tools and Permissions

- [ ] Tools are allowlisted.
- [ ] Active tool count is < 20 per agent (or RAG-over-tools is used).
- [ ] Tool inputs are schema-validated.
- [ ] Permissions are enforced in code.
- [ ] Destructive actions require approval.
- [ ] Financial actions require approval.
- [ ] External communication requires approval.
- [ ] Tool calls are logged.

### Tenant Isolation (if multi-tenant)

- [ ] An isolation model is chosen per data store and recorded in the Agent Contract.
- [ ] `tenant_id` is derived from auth only; a request with no tenant fails closed.
- [ ] Isolation is enforced below the LLM (row-level security / repository layer) and survives prompt injection.
- [ ] Retrieval, memory, cache keys, traces, sub-agent messages, and background jobs are all tenant-scoped.
- [ ] Tools ignore any model-supplied tenant; a mismatch is audited and rejected.
- [ ] A code-asserted cross-tenant leakage eval exists and runs in CI.

### Security & Identity

- [ ] The lethal-trifecta check is performed and documented; if all three legs are present, at least one is broken.
- [ ] MCP tool definitions are pinned by hash with change alerts; servers come from an allow-listed registry, version-pinned and signature-checked.
- [ ] Tokens are OAuth 2.1 scoped, short-lived, and audience-bound; no token passthrough; no over-scoping.
- [ ] Each agent has a distinct least-privilege identity; identity and tenant are derived from auth, never from the model.
- [ ] Indirect prompt injection (poisoned documents / tool output) is in the threat model, not just user-turn injection.

### Cost

- [ ] A per-run token / cost ceiling is enforced in code (circuit breaker on runaway sessions).
- [ ] Cost-per-task is tracked in traces; prompt/KV caching is enabled on stable prefixes.
- [ ] For multi-agent designs, the value of the task justifies the ~15× token cost.

### Reliability

- [ ] Agent execution can retry with backoff.
- [ ] Side-effecting actions are idempotent.
- [ ] Long-running work can pause/resume (durable execution).
- [ ] Errors are structured.
- [ ] Timeouts exist at external boundaries.
- [ ] Fallback paths exist.
- [ ] Guardrails run on input and output.
- [ ] Human escalation exists (notify / ask / review).

### Evals

- [ ] Each agent has golden cases.
- [ ] Each agent has failure-mode tests.
- [ ] Production failures become regression tests.
- [ ] Subjective judges use binary outputs.
- [ ] Judges are calibrated against human labels (TPR/TNR tracked).
- [ ] Human review exists for high-risk changes.
- [ ] CI blocks critical regressions.

### Observability

- [ ] 100% of production agent runs are traced.
- [ ] Tool calls are visible in traces.
- [ ] Context selection is visible in traces.
- [ ] Permission checks are visible in traces.
- [ ] Guardrail and approval decisions are visible in traces.
- [ ] Errors can be grouped by failure mode.

## Review Output Format

When reviewing, return:

```md
# Production Readiness Review

## Verdict
Ready / Not Ready / Ready With Conditions

## Critical Blockers
Items that must be fixed before release.

## Major Risks
Items likely to cause failures.

## Missing Controls
Required controls not yet present.

## Recommended Architecture Changes
Specific structural improvements.

## Required Evals
Tests that must be added.

## Release Gate
Exact condition for approval.
```

---

# Universal Agent Definition of Done

An agent is done only when all of these are true:

```md
- [ ] Agent Contract exists.
- [ ] Agent has one clear owner artifact.
- [ ] Inputs are schema-validated.
- [ ] Outputs are schema-validated.
- [ ] Guardrails run on input and output.
- [ ] Context is scoped (utilization target < ~40%).
- [ ] State is externalized and durable.
- [ ] Tools are allowlisted (< 20 active, or RAG-over-tools).
- [ ] Permissions are enforced in code.
- [ ] Side effects are classified (P0–P6).
- [ ] Approval gates exist where needed.
- [ ] Lethal-trifecta check performed and documented; a leg is broken if all three are present.
- [ ] MCP tool definitions pinned by hash; servers allow-listed; OAuth 2.1 scoped tokens, no passthrough.
- [ ] Per-run token/cost ceiling enforced in code; cost-per-task tracked.
- [ ] Retry, timeout, and idempotency policies exist.
- [ ] Long-running work can pause/resume.
- [ ] Trace events are emitted (OTel GenAI conventions).
- [ ] Known failure modes are documented.
- [ ] Golden evals exist.
- [ ] Failure-mode evals exist.
- [ ] Regression evals exist or have a place to live.
- [ ] Human escalation path exists.
- [ ] README explains how to run, test, and debug the agent.
```

---

# Universal Multi-Agent Definition of Done

A multi-agent system is done only when all of these are true:

```md
- [ ] Multi-agent architecture is justified (breadth-first, parallelizable, independent sub-tasks).
- [ ] Single-agent or workflow baseline was considered.
- [ ] The token-cost multiple of multi-agent is acceptable for the value gained.
- [ ] Orchestrator responsibilities are explicit.
- [ ] Every sub-agent has a contract.
- [ ] Every sub-agent has scoped context.
- [ ] Every sub-agent has an output schema.
- [ ] Agent communication uses Message Envelope.
- [ ] Handoffs use Handoff Contracts.
- [ ] Shared state is explicit.
- [ ] Sub-agents return condensed findings, not raw transcripts.
- [ ] Conflict resolution exists.
- [ ] Final synthesis owner exists.
- [ ] QA layer checks compatibility of outputs.
- [ ] Approval gates exist before external side effects.
- [ ] End-to-end traces exist.
- [ ] End-to-end evals exist.
```

---

# Default Implementation Prompt for Claude Code

Use this prompt when asking Claude Code to implement an agent.

```md
You are implementing an agentic product module using the Agentic Product Agent Standard.

Before writing code:
1. Identify the least autonomous architecture that solves the task.
2. Create or update the Agent Contract.
3. Define input and output schemas.
4. Define allowed tools and permission tiers (P0–P6).
5. Define state, durability, and trace events.
6. Define eval cases.

Implementation requirements:
- Use deterministic control flow wherever possible.
- Use LLM calls only where reasoning, generation, classification, or synthesis is genuinely needed.
- Validate all inputs and outputs with schemas; add guardrails on both.
- Keep state outside the context window; make it durable and resumable.
- Scope context per task; target context-window utilization below ~40%.
- Enforce permissions in code.
- Log all agent decisions, tool calls, validations, and errors.
- Add retry, timeout, and idempotency policies.
- Add eval fixtures and tests.
- Do not rely on prompt instructions for security or permissions.
- Do not introduce multi-agent architecture unless justified.

Required output:
- agent contract
- schemas
- runner
- tool interface
- permission checks
- guardrails
- durable state / retry policy
- trace events
- eval fixtures
- tests
- README
```

---

# Default Implementation Prompt for Multi-Agent Workflows

```md
You are implementing a multi-agent workflow using the Agentic Product Agent Standard.

Before writing code:
1. Prove why a multi-agent design is needed (breadth-first, parallelizable, independent sub-tasks) and that the token-cost multiple is acceptable.
2. Define the orchestrator.
3. Define each sub-agent contract.
4. Define the message envelope.
5. Define handoff contracts.
6. Define shared state.
7. Define conflict resolution.
8. Define the QA layer.
9. Define end-to-end evals.

Implementation requirements:
- The orchestrator owns planning, delegation, synthesis, and final QA.
- Sub-agents own bounded artifacts only.
- Sub-agents must return condensed findings, not raw transcripts.
- All messages must use a structured envelope.
- All handoffs must be explicit.
- All outputs must be schema-validated.
- All tools must go through permission checks.
- All external side effects must require approval.
- All runs must be traceable.
- The system must support retry and partial failure recovery.

Required output:
- orchestrator contract
- sub-agent contracts
- message envelope schema
- handoff schema
- shared state schema
- orchestrator runner
- sub-agent runners
- QA/evaluator module
- trace events
- eval fixtures
- end-to-end tests
- README
```

---

# Review Prompt

Use this prompt to review existing agentic code.

```md
Review this implementation against the Agentic Product Agent Standard.

Evaluate:
1. Is this the least autonomous architecture sufficient for the task?
2. Are agent boundaries clear?
3. Does every agent have a contract?
4. Are inputs and outputs schema-validated, with guardrails?
5. Is context scoped, and does utilization stay below ~40%?
6. Is state externalized and durable/resumable?
7. Are tools allowlisted and kept under ~20 active?
8. Are permissions enforced in code?
9. Are side effects classified (P0–P6)?
10. Are approval gates present for P3+ actions?
11. Are retries, timeouts, and idempotency handled?
12. Are traces emitted for every run?
13. Are evals present and judges calibrated?
14. Are failure modes tested?
15. Is multi-agent architecture justified?
16. What would fail in production?

Return:
- verdict;
- critical blockers;
- major risks;
- missing controls;
- recommended code changes;
- required evals;
- release gate.
```

---

# Non-Negotiable Rules

1. Do not create an agent without an Agent Contract.
2. Do not create a tool-using agent without a Tool Contract.
3. Do not create a multi-agent system without an orchestrator.
4. Do not pass raw sub-agent transcripts to parent agents.
5. Do not let agents communicate through unstructured free-form text when state matters.
6. Do not rely on prompts for permission enforcement.
7. Do not let agents perform destructive actions without approval.
8. Do not let agents perform financial actions without approval.
9. Do not let agents send external communications without approval.
10. Do not treat memory as a dumping ground.
11. Do not use LLM-as-judge where code assertions are enough.
12. Do not use LLM-as-judge without calibrating against human labels.
13. Do not use generic evals as the primary quality signal.
14. Do not ship long-running agents without durable execution.
15. Do not exceed ~40% context-window utilization by default.
16. Do not claim production readiness without traces.
17. Do not add autonomy without eval evidence.
18. Do not choose a framework before defining the architecture.
19. Do not express a forbidden action only in prose — pair it with a code-asserted anti-criterion.
20. Do not let the model select from an open vocabulary where a closed enumeration can be inlined.
21. Do not ship the lethal trifecta (private data × untrusted content × external comms) without breaking at least one leg.
22. Do not load community MCP tool definitions without pinning them by hash and alerting on change.

---

# Final Mental Model

```text
Agent =
Contract
+ Scoped Context
+ Tools
+ Permissions
+ Durable State
+ Verification
+ Trace
```

```text
Multi-Agent System =
Orchestrator
+ Specialist Agents
+ Message Envelope
+ Handoff Contracts
+ Shared State
+ QA Layer
+ End-to-End Evals
```

```text
Harness =
Agent Loop
+ Context & Memory
+ Durable Execution
+ Guardrails
+ Human-in-the-Loop
+ Evaluation
+ Observability
```

```text
Production Agentic Product =
Deterministic Workflow
+ Bounded Agency
+ Durable Execution
+ Human Approval Gates
+ Observability
+ Continuous Evals
```

The model is replaceable.
The harness is the product.

---

# Appendix: Evidence & Sources

This standard is prescriptive, but its load-bearing claims are grounded in published
production practice from 2024–2026. The anchors below let a reader verify the
numbers rather than take them on faith; treat vendor-published figures as
directionally correct, not as audited benchmarks.

| Claim in this document | Anchor / source |
|---|---|
| Workflows vs. agents distinction; the five composition patterns; "start with LLM APIs directly" | Anthropic, *Building Effective Agents* (Schluntz & Zhang, Dec 2024) |
| Production-oriented ladder of autonomy; routing, handoff vs. agent-as-tool | OpenAI, *A Practical Guide to Building Agents* (2025) |
| Own your prompts/context/control flow; agents as pure functions of state; resumability; <100 tools / <20 steps | HumanLayer, *12 Factor Agents* (Dex Horthy) |
| Multi-agent ≈90.2% lift on breadth-first research at ~15× token cost; sub-agents return condensed findings; separate citation pass | Anthropic, *How we built our multi-agent research system* (Hadfield, Zhang et al., 2025) |
| Single-agent for depth-first / shared-context work; "telephone game" risk | Cognition, *Don't Build Multi-Agents* (Walden Yan, Jun 2025) |
| Context engineering = write / select / compress / isolate | LangChain, *Context Engineering for Agents* (Lance Martin, Jun 2025) |
| The ~40% context-window "dumb zone" | HumanLayer (Dex Horthy), empirical context-budget guidance |
| ~98% of a production coding agent is harness, not model loop; harness as the durable advantage | OpenAI, *Harness Engineering* (Feb 2026); Liu et al., Claude Code analysis (arXiv:2604.14228); LangChain, *Improving Deep Agents with harness engineering* (Mar 2026) |
| RAG over tool descriptions ≈3.2× tool-selection accuracy; cuts prompt tokens >50% | *RAG-MCP* (arXiv:2505.03275) |
| MCP scale (10,000+ servers, 177,000+ tools) and MCP/A2A split | MCP security framework (arXiv:2604.05969); *How are AI agents used?* (arXiv:2603.23802); A2A (Google → Linux Foundation, 2025) |
| Permissions must be enforced outside the model — Replit deleted a production DB despite a prompt "code freeze" | Fortune, *AI-powered coding tool wiped out a software company's database* (Jul 23, 2025) |
| Durable execution: agent loop = Workflow (replayable), LLM/tool calls = Activities (retried) | Temporal pattern; first-party integrations for OpenAI Agents SDK, Pydantic AI, Vercel AI SDK, mcp-agent |
| Eval discipline: error analysis first; 3-level pyramid; binary judges; calibrate against ~100 human labels; track TPR/TNR; product-specific failure modes | Hamel Husain, *A Field Guide to Rapidly Improving AI Products* / *Your AI Product Needs Evals*; Shreya Shankar, *Who Validates the Validators?* |
| HITL patterns notify / ask / review; agent inbox; interrupt between tool selection and invocation | LangChain (Harrison Chase), *Introducing ambient agents* (Jan 14, 2025) |
| Guardrails as defense in depth; structured outputs + assertions catch more than judges; trace-based monitoring | OpenAI / Anthropic / Husain reliability-stack consensus |
| Framework choice by dominant constraint, not hype | Research synthesis across LangGraph, OpenAI Agents SDK, Claude Agent SDK, CrewAI, Pydantic AI, LlamaIndex |
| Bitter-pill maintenance (shrink the harness as models improve); closed-enumeration over open vocabulary; derived anti-criteria; conjecture/refutation learning trail | Personal AI Infrastructure (PAI), Daniel Miessler, MIT License (Algorithm v6.3.0; ISA; BitterPillEngineering) |

**Caveats.** The field moves quarterly — "production-grade" drifts. The single-vs-multi-agent boundary is genuinely unsettled at the edge and task classification is itself a judgment call. Memory-vendor and multi-agent benchmarks are largely self-reported. Security (MCP auth, prompt-injection defense, supply-chain integrity of community servers/skills) is the least-mature dimension; treat every agent-executable tool surface with the paranoia you would apply to any RPC endpoint exposed to untrusted input.
