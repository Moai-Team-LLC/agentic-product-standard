# Templates — artifact-contracts

Copy-paste **artifacts**, not framework boilerplate. These are the structured
contracts and schemas the standard asks every agent to have — the bridge from
*knowing what to build* (`AGENT_STANDARD.md` at the repo root) to *having
something to fill in*.

> **Why these exist despite the "no code templates" rule.** The rule (see
> `CONTRIBUTING.md`) bars *framework-specific implementation code that rots* (a
> LangGraph graph, a CrewAI crew). These files are the opposite: framework-agnostic
> **contracts and schemas** that outlive any library. Keep them that way — if a
> template starts importing a framework, it belongs in that framework's docs, not
> here.

## What's here

| File | Artifact | From |
|---|---|---|
| `agent-contract.md` | Agent Contract (13 sections) | Sub-Skill 1 |
| `tool-contract.md` | Tool Contract (P0–P6) | Sub-Skill 5 |
| `schemas.ts` / `schemas.py` | Typed input/output skeletons | Sub-Skill 2 |
| `agent-message-envelope.ts` | Multi-agent message envelope | Sub-Skill 3 |
| `handoff-contract.json` | Handoff between agents | Sub-Skill 3 |
| `context-pack.json` | What context entered the window, and why | Sub-Skill 4 |
| `trace-event.json` | Minimum trace event | Sub-Skill 7 |
| `eval/cases.json` | Golden / failure / regression case shape | Sub-Skill 7 |
| `eval/judge-labels.json` | LLM-judge calibration shape (TPR/TNR) | Sub-Skill 7 |
| `CLAUDE.md` | Drop-in persistent contract for your own repo | — |

## How to use

1. Start from `agent-contract.md` — fill every section before writing code.
2. Turn sections 4/9 into `schemas.ts` or `schemas.py`.
3. For each tool, copy `tool-contract.md` and set its permission tier.
4. Wire `trace-event.json` into your runner; emit one per step.
5. Seed `eval/cases.json` with your top failure modes **before** claiming the agent works.
6. Going multi-agent? Add `agent-message-envelope.ts` and `handoff-contract.json`.

Placeholders are written as `{like-this}` — replace them all.
