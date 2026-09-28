<!--
Standalone copy for after a split (git subtree split --prefix=aitm-smb).
Inert while AITM-SMB lives inside the Agentic Product Standard repository:
GitHub reads the pull-request template only from the host's .github/.

One topic per pull request. Semantic changes start with an issue (CONTRIBUTING.md).
-->

## What changed

<!-- One or two sentences. -->

## Why

<!-- What is wrong, missing, or unclear today? Link the issue. -->

## Change class

- VERSIONING.md class: <!-- PATCH | MINOR | MAJOR -->
- PUBLIC_API.md impact: <!-- none | compatible addition | incompatible (requires 2.0) -->

## Checklist

- [ ] `python3 tools/validate.py` and `python3 tools/validate.py --engagement examples/compact-scenario-b` pass with 0 errors (MAINTENANCE.md §2)
- [ ] VERSIONING.md class stated above; no incompatible change to a PUBLIC_API.md §1–§8 item
- [ ] CHANGELOG.md updated; any renamed field is in the migration table
- [ ] ADR added from decisions/ADR-0000-template.md for a material change
- [ ] The canonical source (CANONICAL_CONCEPTS.md) was changed; other files reference it rather than copy it
- [ ] No named companies, clients, vendors, or products in the core; examples are fictional and live in examples/
