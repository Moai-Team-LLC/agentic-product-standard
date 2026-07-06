# Case study: AgenticOps — a reference implementation of *Fleet operations*

[AgenticOps](https://github.com/Moai-Team-LLC/AgenticOps) (Apache-2.0) is the
runtime / operations companion to this standard. Where `AGENT_STANDARD.md` and the
nine-layer stack describe how to build one correct agent or system, AgenticOps
implements the **Fleet operations** surface from `SCORECARD.md` — running many
long-lived agents as deployed infrastructure.

It is deliberately lean (Bun + TypeScript, `bun:sqlite`, no platform): take the
pattern, write the minimum. The whole layer is exercised end-to-end in
`examples/end-to-end.ts` (in that repo) and covered by 22 tests.

## Gate → implementation

| SCORECARD "Fleet operations" gate | AgenticOps module | How |
|---|---|---|
| Versioned runtime manifest (M2) | `manifest` | zod schema + YAML loader; `${VAR}` env interpolation at load; agent-logic path kept separate from the platform prompt |
| Coordinated scheduling + misfire (M2) | `scheduler` | zero-dep cron evaluator (UTC + IANA via `Intl`); fire-once `fires` ledger across replicas; missed fires coalesced to the latest |
| Durable backlog (M2) | `backlog` | SQLite FIFO; atomic claim + lease; an expired lease is re-claimable; retry-then-park |
| Bounded execution / graceful termination (M2) | `runner` | explicit max-turns + wall-clock timeout + graceful cancel; runtime-agnostic turn injection |
| Fleet observability (M3) | `telemetry` | append-only ops audit (lifecycle / auth / tool) + per-agent heartbeat / health; best-effort exporter sink |
| Inter-agent call matrix (M3) | `policy` + `delegate` | default-deny "who-may-call-whom" from each manifest's `mayCall`; `delegate()` enforces it fail-closed before enqueuing, with audit |

## The stack

**Agentic Product Standard** (this repo — the contract) →
**[AgenticMind](https://github.com/Moai-Team-LLC/AgenticMind)** (the knowledge /
judgment layer) →
**[AgenticOps](https://github.com/Moai-Team-LLC/AgenticOps)** (the runtime / ops layer).
