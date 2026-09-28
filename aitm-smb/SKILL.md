---
name: aitm-smb
description: "AITM-SMB: an agent-readable, domain-neutral methodology for the AI transformation of small and medium-sized businesses. Use when planning, running, or auditing the AI transformation of an SMB or of one business capability: framing measurable Outcomes, mapping capabilities and their current state, diagnosing gaps and causes, deciding whether and where AI belongs versus simpler fixes and how much authority it gets, designing target states, roadmaps, pilots and rollouts, governing AI in operation, and proving value realization; or when running an AITM-SMB engagement or producing and reviewing its artifacts. Do not use for building the AI or agent software itself (its architecture, code, prompts, or component evals); hand that over through the crosswalk to the Agentic Product Standard."
license: MIT
---

# AITM-SMB

AITM-SMB redesigns a small or medium-sized business as a measurable human + software + AI operating system.
Its unit of transformation is the Business Capability, not the AI use case: every change traces Outcome → Capability → Gap → Intervention → Initiative → Target State → Metric → Evidence (`EXECUTION_MODEL.md` §6).
AI is optional; its authority is granted explicitly by humans and can always be reduced.

This file routes. It is informative guidance (`NORMATIVE_INDEX.md`); on any conflict, the files it points to govern.

## Operating rules

1. **Paths.** Every path here and in the files it points to is relative to the directory containing this `SKILL.md` (the AITM root; it also contains `MANIFEST.md`). Install and keep the whole directory as one skill; never copy single skills out of it (`AGENT_CONTEXT_POLICY.md`).
2. **Context.** Load the Core bundle, then only the Task bundle, as `AGENT_CONTEXT_POLICY.md` defines. Do not load the whole repository.
3. **Workspace.** Never write into `artifacts/` or anywhere else in this directory; `artifacts/` holds contracts, not instances. Ask the user for an engagement workspace outside it and write every instance there (`artifacts/_ARTIFACT_CONTRACT.md` §6).
4. **Human gates.** Stop at every `STANDARD.md` §8 gate with status `HUMAN_DECISION_REQUIRED`. Record an approval only as the named human explicitly gives it; never approve on the user's behalf (`AGENTS.md` §4). Reducing AI authority needs no gate.
5. **Facts.** Never invent business facts. Label inference `[HYPOTHESIS]` or `[ASSUMPTION]` (`AGENTS.md` §3); return `INSUFFICIENT_EVIDENCE` when proceeding would require invented facts, and record the Evidence Debt.
6. **Proportionality.** Produce only what the active profiles require (`APPLICATION_PROFILES.md`).
7. **Handoff.** End every skill run with the `aitm_output` block defined in `AGENT_OUTPUT_STANDARD.md`.

## Routing

Run the orchestrator for the phase; it invokes its specialists. Every skill by number, with purpose, phase, gates and outputs: `skills/INDEX.md` §2.

| User intent | Phase | Orchestrator | Key specialists |
|---|---|---|---|
| start an engagement; frame the problem and Outcomes | 0 Frame | `skills/01-discover-transformation/SKILL.md` | 36 profiles, 37 context |
| map capabilities, systems, and how work runs today | 1 Observe | `skills/02-map-current-system/SKILL.md` | 11 |
| find why a capability underperforms | 2 Diagnose | `skills/03-diagnose-capabilities/SKILL.md` | 12, 16 |
| decide whether and where AI belongs, and how much authority it may get | 3 Design Interventions | `skills/04-design-interventions/SKILL.md` | 13, 14 |
| choose what to do first; commit budget | 4 Decide | `skills/05-prioritize-initiatives/SKILL.md` | — |
| design target capabilities, decision rights, and the operating architecture | 5 Design Target System | `skills/06-design-target-system/SKILL.md` | 15, 17–20, 23, 24 |
| plan the roadmap, transition states, and pilots | 6 Design Transition | `skills/07-build-roadmap/SKILL.md` | 21, 22, 25, 26, 27 |
| run and evaluate pilots, roll out, govern, change AI authority | 7 Operationalize | `skills/08-design-operating-model/SKILL.md` | 28–32, 34, 35 |
| measure effect, prove value, adjust authority from evidence | 8 Measure & Evolve | `skills/09-measure-evolution/SKILL.md` | 26, 33, 34 |
| check an engagement for conformance | any | `skills/10-audit-aitm-engagement/SKILL.md` | 38 |
| an AI-enabled operation failed or misbehaved | 7–8 | `skills/40-handle-incident/SKILL.md` | 34, 27 |
| change or release the methodology itself | — | `skills/39-audit-framework-integrity/SKILL.md` | `CONTRIBUTING.md`, `MAINTENANCE.md` |

Phases, exit conditions and typical gates: `EXECUTION_MODEL.md` §1–§2.

## First run

1. Ask for the engagement workspace path, the business context, and the accountable Outcome owner.
2. `skills/36-select-application-profile/SKILL.md`: propose the profiles (default Standard + Measured when uncertain; Compact only when every Compact use-when condition in `APPLICATION_PROFILES.md` §3 holds) and record the Decision.
3. `skills/37-build-context-bundle/SKILL.md`: load the bounded context for the next skill.
4. `skills/01-discover-transformation/SKILL.md`: Transformation Intent with Outcome records; stop at `HG-OUTCOME`, which also confirms the profiles.
5. Continue phase by phase, 02 through 09, stopping at each gate; return to an earlier phase when Evidence invalidates earlier work (`EXECUTION_MODEL.md` §3).
6. Audit with 10 at any time. Before claiming conformance, run 38 and `python3 tools/validate.py --engagement <workspace>`.

Resuming an engagement: run 37, read the approved profile Decision and the open gates and Evidence Debt of the last handoff, and continue at the first phase whose exit condition does not hold yet.

## Models to imitate

- `QUICKSTART.md`: a first Compact engagement, step by step.
- `examples/compact-scenario-b/`: a finished Compact engagement: the instance files, IDs, and gate Decisions a complete run produces.
- `README.md` and `STANDARD.md`: the thesis and the rules, for humans.

## Beyond AITM-SMB: building the AI component

AITM-SMB decides whether AI belongs, what authority it gets, and how it is evaluated, governed, and valued. It does not design or build the software. When an approved Initiative moves on to building an AI component or agent, continue with `docs/crosswalk-agentic-product-standard.md`. AITM autonomy levels are authority levels, not architecture levels: write `AITM-L3` versus `APS-L3` when both appear.
