# Changelog

All notable changes to The Agentic Product Standard are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- **AITM-SMB 1.1.0** in [`aitm-smb/`](aitm-smb/README.md) — the business-level AI transformation methodology that sits upstream of this standard (which capability changes, whether AI belongs, how much authority it gets). Self-contained and split-ready with its own semver, MIT license, 40 agent skills plus a root `SKILL.md` adapter, artifact contracts, a fictional worked example, and a stdlib-only validator. See its [changelog](aitm-smb/CHANGELOG.md).
- [`.github/workflows/aitm-smb.yml`](.github/workflows/aitm-smb.yml) — validates the methodology and its worked example on every change under `aitm-smb/`, and on an `aitm-smb-vX.Y.Z` tag publishes a GitHub Release with the Core and Full distributions attached (not marked Latest). It publishes the build it validated, after checking that the unpacked Full distribution validates on its own; run manually with an existing tag, it rebuilds and replaces that release's assets without moving the tag.
- [ADR-0006](docs/adr/0006-host-aitm-smb-as-split-ready-subfolder.md) — why AITM-SMB is hosted here as a split-ready folder, and how its authority ladder relates to this standard's operating point.

### Changed
- `CONTEXT.md` scopes its vocabulary to this standard's own skills and separates **APS-L<n>** / **APS-O<n>** (autonomy and oversight) from **AITM-L<n>** (business authority); README and ECOSYSTEM link the [crosswalk](aitm-smb/docs/crosswalk-agentic-product-standard.md).
- The `validate` workflow's skill-frontmatter check also covers `aitm-smb/SKILL.md` and `aitm-smb/skills/`.

## [4.0.0] — 2026-09-28

The **Conformance Contract**. v3.x added a license, then a science, then a gate, then a graph — each release grew the Definition of Done and the copies of it drifted. v4.0 stabilizes the contract instead of growing it again. The standard gets one machine-readable source that every document is generated from. It gets a conformance tool that checks a product against that source in CI. The ladder is redrawn on two axes — how much the agent decides, and how closely a human oversees it — which the EU AI Act already treats separately. And the protocol baselines the standard leans on — MCP, A2A, OpenTelemetry, the EU AI Act — are brought up to their state as of September 2026. This is a **major** release: some v3.3-conformant products will not be v4.0-conformant (see *Migration*).

