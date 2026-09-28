<div align="center">

# The Agentic Product Standard

### A canonical standard for building production-grade agentic products — plus a Claude Code skill set that operationalizes it.

*Distilled from the production practices of Anthropic, OpenAI, Cognition, Sierra, LangChain, and leading practitioners — 2024–2026.*

<!-- canon:begin:readme.badges -->
[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Claude Code Skills](https://img.shields.io/badge/Claude%20Code-Skills-d97757.svg)](skills/agentic-product-architect)
[![Standard v4.0.0](https://img.shields.io/badge/Standard-v4.0.0-blue.svg)](STANDARD.md)
[![Self-assessment scorecard](https://img.shields.io/badge/scorecard-M0–M3-success.svg)](SCORECARD.md)
[![Conformance: aps-conformance](https://img.shields.io/badge/conformance-aps--conformance-informational.svg)](docs/conformance.md)
[![Stars](https://img.shields.io/github/stars/Moai-Team-LLC/agentic-product-standard?style=social)](https://github.com/Moai-Team-LLC/agentic-product-standard/stargazers)

<!-- canon:end:readme.badges -->

**[Product Standard →](STANDARD.md)**  ·  **[Agent Standard →](AGENT_STANDARD.md)**  ·  **[Install the Skills →](#-install-the-skills)**  ·  **[Decision Checklist →](#-the-10-question-checklist)**

</div>

---

> **An agentic product is not "a product with AI."**
> It is a product where part of the process is dynamically directed by an LLM within a *deterministic architecture* with *explicit trust boundaries*.

Most teams ship agent demos. Few ship agents that survive contact with production. The difference is almost never the model — it's the **architecture, the harness, and the eval discipline** around it. This repo is the field-tested standard for that work, plus a set of [Claude Code skills](skills/) that put it into your editor.

> **Not to be confused with** Klarna's *Agentic Product Protocol* (APP — a draft protocol for agent-driven product discovery, archived in August 2026) or *AgentReady* (ora.ai + Vercel's standard for making a product usable **by** outside agents). This standard governs how you **build and operate** an agentic product.

## Table of contents

- [Why this exists](#why-this-exists)
- [The six principles](#the-six-principles)
- [What's in this repo](#whats-in-this-repo)
- [Install the skills](#-install-the-skills)
- [The AgenticProduct family](#-the-agenticproduct-family)
- [Upstream: AITM-SMB](#-upstream-aitm-smb--deciding-where-ai-belongs)
- [The Autonomy Ladder](#the-autonomy-ladder)
- [The five composition patterns](#the-five-composition-patterns)
- [The 9-layer harness](#the-9-layer-harness)
- [The 10-question checklist](#-the-10-question-checklist)
- [The decision tree](templates/decision-tree/README.md)
- [Score yourself — and prove it in CI](#-score-yourself)
- [The Loop License](#-the-loop-license)
- [Production readiness — Definition of Done](#production-readiness--definition-of-done)
- [Anti-patterns](#anti-patterns)
- [Regulation & frameworks](#-regulation--frameworks)
- [Reading list](#reading-list)
- [Contributing](#contributing)
- [License](#license)

## Why this exists

Six principles converged *independently* across the production practices of the labs and the leading practitioners. They are the spine of every decision in this standard:

## The six principles

<!-- canon:begin:readme.principles -->
| # | Principle | What it means |
|---|---|---|
| 1 | **Determinism by default, agency by necessity** | Every degree of autonomy must be *earned*, not granted upfront. |
| 2 | **Architecture beats framework** | Patterns outlive libraries. |
| 3 | **Harness > model** | Reliability lives in the code *around* the LLM — in Claude Code, by one community estimate, that harness is ~98% of the code. |
| 4 | **Context engineering is the core discipline** | What enters the context window determines everything. |
| 5 | **Eval-driven development is non-negotiable** | No measurement → no improvement. No trace review → no understanding. |
| 6 | **Security is a structural property, not a guardrail** | Safety comes from architecture — identity, least privilege, isolation, pinned tools — not filters bolted onto the edges. |

<!-- canon:end:readme.principles -->

> **The single most important rule:** *Architecture is what remains when the model improves. The model is the variable, the harness is the constant. Invest proportionally.*

## What's in this repo

```
agentic-product-standard/
├── STANDARD.md                          ← the canonical standard (product level)
├── AGENT_STANDARD.md                    ← the single-agent operational standard (mirrored in agent-builder)
├── SCORECARD.md                         ← M0–M3 self-assessment, mapped to the operating envelope
├── CROSSWALK.md                         ← DoD ↔ EU AI Act · OWASP Agentic Top 10 · NIST AI RMF · IMDA
├── CONTEXT.md                           ← shared vocabulary every skill speaks
├── canon/                               ← the machine-readable canon: principles, ladder, harness, DoD, scorecard
├── tools/aps.py                         ← renders the docs from the canon; validates skills; scores conformance
├── action.yml                           ← the aps-conformance GitHub Action (M-level + SARIF for your product)
├── setup.sh                             ← quick setup: skills + (optional) AgenticMind, one run
├── family.sh                            ← stand up the whole reference stack locally, one command
├── templates/conformance/               ← aps-conformance.yaml template, generated from the canon
├── templates/security/                  ← red-team kit: lethal-trifecta gate, injection suite, MCP pin
├── templates/ci/                        ← CI gates: eval regression (pass@1 · pass^k · legitimacy), MCP conformance
├── templates/telemetry/                 ← OTel GenAI trace checker for the telemetry contract (DoD 29)
├── templates/safe-outputs/              ← typed safe-output pattern: the agent proposes, a deterministic applier writes
├── templates/loop-license/CHECKLIST.md  ← one-page Loop License gate (six gates, O1+)
├── templates/graph-license/CHECKLIST.md ← one-page Graph License gate (composition, O1+)
├── templates/decision-tree/             ← which architecture to build, and the license it owes
├── examples/                            ← reference implementations, audited against the canon
├── docs/                                ← conformance guide, advisories, architecture decision records
├── aitm-smb/                            ← AITM-SMB: business-level AI transformation methodology (own semver, split-ready)
└── skills/                              ← Claude Code skill set (operationalizes the standard; hash-locked)
    ├── agent-builder/                    ← single-agent track (bundles AGENT_STANDARD.md + templates/)
    └── agentic-product-architect/        ← multi-agent track: master router + sub-skills
        ├── SKILL.md                      ← master: router + philosophy
        ├── architecture-design/          ← autonomy ladder, 5 patterns, single vs multi
        ├── context-engineering/          ← write/select/compress/isolate, the 40% rule
        ├── harness-engineering/          ← the 9 layers around the LLM loop
        ├── tool-design-mcp/              ← MCP-first, <20 tools, RAG-MCP, sandboxing
        ├── memory-architecture/          ← Mem0 / Zep / Letta / LangMem / files
        ├── tenant-isolation/             ← multi-tenant: pooled/silo, leakage paths, leakage eval
        ├── durable-execution/            ← Temporal Workflow + Activity pattern
        ├── eval-driven-dev/              ← Husain/Shankar pyramid + judge calibration
        ├── framework-selection/          ← LangGraph / Claude SDK / OpenAI SDK / others
        ├── production-readiness/         ← 33-point Definition of Done audit (DOD.md generated from the canon)
        ├── antipatterns-review/          ← code review through 20 known failure modes
        └── reference-stack/              ← the paved road: install & wire the AgenticProduct family
```

Two standards, one practice:

- **[`STANDARD.md`](STANDARD.md)** is the *product-level* reference — read it once, return to it often.
- **[`AGENT_STANDARD.md`](AGENT_STANDARD.md)** is the *single-agent* operational standard — contract, schemas, permission tiers, durable state, evals (also bundled into the `agent-builder` skill so it ships self-contained).
- **[`skills/`](skills/)** is the *practice* — two Claude Code skills (`agent-builder` for one agent, `agentic-product-architect` for multi-agent products) that auto-load the right guidance while you design, build, and review.

## 🚀 Install the skills

The skill set works with [Claude Code](https://claude.com/claude-code). Two tracks share the same sub-skills: **`agent-builder`** for building one production-grade agent (it bundles `AGENT_STANDARD.md` + copy-paste `templates/`), and **`agentic-product-architect`** — a master skill that routes to twelve specialized sub-skills for multi-agent products. Each is independently triggerable.

### Fastest: one command, no clone

If you have [`skills`](https://github.com/mattpocock/skills) (the community skill installer), pull the skill straight from this repo — it scans `skills/`, lets you pick `agent-builder` and/or `agentic-product-architect`, and installs them into the agents you choose:

```bash
npx skills@latest add Moai-Team-LLC/agentic-product-standard
```

> This installs the **skills only**. To also stand up the runnable memory layer ([AgenticMind](https://github.com/Moai-Team-LLC/AgenticMind)), run the `setup.sh --with-agenticmind` flow below — or, after adding the skills, point your agent's MCP client at a self-hosted AgenticMind (see its [Quickstart](https://github.com/Moai-Team-LLC/AgenticMind#-quickstart)).

### Quick setup (one train)

`setup.sh` installs the skills and, in the same run, can stand up **[AgenticMind](https://github.com/Moai-Team-LLC/AgenticMind)** — the reference implementation — as a runnable **knowledge & memory layer** your agent calls over MCP. Design guidance *and* a working substrate, end to end:

```bash
git clone https://github.com/Moai-Team-LLC/agentic-product-standard.git
cd agentic-product-standard
./setup.sh --with-agenticmind        # skills → clone AgenticMind → its setup.sh (deps + Postgres + migrations)
```

Run bare (`./setup.sh`) and it installs the skills, then *asks* whether to set AgenticMind up next. AgenticMind's leg needs [Bun](https://bun.sh) ≥1.3 + Docker; the skills themselves need neither.

```bash
./setup.sh                  # install skills here, then prompt about AgenticMind
./setup.sh --user           # install skills into ~/.claude/skills (every project)
./setup.sh --skills-only    # skills only, no prompt
```

### Manual install

**User-level (available in every project):**

```bash
cp -R agentic-product-standard/skills/* ~/.claude/skills/   # both tracks; they share sub-skills
```

**Project-level (scoped to one repo):**

```bash
mkdir -p .claude/skills
cp -R /path/to/agentic-product-standard/skills/* .claude/skills/   # both tracks
```

Claude Code discovers skills via each `SKILL.md` and its YAML frontmatter. Once installed, `agent-builder` triggers when you set out to build, implement, or review **one** agent, while `agentic-product-architect` triggers for multi-agent products, an agent loop, or any major agentic framework (LangGraph, CrewAI, OpenAI Agents SDK, Claude Agent SDK, Pydantic AI, AutoGen). Ask a focused question — *"Mem0 or Zep?"*, *"how should I structure context?"*, *"review my agent code"* — and the relevant sub-skill loads directly.

## 🌐 The AgenticProduct family

The standard tells you *how*; five reference implementations are repos you can *run* — each building one surface the standard defines. **AgenticOps** *runs* the fleet, **[AgenticMind](https://github.com/Moai-Team-LLC/AgenticMind)** *judges and grounds* its answers, **AgenticPerformance** *measures and improves* what runs, **AgenticGateway** *carries* every model call, and **AgenticAssurance** *red-teams* it — all conforming to this standard.

|     | Member | Role | License |
| --- | --- | --- | --- |
| 📐 | **agentic-product-standard** (this repo) | The contract — principles, autonomy ladder, harness layers, eval discipline (+ Claude Code skills). | MIT |
| ⚙️ | **[AgenticOps](https://github.com/Moai-Team-LLC/AgenticOps)** | Runtime & operations — manifests, scheduling, durable backlog, bounded runner, fleet health. | Apache-2.0 |
| 🧠 | **[AgenticMind](https://github.com/Moai-Team-LLC/AgenticMind)** | Knowledge & memory — auditable, self-improving, citation-enforced, over MCP; Postgres-only. | Apache-2.0 |
| 📈 | **[AgenticPerformance](https://github.com/Moai-Team-LLC/AgenticPerformance)** | Evals & observability — OTel traces, golden-set evals + CI gate, failure clusters, improvement loop. | Apache-2.0 |
| 🌉 | **[AgenticGateway](https://github.com/Moai-Team-LLC/AgenticGateway)** | Model & cost plane — one key, measured routing, ceilings, cache, evidence. | Apache-2.0 |
| 🛡️ | **[AgenticAssurance (AAL)](https://github.com/Moai-Team-LLC/AgenticAssurance)** | Security & assurance — red-teams any agent (OWASP Agentic + MITRE ATLAS), toxic-flow graph, SARIF output. | MIT |

**How they compose.** **AgenticOps** runs the fleet, **AgenticMind** gives agents auditable knowledge & memory, and **AgenticPerformance** measures every run with traces and evals — closing the **run → remember → measure** loop. **AgenticGateway** is the model plane every LLM call in that loop passes through — one key, eval-measured routing, cost ceilings — and **AgenticAssurance** red-teams any agent in the loop, with the whole stack conforming to the **[agentic-product-standard](https://github.com/Moai-Team-LLC/agentic-product-standard)**.

> **Want the whole loop as one deployable engine?** The **[Agentic Platform](https://github.com/Moai-Team-LLC/agentic-platform)** vendors these members as pinned submodules and assembles them into one runnable product — a unified `agentic` CLI, a live console, and a per-product engine you `agentic init` → `agentic up`. ([`family.sh`](family.sh) below spins the family up to *explore*; the platform is the deployable, operable engine.)

**[AgenticMind](https://github.com/Moai-Team-LLC/AgenticMind)** remains the flagship reference implementation — an auditable, self-improving **knowledge & memory layer** agents plug into over MCP (the OSS pick for the memory slot in [`memory-architecture`](skills/agentic-product-architect/memory-architecture)); install it with [`./setup.sh --with-agenticmind`](#quick-setup-one-train). See its [**case study**](examples/agenticmind-case-study.md) for a layer-by-layer conformance map, and **[`ECOSYSTEM.md`](ECOSYSTEM.md)** for the full family — which surface each repo implements, its status, and how they compose.

**Run the whole family locally — one command.** [`family.sh`](family.sh) clones every member and brings up the three long-lived services (Mind, Performance, Gateway) through each repo's own compose + run scripts, then prints how to use the library (Ops) and the CLI (Assurance):

```bash
./family.sh up        # clone + stand up the reference stack   (needs git, docker, bun)
./family.sh status    # health of every service
./family.sh down      # stop everything (Docker volumes preserved)
```

Generated secrets are written into each member's local `.env` and never printed. Paved road, not a mandate — swap any member for your own (Principle 2).

## 🧭 Upstream: AITM-SMB — deciding *where* AI belongs

This standard answers *how to build* an agentic product. **[AITM-SMB](aitm-smb/README.md)** (AI Transformation Methodology for Small and Medium-Sized Businesses) answers the question that comes before it: *which business capability should change, whether AI belongs in that change at all, and how much authority it may have*. It starts from a measurable business Outcome and a Business Capability, not from an AI use case. It treats AI as optional — four of its eighteen intervention families involve AI, and simpler fixes are challenged first — and it requires evidence and human decision gates before AI authority or scale increases.

AITM-SMB lives in [`aitm-smb/`](aitm-smb/) as a self-contained, split-ready methodology with its own versioning (currently 1.1.0), [skills](aitm-smb/skills/INDEX.md), [artifact contracts](aitm-smb/artifacts/INDEX.md), [worked example](aitm-smb/examples/compact-scenario-b/README.md), and [validator](aitm-smb/tools/validate.py). Start with its [quickstart](aitm-smb/QUICKSTART.md).

> **Different ladders, different questions.** AITM-SMB's **L0–L5** is a business *authority* ladder: what the AI may do in the business (suggest, draft, execute with approval, execute within policy, pursue a bounded objective). This standard's operating point describes the AI component: *autonomy* **L0–L4** (who chooses the next step) × *oversight* **O0–O2** (whether a human approves each consequential action). AITM authority corresponds to the oversight axis: up to AITM-L3 a human approves every consequential action (**O0**); AITM-L4 and L5 act without per-action approval (**O1/O2**), so the Loop License binds. Write **AITM-L3** / **APS-L3** in mixed contexts. The [crosswalk](aitm-smb/docs/crosswalk-agentic-product-standard.md) maps the two and shows where an AITM-SMB decision hands off to this standard.

## The Autonomy Ladder

Never start with "build an agent." Start with *"what is the minimum autonomy this task requires — and must a human still approve each action?"* Since v4.0 those are two axes, earned separately; together they are the system's **operating point**. The cost of getting either wrong is asymmetric.

<!-- canon:begin:readme.ladder -->
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

<!-- canon:end:readme.ladder -->

*These are the AI component's autonomy levels and oversight modes (APS-L0…L4, APS-O0…O2). They are not the business-authority levels of [AITM-SMB](aitm-smb/docs/crosswalk-agentic-product-standard.md), which correspond to the oversight axis.*

## The five composition patterns

Compose agentic products from these primitives *like Lego* — before reaching for a framework.

<!-- canon:begin:readme.patterns -->
1. **Prompt Chaining** — sequential decomposition (outline → draft → polish)
2. **Routing** — classifier + dispatcher to a specialist
3. **Parallelization** — fan-out of independent subtasks + aggregation
4. **Orchestrator-Workers** — central planner + dynamic workers
5. **Evaluator-Optimizer** — generator + critic in a loop until acceptance

**Meta-principle:** First try to solve the task by composing these patterns in deterministic code. A full agent loop is the *last* resort.

<!-- canon:end:readme.patterns -->

## The 9-layer harness

In a production agent, the harness — everything *around* the LLM loop — is **most of the code**: ~98% in Claude Code, by a community estimate cited by Liu et al., *Dive into Claude Code* (arXiv:2604.14228). Seven layers stack around the loop; two more cut across all of them.

<!-- canon:begin:readme.harness -->
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

<!-- canon:end:readme.harness -->

> **Permission boundaries are enforced by code, never by prompt.** The Replit incident of July 2025 — an agent deleted a production database holding records on 1,206 executives and 1,196+ companies despite an explicit "code freeze" in its prompt ([Fortune, 23 Jul 2025](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/)) — is the canonical proof. The model will ignore prompt-level restrictions under enough pressure. Code won't.

> **Layers 8 and 9 are cross-cutting.** Identity, least privilege, and isolation constrain every layer; injection defense spans input and output. Run the **lethal-trifecta** check (private data × untrusted content × external comms) on every deployment, **pin MCP tool definitions by hash** so a server can't rug-pull you, speak **MCP 2026-07-28** with its hardened auth, and give **every agent its own identity**. A guardrail is one tactic, not the discipline — see [`STANDARD.md` · Stack 8](STANDARD.md#stack-8-security--identity--cross-cutting) and the [red-team kit](templates/security/README.md). Cost is the same kind of property: a per-run ceiling enforced in code and re-derived on every model change, not a dashboard someone reads after the invoice (Layer 9).

## ✅ The 10-question checklist

Run this before drafting any architecture. It unblocks 80% of design debates.

<!-- canon:begin:readme.checklist -->
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
```

<!-- canon:end:readme.checklist -->

If you can't answer half of these, **slow down and answer them together — don't write code yet.**

Once you can, [**the decision tree**](templates/decision-tree/README.md) turns these answers into a named architecture **and the license it owes** — every leaf lands on both, because the shape is the easy half.

## 📊 Score yourself

Principles are easy to nod along to; **[`SCORECARD.md`](SCORECARD.md)** makes you prove it. It turns the Definition of Done into a binary Yes/No maturity self-assessment with four bands. Your **operating point** decides the band you must reach — autonomy *and* oversight:

<!-- canon:begin:readme.bands -->
| Band | Operating envelope | Means |
|---|---|---|
| **M0 · Prototype** | any autonomy at O0 — no production claim | Works on a demo. No production claim. |
| **M1 · Shippable** | L0–L2 at O0 | Contracts, schemas, guardrails, an eval set, permissions in code, a declared operating point. Every consequential action is human-approved. Safe to put in front of users behind a workflow. |
| **M2 · Production** | up to L3; O1/O2 only with a Loop License | Durable, observable, tenant-isolated, security-checked, identity-scoped, cost-bounded, CI-gated on evals, on the current protocol baselines. |
| **M3 · Autonomous-ready** | L4 at any oversight mode | Online evals, `pass^k` reliability, red-team kit run, full OTel trajectory observability. Earns the right to an open-ended loop. |

<!-- canon:end:readme.bands -->

Run it with the team against a real deployment each release — the first **No** you hit is your next piece of work.

**Then make CI hold you to it.** Answer the scorecard in an `aps-conformance.yaml` — every Yes with evidence (a path in your repo or a URL) — and the **aps-conformance** Action scores it on every PR: the band you reached, the band your operating point requires, and each open control as a SARIF finding tagged with the DoD items and regulatory obligations it supports.

```yaml
# .github/workflows/aps-conformance.yml
- uses: actions/checkout@v4
- uses: Moai-Team-LLC/agentic-product-standard@v4.0.0
  with:
    file: aps-conformance.yaml      # start from templates/conformance/aps-conformance.template.yaml
```

Details: [`docs/conformance.md`](docs/conformance.md). The canon behind the scorecard is machine-readable too — [`canon/`](canon/) holds the principles, the ladder, the harness, the DoD, and the scorecard as YAML with JSON Schemas, and every count in these documents is generated from it.

## 🔒 The Loop License

Autonomy is earned, not granted. Before a system acts **without a human approving each action** — oversight **O1** (a human on the loop) or **O2** (unattended), at any autonomy level — it must hold a **Loop License**: six gates, all required, each enforced in code and tested.

> **Eval threshold (pass@1 *and* pass^5) · regression gate · declared blast radius · cost cap · kill switch · escalation path.**

Miss any one and the system stays at O0 — a human approves each consequential action — no matter how good the model is. Backing the gates: **independent verification** (the producing model never grades its own work, and the checks sit outside its reach — deterministic checks first, a decorrelated calibrated judge second), a **success-legitimacy audit** at O2 (a sample of "successes" is reviewed for gamed checks, and the legitimacy rate gates promotion), a governed **instruction supply chain** (skills and prompts are versioned, spec-valid, hash-locked, eval-gated artifacts), and a hard **ingestion boundary** ("find work" is untrusted input). Full treatment in [`STANDARD.md` Part IV](STANDARD.md#part-iv-the-loop-license--acting-without-per-action-approval-o1); the one-page gate is [`templates/loop-license/CHECKLIST.md`](templates/loop-license/CHECKLIST.md).

## Production readiness — Definition of Done

<!-- canon:begin:readme.dod -->
An agentic product is **not production-ready** until every Definition of Done item that binds to it is satisfied — **33 items**, each with a stable number (numbers are identifiers, so a group may list them out of order). Items marked with a condition bind only when it holds; the rest bind for every production system. [`SCORECARD.md`](SCORECARD.md) says which items evidence each one and the band at which a system may *ship* before it is production-ready; [`CROSSWALK.md`](CROSSWALK.md) maps each to the EU AI Act, OWASP, NIST, and IMDA. Full text in [`STANDARD.md`](STANDARD.md#part-iii-production-readiness--definition-of-done).

| Group | Items |
|---|---|
| Context and state | **1** Context budget held · **2** State externalized · **3** Compaction tested |
| Tools and permissions | **4** Destructive actions need approval · **5** Permissions in code, not prompt · **6** Sandboxed tool execution · **32** Tenant isolation below the LLM *(multi-tenant)* |
| Reliability | **7** Durable pause/resume/retry · **8** Schema-validated outputs · **9** Input/output guardrails |
| Evals and observability | **10** ≥50 evals per failure mode · **11** Judges calibrated (TPR/TNR) *(LLM judges)* · **12** CI blocks regression; 100% traced · **29** Telemetry contract |
| Security and identity | **13** Lethal-trifecta check · **14** MCP tool defs pinned; allow-listed registry *(MCP)* · **26** MCP protocol & auth baseline *(MCP)* · **27** Per-agent identity |
| Cost | **15** Per-run cost ceiling in code |
| Operating without per-action approval (O1+) — the Loop License | **16** Loop License (six gates) *(O1+)* · **17** Stop conditions *(L3+ or O1+)* · **18** Independent verification *(O1+)* · **19** Loop economics *(O1+)* · **30** Success-legitimacy audit *(O2)* |
| Measurement science and human oversight | **20** Judge calibration (ECE/Brier) *(gating judges)* · **21** Retrieval metrics *(retrieval)* · **22** Ground-truth provenance · **23** Drift monitoring · **33** Human oversight as a program |
| Gate integrity | **24** No safety gate silenced to pass CI |
| Composition (multi-agent) | **25** Graph License *(multi-agent, O1+)* · **28** Inter-agent trust *(cross-boundary)* |
| Governance and regulation | **31** Regulatory classification record *(regulated)* |

<!-- canon:end:readme.dod -->

## Anti-patterns

The fastest way to recognize a doomed agent project — the skill set's `antipatterns-review` flags each with a diagnostic and a fix.

<!-- canon:begin:readme.antipatterns -->
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
13. Trusting community MCP servers without pinning or scanning (rug pulls)
14. Deploying the lethal trifecta with no mitigation
15. Token passthrough / over-scoped OAuth (confused deputy)
16. No budget ceiling on autonomous sessions
17. Peer-to-peer multi-agent buses instead of an orchestrator
18. Prose topology counted as a control (an SOP-defined route is not a guardrail)
19. License inheritance by wiring (a graph of licensed loops is not a licensed graph)
20. Counting a pass as a success without legitimacy review

<!-- canon:end:readme.antipatterns -->

## 📜 Regulation & frameworks

Every Definition of Done item produces evidence — a test, a trace, a record, a gate. **[`CROSSWALK.md`](CROSSWALK.md)** maps that evidence onto the frameworks teams get asked about: the **EU AI Act** (with the dates fixed by the Digital Omnibus, Regulation (EU) 2026/1744 — Art. 50 transparency from 2 Aug 2026, high-risk obligations from 2 Dec 2027 for Annex III and 2 Aug 2028 for Annex I), the **OWASP Top 10 for Agentic Applications**, the **NIST AI RMF**, and Singapore **IMDA**'s agentic governance framework. DoD 31 asks for the input all of it depends on: a written **regulatory classification record** — your role and risk class — kept in version control. A crosswalk is not a compliance claim, and none of this is legal advice.

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
9. Anthropic — *Effective Context Engineering for AI Agents* (just-in-time retrieval)
10. OWASP — *Top 10 for Agentic Applications (2026)* + Simon Willison — *The lethal trifecta*
11. OpenTelemetry — *GenAI semantic conventions* (the observability standard)

**Primary specifications** — the protocols this standard builds on. Pin the revision you conform to:

- [MCP specification **2026-07-28**](https://modelcontextprotocol.io/specification/2026-07-28) (final 28 Jul 2026) and the official [conformance suite](https://github.com/modelcontextprotocol/conformance). What changed: advisory [APS-2026-01](docs/advisories/APS-2026-01-mcp-2026-07-28.md).
- [A2A specification **v1.0.1**](https://github.com/a2aproject/A2A/blob/v1.0.1/docs/specification.md) — v1.0, the first stable release, shipped 12 Mar 2026; §8.4 defines signed Agent Cards.
- [OpenTelemetry GenAI semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai) — moved out of the core semantic conventions at v1.42.0 (June 2026); still *Development* status with no tagged release, so pin a commit.
- [Agent Skills specification](https://agentskills.io/specification) — the open format the skills in this repo follow.

**Governance frameworks** — mapped item by item in [`CROSSWALK.md`](CROSSWALK.md): the [EU AI Act, consolidated with the Digital Omnibus](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng); [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/); [NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf); [IMDA Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/factsheets/2026/updated-model-ai-governance-framework-for-agentic-ai).

## Contributing

This standard is meant to evolve — the field moves fast. Corrections, new exemplars, framework updates, and translations are all welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

The architectural canons (the autonomy ladder, the 5 patterns, single-vs-multi, the harness) are stable. Specific vendors and framework rankings will shift — those are exactly the kind of PRs we want.

Anything enumerable — a principle, a ladder level, a harness layer, a DoD item, an anti-pattern, a scorecard item — lives in [`canon/`](canon/). Edit it there, run `python3 tools/aps.py render`, and commit the regenerated documents with it; CI (`python3 tools/aps.py check`) fails on any drift. [`AGENTS.md`](AGENTS.md) has the full loop for humans and coding agents alike.

## License

[MIT](LICENSE) — use it, fork it, ship with it.

---

<div align="center">

**If this saved you a week of architecture debates, [star the repo](https://github.com/Moai-Team-LLC/agentic-product-standard/stargazers) ⭐ so others find it.**

<!-- canon:begin:readme.footer -->
*v4.0.0 · assembled from production practices as of September 2026*

<!-- canon:end:readme.footer -->

</div>
