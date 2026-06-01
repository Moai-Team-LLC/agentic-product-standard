# Security Policy

This repository ships **documentation and Claude Code skills** — there is no runtime
service here. The most relevant "security" concerns are (a) the integrity of the guidance
itself and (b) the [`setup.sh`](setup.sh) installer that copies skills onto your machine.

## Reporting a vulnerability

Please **do not open a public issue** for security-relevant problems. Instead use GitHub's
private reporting:

1. Go to the **[Security tab](https://github.com/Moai-Team-LLC/agentic-product-standard/security)**.
2. Click **"Report a vulnerability"** to open a private advisory.

We aim to acknowledge within **3 business days** and to agree on a disclosure timeline with
you. Credit is given to reporters unless you ask us not to.

### In scope

- Anything in `setup.sh` or tooling that could execute unexpected code, exfiltrate data, or
  write outside the intended skill directories.
- Skill content that could induce an agent to take unsafe actions (e.g. prompt-injection
  payloads embedded in the guidance).
- Supply-chain issues in anything this repo asks you to run.

### Out of scope

- The behavior of third-party tools, models, or frameworks referenced in the standard.
- Disagreements with the *architectural opinions* in `STANDARD.md` — those belong in
  [issues](https://github.com/Moai-Team-LLC/agentic-product-standard/issues) or a PR.

## Supported versions

This is a living document; the `main` branch is the only supported version. Pin a tag or
commit if you need stability.
