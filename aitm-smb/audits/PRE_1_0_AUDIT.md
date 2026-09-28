# AITM-SMB Pre-1.0 Integrity Audit

> Historical record, produced with internal pre-publication tooling that is not part of this repository. Its counts describe the 1.0.0 tree, not the current one. Reproducible checks: [`tools/validate.py`](../tools/validate.py) and [`skills/39-audit-framework-integrity/SKILL.md`](../skills/39-audit-framework-integrity/SKILL.md) (see [`MAINTENANCE.md`](../MAINTENANCE.md)). Findings from the 1.1.0 release review are summarized in [`audits/1.1_RELEASE_AUDIT.md`](1.1_RELEASE_AUDIT.md).

## Result

**PASS**

## Repository

- Markdown files: 170
- Active skill files: 39
- Markdown references checked: 273
- Broken references: 0
- Skill contract errors: 0
- Missing canonical concept sources: 0
- Application profiles detected: Compact, Standard, Governed, Portfolio, Measured

## Consolidation decisions

- Phase skills 01–10 are now orchestrators rather than duplicate methodology definitions.
- Capability Target State and Target Operating Architecture are now separate canonical abstraction levels.
- `AI Opportunity Map` is deprecated in favor of the general `Intervention Map`.
- Deprecated artifacts remain as redirect stubs for compatibility.
- Canonical concept ownership is explicit in [`CANONICAL_CONCEPTS.md`](../CANONICAL_CONCEPTS.md).
- The root [`MANIFEST.md`](../MANIFEST.md) now contains a small canonical core instead of an accumulated list of all modules.

## Broken references

- none

## Skill errors

- none

## Missing concept sources

- none

## Release recommendation

Proceed to 1.0 only after a final editorial pass over the Canonical Core and a clean rerun of this audit.
Do not add new Core concepts during that pass unless they close a demonstrated semantic gap.
