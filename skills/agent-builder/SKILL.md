---
name: agent-builder
description: Build, implement, review, or harden a SINGLE production-grade agent — its contract, schemas, tools and permission tiers, durable state, guardrails, traces, and evals. Use when the user wants to create one agent (not a multi-agent product), implement an agent runner, add tools/memory/evals to an existing agent, or review whether one agent is production-ready. For multi-agent products, orchestration, or framework selection, use the agentic-product-architect skill instead. The full operational standard this skill applies is AGENT_STANDARD.md (bundled with this skill); copy-paste artifacts are in templates/.
---

# Agent Builder

You are building **one** production-grade agent. The operational standard you apply is
`AGENT_STANDARD.md` (bundled alongside this SKILL.md); the fill-in artifacts are in
`templates/` (also bundled here). This skill is the **single-agent track** — for multi-agent
products, orchestration, or "which framework", switch to the `agentic-product-architect` skill.

Core principle: *an agent is not a prompt.* It is a bounded execution unit with a contract,
scoped context, tools, permissions, durable state, verification, and traceability. Default
to deterministic code; add agency only where the path cannot be predefined.

## The build sequence (follow in order)

1. **Classify the work.** Design a new agent? Implement one? Add tools / memory / evals?
   Review for production? Each maps to a sub-skill below.
2. **Choose the minimal architecture.** Ask: *what is the least autonomous design that
   solves this?* Prefer, in order: deterministic function → workflow with LLM steps →
   single agent with a bounded loop. Do not reach for an autonomous loop (L4) unless the
   path genuinely cannot be enumerated. Do not escalate a level until the current one
   passes ≥90% on a curated eval set.
3. **Write the Agent Contract first.** Copy `templates/agent-contract.md` and fill **every**
   section before any code. No complete contract → not ready to implement.
4. **Implement with guardrails.** Validate input and output against schemas
   (`templates/schemas.ts` / `schemas.py`); enforce permission tiers (P0–P6) in code;
   externalize state; emit a trace event per step (`templates/trace-event.json`); add
   retry/timeout/idempotency for anything long-running.
5. **Add evals before claiming completion.** Seed `templates/eval/cases.json` with your top
   failure modes (the concrete ones from Contract §11), code-assert the deterministic
   requirements, and only promote to a (calibrated, binary) LLM-judge for subjective modes.

## Map to sub-skills (read before answering substantively)

These live under `../agentic-product-architect/` and are shared across both tracks:

| Signal | Sub-skill |
|---|---|
| Pattern choice, autonomy level, single vs multi | `architecture-design/SKILL.md` |
| Context window, RAG, compaction, the 40% rule | `context-engineering/SKILL.md` |
| Agent loop, verification, scaffolding | `harness-engineering/SKILL.md` |
| MCP, tool descriptions, too many tools | `tool-design-mcp/SKILL.md` |
| Long-term memory / persistence | `memory-architecture/SKILL.md` |
| Long-running, pause/resume, retries, crashes | `durable-execution/SKILL.md` |
| Evals, LLM-as-judge, calibration, regressions | `eval-driven-dev/SKILL.md` |
| Pre-launch checklist / DoD | `production-readiness/SKILL.md` |
| Review existing agent code | `antipatterns-review/SKILL.md` |

## Operating posture

- **Contract before code.** If the contract is incomplete, finish it together — don't write a runner yet.
- **Permissions in code, never in the prompt.** P3+ side effects (external write, financial, communication, destructive) require human approval enforced by the harness.
- **Structured outputs only** for critical results. Never treat successful text generation as task completion.
- **Prefer the boring answer.** Workflow over loop, deterministic over emergent, files over databases, code-enforced permissions over prompt-enforced.
- **Every production failure becomes a regression test.**

## Definition of Done (single agent)

An agent is done only when: contract complete · one owned artifact · inputs & outputs
schema-validated · guardrails on both · context scoped (<~40%) · state externalized &
durable · tools allowlisted (<20 active) · permission tiers enforced in code · approval
gates where needed · retry/timeout/idempotency · trace events emitted · failure modes
documented · golden + failure-mode + regression evals exist · human escalation path · a
README that says how to run, test, and debug it.

The full checklist, contract structures, runner flow, and the evidence behind these claims
are in `AGENT_STANDARD.md`.
