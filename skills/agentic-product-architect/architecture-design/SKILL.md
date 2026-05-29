---
name: architecture-design
description: Design the architecture of an agentic product — choose the autonomy level (L0–L4), compose solutions from the 5 canonical patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer), decide single-agent vs multi-agent, and identify the right production exemplar to model after. Use whenever the user is starting a new agentic project, restructuring an existing one, asking "what pattern should I use," debating single vs multi-agent, or trying to decide between a deterministic workflow and an autonomous agent loop.
---

# Architecture Design for Agentic Products

The architectural decisions made in the first hour of a project determine whether it ships. This skill walks the user through them deliberately.

## Step 1: Determine the autonomy level (Autonomy Ladder)

Never start with "build an agent." Start with "what is the minimum autonomy this task requires?" The cost of getting this wrong is asymmetric: too much autonomy = unreliable, expensive, slow, hard to debug. Too little = doesn't capture value.

| Level | What it is | Cost / latency | Use when |
|---|---|---|---|
| **L0. Single LLM call** | One prompt → one response | Lowest | Classification, extraction, summarization, generation with known structure |
| **L1. Augmented LLM** | LLM + retrieval / tools / memory, but single-shot | Low | Q&A over docs, simple structured tasks, lookup + reformat |
| **L2. Workflow** | Deterministic code orchestrates LLM steps; path is predefined | Low–medium | The execution path is knowable in advance; predictability matters |
| **L3. Orchestrator-Worker** | LLM plans dynamically, dispatches to bounded sub-agents | Medium–high | Parallelizable subtasks (research, multi-source synthesis); breadth-first work |
| **L4. Autonomous Agent Loop** | LLM chooses next step iteratively until termination | Highest | Path cannot be enumerated; emergent behavior is the value; cost compounding is acceptable |

### Escalation rule (non-negotiable)

Do not climb to level N+1 until level N delivers **≥90% pass rate on a curated eval set** of 20–50 examples representing real use.

### Heuristics for choosing the level

Push DOWN one level if any of these apply:
- The user can describe the steps in advance with conditional branches
- Mistakes are expensive (financial, legal, irreversible)
- Latency budget is < 5 seconds end-to-end
- Cost per call is a top-3 constraint
- Debugging needs to be straightforward for a team < 5 engineers

Push UP one level if any of these apply:
- The path genuinely branches in ways you cannot enumerate
- Users explicitly want exploratory or open-ended behavior
- The value is the agent's adaptation, not its output
- You have eval infrastructure ready to catch regressions

## Step 2: Compose from the 5 patterns before reaching for a loop

The industry vocabulary, formalized by Anthropic and adopted by OpenAI, LangChain, LlamaIndex, Spring AI. Most "agentic" products are compositions of these — full agent loops are rare.

### Pattern 1: Prompt Chaining

Decompose into sequential LLM steps. Each step's output feeds the next.

```
input → LLM_step_1 → output_1 → LLM_step_2 → output_2 → LLM_step_3 → final
```

**When to use:** the steps are known and ordered. Adding more steps trades latency for accuracy.

**Example:** outline → draft → polish. Or: extract entities → resolve → format.

**Production tip:** put a code-based gate between LLM steps when the intermediate output has structure that can be checked (schema validation, presence of required fields). Cheap reliability win.

### Pattern 2: Routing

A classifier (small LLM or rule) tags the input; a dispatcher sends it to the right specialist.

```
input → classifier → {handler_A | handler_B | handler_C | escalate_to_human}
```

**When to use:** different types of requests need different handling, and lumping them together hurts quality.

**Example:** customer service triage. Code-review by language. Different prompts for different document types.

**Production tip:** use a small fast model (Haiku, GPT-4.1-mini, Gemini Flash) for the classifier. The cost saving is enormous and the routing accuracy is usually fine.

### Pattern 3: Parallelization

Fan out independent subtasks; aggregate results.

```
input → split → [LLM_1, LLM_2, LLM_3] → aggregate → output
```

Two flavors:
- **Sectioning:** different aspects in parallel (sentiment + topic + intent extraction).
- **Voting:** N runs of the same task; majority or critic picks the winner. Improves reliability on hard problems.

**When to use:** subtasks are genuinely independent; latency matters.

**Production tip:** run guardrails in parallel with the main output — fail-fast on policy violations without blocking the happy path.

### Pattern 4: Orchestrator-Workers

A lead LLM decomposes a task dynamically, spawns workers for each piece, synthesizes their results.

```
input → orchestrator (plans, decides workers) → [worker_1, worker_2, ...] 
      → orchestrator (synthesizes) → output
```

**When to use:** the decomposition itself depends on the input, but the overall shape (plan → workers → synthesize) is known.

