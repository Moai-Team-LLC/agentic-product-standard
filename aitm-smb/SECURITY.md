# Security Policy

AITM-SMB is a documentation project: Markdown methodology, agent skills, and two small Python scripts. It runs no service. The security concerns that matter are the integrity of the guidance that AI agents follow, and the scripts in [`tools/`](tools/).

## Reporting a vulnerability

Do **not** open a public issue for a security or agent-safety problem. Report it privately through GitHub Security Advisories:

1. Open the [Security tab](https://github.com/Moai-Team-LLC/agentic-product-standard/security) of the repository that hosts AITM-SMB.
2. Choose **Report a vulnerability** to open a private advisory. Name the affected file and section, and say which version or commit you tested.

The maintainers aim to acknowledge a report within 3 business days and to agree on a disclosure timeline with you. Reporters are credited unless they ask not to be.

## In scope

- **Guidance that could lead an agent across a human gate or into unsafe action.** For example: wording that lets an agent approve or infer approval of a [`STANDARD.md`](STANDARD.md) §8 gate, raise AI authority without `HG-AUTHORITY`, treat a proposed Authority Ceiling as approved, fabricate business facts as Evidence, or write outside the engagement workspace.
- **Prompt-injection-like content** in [`SKILL.md`](SKILL.md), any file under [`skills/`](skills/), artifact contracts, examples, or other files an agent loads: instructions that would override [`AGENTS.md`](AGENTS.md), hide actions from the handoff, or exfiltrate engagement data.
- **Guidance that would leak engagement data**, such as instructions to copy personal or confidential data into prompts, datasets, or artifacts contrary to [`AGENT_CONTEXT_POLICY.md`](AGENT_CONTEXT_POLICY.md).
- **The scripts** [`tools/validate.py`](tools/validate.py) and [`tools/build_dist.py`](tools/build_dist.py): anything that could execute unexpected code, touch files beyond what they are pointed at (the AITM-SMB folder, a workspace given with `--engagement`, the `dist` output), or put files into a distribution that should not be there.
- **The release workflow** in `.github/workflows/` and anything else this folder asks you to run.

## Out of scope

- Behavior of the AI models, agent runtimes, or third-party tools used to run the methodology.
- Business decisions made in an engagement, and disagreements with the methodology's choices. Open an issue or a pull request instead ([`CONTRIBUTING.md`](CONTRIBUTING.md)).
- Problems in the Agentic Product Standard outside this folder; report those under that repository's [security policy](https://github.com/Moai-Team-LLC/agentic-product-standard/blob/main/SECURITY.md).

## Supported versions

The latest 1.x release and the `main` branch receive fixes. Pin a release tag if you need stability ([`VERSIONING.md`](VERSIONING.md) §10).
