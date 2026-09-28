# AITM-SMB Release Readiness

**Status:** Informative ([`NORMATIVE_INDEX.md`](../NORMATIVE_INDEX.md) tier 13). The judgment part of the release checks in [`MAINTENANCE.md`](../MAINTENANCE.md) §2, which govern. The automated part is `python3 tools/validate.py`; this list does not repeat what it checks (references, registries, versions, deprecated content, identifiers, gates). The 1.0.0 record: [`releases/1.0.0-release-checklist.md`](../releases/1.0.0-release-checklist.md). Typical use: [`skills/39-audit-framework-integrity/SKILL.md`](../skills/39-audit-framework-integrity/SKILL.md).

Before a release verify:

## Automated

- [ ] `python3 tools/validate.py` passes with 0 errors
- [ ] `python3 tools/validate.py --engagement examples/compact-scenario-b` passes
- [ ] orphan warnings resolved

## Canonical Core

- [ ] Core files have no semantic contradictions
- [ ] Core concepts have one canonical definition ([`CANONICAL_CONCEPTS.md`](../CANONICAL_CONCEPTS.md))
- [ ] normative precedence is explicit
- [ ] method flow matches phase semantics ([`METHOD_FLOW.md`](../METHOD_FLOW.md), [`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md))

## Profiles

- [ ] Compact profile is genuinely lightweight
- [ ] Standard profile is sufficient for most SMB transformations
- [ ] Governed profile covers authority/risk escalation
- [ ] Portfolio profile handles multi-initiative coordination
- [ ] Measured profile closes value realization
- [ ] every [`APPLICATION_PROFILES.md`](../APPLICATION_PROFILES.md) item resolves to an artifact contract, module, or skill

## Agent Execution

- [ ] Core bundle and Task bundle ([`AGENT_CONTEXT_POLICY.md`](../AGENT_CONTEXT_POLICY.md)) are sufficient
- [ ] skills reference existing artifacts
- [ ] skills reference existing modules
- [ ] handoff format is consistent ([`AGENT_OUTPUT_STANDARD.md`](../AGENT_OUTPUT_STANDARD.md))
- [ ] human gates are preserved ([`STANDARD.md`](../STANDARD.md) §8)

## Repository

- [ ] CHANGELOG and release notes complete, including the migration table for any field rename ([`VERSIONING.md`](../VERSIONING.md) §9)
- [ ] no dangerous duplicate definitions ([`MAINTENANCE.md`](../MAINTENANCE.md) §4)
