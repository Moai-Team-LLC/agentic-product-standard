# Changelog

All notable changes to The Agentic Product Standard are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- **Cycle of Trust (Canon 5)** gains a **gate-integrity invariant** (`STANDARD.md`): a gate is trust-bearing only if its green state means the property holds, not that the check was silenced. Weakening a correctness / type-safety / security / eval gate to pass CI — disabling a rule repo-wide, `@ts-ignore`, `.skip`, deleting an assertion, lowering a threshold — is a defect, not a fix; a false positive is scoped to a file/glob with a named reason and the gate re-proven to still fire. The mechanical form (a test that fails if the safety rules are flipped off) is exemplified in AgenticMind's shared lint config.
- **SCORECARD** gains a *gate-integrity* control under *Maintenance discipline* (M1).

_Deferred to the next version cut: formalize as a numbered Definition of Done item (23 → 24) with the matching README/badge count update._

## [3.1.0] — 2026-07-13

The **Eval-Science** release. Deepens the Loop License (v3.0) with the measurement discipline that makes an autonomy license trustworthy: you cannot license a loop on evals and judges you have not shown to be sound. Origin — a gap analysis against classical ML evaluation practice (judge calibration, retrieval ranking, annotation ops, drift monitoring, HITL operations).

### Added
- **Part V renamed to "Eval discipline & measurement science"** (`STANDARD.md`), with five new normative subsections:
  - **Judge calibration & bias** — a verdict that gates L3+/auto-apply/release MUST come from a judge with documented calibration (accuracy + ECE/Brier vs. an anchored ground-truth sample, within a recency window); unvalidated verbalized confidence MUST NOT be a gating signal (use self-consistency / swap-consistency); screen for position, verbosity, and self-preference bias.
  - **Retrieval evaluation** — memory/retrieval MUST be evaluated with retrieval metrics (Recall@k, MRR) on a labeled set, separately from end-to-end evals; embedding/chunking/index changes MUST pass a retrieval regression gate.
  - **Ground-truth discipline** — golden sets MUST declare labeling provenance; unanchored sets back no license or release gate; rubrics are versioned instruction artifacts that re-baseline their judges on change.
  - **Drift monitoring** — deployments MUST monitor input drift with a declared eval-refresh policy; provider-hosted models SHOULD be canaried, a detected change triggering the regression gate.
  - **Human oversight as a program** — an L3+ Loop License MUST declare a human-oversight plan (sampling schedule per level, reviewer SLA, re-escalation triggers); reviews MUST be captured as stratified labeled data.
- **Cycle of Trust (Canon 5)** gains a **calibration invariant**: a judge whose status is not `calibrated` MUST NOT gate an L3 transition, auto-apply, or release.
- **Definition of Done 19 → 23** (items 20–23 plus an L3+ human-oversight item), grouped as *Measurement science & human oversight*.
- **SCORECARD** gains a *Measurement science & oversight* section; **AGENT_STANDARD** extends Doctrines 4, 5, and 8 (bundled copy kept byte-identical); the glossary bridge maps autorater → Judge, model card → Judge Card, eval set → Golden set, ATO → Loop License, graduation → Cycle of Trust.
- The `production-readiness` sub-skill, README, and badge updated to match (DoD 19 → 23; Standard v3.1).

Compliance pointers added for EU AI Act Arts. 14 (human oversight), 15 (accuracy & robustness), and 72 (post-market monitoring). Per the standard's threshold philosophy, this mandates *that* thresholds exist and are declared, not their numeric values. The concrete artifacts (Judge Card, retrieval harness, provenance schema, canaries, review pipeline) live in the reference implementations (AgenticPerformance, AgenticMind, AgenticGateway, AgenticAssurance).

[3.1.0]: https://github.com/Moai-Team-LLC/agentic-product-standard/releases/tag/v3.1.0

## [3.0.0] — 2026-07-11

The **Loop License** release. Names the conditions an agent must satisfy to run *unattended* (Autonomy Ladder L3+) and makes them checkable — the standard's answer to "loop engineering" and the "factory with no QC" failure mode.

