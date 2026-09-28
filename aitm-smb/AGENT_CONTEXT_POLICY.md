# AITM-SMB Agent Context Policy

**Version:** 1.1.0

AITM-SMB is designed for bounded context loading.

## Path resolution

All paths in AITM-SMB files are relative to the AITM root: the directory containing `MANIFEST.md`. Resolve every path against the AITM root, never against the citing file.

Keep the AITM root intact when installing it, for example as one skill through the root `SKILL.md`. Do not copy single skills out of it; their references would break.

## Core bundle

Every agent reads, besides this file:

```text
MANIFEST.md
STANDARD.md
NORMATIVE_INDEX.md
PUBLIC_API.md
CANONICAL_CONCEPTS.md
CORE_MODEL.md
METHOD_FLOW.md
EXECUTION_MODEL.md
TRACEABILITY.md
AGENTS.md
AGENT_OUTPUT_STANDARD.md
ontology/ONTOLOGY.md
```

The Core bundle is a loading set. It is not the Canonical Core (`NORMATIVE_INDEX.md`).

## Task bundle

Then load only:

```text
selected Application Profile (see Profile)
relevant methodology phase (methodology/, per EXECUTION_MODEL.md §1)
relevant module
relevant artifact contract
relevant skill
approved upstream artifacts (engagement workspace)
required Evidence
```

Add only when the task needs it:

```text
DECISION_MODEL.md             intervention, AI, or autonomy decisions
AGENT_DIAGNOSTIC_PROTOCOL.md  diagnosis
CONFORMANCE.md                conformance audits
```

## Profile

The active profiles are recorded as an approved Decision (skill 36) in the engagement's Decision & Assumption Log, and confirmed with `HG-OUTCOME`.

To load a profile:

1. read the approved, non-superseded profile Decision in the engagement workspace;
2. load the `APPLICATION_PROFILES.md` sections for those profiles (artifact mapping: `MINIMUM_ARTIFACT_SET.md`);
3. if no profile Decision exists, run `skills/36-select-application-profile/SKILL.md` before any step that needs a profile.

Until that Decision is approved, the profile is provisional; say so in `status_reason`.

## Engagement workspace

Engagement instances (filled artifacts, Evidence, Decisions, conformance declarations) live in an engagement workspace outside the AITM root (`artifacts/_ARTIFACT_CONTRACT.md`).

Agents MUST NOT write engagement instances into the AITM root, including `artifacts/`, which holds contracts only. Paths in `artifacts_changed` are workspace paths.

Load engagement data by reference and only as much as the task needs. Minimize and redact personal data before it enters agent context, evaluation datasets, or artifacts; reference sensitive sources by Evidence ID instead of copying them.

## Rule

Do not load the full repository merely because it exists.

Excess unrelated context increases:

```text
instruction conflict
semantic drift
token cost
hallucinated dependency
```

If a normative dependency is missing, load it rather than infer it.
