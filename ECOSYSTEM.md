# The AgenticProduct family — Ecosystem

The AgenticProduct family is one standard and five reference implementations. The
standard is the contract — prose-canon (ADR-0002), vendor-neutral, MIT. Each
implementation is the reference build of one surface the standard defines, and
conforms to it rather than extends it. This document is a map of the family, not
a migration guide.

## Surface → reference implementation

| Surface / layer | Reference implementation | Repository | Status | License | Visibility |
|---|---|---|---|---|---|
| The contract (the standard itself) | agentic-product-standard | https://github.com/Moai-Team-LLC/agentic-product-standard | Mature — standard v2.x, latest release v2.1.0 (2026-06-06) | MIT | Public |
| Knowledge & memory (Layer 2 Context & Memory) | AgenticMind | https://github.com/Moai-Team-LLC/AgenticMind | Public, actively developed, pre-1.0 (tags to v0.12.0; MCP contract v1.2.0) | Apache-2.0 | Public |
| Runtime & fleet operations (durable execution + scheduling + fleet health) | AgenticOps | https://github.com/Moai-Team-LLC/AgenticOps | v0.1.0 (2026-06-20), early — some modules are skeletons | Apache-2.0 | Public |
| Evals & observability (Layer 6 Evaluation + Layer 7 Observability, error taxonomy, improvement loop) | AgenticPerformance (APL) | https://github.com/Moai-Team-LLC/AgenticPerformance | v0.1.0; core/ingest/worker built and tested, SDK next | Apache-2.0 | Public |
| Model & provider + Cost & FinOps (Layer 1 + Layer 9) | AgenticGateway | https://github.com/Moai-Team-LLC/AgenticGateway | Public, actively developed, pre-1.0 (v0.1.0) | Apache-2.0 | Public |
| Security & assurance (red-team the agent: OWASP Agentic + MITRE ATLAS attack library, toxic-flow graph, SARIF) | AgenticAssurance (AAL) | https://github.com/Moai-Team-LLC/AgenticAssurance | offensive core; OWASP-mapped attacks + SARIF/code-scanning output | MIT | Public |

All members are public and open-source: AgenticAssurance and the standard are MIT;
the other implementations are Apache-2.0 (some with a separate enterprise edition).

## How they compose

The standard sets the contract every member is measured against — the agent loop,
context and memory discipline, durable execution, guardrails, human-in-the-loop,
evaluation, observability, and cross-cutting security and identity. It ships as a
prose canon plus two Claude Code skill tracks (agent-builder for a single agent,
agentic-product-architect for multi-agent products).

The five implementations divide the operational surface:

- **AgenticOps runs the fleet.** It is the Day-2 runtime: a runtime manifest that
  treats an agent as a deployable artifact, a bounded runner, timezone-aware
  coordinated scheduling, a durable backlog that survives restarts, fleet
  observability, and a default-deny inter-agent call policy.
- **AgenticMind judges and grounds.** It is the knowledge & memory substrate:
  citation-enforced answers with a replayable why-trace, a judge-gated compounding
  corpus, and bitemporal revision-aware memory — served headlessly to any agent
  over MCP, self-hostable on Postgres + pgvector alone.
- **AgenticPerformance measures and improves.** It instruments any LLM-agent
  system over OpenTelemetry and turns raw execution into reasoned traces, per-agent
  golden-set evals with a CI gate, named failure clusters, and a governed
  three-level improvement loop inside a mechanically-enforced safety envelope.
- **AgenticGateway is the model plane.** Every LLM call in the loop flows
  through its one OpenAI-compatible key: routing chosen from AgenticPerformance
  eval runs, per-run/tenant cost ceilings enforced in code, caching at the data
  plane, and a hash-not-text evidence event per call into AgenticMind's sink —
  on a Bifrost data plane it configures rather than re-implements.
- **AgenticAssurance red-teams the agent.** It is the framework-neutral offensive
  core of the Agent Assurance Layer (AAL): given a capability manifest and a runner
  adapter, it runs an OWASP-Agentic / MITRE-ATLAS attack library against an isolated
  copy of the target, builds a toxic-flow graph over the declared tools to find
  lethal-trifecta / RCE composition paths single-prompt scanners miss, detects
  text-refusal-vs-side-effect divergence, and emits SARIF for CI code-scanning. Not
  a runtime guardrail; the compliance/evidence layer is a separate package.

The implementations reference each other through optional adapters, never hard
dependencies: AgenticPerformance ingests AgenticOps runs and AgenticMind telemetry
into its contract with zero dependency on their packages. Each runs on its own.

## Conformance

Conformance is measured against the standard's surfaces and scorecard, not against
each other. Each implementation carries its own scorecard and, where present, a
CONFORMANCE.md that maps it onto the standard's harness layers and reports its gaps
honestly — for example AgenticMind's pending CI eval-regression gate. Early
members are labeled as such; a badge asserting a surface is a
claim about the reference build, not a guarantee of feature-completeness. Some
implementations offer a separate enterprise edition (SSO/RBAC, audit, on-prem); the
open core is Apache-2.0. The standard remains the canon; this map only points to
where each surface is implemented.
