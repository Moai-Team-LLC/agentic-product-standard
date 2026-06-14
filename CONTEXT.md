# CONTEXT — shared domain language

The vocabulary every skill in this repo speaks. When a skill says "the harness"
or "L3," it means exactly what is defined here. Keep this file authoritative;
when a term's meaning shifts, change it here and the skills inherit it.

## Core stance

- **Agentic product** — a product where part of the process is dynamically
  directed by an LLM **within a deterministic architecture with explicit trust
  boundaries**. Not "a product with AI."
- **Determinism by default, agency by necessity** — autonomy is earned on evals,
  not granted upfront.
- **Harness > model** — ~98% of production reliability lives in the code around
  the LLM, not in the model.

## The ladder (autonomy levels)

- **L0** — single LLM call (classify / extract / summarize).
- **L1** — augmented LLM (+ retrieval, + tools, + memory).
- **L2** — workflow (deterministic code orchestrates LLM steps).
- **L3** — orchestrator–worker (LLM decomposes dynamically; the graph is bounded).
- **L4** — autonomous agent loop (the LLM chooses the next step until termination).

**Escalation rule** — do not climb to L+1 until L hits ≥90% on a curated eval set.

## The five composition patterns

Prompt Chaining · Routing · Parallelization · Orchestrator–Workers ·
Evaluator–Optimizer. Compose these in deterministic code first; a full agent
loop is the last resort.

## The harness (eight layers)

1. Agent Loop (gather → act → verify) · 2. Context & Memory · 3. Durable
Execution · 4. Guardrails (input/output) · 5. Human-in-the-Loop · 6. Evaluation
(CI gates) · 7. Observability & Tracing — over MCP / function calling to Tools.
8. Security & Identity (cross-cutting: identity, least privilege, injection
defense, pinned tool definitions) constrains all seven.

## Recurring terms

- **Trust boundary** — the line where an action is checked by **code, not
  prompt** (permissions, preconditions, outcome verification).
- **Cycle of Trust** — gather → propose → check permissions → verify
  preconditions → execute → verify outcome → log trace → update memory.
- **Context engineering** — the four operations on the context window: **Write,
  Select, Compress, Isolate**. The 40% rule: keep utilization < 40% of the limit.
- **Eval pyramid** — L1 code assertions (every change) · L2 LLM-as-judge
  (calibrated, binary) · L3 human/agent trace review.
- **Failure mode** — a named, product-specific way the system loses trust (e.g.
  "missed human handoff," "wrong tool selection"). Evals are organized by these,
  never by generic "quality."
- **Sub-agent returns synthesis, not transcript** — never pass a raw sub-agent
  transcript up to the parent.

## Skill conventions (how skills in this repo are written)

- One **`SKILL.md`** per skill directory, with YAML frontmatter: `name`
  (kebab-case, matches the directory) and `description` (when-to-use, written as
  a prompt — the router reads it).
- A **master skill** (`agentic-product-architect`) routes to **sub-skills** by
  dominant concern (architecture, context, harness, tools/MCP, memory, durable
  execution, evals, framework choice, production readiness, antipatterns).
- **Progressive disclosure** — the master stays thin; depth lives in the
  sub-skill it routes to.
- Skills are **small, composable, model-agnostic**, and reference this CONTEXT
  for shared terms rather than re-defining them.

## Authoritative sources

`STANDARD.md` is the canon. `examples/agenticmind-case-study.md` is the
reference implementation mapped layer-by-layer. Architectural decisions about
this repo itself live in `docs/adr/`.
