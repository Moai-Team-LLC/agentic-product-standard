# Changelog

All notable changes to The Agentic Product Standard are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2.0.0] — 2026-06-06

The "credibility document → operational tool" increment. Security becomes first-class, cost becomes a discipline, the 2026 landscape is refreshed, and the standard ships its first runnable artifacts and a self-assessment scorecard.

### Added
- **Security as a first-class concern.** New **Principle 6** ("Security is a structural property, not a guardrail"), an **8th harness layer** (Security & Identity, cross-cutting), a new **Layer 8** in the stack (OWASP Top 10 for Agentic Applications, the **lethal trifecta** check, MCP supply-chain controls, OAuth 2.1, agent identity), and **Operating Doctrine 7** in `AGENT_STANDARD.md`. Hardened the Tool Permission sub-skill and guardrails (indirect injection, egress check); added DoD items 13–14, Non-Negotiable Rules 21–22, and four anti-patterns.
- **Cost & FinOps discipline.** New **Layer 9** (per-run token/cost ceilings, prompt/KV caching, model routing, cost-per-outcome, the multi-agent ~15× economics rule), DoD item 15, and a budget-ceiling anti-pattern.
- **Self-assessment scorecard** ([`SCORECARD.md`](SCORECARD.md)) — a binary M0–M3 maturity model mapped to the Autonomy Ladder, scored against the Definition of Done plus the new security/cost items.
- **Runnable artifacts** — a red-team kit ([`templates/security/`](templates/security/README.md): lethal-trifecta gate, indirect-prompt-injection suite, MCP tool-definition hash-pinning / rug-pull detector) and a CI eval-gating workflow template ([`templates/ci/eval-gate.yml`](templates/ci/eval-gate.yml)).
- **PAI-derived rules** (adapted from Daniel Miessler's Personal AI Infrastructure, MIT) — Doctrine **6 Bitter-Pilled Maintenance** (shrink the harness as models improve), **closed enumerations over open vocabularies**, **derived anti-criteria** from every forbidden action, **hard-to-vary** acceptance criteria, a **conjecture/refutation learning trail** on regressions, conservative-escalation default, and Non-Negotiable Rules 19–20.
- **Part IX: Emerging & deferred** — an explicit "not yet promoted" list (A2A depth, model adaptation / RL, agent experience, orchestration topologies, agentic/Graph RAG, computer-use & voice).

### Changed
- **2026 refresh:** Microsoft Agent Framework 1.0 GA (AutoGen + Semantic Kernel → maintenance), production-grade vendor SDKs, MCP 2025-11-25 stable / 2026-07-28 RC + OAuth 2.1 + registry, A2A at the Linux Foundation; observability re-anchored on **OpenTelemetry GenAI semantic conventions** (agent vs. LLM observability, online evals); the **40% rule** reframed as harness doctrine backed by context-rot research; single-vs-multi-agent reaffirmed as the **orchestrator-subagent** consensus.
- **Evals:** added trajectory / multi-turn / session-level evaluation, the **`pass^k`** reliability metric, online/production evals, and reference benchmarks.
- Definition of Done grew from **12 → 15** items.

[2.0.0]: https://github.com/Moai-Team-LLC/agentic-product-standard/releases/tag/v2.0.0

## [1.4.0] — 2026-06-01

### Added
- **`tenant-isolation` sub-skill** — multi-tenancy for agentic products: the pooled / bridge / silo isolation models, the agent-specific leakage paths most teams miss (cross-tenant retrieval, memory, **cache**, traces, a model-supplied `tenant_id`, sub-agent hand-off), `tenant_id` modeled as a principal dimension enforced below the LLM (fail-closed), reference RLS patterns, and a mandatory code-asserted cross-tenant leakage eval. Threaded into `AGENT_STANDARD.md`, `STANDARD.md` (Part III), the `production-readiness` and `memory-architecture` sub-skills, the master router, and the `agent-builder` eval template.

[1.4.0]: https://github.com/Moai-Team-LLC/agentic-product-standard/releases/tag/v1.4.0

## [1.3.0] — 2026-06-01

### Added
- **`agent-builder` skill track** — a self-contained single-agent standard (`AGENT_STANDARD.md`, surfaced at the repo root and bundled into the skill) with copy-paste `templates/`, alongside the multi-agent `agentic-product-architect` track.
- **AgenticMind as the flagship reference implementation** — a layer-by-layer compliance case study ([`examples/agenticmind-case-study.md`](examples/agenticmind-case-study.md)), cross-links across the skills and README, and a `setup.sh --with-agenticmind` one-run installer.
- **`npx skills add` install path**, a shared domain vocabulary ([`CONTEXT.md`](CONTEXT.md)), and architecture decision records ([`docs/adr/`](docs/adr/)).
- Community-health files: SECURITY, GOVERNANCE, SUPPORT, ROADMAP, CODEOWNERS.

### Removed
- The Russian translation (`docs/STANDARD.ru.md`). The standard is now English-only.

[1.3.0]: https://github.com/Moai-Team-LLC/agentic-product-standard/releases/tag/v1.3.0

## [1.0.0] — 2026-05-29

### Added
- The canonical standard ([`STANDARD.md`](STANDARD.md)) in English.
- The five principles, the Autonomy Ladder (L0–L4), the five composition patterns, the single-vs-multi-agent decision, the seven-layer harness, and the Cycle of Trust.
- The 12-point production-readiness Definition of Done.
- The three-level eval pyramid and judge-calibration discipline (Husain/Shankar).
- The 12 anti-patterns and the 12-week build roadmap.
- The `agentic-product-architect` Claude Code skill set: one master skill routing to ten sub-skills (architecture, context, harness, tools/MCP, memory, durable execution, evals, framework selection, production readiness, antipatterns review).
