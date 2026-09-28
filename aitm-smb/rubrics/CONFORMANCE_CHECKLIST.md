# AITM-SMB Conformance Checklist

**Status:** Informative (`NORMATIVE_INDEX.md` tier 13). A review aid for `CONFORMANCE.md`, which governs on any conflict. Item numbers refer to `CONFORMANCE.md` §1. Typical use: `skills/38-audit-conformance/SKILL.md`, `skills/10-audit-aitm-engagement/SKILL.md`.

## Core (`CONFORMANCE.md` §1)

- [ ] 1 at least one measurable Outcome, with owner, baseline or known baseline gap, and target
- [ ] 2 relevant Capabilities identified
- [ ] 3 Current State represented sufficiently for diagnosis
- [ ] 4 a material Gap identified
- [ ] 5 Cause distinguished from Symptom; every Gap has Evidence or explicit Hypothesis status; causal uncertainty is visible
- [ ] 6 non-AI alternatives were considered
- [ ] 7 AI justified where selected; the `AI_*` intervention family is explicit
- [ ] 8 Capability Target State defined
- [ ] 9 every selected Initiative links to an Outcome, to a Capability, and to the Gaps it closes
- [ ] 10 every Initiative has success Metrics; a business metric exists; material claims have Evidence; missing baselines are visible
- [ ] 11 AI authority explicitly granted, not inferred; autonomy level justified; how authority is observed and reduced is defined
- [ ] 12 end-to-end trace intact; missing links visible (`TRACEABILITY.md` §4)
- [ ] 13 system effects checked for selected Initiatives: upstream, downstream, shared-resource, incentive, Constraint Migration
- [ ] 14 each `STANDARD.md` §8 gate decision recorded as an approved Decision naming the human approver

## Invariants (`STANDARD.md` §3)

- [ ] facts, Evidence, Assumptions, Hypotheses, Decisions and Open Questions are separated (INV-04)
- [ ] AI metrics do not replace business metrics (INV-13)
- [ ] no other MUST invariant is violated, or the waiver is listed as an exception (`CONFORMANCE.md` §6)

## Profiles, declaration, exceptions

- [ ] not only a component that is non-conforming by itself (`CONFORMANCE.md` §2)
- [ ] every claimed profile has the content `APPLICATION_PROFILES.md` lists for it, or a recorded waiver (`CONFORMANCE.md` §3)
- [ ] conformance declaration recorded in the Transformation Intent (`CONFORMANCE.md` §5)
- [ ] every waiver records requirement, reason, risk, owner and review trigger (`CONFORMANCE.md` §6)

## Beyond `CONFORMANCE.md` §1 (profile-dependent)

- [ ] owner exists
- [ ] approvals are explicit
- [ ] escalation is explicit
- [ ] failure ownership is explicit
- [ ] recovery or rollback is defined where relevant
- [ ] operating metric exists where useful
- [ ] post-implementation Evidence can change prior decisions
