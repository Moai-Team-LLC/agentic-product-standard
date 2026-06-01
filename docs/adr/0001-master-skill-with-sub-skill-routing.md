# ADR-0001: Master skill with sub-skill routing

- **Status:** Accepted
- **Date:** 2026-05-30

## Context

The standard spans ten-plus concerns (architecture, context engineering, harness,
tools/MCP, memory, durable execution, evals, framework choice, production
readiness, antipatterns). Loading all of it into one skill would blow the
context budget and bury the relevant guidance for any single request. But the
concerns are interdependent — a user rarely knows up front which one they need.

## Decision

Ship one **master skill** (`agentic-product-architect`) whose job is to *route*,
plus a **sub-skill per concern** under it. The master stays thin: it recognizes
intent from the request and dispatches to exactly the sub-skill(s) that apply.
Each sub-skill is self-contained, references `CONTEXT.md` for shared terms, and
carries its own depth.

## Consequences

- Progressive disclosure: a request pulls in only the relevant depth, keeping
  context utilization low (the standard's own 40% rule).
- Sub-skills evolve independently; the master's routing description is the only
  cross-cutting surface to keep current.
- Cost: the routing layer must stay accurate — a stale `description` sends
  requests to the wrong sub-skill. Routing quality is a maintenance obligation.
- New concerns are added as new sub-skills, not by growing the master.

## Alternatives considered

- **One monolithic skill** — simplest to author, but unbounded context and poor
  retrieval of the relevant section. Rejected.
- **Flat set of peer skills, no master** — loses the single entry point; the
  user (or host) must already know which skill to invoke. Rejected for
  discoverability.
