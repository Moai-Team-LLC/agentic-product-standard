<!-- One topic per PR. A vendor update and a new exemplar are two PRs. -->

## What changed

<!-- Summarize the change in a sentence or two. -->

## Why

<!-- What's wrong/outdated/missing today, and why does this fix it? -->

## Sources

<!-- Link primary sources for any factual claim. Single-vendor benchmarks are directional, not ground truth. -->

## Checklist

- [ ] Edited the relevant `STANDARD.md` section and/or matching `skills/.../SKILL.md`
- [ ] Enumerable changes made in `canon/`, rendered with `python3 tools/aps.py render`; `python3 tools/aps.py check` passes
- [ ] Hand-written guidance updated in both `STANDARD.md` and the matching `skills/.../SKILL.md`
- [ ] No framework boilerplate added to the skills (framework-neutral gates belong in `templates/`)
- [ ] Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/)
- [ ] For `aitm-smb/` changes: from inside `aitm-smb/`, `python3 tools/validate.py` and `python3 tools/validate.py --engagement examples/compact-scenario-b` pass; the VERSIONING class is stated; no incompatible change to a `PUBLIC_API.md` item; `aitm-smb/CHANGELOG.md` updated (renamed fields in the release notes' migration table); no named companies or vendors in the normative core (see [`aitm-smb/CONTRIBUTING.md`](../aitm-smb/CONTRIBUTING.md))
