<!-- One topic per PR. A vendor update and a new exemplar are two PRs. -->

## What changed

<!-- Summarize the change in a sentence or two. -->

## Why

<!-- What's wrong/outdated/missing today, and why does this fix it? -->

## Sources

<!-- Link primary sources for any factual claim. Single-vendor benchmarks are directional, not ground truth. -->

## Checklist

- [ ] Edited the relevant `STANDARD.md` section and/or matching `skills/.../SKILL.md`
- [ ] Kept the English and Russian standards in sync (or noted what still needs syncing)
- [ ] No code templates added (the skill set teaches judgment, not boilerplate)
- [ ] Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/)
- [ ] For `aitm-smb/` changes: from inside `aitm-smb/`, `python3 tools/validate.py` and `python3 tools/validate.py --engagement examples/compact-scenario-b` pass; the VERSIONING class is stated; no incompatible change to a `PUBLIC_API.md` item; `aitm-smb/CHANGELOG.md` updated (renamed fields in the release notes' migration table); no named companies or vendors in the normative core (see [`aitm-smb/CONTRIBUTING.md`](../aitm-smb/CONTRIBUTING.md))
