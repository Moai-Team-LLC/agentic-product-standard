# AGENTS.md — working in this repository

Instructions for coding agents (and humans) changing The Agentic Product Standard. The standard is documentation plus a small Python tool; the rules below keep the two from drifting apart.

## The one rule: edit the canon, not the copies

Anything enumerable — a principle, an autonomy level or oversight mode, a harness layer, a Definition of Done item, an anti-pattern, a scorecard item, a crosswalk entry — lives once, in `canon/*.yaml`. The documents that repeat it contain **generated regions**:

```
<!-- canon:begin:readme.dod -->
…generated…
<!-- canon:end:readme.dod -->
```

Never edit inside those markers, and never hand-edit generated files (`CROSSWALK.md`, `skills/agentic-product-architect/production-readiness/DOD.md`, `templates/conformance/aps-conformance.template.yaml`, `skills-lock.json`). Change the canon, then:

```bash
python3 tools/aps.py render     # rewrite every generated region and file
python3 tools/aps.py check      # what CI runs: canon integrity, drift, prose counts, skills
python3 -m unittest discover -s tools/tests
```

Requirements: Python 3.9+ and PyYAML (`pip install pyyaml jsonschema` — jsonschema adds schema validation).

## Invariants CI enforces

- DoD numbers, anti-pattern numbers, and scorecard ids are **identifiers**: never renumber, never reuse. New items take the next number.
- Every DoD item is evidenced by at least one scorecard item.
- Counts written in prose ("33-point Definition of Done", "20 anti-patterns", "nine-layer harness") match the canon — `check` fails otherwise. History (`CHANGELOG.md`, `docs/adr/`, `docs/advisories/`, `examples/`) is exempt.
- `AGENT_STANDARD.md` at the root and `skills/agent-builder/AGENT_STANDARD.md` are byte-identical (render copies the root).
- Every `SKILL.md` follows the Agent Skills specification (name = directory, description ≤ 1024 chars, spec fields only) and no skill file carries hidden content. Changing a skill changes `skills-lock.json` — commit both.
- The 10-question checklist in the README (generated from `canon/checklist.yaml`) must appear verbatim in `templates/decision-tree/README.md`.
- Relative links in Markdown must resolve. In canon YAML, write repo links as `@/path`; the renderer makes them relative for each target.

## Vocabulary

"Layer N" is a **harness** layer (Canon 4). `STANDARD.md` Part II sections are **Stack N**. The operating point is `L0–L4 · O0–O2` (autonomy × oversight); the Loop License binds at O1+. See `CONTEXT.md`.

## `aitm-smb/` is a separate methodology

`aitm-smb/` hosts AITM-SMB, the upstream business-level methodology, with its own semver, changelog, canonical source and release tags (`aitm-smb-vX.Y.Z`), kept split-ready ([ADR-0006](docs/adr/0006-host-aitm-smb-as-split-ready-subfolder.md)). The canon rule above does not reach into it: its single source is `aitm-smb/CANONICAL_CONCEPTS.md`, and its rules are `aitm-smb/CONTRIBUTING.md` and `aitm-smb/MAINTENANCE.md`. Run its checks from inside the folder (`cd aitm-smb && python3 tools/validate.py`). The repo-wide link, prose-count and skill-frontmatter checks still cover it; its skills are not in `skills-lock.json`. Its `L0–L5` is a business-authority ladder, not the operating point — write `AITM-L<n>` beside `APS-L<n>` / `APS-O<n>` where both appear.

## Changes and releases

- Conventional Commits, header ≤ 72 characters (`.githooks/commit-msg`; `git config core.hooksPath .githooks`).
- Substantive changes to the canon go through an ADR in `docs/adr/` (see `GOVERNANCE.md`); breaking the canon needs a migration note in `CHANGELOG.md`.
- A release bumps `version` in `canon/meta.yaml`, renders, adds the `CHANGELOG.md` section, and is tagged `v<version>` — the release workflow checks the tag matches the canon.
- Factual claims need primary sources. Mark anything you could not verify, and prefer the durable claim over the exciting one.