### Added
- **Part IV — The Loop License** (`STANDARD.md`): a new normative section governing **unattended operation (L3+)**. An agent may not run unattended without holding a **Loop License** — six gates, all required and enforced in code: **eval pass-rate threshold, regression gate, declared blast radius, cost cap, kill switch, escalation path**. Ships with a one-page artifact, [`templates/loop-license/CHECKLIST.md`](templates/loop-license/CHECKLIST.md).
- **Independent verification** (Part IV): self-check by the producing model does not count as verification; deterministic-first; the LLM judge has its own eval and is decorrelated from the writer; a "Writer / Checker, done right" reference pattern.
- **Stop conditions & fail paths** (Part IV): max iterations, budgets, timeout, and escalation-after-N become mandatory Agent Contract fields — **DoD item 17**.
- **The ingestion boundary** (Part IV): "find work" is untrusted input — indirect-injection cases in the eval suite, instruction/data separation, least-privilege triggers; a threat checklist mapped to **OWASP LLM01**.
- **The instruction supply chain** (Part IV): skills, prompts and instructions are supply-chain artifacts — versioned, provenanced, eval-gated before deploy, regression-tested on update, trigger-collision audited; mapped to **OWASP LLM03** and **AIUC-1**.
- **Economics of the loop** (Part IV): measure cost per run **and** cost per *verified* outcome, declare cost caps — **DoD item 19**.
- **Architecture-phase declarations** (Part IV): the memory model (retention, provenance, replayability) and the determinism map are declared at design time, as mandatory Agent Contract sections.
- **Glossary bridge** (Part IV): the loop-engineering lexicon (loop, intent debt, writer/checker, state memory, find work, blast radius) mapped onto the standard's own vocabulary.
- **Operating Doctrine 8 — The Loop License** in `AGENT_STANDARD.md`, plus Agent Contract sections 14–16 (stop conditions, memory model, determinism map).
- **Scorecard** gains an *Unattended operation (Loop License)* section (`SCORECARD.md`).

### Changed
- **Definition of Done 15 → 19** (`STANDARD.md` Part III): items 16 (Loop License), 17 (stop conditions), 18 (independent verification), 19 (loop economics), grouped under *Unattended operation (L3+)*; the `production-readiness` sub-skill and README updated to match.
- Parts IV–IX renumbered to V–X to seat the Loop License as Part IV.
- Standard version badge and title → **v3.0**.

### Note
- This is a **major** release: the new required gates tighten what "conformant" means for any L3+ system, consistent with how v2.0 treated the addition of Layers 8–9. Entries [2.1.0] and [2.2.0] below record interim changes folded into this line.

[3.0.0]: https://github.com/Moai-Team-LLC/agentic-product-standard/releases/tag/v3.0.0

## [2.2.0] — 2026-06-14

### Changed
- **`agentic-product-architect` sub-skills resynced with Standard v2.0.** The `production-readiness` sub-skill now enumerates the full **15-point** Definition of Done — adding the security/identity and cost items that landed in v2.0: the **lethal-trifecta check** (13), **MCP tool-definition pinning + allow-listed registry + OAuth 2.1 scoped tokens** (14), and a **per-run token/cost ceiling enforced in code** (15) — each as a full audit point with checklist, *Why*, and *Common gap*. The `antipatterns-review` sub-skill now lists all **17** anti-patterns, adding: trusting community MCP servers without pinning/scanning (13), deploying the lethal trifecta with no mitigation (14), token passthrough / over-scoped OAuth (15), no budget ceiling on autonomous sessions (16), and peer-to-peer multi-agent buses instead of an orchestrator (17) — each with *Signal*, *Failure mode*, *Fix*, and *Severity*. All "12" counts in both sub-skills and the track `README.md` updated to 15 / 17. No change to `STANDARD.md` or `AGENT_STANDARD.md`; this aligns the skills with the canon they already reference.

[2.2.0]: https://github.com/Moai-Team-LLC/agentic-product-standard/releases/tag/v2.2.0

## [2.1.0] — 2026-06-06

### Added
- **Secure Write Actions pattern** ([`skills/agentic-product-architect/tool-design-mcp/SECURE-WRITE-ACTIONS.md`](skills/agentic-product-architect/tool-design-mcp/SECURE-WRITE-ACTIONS.md)) — the operational write path behind "require approval": read-only by default; P3+ mutations need explicit, scoped, time-bounded **elevation** confirmed **out-of-band** through a channel the agent cannot read (no self-approval); each write cites its exact target; destructive actions get a dry-run; credential reads return metadata only. Mapped to the P0–P6 tiers and composed with Layer 8 / the lethal-trifecta check. Threaded into the `tool-design-mcp` skill and `AGENT_STANDARD.md` Tool Safety Rules. Distilled vendor-neutrally from Descope's MCP-server design + OAuth 2.1.

[2.1.0]: https://github.com/Moai-Team-LLC/agentic-product-standard/releases/tag/v2.1.0

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
