_One topic per pull request. Semantic changes start with an issue ([CONTRIBUTING.md](../CONTRIBUTING.md)). This template is the standalone copy for after a split; while AITM-SMB lives inside the Agentic Product Standard repository, GitHub uses the host repository's template._

## What changed

_One or two sentences._

## Why

_What is wrong, missing, or unclear today? Link the issue._

## Change class

- VERSIONING.md class: _PATCH, MINOR or MAJOR_
- PUBLIC_API.md impact: _none, compatible addition, or incompatible (requires 2.0)_

## Checklist

- [ ] `python3 tools/validate.py` and `python3 tools/validate.py --engagement examples/compact-scenario-b` pass with 0 errors (MAINTENANCE.md §2)
- [ ] VERSIONING.md class stated above; no incompatible change to a PUBLIC_API.md §1–§8 item
- [ ] CHANGELOG.md updated; any renamed field is in the release notes' migration table
- [ ] ADR added from decisions/ADR-0000-template.md for a material change
- [ ] The canonical source (CANONICAL_CONCEPTS.md) was changed; other files reference it rather than copy it
- [ ] No named companies, clients, vendors, or products in the core; examples are fictional and live in examples/
