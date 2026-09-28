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
