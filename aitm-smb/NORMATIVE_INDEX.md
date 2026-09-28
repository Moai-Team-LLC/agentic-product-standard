# AITM-SMB Normative Index

**Version:** 1.1.0

Paths are relative to the AITM root: the directory containing [`MANIFEST.md`](MANIFEST.md).

## Normative precedence

When methodology rules conflict, the higher tier wins:

```text
1.  approved human decision for the engagement (DEC-###)
2.  STANDARD.md
3.  PUBLIC_API.md
4.  CORE_MODEL.md, ontology/ONTOLOGY.md, CANONICAL_CONCEPTS.md
5.  TRACEABILITY.md
6.  EXECUTION_MODEL.md, METHOD_FLOW.md
7.  DECISION_MODEL.md
8.  CONFORMANCE.md, APPLICATION_PROFILES.md
9.  AGENTS.md, AGENT_CONTEXT_POLICY.md, AGENT_OUTPUT_STANDARD.md
10. activated module
11. artifact contract
12. skill
13. informative guidance
```

Lower-priority material MUST NOT override higher-priority semantics.

Within one tier, the canonical source named in [`CANONICAL_CONCEPTS.md`](CANONICAL_CONCEPTS.md) wins.

Record shapes: the record contract named in [`CANONICAL_CONCEPTS.md`](CANONICAL_CONCEPTS.md) owns field names; the module owns meaning and rules.

Human-decision floor (tier 1): an approved human decision MAY waive SHOULD and profile requirements ([`CONFORMANCE.md`](CONFORMANCE.md) §6). Waiving a MUST, including a [`STANDARD.md`](STANDARD.md) §3 invariant, makes the application non-conforming for that requirement and is recorded as an exception. No decision can hand a [`STANDARD.md`](STANDARD.md) §8 gate decision to an AI agent.

This precedence resolves conflicts between methodology rules. Conflicts between engagement facts follow [`AGENTS.md`](AGENTS.md) §2.

## Placement of other files

```text
tier 2   SCOPE.md (elaborates STANDARD.md §13; STANDARD.md wins on conflict)
n/a      MANIFEST.md, NORMATIVE_INDEX.md (registries: the machine-readable core list and this precedence; no engagement semantics)
tier 8   PROFILE_SELECTION.md, MINIMUM_ARTIFACT_SET.md (subordinate to APPLICATION_PROFILES.md)
tier 10  methodology/ phase files (always active; they refine EXECUTION_MODEL.md and MUST agree with it)
tier 10  canonical concept sources, e.g. METRICS.md, evidence/EVIDENCE_STANDARD.md (always active)
tier 10  AGENT_DIAGNOSTIC_PROTOCOL.md (active whenever an agent performs diagnosis)
tier 13  README.md, QUICKSTART.md, GLOSSARY.md, SKILL.md, docs/, examples/, rubrics/,
         maturity/, reference-architecture/, validation/, releases/, audits/
untiered NORMATIVE_INDEX.md, MANIFEST.md (they define these tiers and list the Canonical Core)
```

Framework governance, not engagement rules: [`VERSIONING.md`](VERSIONING.md), [`EXTENSION_MODEL.md`](EXTENSION_MODEL.md), [`MAINTENANCE.md`](MAINTENANCE.md), [`CONTRIBUTING.md`](CONTRIBUTING.md), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), [`SECURITY.md`](SECURITY.md), `LICENSE`, [`CITATION.cff`](CITATION.cff), [`decisions/`](decisions/) (maintainer ADRs), [`CHANGELOG.md`](CHANGELOG.md), [`REPO_STRUCTURE.md`](REPO_STRUCTURE.md) (generated file tree), [`tools/`](tools/) (validation and distribution scripts), `.github/` (standalone CI workflow and templates).

## Canonical Core

Applies to every engagement, whatever the profile. Machine-readable list: [`MANIFEST.md`](MANIFEST.md) `canonical_core`.

```text
README.md
MANIFEST.md
STANDARD.md
SCOPE.md
NORMATIVE_INDEX.md
PUBLIC_API.md
CANONICAL_CONCEPTS.md
CORE_MODEL.md
METHOD_FLOW.md
TRACEABILITY.md
EXECUTION_MODEL.md
DECISION_MODEL.md
CONFORMANCE.md
APPLICATION_PROFILES.md
AGENTS.md
AGENT_CONTEXT_POLICY.md
AGENT_OUTPUT_STANDARD.md
ontology/ONTOLOGY.md
```

[`README.md`](README.md) is part of the Canonical Core for distribution; its content is informative (tier 13).

## Registries

Registries enumerate; they define no semantics. Machine-readable list: [`MANIFEST.md`](MANIFEST.md) `registries`.

```text
MODULE_CATALOG.md
artifacts/INDEX.md
skills/INDEX.md
```

## Modules

Modules ([`MODULE_CATALOG.md`](MODULE_CATALOG.md)) become normative for an engagement only when:

```text
required by the selected profile
or explicitly activated by a documented decision
```

A canonical concept source is normative for its concept whenever that concept is used, regardless of activation; the module's procedures remain activation-dependent ([`CANONICAL_CONCEPTS.md`](CANONICAL_CONCEPTS.md) §3).

## Distributions

```text
Core  Canonical Core + Registries + LICENSE + CHANGELOG.md (links from Core files to modules, skills and contracts resolve only in the Full distribution)
      read, implement, or integrate against the stable semantic contract
Full  the whole AITM root
      execute the methodology
```

[`tools/build_dist.py`](tools/build_dist.py) builds both ([`MANIFEST.md`](MANIFEST.md) `distributions`); each release attaches them.
