# AITM-SMB Agent Context Policy

**Version:** 1.0.0

AITM-SMB is designed for bounded context loading.

## Core bundle

Every agent reads:

```text
MANIFEST.md
STANDARD.md
NORMATIVE_INDEX.md
PUBLIC_API.md
CORE_MODEL.md
METHOD_FLOW.md
TRACEABILITY.md
AGENTS.md
ontology/ONTOLOGY.md
```

## Task bundle

Then load only:

```text
selected Application Profile
relevant methodology phase
relevant module
relevant artifact contract
relevant skill
approved upstream artifacts
required Evidence
```

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
