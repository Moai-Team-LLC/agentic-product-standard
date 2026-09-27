# Roadmap

A living view of where the Agentic Product Standard is headed. Not a commitment — a
direction. Issues and PRs that move these forward are very welcome; see
[CONTRIBUTING.md](CONTRIBUTING.md).

## Now — v4.0 "Conformance Contract" (release candidate 4.0.0-rc.1)

- **Request for comments.** 4.0.0-rc.1 is open for two weeks of review in GitHub
  Discussions before 4.0.0 is cut: the two-axis ladder (ADR-0004), DoD items 26–33, the
  machine-readable canon (ADR-0003), and the `aps-conformance` Action.
- **Dogfood the family.** Run every [AgenticProduct family](ECOSYSTEM.md) member through
  `aps-conformance` and publish the results — the standard's strongest argument is its own
  reference stack passing it. Re-audit the case studies in [`examples/`](examples/) against
  v4.0 at the same time.
- **Move the family to the v4.0 baselines:** MCP 2026-07-28 in AgenticMind and AgenticGateway
  (stateless core, Client ID Metadata Documents, conformance suite in CI); a production auth
  profile for AgenticMind (short-lived, per-agent credentials — the static bearer stays
  localhost-only); the telemetry contract in AgenticPerformance.

## Next

- **Evidence behind the thresholds.** The standard's numbers (≥90% pass@1, ≥50 evals per
  failure mode, the 40% default context budget) are practitioner consensus. Publish a dataset
  of recorded runs that grounds or corrects each one — the way AgentReady derives its measured
  claims — and let a measured number override a default everywhere.
- **Skill portability.** Sub-skills link to `STANDARD.md` and `templates/` with relative
  paths, which break when the skills are installed on their own. Bundle what each skill needs
  (as `production-readiness/DOD.md` already does) or link to the tagged release.
- **Consistency tooling for prose.** The canon removes count drift; a reviewer checklist or
  linter for the remaining hand-written cross-references (anchors, Stack/Layer references).
- **More worked examples** — a reference exemplar per operating point (e.g. `L2 · O2`,
  `L3 · O0`, `L4 · O1`), each a short case study with its `aps-conformance.yaml`.
- **Eval appendix** — concrete, copyable eval-set templates per failure mode to go with the
  `eval-driven-dev` sub-skill, including a legitimacy-audit sampling template.
- **Framework matrix upkeep** — keep `framework-selection` current as LangGraph / Claude SDK /
  OpenAI Agents SDK / Microsoft Agent Framework / CrewAI / Pydantic AI evolve.

## Watching (signals, not yet standard)

- NIST's agent identity work (NCCoE project) and the COSAiS SP 800-53 overlays for agent use
  cases — DoD 27 fixes the outcome now; a profile would fix the mechanism.
- OWASP's *Agentic Skills Top 10* (incubator) — a candidate anchor for the instruction supply
  chain once it reaches v1.0.
- OpenTelemetry `semantic-conventions-genai` tagged releases — when they arrive, DoD 29 pins a
  tag instead of a commit.
- MCP deprecations — Roots, Sampling, and Logging can be removed no earlier than a revision
  dated 2027-07-28; the baseline moves with the spec.

## Later / help wanted

- **Translations** of `STANDARD.md` (the canon travels; the field is global).
- **Editor coverage beyond Claude Code** — the skills follow the open Agent Skills
  specification; document and test them in other clients (Codex, Gemini CLI, Copilot).

## Done

- **Conformance linter** (open ask since v2.0) — shipped in v4.0 as `tools/aps.py` and the
  `aps-conformance` GitHub Action, scoring a product's `aps-conformance.yaml` against the
  machine-readable scorecard with SARIF output ([`docs/conformance.md`](docs/conformance.md)).

## Out of scope

- Becoming a framework. This is a *standard* plus skills; it stays vendor-neutral.
- Endorsing or ranking specific model vendors as ground truth (see anti-pattern #12).
- Legal advice. [`CROSSWALK.md`](CROSSWALK.md) maps evidence to obligations; it does not
  certify compliance.

Have something that belongs here? [Open an issue](https://github.com/Moai-Team-LLC/agentic-product-standard/issues/new/choose).