**Canonical examples:**
- Anthropic Research feature: LeadResearcher + 3–5 parallel sub-researchers + separate CitationAgent
- Claude Code Task tool: spawns ephemeral Haiku sub-agents for exploration

**Production rules:**
- Sub-agents return **condensed findings**, not raw transcripts ("telephone game" failure mode)
- Each sub-agent gets isolated context window
- The orchestrator owns the final answer, not the sub-agents

### Pattern 5: Evaluator-Optimizer

Generator + critic in a loop. Generator produces output; critic checks against criteria; loop until accept or budget exhausted.

```
input → generator → critic → {accept | feedback} → generator → ... → output
```

**When to use:** "good" is recognizable but not generable in one shot. Quality criteria are clear. Examples: translation refinement, code generation, content with constraints.

**Production tip:** the critic can be a smaller cheaper model or the same model with a different prompt. Cap iterations (typically 3–5) and log every loop for analysis.

## Step 3: Decide single-agent vs multi-agent

This was the most heated architectural debate of 2025. It has been resolved as a task-classification problem.

| Task type | Architecture | Why |
|---|---|---|
| **Breadth-first, parallelizable** — research, exploration, multi-source synthesis, broad audits | Multi-agent (orchestrator + isolated sub-agents) | Isolated context windows; genuine parallelism; sub-agents in separate prompt-engineering modes |
| **Depth-first, coherent** — coding, long-form writing, stateful editing, debugging | Single-agent | Shared context is critical; sub-agents create "game of telephone" |

### The decision algorithm

1. Can the subtasks run in parallel without seeing each other's state? **Yes → consider multi-agent.**
2. Do downstream decisions depend on the full history of upstream choices? **Yes → single-agent.**
3. Is the work bounded by what fits in one context window? **Yes → single-agent.**
4. Is the task primarily exploratory (search, read, summarize) or generative-coherent (build, write, refactor)? **Exploratory → multi-agent; coherent → single-agent.**

### The reconciled view

- Anthropic's Research feature (multi-agent) outperformed single-agent by 90% on research tasks — at 15× the token cost. **Justified because research is breadth-first and parallelizable.**
- Cognition's Devin (single-agent) deliberately avoids multi-agent for coding. **Justified because coding requires coherent context across every step.**

Both are correct for their domain. **The mistake is applying the wrong one.**

## Step 4: Find a reference exemplar

Always anchor a new architecture to a production system whose patterns parallel yours. Recommend the user study its architecture writeup before writing code.

| Your use case | Study this | Key lessons |
|---|---|---|
| Coding / dev tool | Claude Code, Cognition Devin | Harness as 98% of code; permission modes; compaction pipeline; RPI framework |
| Research / synthesis | Anthropic Research feature | Orchestrator + isolated workers + separate citation pass; condensed findings only |
| Customer service / support | Sierra | Agent Development Life Cycle; multi-model constellation; outcome-based pricing forces eval discipline |
| Autonomous codebase work | OpenAI Codex harness | Mechanical invariants via custom linters; progressive disclosure via docs/; self-validation against runtime traces |
| Vertical agent (legal, medical, finance) | Harvey, OpenEvidence | Domain corpora + tool design matters more than model selection |

## Step 5: Sketch the architecture in one diagram

Before writing code, the architecture should fit on one page. Required elements:

- Entry point (what triggers the agent)
- Each LLM call shown explicitly with its model tier (small / flagship)
- Each tool / external API
- State store (where state persists between turns)
- Permission boundaries (what cannot happen without human approval)
- Termination conditions (when does the agent stop)
- Trace points (what gets logged)

If the diagram has more than ~12 boxes, the design is too complex; simplify before building.

## Common architectural failure modes (call these out aggressively)

- **"Let's just give it tools and see what it does"** — the agent will pick the wrong tools, loop, and burn tokens. Specify the path until you have evidence the model can find it.
- **"We need multi-agent for our customer service"** — usually wrong. Customer service is depth-first (one conversation, one context). Route to specialists, don't spawn parallel agents.
- **"Multi-step reasoning needs an agent loop"** — usually wrong. Prompt chaining with a reflection step handles 80% of "multi-step" tasks at L2.
- **"Let the LLM decide which tool to call"** — only with <20 tools and good descriptions. Above that, route or use RAG-MCP first.

## Output of this skill

When you complete an architecture-design conversation, the user should have:

1. A named autonomy level (L0–L4) with justification
2. A composition expressed in the 5-pattern vocabulary
3. A single-vs-multi-agent decision with the deciding heuristic
4. A reference exemplar to study
5. An architecture diagram (textual is fine) with all 7 required elements
6. Three failure modes identified for the eval set

Then route them to:
- `tool-design-mcp/` if they're integrating external systems
- `context-engineering/` for state and prompt design
- `eval-driven-dev/` to build the eval set before writing code
- `framework-selection/` to choose the implementation framework
