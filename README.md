<div align="center">

# The Agentic Product Standard

### A canonical standard for building production-grade agentic products — plus a Claude Code skill set that operationalizes it.

*Distilled from the production practices of Anthropic, OpenAI, Cognition, Sierra, LangChain, and leading practitioners — 2024–2026.*

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Claude Code Skills](https://img.shields.io/badge/Claude%20Code-Skills-d97757.svg)](skills/agentic-product-architect)
[![Standard v1.0](https://img.shields.io/badge/Standard-v1.0-blue.svg)](STANDARD.md)
[![Stars](https://img.shields.io/github/stars/AlexDuchDev/agentic-product-standard?style=social)](https://github.com/AlexDuchDev/agentic-product-standard/stargazers)

**[Read the Standard →](STANDARD.md)**  ·  **[Install the Skills →](#-install-the-skills)**  ·  **[Decision Checklist →](#-the-10-question-checklist)**

</div>

---

> **An agentic product is not "a product with AI."**
> It is a product where part of the process is dynamically directed by an LLM within a *deterministic architecture* with *explicit trust boundaries*.

Most teams ship agent demos. Few ship agents that survive contact with production. The difference is almost never the model — it's the **architecture, the harness, and the eval discipline** around it. This repo is the field-tested standard for that work, plus a set of [Claude Code skills](skills/) that put it into your editor.

## Table of contents

- [Why this exists](#why-this-exists)
- [The five principles](#the-five-principles)
- [What's in this repo](#whats-in-this-repo)
- [Install the skills](#-install-the-skills)
- [The Autonomy Ladder](#the-autonomy-ladder)
- [The five composition patterns](#the-five-composition-patterns)
- [The 7-layer harness](#the-7-layer-harness)
- [The 10-question checklist](#-the-10-question-checklist)
- [Production readiness — Definition of Done](#production-readiness--definition-of-done)
- [Anti-patterns](#anti-patterns)
- [Reading list](#reading-list)
- [Contributing](#contributing)
- [License](#license)

## Why this exists

Five principles converged *independently* across the production practices of the labs and the leading practitioners. They are the spine of every decision in this standard:

## The five principles

| # | Principle | What it means |
|---|---|---|
| 1 | **Determinism by default, agency by necessity** | Every degree of autonomy must be *earned*, not granted upfront. |
| 2 | **Architecture beats framework** | Patterns outlive libraries. |
| 3 | **Harness > model** | 98% of reliability lives in the code *around* the LLM. |
| 4 | **Context engineering is the core discipline** | What enters the context window determines everything. |
| 5 | **Eval-driven development is non-negotiable** | No measurement → no improvement. No trace review → no understanding. |

> **The single most important rule:** *Architecture is what remains when the model improves. The model is the variable, the harness is the constant. Invest proportionally.*

## What's in this repo

```
agentic-product-standard/
├── STANDARD.md                          ← the canonical standard (English)
├── docs/STANDARD.ru.md                  ← original (Russian)
└── skills/agentic-product-architect/    ← Claude Code skill set (operationalizes the standard)
    ├── SKILL.md                          ← master: router + philosophy
    ├── architecture-design/              ← autonomy ladder, 5 patterns, single vs multi
    ├── context-engineering/              ← write/select/compress/isolate, the 40% rule
    ├── harness-engineering/              ← the 7 layers around the LLM loop
    ├── tool-design-mcp/                  ← MCP-first, <20 tools, RAG-MCP, sandboxing
    ├── memory-architecture/              ← Mem0 / Zep / Letta / LangMem / files
    ├── durable-execution/                ← Temporal Workflow + Activity pattern
    ├── eval-driven-dev/                  ← Husain/Shankar pyramid + judge calibration
    ├── framework-selection/              ← LangGraph / Claude SDK / OpenAI SDK / others
    ├── production-readiness/             ← 12-point Definition of Done audit
    └── antipatterns-review/              ← code review through 12 known failure modes
```

Two artifacts, one idea:

- **[`STANDARD.md`](STANDARD.md)** is the *reference* — read it once, return to it often.
- **[`skills/`](skills/agentic-product-architect)** is the *practice* — a hybrid Claude Code skill that auto-loads the right guidance while you design, build, and review agents.

## 🚀 Install the skills

The skill set works with [Claude Code](https://claude.com/claude-code). One master skill routes to ten specialized sub-skills; each is independently triggerable.

**User-level (available in every project):**

```bash
git clone https://github.com/AlexDuchDev/agentic-product-standard.git
cp -R agentic-product-standard/skills/agentic-product-architect ~/.claude/skills/
```

**Project-level (scoped to one repo):**

```bash
mkdir -p .claude/skills
cp -R /path/to/agentic-product-standard/skills/agentic-product-architect .claude/skills/
```

Claude Code discovers skills via each `SKILL.md` and its YAML frontmatter. Once installed, the master skill auto-triggers when you mention building an agent, an agentic product, a multi-agent system, an agent loop, or any major agentic framework (LangGraph, CrewAI, OpenAI Agents SDK, Claude Agent SDK, Pydantic AI, AutoGen). Ask a focused question — *"Mem0 or Zep?"*, *"how should I structure context?"*, *"review my agent code"* — and the relevant sub-skill loads directly.

## The Autonomy Ladder

Never start with "build an agent." Start with *"what is the minimum autonomy this task requires?"* The cost of getting this wrong is asymmetric.

| Level | What it is | Use when |
|---|---|---|
| **L0** · Single LLM call | One prompt → one response | Classification, extraction, summarization |
| **L1** · Augmented LLM | + retrieval, + tools, + memory | Q&A over docs, simple assistants |
| **L2** · Workflow | Deterministic code orchestrates LLM steps | Path is known; predictability matters |
| **L3** · Orchestrator-Worker | LLM decomposes within a bounded graph | Parallelizable, breadth-first work |
| **L4** · Autonomous Agent Loop | LLM chooses the next step until termination | Path cannot be enumerated; cost is acceptable |

> **Escalation rule:** do not climb to L+1 until L delivers **≥90% pass rate** on a curated eval set.

## The five composition patterns

Compose agentic products from these primitives *like Lego* — before reaching for a framework.

1. **Prompt Chaining** — sequential decomposition (outline → draft → polish)
2. **Routing** — classifier + dispatcher to a specialist
3. **Parallelization** — fan-out of independent subtasks + aggregation
4. **Orchestrator-Workers** — central planner + dynamic workers
5. **Evaluator-Optimizer** — generator + critic in a loop until acceptance

**Meta-principle:** first try to solve the task by composing these patterns in deterministic code. A full agent loop is the *last* resort.

## The 7-layer harness

In a production agent, the harness — everything *around* the LLM loop — is **98% of the code**.

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
```

> **Permission boundaries are enforced by code, never by prompt.** The Replit incident of 2025 — an agent wiped a production database for 1,200+ companies despite an explicit "code freeze" in its prompt — is the canonical proof. The model will ignore prompt-level restrictions under enough pressure. Code won't.

## ✅ The 10-question checklist

Run this before drafting any architecture. It unblocks 80% of design debates.

```
□ What is the minimum autonomy level (L0–L4) that solves this?
□ Can it be solved by composing the 5 patterns without a full agent loop?
□ Is the task breadth-first (parallelizable) or depth-first (coherent)?
□ What are the 3 failure modes that would lose user trust first?
□ Where are the permission boundaries? What MUST the agent NOT do?
□ Which constraint dominates framework choice?
□ Where does state live? (in-context = anti-pattern for long-running)
□ Who validates outputs at each stage? (assertion / LLM judge / human review)
□ Where do traces live, with what retention?
□ Eval set: how many examples, who labels, how does it grow?
```

If you can't answer half of these, **slow down and answer them together — don't write code yet.**

## Production readiness — Definition of Done

An agentic product is **not production-ready** until all 12 are satisfied. Full detail in [`STANDARD.md`](STANDARD.md#part-iii-production-readiness--definition-of-done).

| Context & state | Tools & permissions | Reliability | Evals & observability |
|---|---|---|---|
| Context < 40% | Destructive actions need approval | Durable pause/resume/retry | ≥50 evals per failure mode |
| State externalized | Permissions in code, not prompt | Schema-validated outputs | Judges calibrated (TPR/TNR) |
| Compaction tested | Sandboxed tool execution | Input/output guardrails | CI blocks regression; 100% traced |

## Anti-patterns

The fastest way to recognize a doomed agent project — the skill set's `antipatterns-review` flags each with a diagnostic and a fix.

1. Multi-agent before a single-agent baseline
2. Framework abstractions before understanding the raw API
3. LLM judges without calibration against human labels
4. Permissions enforced through prompts
5. Memory as an afterthought
6. Generic evals ("helpfulness," "correctness")
7. Likert scales in an LLM judge (binary only)
8. >100 tools per agent
9. One agent for both breadth and depth
10. Deploying without trace monitoring
11. Hardcoded prompts without version control
12. Treating single-vendor benchmarks as ground truth

## Reading list

The operational base — not reference docs. Read in order:

1. Anthropic — *Building Effective Agents* (Schluntz & Zhang)
2. OpenAI — *A Practical Guide to Building Agents*
3. HumanLayer — *12 Factor Agents* (Dex Horthy)
4. Anthropic — *How we built our multi-agent research system*
5. Cognition — *Don't Build Multi-Agents* (Walden Yan)
6. LangChain — *Context Engineering for Agents* (Lance Martin)
7. Hamel Husain — *A Field Guide to Rapidly Improving AI Products* + *Your AI Product Needs Evals*
8. Anthropic — *Building agents with the Claude Agent SDK*

## Contributing

This standard is meant to evolve — the field moves fast. Corrections, new exemplars, framework updates, and translations are all welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

The architectural canons (the autonomy ladder, the 5 patterns, single-vs-multi, the harness) are stable. Specific vendors and framework rankings will shift — those are exactly the kind of PRs we want.

## License

[MIT](LICENSE) — use it, fork it, ship with it.

---

<div align="center">

**If this saved you a week of architecture debates, [star the repo](https://github.com/AlexDuchDev/agentic-product-standard/stargazers) ⭐ so others find it.**

*v1.0 · assembled from production practices as of May 2026*

</div>
