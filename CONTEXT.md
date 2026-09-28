# CONTEXT — shared domain language

The vocabulary every skill in this repo speaks. When a skill says "the harness,"
"L3," or "O1," it means exactly what is defined here. Keep this file
authoritative; when a term's meaning shifts, change it here and the skills
inherit it. The marked sections are generated from `canon/` — edit the canon,
then run `python3 tools/aps.py render`.

## Core stance

- **Agentic product** — a product where part of the process is dynamically
  directed by an LLM **within a deterministic architecture with explicit trust
  boundaries**. Not "a product with AI."
- **Determinism by default, agency by necessity** — autonomy is earned on evals,
  not granted upfront.
- **Harness > model** — production reliability lives in the code around the LLM,
  not in the model; in a production coding agent that harness is ~98% of the code.

## The operating point (autonomy × oversight)

<!-- canon:begin:context.ladder -->
**Autonomy** — who chooses the next step:

- **L0** — single LLM call (one prompt → one response).
- **L1** — augmented LLM (one call + retrieval, tools, memory).
- **L2** — workflow (deterministic code orchestrates LLM steps).
- **L3** — bounded decomposition (the LLM decomposes the task dynamically, within a bounded graph).
- **L4** — autonomous agent loop (the LLM chooses the next step until termination).

**Oversight** — whether a human approves each consequential (P3+) action:

- **O0** — human in the loop: a human approves each consequential action before it executes.
- **O1** — human on the loop: actions inside the declared blast radius execute without per-action approval; a human supervises live and can veto, pause, or take over.
- **O2** — unattended: no human watches in real time; people are reached through the escalation path and sampled review.

**Escalation** — **Climb autonomy** (L → L+1) only when L delivers **pass@1 ≥ 90%** on a curated eval set. **Relax oversight** (O0 → O1 → O2) only under a **Loop License**, whose eval gate adds consistency: **pass^5 ≥ a declared threshold** on the same set. O2 also requires a published **legitimacy rate** (DoD 30).

<!-- canon:end:context.ladder -->

## The five composition patterns

Prompt Chaining · Routing · Parallelization · Orchestrator–Workers ·
Evaluator–Optimizer. Compose these in deterministic code first; a full agent
loop is the last resort.

## The harness (nine layers)

<!-- canon:begin:context.harness -->
1. Agent Loop · 2. Context & Memory Management · 3. Durable Execution · 4. Guardrails · 5. Human-in-the-Loop · 6. Evaluation · 7. Observability & Tracing — over MCP / function calling to Tools. Two cross-cutting layers constrain all 7: 8. Security & Identity (threat model · injection defense · per-agent identity · least-privilege tokens · pinned tool defs · protocol auth baseline) and 9. Cost & FinOps (per-run ceilings in code · caching · routing · cost per verified outcome).

"Layer N" always means a harness layer. `STANDARD.md` Part II is the technology stack, numbered **Stack N**; the two coincide only at 8 and 9.

<!-- canon:end:context.harness -->

## Recurring terms

- **Trust boundary** — the line where an action is checked by **code, not
  prompt** (permissions, preconditions, outcome verification).
- **Cycle of Trust** — gather → propose → check permissions → verify
  preconditions → execute → verify outcome → log trace → update memory.
- **Operating point** — the autonomy level and oversight mode a system runs at,
  written `L3 · O0`. Declared at design time; it decides which licenses the
  system owes and which scorecard band it must reach.
- **Consequential action** — an action at permission tier P3+ (external write,
  financial, communication, destructive). Oversight is about who approves these.
- **Loop License** — the six gates (eval threshold incl. pass^5, regression gate,
  blast radius, cost cap, kill switch, escalation path) a system must hold to
  run at O1+. The **Graph License** is the same six at graph scope.
- **Legitimacy rate** — legitimate successes ÷ reviewed successes; at O2 it gates
  promotion next to pass@1 and pass^5 (DoD 30).
- **Context engineering** — the four operations on the context window: **Write,
  Select, Compress, Isolate**. The context budget: stay under the fill level
  where your evals start to degrade — 40% of the window until you have measured it.
- **Eval pyramid** — Level 1 code assertions (every change) · Level 2 LLM-as-judge
  (calibrated, binary) · Level 3 human/agent trace review. (Not the autonomy levels:
  "L3" always means autonomy.)
- **Failure mode** — a named, product-specific way the system loses trust (e.g.
  "missed human handoff," "wrong tool selection"). Evals are organized by these,
  never by generic "quality."
- **Sub-agent returns synthesis, not transcript** — never pass a raw sub-agent
  transcript up to the parent.

## Skill conventions (how skills in this repo are written)

- One **`SKILL.md`** per skill directory, with YAML frontmatter that follows the
  open **Agent Skills specification** (agentskills.io): `name` (1–64 chars,
  lowercase kebab-case, matches the directory) and `description` (≤1024 chars,
  when-to-use, written as a prompt — the router reads it). No
  vendor-specific fields, so the skills load in any Agent Skills client; a
  body over ~500 lines moves detail into a referenced file.
- Every file a skill ships is hash-locked in `skills-lock.json` and scanned for
  hidden content (invisible Unicode, stray HTML comments, piped installers) —
  `python3 tools/aps.py skills validate`.
- A **master skill** (`agentic-product-architect`) routes to **sub-skills** by
  dominant concern (architecture, context, harness, tools/MCP, memory, durable
  execution, evals, framework choice, production readiness, antipatterns, tenant
  isolation, and the reference stack).
- **Progressive disclosure** — the master stays thin; depth lives in the
  sub-skill it routes to.
- Skills are **small, composable, model-agnostic**, and reference this CONTEXT
  for shared terms rather than re-defining them.

## Authoritative sources

`STANDARD.md` is the canon in prose; `canon/*.yaml` is the same canon in
machine-readable form and the single source for anything enumerable (principles,
ladder, harness, DoD, anti-patterns, scorecard). `examples/agenticmind-case-study.md`
is the reference implementation mapped layer-by-layer. Architectural decisions
about this repo itself live in `docs/adr/`.