It shipped first as release candidate 4.0.0-rc.1. The maintainer cut the final release the same day, ahead of the two-week comment period that `GOVERNANCE.md` describes. The RFC ([#32](https://github.com/Moai-Team-LLC/agentic-product-standard/issues/32)) stays open until 12 Oct 2026, and its corrections land in 4.0.x.

### Since 4.0.0-rc.1
- The release workflow now rewrites relative links in the release notes to point at the tagged files. Before this, links like `docs/adr/…` broke on the release page; the v3.3.0 and v4.0.0-rc.1 notes are affected.
- The Action pin examples move to `@v4.0.0`.
- `GOVERNANCE.md`: the maintainer may shorten a major release's comment period, and the release notes then say so, as these do.
- `ROADMAP.md`: *Now* covers the feedback on 4.0 and moving the family to the v4.0 baselines.

### Breaking
- **Autonomy × Oversight** (Canon 1, [ADR-0004](docs/adr/0004-autonomy-and-oversight-axes.md)). The single L0–L4 ladder becomes two axes:
  - **autonomy** L0–L4 — who chooses the next step. L3 is renamed *Bounded decomposition* (formerly *Orchestrator-Worker*), so the level is no longer confused with composition pattern 4.
  - **oversight** O0 / O1 / O2 — whether a human approves each consequential (P3+) action: in the loop, on the loop, or unattended.

  A system declares its **operating point** (e.g. `L3 · O0`).
- **The Loop License binds at O1+, at any autonomy level** — not at "L3+ unattended." An L2 pipeline that auto-applies its output now owes the license. An L3 orchestrator whose every action is approved no longer does. O2 additionally requires the success-legitimacy audit. Stop conditions bind at L3+ **or** O1+. Missing a gate caps a system at O0 (formerly "L2"). The weakest-link bound caps an unlicensed path at O0.
- **Escalation rules per axis.** Climbing autonomy still requires pass@1 ≥ 90%. Relaxing oversight now requires a Loop License whose eval gate adds a declared **pass^5** threshold, plus a published **legitimacy rate** at O2. The standard sets no hour thresholds: benchmark time horizons do not transfer to a product.
- **Definition of Done 25 → 33.** New items:
  - 26 *MCP protocol & auth baseline* — MCP 2026-07-28, conformance suite in CI, no session-bound state, Client ID Metadata Documents, RFC 9207 issuer validation, issuer-bound credentials.
  - 27 *Per-agent identity*.
  - 28 *Inter-agent trust* — A2A signed Agent Cards verified before cross-boundary delegation.
  - 29 *Telemetry contract* — OTel GenAI conventions at a pinned revision, content capture off by default.
  - 30 *Success-legitimacy audit* at O2.
  - 31 *Regulatory classification record*.

  The two items that were unnumbered since v1.4/v3.1 get numbers — the numbering itself changes no obligation: **32** tenant isolation and **33** human oversight as a program. Separately, item 33 gains automation-bias measurement: override rate, approval latency, and a rubber-stamp alarm.
- **Numbering.** "Layer N" now always means a harness layer; `STANDARD.md` Part II sections become **Stack 1–9** ([ADR-0005](docs/adr/0005-layer-and-stack-numbering.md)). Part II anchors changed from `#layer-…` to `#stack-…`.
- **Anti-patterns 19 → 20.** New: **20. Counting a pass as a success without legitimacy review.** Anti-pattern 15 gains its 2026 variant: an MCP client that can only register through the deprecated Dynamic Client Registration.

### Added
- **The machine-readable canon** ([`canon/`](canon/), [ADR-0003](docs/adr/0003-machine-readable-canon.md)). It holds the principles, the ladder, the patterns, the harness and stack, the checklist, the Definition of Done (normative text, binding conditions, audit points, crosswalk), the anti-patterns, the scorecard, and the regulatory frameworks as YAML, with JSON Schemas. The README, `STANDARD.md`, `SCORECARD.md`, `CONTEXT.md`, `AGENT_STANDARD.md` (both copies), and five skills now carry generated regions. `CROSSWALK.md`, `production-readiness/DOD.md`, the conformance template, and `skills-lock.json` are generated whole.
- **`tools/aps.py`**:
  - `validate`, `render` and `check` keep the canon and the documents in step. `check` also fails on a count written in prose that disagrees with the canon.
  - `skills validate | lock | verify` checks the instruction supply chain.
  - `conformance` scores a product.
  - Unit tests live in `tools/tests/`, and CI runs all of it.
- **`aps-conformance`** ([`docs/conformance.md`](docs/conformance.md), [`action.yml`](action.yml)). A product answers the scorecard in an `aps-conformance.yaml`, where every *yes* carries evidence. The tool, which is also a composite GitHub Action, then reports:
  - the band achieved;
  - the band the declared operating point requires;
  - DoD coverage, and whether the product is **production-ready** — within its band *and* with no binding DoD item open (`--require-dod` gates CI on it; shippable is not production-ready);
  - each open control as SARIF, tagged with the DoD items and crosswalk entries it supports;
  - an optional endpoint badge.

  This closes the "conformance linter" ask that has been open since v2.0.
- **[`CROSSWALK.md`](CROSSWALK.md)** maps each DoD item to the EU AI Act, OWASP ASI01–ASI10, NIST AI RMF categories, and IMDA's four dimensions wherever an entry applies, with reverse indexes. It includes the dates fixed by the Digital Omnibus (Regulation (EU) 2026/1744): Art. 50 from 2 Aug 2026, Annex III high-risk from 2 Dec 2027, Annex I from 2 Aug 2028. It is a crosswalk, not a compliance claim.
- **Templates:**
  - [`ci/mcp-conformance.yml`](templates/ci/mcp-conformance.yml) runs the official MCP conformance suite, pinned (DoD 26).
  - [`telemetry/`](templates/telemetry/README.md) is a stdlib checker for the telemetry contract (DoD 29).
  - [`safe-outputs/`](templates/safe-outputs/README.md) is the typed safe-output pattern and a reference applier (Loop License gate 3).
  - [`conformance/`](templates/conformance/aps-conformance.template.yaml) is the generated `aps-conformance.yaml` template.
- **Skills supply chain.** Every `SKILL.md` is validated against the open Agent Skills specification. Every file a skill ships is scanned for hidden content and hash-locked in `skills-lock.json`. The scan covers every Unicode format and control character, variation-selector smuggling, stray HTML comments, and piped installers. `aps.py skills verify` checks an installed copy against the lock: a changed, missing, *or added* file fails.
- `llms.txt`, and `AGENTS.md` (+ `CLAUDE.md`) for coding agents working on this repository.
- Scorecard items for DoD 25–33. v3.3 had shipped DoD 25 with no scorecard item. Every scorecard item now has a stable id.

### Changed
- **Stack 2 / Layer 8** now set the MCP 2026-07-28 baseline:
  - a stateless core;
  - multi-round-trip `input_required` in place of server-initiated elicitation;
  - `Mcp-Method` / `Mcp-Name` routing headers as a policy enforcement point outside the model;
  - `ttlMs` / `cacheScope` caching, with the tool-definition pin re-verified on every refetch and `private` entries kept to the authorization context they were fetched under;
  - Roots, Sampling, and Logging deprecated.

  Layer 8 also adds sections on per-agent identity (NIST NCCoE concept paper, Feb 2026) and inter-agent trust (A2A v1.0 signed Agent Cards).
- **Stack 6** pins the OpenTelemetry GenAI conventions. They moved to `semantic-conventions-genai` at semconv v1.42.0 (June 2026), are still *Development*, and have no tags yet, so the pin is a commit. The stack now records `invoke_agent` → `chat` / `execute_tool` spans and token usage, and makes content capture opt-in by policy.
- **The context budget is measured, not assumed** (DoD 1). It is the fill level at which your own evals degrade, with 40% of the window as the default until you have measured it.
- **Cost ceilings are re-derived on every model change** (DoD 15, Stack 1, Stack 9). A model swap is a release, not a config change.
- **The instruction supply chain** (Part IV) adds spec validation, hidden-content scanning, and a lockfile.
- **The Loop and Graph License checklists, the decision tree, `AGENT_STANDARD.md` (doctrines, contract sections 14–17, checklists, rules 23–25, evidence appendix), and the skills** move to the two-axis model.
- `production-readiness` now keeps its audit points in a generated, bundled `DOD.md`, which keeps `SKILL.md` within the spec's size guidance. `eval-driven-dev` adds consistency (`pass^k`) and legitimacy. `tool-design-mcp` adds a 2026-07-28 section. The `tenant-isolation`, `memory-architecture` and `durable-execution` skills pick up the MCP caching and multi-round-trip changes.
- `templates/ci/eval-gate.yml` gates on `pass^k` and the legitimacy rate as well as pass@1. Each metric is checked against its floor and against a committed baseline, so a regression blocks the merge even above the floor (DoD 12).
- `GOVERNANCE.md` describes releases: the canon owns the version, major releases ship as release candidates with a comment period, and tags are immutable contracts. The release workflow publishes `-rc` tags as pre-releases and refuses a tag that does not match the canon.

### Fixed
- **Facts, after a review against primary sources.**
  - The Replit figures now follow the coverage (records on 1,206 executives and 1,196+ companies, by the agent's own count), and Fortune is cited wherever the incident is used as evidence.
  - The ~98%-of-code figure is scoped to Claude Code, the system the estimate describes.
  - Advisory APS-2026-01 corrects several points:
    - HTTP+SSE may go in the next MCP revision.
    - Dynamic Client Registration joins Roots, Sampling and Logging on the 2027 clock.
    - A `private` cache entry is bound to its authorization context, not to a tenant.
    - It is client credentials, not tokens, that are bound to an issuer.
    - The server, not the gateway, checks headers against the body.
    - MCP Apps did not move; it was always an extension.
  - A2A Agent Card signatures date from v0.3.0 and are optional; v1.0 specifies JCS canonicalization.
- The durable-execution skill's frontmatter was not valid YAML: an unquoted `answer:` inside the description broke strict parsers.
- The `agent-builder` contract template lacked the sections the standard makes mandatory at L3+/O1+.

### Migration from 3.3
1. **Declare your operating point.** If your system executes consequential actions without per-action approval, it is at O1 or O2 and owes the Loop License, whatever its autonomy level. If it is L3+ with every action approved, it is at O0 and owes stop conditions but no license.
2. **Add pass^5 to your Loop License eval gate.** At O2, also start the legitimacy audit and move tests, graders, and eval sets out of the agent's write scope.
3. **Renumber your references.** The two formerly unnumbered DoD items are now **32** and **33**. "Part II · Layer N" references become **Stack N**.
4. **Close the new items that bind to you:**
   - MCP 2026-07-28 and its conformance suite (26), if you use MCP;
   - one identity per agent (27);
   - signed-card verification (28), if you delegate across a trust boundary;
   - a pinned telemetry contract with content capture off (29);
   - the classification record (31), if you serve a regulated market;
   - automation-bias metrics on your approval queues (33).
5. **Optionally, adopt `aps-conformance`.** Start from `templates/conformance/aps-conformance.template.yaml`.

*Sources are cited inline in `STANDARD.md`, `CROSSWALK.md`, and `AGENT_STANDARD.md`'s evidence appendix. The MCP, A2A, OpenTelemetry, Agent Skills, and conformance-suite claims were checked against their primary sources — the specification and repository texts. EUR-Lex, Commission, Council, NIST, IMDA, OWASP, and METR pages could not be fetched from the review environment; those claims rest on search-index excerpts of the primary pages and are stated conservatively. Corrections are welcome — open an issue with the source.*

[4.0.0]: https://github.com/Moai-Team-LLC/agentic-product-standard/releases/tag/v4.0.0

## [4.0.0-rc.1] — 2026-09-27

The release candidate of 4.0.0. Its notes are folded into [4.0.0] above; everything that changed after it is listed under *Since 4.0.0-rc.1*.

[4.0.0-rc.1]: https://github.com/Moai-Team-LLC/agentic-product-standard/releases/tag/v4.0.0-rc.1

## [3.3.1] — 2026-09-27

A **consistency** patch. Nothing normative changes. The canon had drifted across its own copies, and this release puts the counts, lists and diagrams back in agreement. It also records where the protocol landscape moved underneath the standard: MCP 2026-07-28 is now final.

### Fixed
- **The harness really has nine layers.** v3.3 declared nine layers (after #30), but every diagram still drew eight, and `AGENT_STANDARD.md` counted "the seven in the stack plus Security & Identity." Layer 9 (Cost & FinOps) now appears as the second cross-cutting layer in the README, `STANDARD.md` Canon 4, both copies of `AGENT_STANDARD.md`, `CONTEXT.md`, and the `harness-engineering` skill. A numbering note separates the harness layers (Canon 4) from Part II's technology-stack sections, which are also numbered 1–9 and coincide with the harness only at 8 and 9.
- **`STANDARD.md` Part VIII listed 17 anti-patterns** while the README and the `antipatterns-review` skill listed 19. Anti-patterns 18 (*prose topology counted as a control*) and 19 (*license inheritance by wiring*) are added to the canon.
- **The master `agentic-product-architect` skill** listed only 12 of the 19 anti-patterns. Its sub-skills index was split by a misplaced section and omitted `reference-stack`, and its paved-road paragraph left out AgenticGateway. All three are corrected.
- **README Definition of Done.** The 4×4 grid could not show which cell was which of the 25 items. It is replaced by a grouped table keyed by item number, including the two conditional items (multi-tenant isolation; the L3+ oversight plan).
- **Stale text.** `CONTRIBUTING.md` still said "eight-layer harness" and told contributors never to add code templates, which contradicted `templates/`. The PR template asked contributors to keep the Russian translation in sync, although it was removed in v1.3.0. `production-readiness` referred to "21 of 23". The architect track README was versioned "v2.1 — June 2026". `framework-selection` recommended Semantic Kernel and AutoGen, although `STANDARD.md` records both as superseded by Microsoft Agent Framework. The `harness-engineering` skill pointed observability at OpenInference/OpenLLMetry instead of the OpenTelemetry GenAI conventions the standard mandates.

### Changed
- **Principle 3** no longer claims that "98% of *reliability*" lives in the harness, which is a share of reliability no one has measured. It now says the harness is ~98% of the *code* and cites the source: a community estimate for Claude Code (~1.6% AI decision logic, ~98.4% operational infrastructure) quoted in Liu et al., *Dive into Claude Code* (arXiv:2604.14228).
- **The Replit incident** now cites its primary coverage (Fortune, 23 Jul 2025) in `STANDARD.md` and the README.
- **Reading lists** add the primary specifications the standard builds on, with the version to pin.
- The README says in one line how this standard differs from Klarna's *Agentic Product Protocol* and from *AgentReady*.

### Added
- **Advisory [APS-2026-01](docs/advisories/APS-2026-01-mcp-2026-07-28.md): MCP 2026-07-28.** This informative note covers the stateless core, multi-round-trip requests, routing headers, caching scope, and authorization changes: Client ID Metadata Documents replacing Dynamic Client Registration, RFC 9207 issuer validation, and issuer-bound credentials. It also covers the deprecations and the official conformance suite. For each change it gives what the change means for Layer 8, DoD 14, and anti-pattern 15, plus a checklist to act on before v4.0 makes it normative.

[3.3.1]: https://github.com/Moai-Team-LLC/agentic-product-standard/releases/tag/v3.3.1

## [3.3.0] — 2026-08-05

The **License Composition** release. v3.0 gave a *loop* a license; a graph of licensed loops multiplies that question rather than answering it. The vocabulary for wiring agents together — nodes, edges, shared state, fan-out — crystallized in the market as *graph engineering* one rung above loop engineering, and arrived with no governance attached. This release supplies it: Part IV now binds the **topology**, not the runtime, and takes no position on which framework draws the graph.

The load-bearing claim is the negative one. **A graph of licensed loops is not a licensed graph.** The risks that hurt are precisely the ones no single node owns: nodes that pass in isolation failing in composition, fan-out multiplying spend past every per-node cap while each cap reads green, an uncalibrated node lending a whole path an autonomy it never earned, and an escalation path that forks until no human is on the hook for the system.

### Added
- **Part IV: License Composition** (`STANDARD.md`) — the **Graph License**: the six Loop License gates re-evaluated at graph scope (graph-level golden tasks rather than the union of per-node suites; a regression gate on that set; blast radius as the union of node radii **plus the shared state store**; cost caps **per-node and aggregate**, because fan-out multiplies burn; a kill switch verified against **in-flight parallel branches**; and one escalation path with one named owner). Plus four bounds that only exist at graph scale: the **weakest-link bound** (a path's autonomy level is the *minimum* licensed level of any node on it — an unlicensed or uncalibrated node caps that path at L2); **shared-state provenance** (writer, timestamp, `verified_by`/`unverified`, filterable, with no external action firing from an unverified field); **fan-in as a verification point** (unverified aggregation upstream of an external action is prohibited at L3+ — merging adds confidence, not correctness, and treating the aggregate as validated is self-verification wearing a topology); and **edges as ingestion boundaries** (a node's output is untrusted input downstream, with poisoned-state scenarios in the graph eval suite, and reviewer nodes calibrated and decorrelated **per edge**).
- **Declared vs. enforced topology** (`STANDARD.md`, Part IV) — architecture-phase declarations now state, per edge class, whether routing is **enforced** (the runtime or the code makes other routes unavailable) or **declared** (an SOP, a skill, a prompt). **Declared-only edges MUST NOT be counted as controls in any license.** The graph-scale form of "permissions enforced by code, not by prompt" (DoD 5): an instruction-defined route binds exactly as well as an instruction-defined permission — which is to say not at all under adversarial input (Principle 6).
- **Definition of Done grew 24 → 25.** New item **25** (Graph License), binding wherever more than one agent is composed. Mirrored in the `production-readiness` sub-skill.
- **[`templates/graph-license/CHECKLIST.md`](templates/graph-license/CHECKLIST.md)** — the one-page gate, sibling of the loop-license checklist and explicitly assuming it: per-node inventory, the six gates at graph scope, **path analysis** (every path to an external action with its weakest link), shared-state provenance, fan-in points and their verification method, per-edge-class enforcement declaration, kill-switch test record, and the named escalation owner.
- **Anti-patterns 17 → 19.** **18. Prose topology counted as a control** — a route described in an SOP or a system prompt, cited in a review as though it constrained anything; it holds until the moment it matters, and prose cannot fail loudly. **19. License inheritance by wiring** — "every agent is production-ready, so the graph is." Both carry *Signal · Failure mode · Fix · Severity* in the `antipatterns-review` sub-skill.
- **Glossary bridge extended to the graph-engineering lexicon**, plus a mapping of the market's five-layer ladder (prompt → context → harness → loop → graph engineering) onto the constructs this standard already governs. The ladder is a useful map of what people are talking about; it is not an architecture.
- **Layer 5 (Durable execution) gains a durable-HITL invariant** (`STANDARD.md`,
  Part II): a human-in-the-loop request is a **tool call the agent emits** (MCP
  elicitation, Layer 2) that **suspends the workflow on the same durable substrate**,
  resumed by the human's reply as the next event — not an in-process block or a
  side-channel notification the loop waits on (which loses the work on a crash).
  Unifies the HITL layer (Canon 4), durable execution (Layer 5), and the Loop
  License escalation path (Part IV) as one durable-tool-call pattern; folds in
  12-Factor-Agents F7 (contact humans with tool calls) atop the F6/F12 durability
  already at Layer 5.

[3.3.0]: https://github.com/Moai-Team-LLC/agentic-product-standard/releases/tag/v3.3.0

## [3.2.0] — 2026-07-21

The **Gate Integrity** release. A standard that gates autonomy on evals, judges, and CI is only as trustworthy as those gates — and a gate that has been silenced to make CI pass is not a gate, it just looks like one. This release names *gate integrity* as a first-class trust invariant and a Definition-of-Done item. Origin — a real incident in a reference implementation where a `no-unsafe-*` type-safety lint family was disabled repo-wide to get a green check, quietly removing the net that catches `any` leaking into typed code (the hole `strict` `tsc` leaves open by design).

### Added
- **Cycle of Trust (Canon 5)** gains a **gate-integrity invariant** (`STANDARD.md`): a gate is trust-bearing only if its green state means the property holds, not that the check was silenced. Weakening a correctness / type-safety / security / eval gate to pass CI — disabling a rule repo-wide, `@ts-ignore`, `.skip`, deleting an assertion, lowering a threshold — is a defect, not a fix; a false positive is scoped to a file/glob with a named reason and the gate re-proven to still fire. The mechanical form (a test that fails if the safety rules are flipped off) is exemplified in AgenticMind's shared lint config.
- **SCORECARD** gains a *gate-integrity* control under *Maintenance discipline* (M1).
- **Definition of Done 23 → 24** (`STANDARD.md`, Part III): new item **24 — gate integrity** ("no safety-class gate silenced to pass CI"), binding wherever a correctness/type-safety/security/eval gate exists. The `production-readiness` sub-skill, README, and skill index updated to the 24-point count; point 24 added to the skill's enumerated audit.

Per the standard's threshold philosophy, this mandates *that* a green gate must mean the property holds — not any particular tool. The mechanical exemplar (a tripwire test asserting the safety rules stay `error`) lives in the reference implementation, AgenticMind.

[3.2.0]: https://github.com/Moai-Team-LLC/agentic-product-standard/releases/tag/v3.2.0

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
