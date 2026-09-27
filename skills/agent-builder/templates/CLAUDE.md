# {Project} — agent contract for Claude Code

> Drop this at your repo root (or `AGENTS.md`). It is the persistent, versioned
> contract an agent reads on every session. Keep it ~100 lines — a table of
> contents into a structured `docs/` tree beats one giant file.

## What this system is
{One paragraph: the product, and the one part an LLM dynamically directs.}

## Operating point
{L0–L4 · O0–O2} — autonomy (who picks the next step) × oversight (whether a human approves each consequential action). Do not climb autonomy without eval evidence (≥90% pass@1); do not relax oversight below O0 without a Loop License.

## What the agent owns / must not do
- Owns: {the primary artifact}
- Must NOT: {forbidden actions; the permission boundary}

## Permission tiers in play
{Which P-tiers exist here, and which require human approval. P3+ always gated.}

## Where state lives
{Externalized store / files — never only the context window. Keep utilization under the measured context budget (~40% of the window until measured).}

## Tools
{Allowlisted tools and their permission tiers. The model never invents tool names.}

## How to verify a change works
{Commands to run, what "done" means, where traces and evals live.}

## House rules
- Deterministic control flow by default; LLM calls only where reasoning/generation is genuinely needed.
- Validate all inputs and outputs against schemas; guardrails on both.
- Permissions and approvals are enforced in code, not here in prose.
- Every production failure becomes a regression test.
