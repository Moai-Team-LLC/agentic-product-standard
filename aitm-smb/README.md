# AITM-SMB

**AI Transformation Methodology for Small and Medium-Sized Businesses.** An open, domain-neutral, agent-readable method for deciding which business capability should change, whether AI belongs in that change, and how much authority AI may hold, then proving that the business actually improved.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version 1.1.0](https://img.shields.io/badge/version-1.1.0-informational.svg)](CHANGELOG.md)

**Current version: 1.1.0**, the first public release. It consolidates the internal 1.0.0; what changed and how to migrate is in the [changelog](CHANGELOG.md).

## Thesis

> The unit of AI transformation is the Business Capability, not the AI use case.

AITM-SMB starts from a measurable business Outcome and the Capability that must change. AI is one possible kind of intervention, never the default. Its authority is granted explicitly by humans, bounded, observable, and always reducible.

## What it is

- **A method from Outcome to evidence.** Every selected change traces back to an Outcome through a Capability, a diagnosed Gap and its Cause. The canonical chain is defined once, in [`STANDARD.md`](STANDARD.md) §2; the minimum valid path is [`EXECUTION_MODEL.md`](EXECUTION_MODEL.md) §6.
- **AI-optional by design.** Eighteen intervention families, four of them AI ([`PUBLIC_API.md`](PUBLIC_API.md) §6); simpler fixes are challenged first ([`STANDARD.md`](STANDARD.md) §5).
- **Human-gated.** Nine human decision gates ([`STANDARD.md`](STANDARD.md) §8) that no agent may cross, identified `HG-*` (human gate), e.g. `HG-TOA` for the Target Operating Architecture (TOA).
- **Proportional.** Composable profiles, from a Compact engagement to a governed, measured portfolio.
- **Agent-readable.** Stable identifiers, record contracts, 40 skills with a router, and a machine-readable handoff block.

## What it is not

- Not an AI maturity survey, use-case brainstorm, tool selection, automation backlog, or agent architecture. Each can be a component inside an application, but none is one by itself ([`CONFORMANCE.md`](CONFORMANCE.md) §2).
- Not industry-, vendor-, or cloud-specific. Specialization belongs in Extensions ([`EXTENSION_MODEL.md`](EXTENSION_MODEL.md)).
- Not a software-engineering standard for building the AI component. For that, see [Relation to the Agentic Product Standard](#relation-to-the-agentic-product-standard).

AITM-SMB rejects:

```text
pain point → AI tool
AI adoption = business value
deployment = transformation
more autonomy = more maturity
local KPI improvement = system improvement
```

## Who it is for

- **Owners and operators of small and medium-sized businesses (SMBs)** who want AI to change a business result, not only a tool list.
- **Transformation consultants and facilitators** who need a repeatable, auditable engagement method.
- **AI-agent builders** who need a business-level method that decides whether, where, and with how much authority an agent should act.

## Start here

| You are | Start with | Then |
|---|---|---|
| Owner, operator, or consultant | [`QUICKSTART.md`](QUICKSTART.md): your first Compact engagement | [`STANDARD.md`](STANDARD.md), [`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) |
| Want to see a finished engagement | [`examples/compact-scenario-b/README.md`](examples/compact-scenario-b/README.md) (fictional, informative) | [`QUICKSTART.md`](QUICKSTART.md) |
| AI agent, Claude Code, or another runtime | [`SKILL.md`](SKILL.md) (router) | [`AGENTS.md`](AGENTS.md), [`AGENT_CONTEXT_POLICY.md`](AGENT_CONTEXT_POLICY.md) |
| Implementer or Extension author | [`PUBLIC_API.md`](PUBLIC_API.md) | [`EXTENSION_MODEL.md`](EXTENSION_MODEL.md), [`VERSIONING.md`](VERSIONING.md) |
| Reviewer of the rules | [`STANDARD.md`](STANDARD.md) | [`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md) (precedence), [`CANONICAL_CONCEPTS.md`](CANONICAL_CONCEPTS.md) |

## The method at a glance

Nine phases ([`EXECUTION_MODEL.md`](EXECUTION_MODEL.md) §1). Each phase has one orchestrator skill that invokes its specialists ([`skills/INDEX.md`](skills/INDEX.md)).

| Phase | Phase file | Orchestrator skill | Typical human gates |
|---|---|---|---|
| 0 Frame | [`methodology/00-intent.md`](methodology/00-intent.md) | [`01-discover-transformation`](skills/01-discover-transformation/SKILL.md) | `HG-OUTCOME` |
| 1 Observe | [`methodology/01-current-system.md`](methodology/01-current-system.md) | [`02-map-current-system`](skills/02-map-current-system/SKILL.md) | — |
| 2 Diagnose | [`methodology/02-capability-diagnosis.md`](methodology/02-capability-diagnosis.md) | [`03-diagnose-capabilities`](skills/03-diagnose-capabilities/SKILL.md) | — |
| 3 Design Interventions | [`methodology/03-intervention-design.md`](methodology/03-intervention-design.md) | [`04-design-interventions`](skills/04-design-interventions/SKILL.md) | `HG-AUTHORITY` |
| 4 Decide | [`methodology/04-prioritization.md`](methodology/04-prioritization.md) | [`05-prioritize-initiatives`](skills/05-prioritize-initiatives/SKILL.md) | `HG-INITIATIVE`, `HG-BUDGET` |
| 5 Design Target System | [`methodology/05-target-system-design.md`](methodology/05-target-system-design.md) | [`06-design-target-system`](skills/06-design-target-system/SKILL.md) | `HG-TOA`, `HG-DECISION-RIGHTS` |
| 6 Design Transition | [`methodology/06-roadmap.md`](methodology/06-roadmap.md) | [`07-build-roadmap`](skills/07-build-roadmap/SKILL.md) | `HG-BUDGET` |
| 7 Operationalize | [`methodology/07-operating-model-governance.md`](methodology/07-operating-model-governance.md) | [`08-design-operating-model`](skills/08-design-operating-model/SKILL.md) | `HG-AUTHORITY`, `HG-DECISION-RIGHTS`, `HG-RISK`, `HG-PROMOTION` |
| 8 Measure & Evolve | [`methodology/08-measurement-evolution.md`](methodology/08-measurement-evolution.md) | [`09-measure-evolution`](skills/09-measure-evolution/SKILL.md) | `HG-VALUE`, `HG-AUTHORITY` |
| any | — | [`10-audit-aitm-engagement`](skills/10-audit-aitm-engagement/SKILL.md) | — |

"Typical" is a reading aid: any gate applies whenever its trigger occurs, in any phase. For example, `HG-RISK` applies in phase 6 when a pilot would accept material risk.

## Profiles

Composable. A base profile (Compact or Standard) plus any add-ons. Content per profile: [`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md); selection: [`PROFILE_SELECTION.md`](PROFILE_SELECTION.md).

| Profile | Use it when | Adds |
|---|---|---|
| Compact | one or two Capabilities, low or moderate risk, reversible change | the floor that every application provides |
| Standard | several interdependent Capabilities or systems | system map, network, constraint, Target Operating Architecture, transition states, pilots, operating model, value report |
| Governed | material customer, financial, legal, or security exposure; sensitive data; regulated or irreversible actions; high AI authority | complete AI governance, Authority Ceilings, AI change control, incident handling, evaluation datasets, execution gates, explicit risk ownership |
| Portfolio | several Initiatives across value streams or shared enablers | portfolio, WIP limits, cross-capability dependencies |
| Measured | realized value must be demonstrated | benefit evidence chain, attribution confidence, sustained-value review |

Default when uncertain: **Standard + Measured**; an unknown Governed condition counts as holding unless the Outcome owner records otherwise ([`PROFILE_SELECTION.md`](PROFILE_SELECTION.md) §4). Typical with material customer, financial, security, legal, or autonomy risk: Standard + Governed + Measured. The selected profiles are recorded as a Decision, approved with `HG-OUTCOME`; an application that declares none is evaluated as Compact, and one that declares only add-ons as Standard plus those add-ons.

## Human decision gates

IDs and one-line triggers; binding text [`STANDARD.md`](STANDARD.md) §8. An agent that reaches an open gate records it as a proposed Decision and stops with `HUMAN_DECISION_REQUIRED`; the approval updates that Decision with the name of the human who gave it.

| Gate | Human approval before |
|---|---|
| `HG-OUTCOME` | approving transformation Outcomes |
| `HG-INITIATIVE` | selecting material Initiatives |
| `HG-TOA` | approving the Target Operating Architecture (Compact: the Capability Target States) |
| `HG-DECISION-RIGHTS` | changing material Decision Rights |
| `HG-AUTHORITY` | granting or increasing AI authority (any level above L0, including an Authority Ceiling) |
| `HG-RISK` | accepting material customer, financial, security, legal, or operational risk |
| `HG-BUDGET` | committing material budget |
| `HG-PROMOTION` | promoting a material pilot to rollout |
| `HG-VALUE` | declaring value realized (value state REALIZED or SUSTAINED) |

Reducing AI authority never needs a gate. "Material" is defined in [`STANDARD.md`](STANDARD.md) §16.

## Repository map

| Path | Role |
|---|---|
| root `*.md` | Canonical Core ([`MANIFEST.md`](MANIFEST.md) `canonical_core`) plus framework governance and registries ([`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md)) |
| [`methodology/`](methodology/) | one file per phase, 0–8 |
| [`skills/`](skills/) | 40 numbered skills (procedures) and their router [`skills/INDEX.md`](skills/INDEX.md) |
| [`artifacts/`](artifacts/) | artifact contracts: the record shapes that engagement instances follow (never the instances) |
| `diagnostics/` `design/` `transition/` `portfolio/` `execution/` `evaluation/` `operations/` `governance/` `change/` `measurement/` `economics/` `evidence/` `ontology/` | modules, activated per profile ([`MODULE_CATALOG.md`](MODULE_CATALOG.md)) |
| [`examples/`](examples/) | fictional, informative worked example |
| [`docs/`](docs/) | informative guides, e.g. the crosswalk to the Agentic Product Standard |
| [`rubrics/`](rubrics/) | informative quality rubrics and anti-patterns for judging AITM-SMB outputs |
| [`validation/`](validation/) | abstract scenarios the method must generalize across |
| [`maturity/`](maturity/), [`reference-architecture/`](reference-architecture/) | informative descriptions; not targets or required stacks |
| [`tools/`](tools/) | [`tools/validate.py`](tools/validate.py) (integrity checks) and [`tools/build_dist.py`](tools/build_dist.py) (distributions); Python 3 standard library only |
| [`decisions/`](decisions/) | Architecture Decision Records for the methodology |
| [`releases/`](releases/), [`audits/`](audits/) | release records and historical audits |
| [`.github/`](.github/) | standalone workflow and contribution templates; inert while hosted in the Agentic Product Standard repository |

## Using it with Claude Code

The whole folder is one skill named `aitm-smb`; the root [`SKILL.md`](SKILL.md) routes to the numbered skills. Install the folder intact; single skills copied out of it lose their references.

```bash
git clone https://github.com/Moai-Team-LLC/agentic-product-standard.git
mkdir -p ~/.claude/skills

# pick one:
# A. personal install, copied
cp -R agentic-product-standard/aitm-smb ~/.claude/skills/aitm-smb
# B. personal install, symlinked (follows git pull)
ln -s "$PWD/agentic-product-standard/aitm-smb" ~/.claude/skills/aitm-smb
# C. one project only
mkdir -p <project>/.claude/skills
cp -R agentic-product-standard/aitm-smb <project>/.claude/skills/aitm-smb
```

Then ask, for example: *"Run an AITM-SMB Compact engagement for our order-intake process. Use ./engagement as the workspace."* The agent asks for an accountable Outcome owner, writes every instance into the workspace (never into the skill folder), and stops at each human gate for your decision.

## Using it with other agents

Point the agent at [`AGENTS.md`](AGENTS.md) (for example from your project's own agent instructions) and have it load context as [`AGENT_CONTEXT_POLICY.md`](AGENT_CONTEXT_POLICY.md) defines. All paths are relative to this folder. Every skill ends with the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](AGENT_OUTPUT_STANDARD.md).

## Validation and distributions

Run from this folder:

```bash
python3 tools/validate.py                                        # framework integrity
python3 tools/validate.py --engagement examples/compact-scenario-b   # trace integrity of an engagement
python3 tools/build_dist.py                                      # Core and Full zips in dist/
```

Point `--engagement` at your own workspace to check its trace before claiming conformance. Each release attaches the Core and Full zips. The whole folder is the Full distribution; the Core distribution is defined in [`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md) §Distributions and has no `tools/`, so these commands need Full.

## Relation to the Agentic Product Standard

AITM-SMB decides *whether and how much* AI a business change should use: the Intervention type, the authority level, the Authority Ceiling, and the pilot evidence. The [Agentic Product Standard](https://github.com/Moai-Team-LLC/agentic-product-standard) (APS), which hosts this folder, decides *how to build and license* the AI component. The two use unrelated ladders: AITM-SMB L0–L5 is a business authority ladder, APS L0–L4 an architecture ladder; write `AITM-L3` or `APS-L3` when both appear. The informative [crosswalk](docs/crosswalk-agentic-product-standard.md) maps the ladders, the artifacts, and the hand-off. It adds no requirement to either standard.

## Versioning and stability

Semantic versioning ([`VERSIONING.md`](VERSIONING.md)). Within 1.x, the stable objects, identifiers, core trace, profiles, intervention families, autonomy levels, and agent statuses keep their meaning ([`PUBLIC_API.md`](PUBLIC_API.md) §9); an incompatible change requires 2.0. Releases are tagged `aitm-smb-vX.Y.Z` in the hosting repository.

## Contributing

Issues and pull requests are welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) first: semantic changes start with an issue, and every pull request states its version class. Conduct: [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Security or agent-safety problems: [`SECURITY.md`](SECURITY.md), privately.

## License

[MIT](LICENSE). Copyright (c) 2026 Alex Duchenchuk. Contributions are accepted under the same license.

## Citation

Cite AITM-SMB with the metadata in [`CITATION.cff`](CITATION.cff).
