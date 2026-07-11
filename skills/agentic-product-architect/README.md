# Agentic Product Architect — Skill Set

Hybrid skill set for building production-grade agentic products with Claude Code. One master skill (`agentic-product-architect`) routes to twelve specialized sub-skills covering architecture, context, harness, tools, memory, durable execution, evals, framework choice, production readiness, and antipattern review.

## Structure

```
agentic-product-architect/
├── SKILL.md                          ← master: router + philosophy
├── architecture-design/SKILL.md      ← autonomy ladder, 5 patterns, single vs multi
├── context-engineering/SKILL.md      ← write/select/compress/isolate, 40% rule
├── harness-engineering/SKILL.md      ← the 8 layers around the LLM loop
├── tool-design-mcp/SKILL.md          ← MCP-first, <20 tools, RAG-MCP, sandboxing
├── memory-architecture/SKILL.md      ← Mem0 / Zep / Letta / LangMem / files decision
├── durable-execution/SKILL.md        ← Temporal Workflow + Activity pattern
├── eval-driven-dev/SKILL.md          ← Husain/Shankar pyramid + judge calibration
├── framework-selection/SKILL.md      ← LangGraph / Claude SDK / OpenAI SDK / others
├── production-readiness/SKILL.md     ← 19-point Definition of Done audit
├── antipatterns-review/SKILL.md      ← code review through 17 known failure modes
├── tenant-isolation/SKILL.md         ← pooled/silo, leakage paths, cross-tenant leakage eval
└── reference-stack/SKILL.md          ← the paved road: install & wire the AgenticProduct family
```

## How it works

The master skill (`agentic-product-architect`) auto-triggers whenever the user mentions building an agent, agentic product, multi-agent system, agent loop, or any major agentic framework. It loads the philosophy (the six principles, the autonomy ladder, the five composition patterns) and routes to the relevant sub-skill based on the user's specific question.

Each sub-skill is independently triggerable when the user asks something specific to its domain — e.g., a question about Mem0 vs Zep auto-loads `memory-architecture/SKILL.md` without going through the master.

The hybrid design means:
- A new conversation about "I'm thinking about building an agentic product" → master loads, walks through the 10-question checklist, then pulls in sub-skills as needed.
- A focused conversation about "how should I structure context?" → `context-engineering` loads directly.
- A code review request → `antipatterns-review` scans through the 17 antipatterns.

## Installation in Claude Code

Place the entire `agentic-product-architect/` directory in your user-level or project-level skills directory:

- User-level: `~/.claude/skills/agentic-product-architect/`
- Project-level: `<repo>/.claude/skills/agentic-product-architect/`

Claude Code discovers skills via the SKILL.md files and their YAML frontmatter (`name` and `description` fields). The master and each sub-skill register independently.

## Design choices

**Why hybrid?** Building agentic products spans 10+ distinct concerns (architecture, evals, durability, etc.). A monolithic skill would either be too shallow on each concern, or too long for Claude's context budget. The master provides the philosophy and routing; specialized sub-skills load only when needed.

**Why these 12 sub-skills?** They map to the core sections of the Agentic Product Standard plus two operational skills (production readiness audit, antipatterns review) that surface naturally in real building work.

**Why no code templates or scripts?** This skill set teaches architectural judgment, not boilerplate. The relevant code is framework-specific and changes quarterly; the patterns and judgment are durable. When you need code, use the framework's docs (referenced by name in `framework-selection/`).

## Sources

The content distills production practices from:

- Anthropic — "Building Effective Agents" (Schluntz & Zhang); "How we built our multi-agent research system"; "Building agents with the Claude Agent SDK"
- OpenAI — "A Practical Guide to Building Agents"; "Harness Engineering"
- Cognition — "Don't Build Multi-Agents" (Walden Yan)
- HumanLayer — "12 Factor Agents" (Dex Horthy)
- LangChain — "Context Engineering for Agents" (Lance Martin); ambient agents (Harrison Chase)
- Hamel Husain & Shreya Shankar — eval methodology
- Liu et al. — arXiv:2604.14228 (Claude Code architecture analysis)
- Production deployments at Sierra, Cognition, Anthropic, OpenAI, Uber, Klarna, LinkedIn

## Versioning

v2.1 — June 2026

Skills should evolve. The field moves fast; revisit quarterly. The architectural canons (the autonomy ladder, 5 patterns, single-vs-multi, the harness) are stable. Specific vendors and framework rankings will shift.
