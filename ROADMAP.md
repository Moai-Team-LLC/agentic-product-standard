# Roadmap

A living view of where the Agentic Product Standard is headed. Not a commitment — a
direction. Issues and PRs that move these forward are very welcome; see
[CONTRIBUTING.md](CONTRIBUTING.md).

## Now

- **Reference implementation depth** — keep [AgenticMind](https://github.com/Moai-Team-LLC/AgenticMind)
  (the Layer-4 memory exemplar) mapped 1:1 to the canon via the
  [case study](examples/agenticmind-case-study.md).
- **ADR discipline** — capture each substantive decision under [`docs/adr/`](docs/adr/) so the
  *why* behind the standard is auditable.

## Next

- **More worked examples** — a reference exemplar per autonomy level (L1–L4), each a short
  case study like the AgenticMind one.
- **Eval appendix** — concrete, copyable eval-set templates per failure mode to go with the
  `eval-driven-dev` sub-skill.
- **Framework matrix upkeep** — keep `framework-selection` current as LangGraph / Claude SDK /
  OpenAI Agents SDK / CrewAI / Pydantic AI evolve.

## Later / help wanted

- **Translations** of `STANDARD.md` (the canon travels; the field is global).
- **Editor coverage beyond Claude Code** — adapt the skill set for other agentic IDEs.
- **Conformance checklist** — a machine-checkable "does my repo follow the standard?" linter.

## Out of scope

- Becoming a framework. This is a *standard* plus skills; it stays vendor-neutral.
- Endorsing or ranking specific model vendors as ground truth (see anti-pattern #12).

Have something that belongs here? [Open an issue](https://github.com/Moai-Team-LLC/agentic-product-standard/issues/new/choose).
