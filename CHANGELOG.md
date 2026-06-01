# Changelog

All notable changes to The Agentic Product Standard are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
