# Contributing to AITM-SMB

Contributions should improve decision quality, execution quality, or agent reliability.

Framework governance ([`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md)): this file covers changes to the methodology itself, not engagements. Agents that change this repository follow it too, with [`MAINTENANCE.md`](MAINTENANCE.md) and [`VERSIONING.md`](VERSIONING.md).

## Preferred contributions

- clearer artifact contracts;
- stronger skills;
- abstract validation scenarios;
- evaluation cases;
- counterexamples;
- evidence-backed methodology changes;
- vendor-neutral reference patterns.

## Avoid

- adding terminology without decision value;
- expanding the framework because an enterprise framework contains a concept;
- tool/vendor promotion;
- AI-first assumptions;
- unverifiable maturity claims.

Every addition answers at least one question: what decision does it improve, what risk does it control, what evidence does it produce ([`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md) §9, INV-15)? If none, leave it out.

## How to contribute

1. **Issue first for semantic changes.** Anything that changes meaning (a rule, a record field, a gate, a profile's content, a [`PUBLIC_API.md`](PUBLIC_API.md) item) starts as an issue, so the change can be discussed before it is written. Typos, broken references, and clarifications can go straight to a pull request.
2. **One topic per pull request.** A clarification and a new module are two pull requests.
3. **State the change class.** Each pull request names its [`VERSIONING.md`](VERSIONING.md) class (PATCH, MINOR, or MAJOR) and confirms that no [`PUBLIC_API.md`](PUBLIC_API.md) §1–§8 item changes incompatibly. The 1.x compatibility promise is [`PUBLIC_API.md`](PUBLIC_API.md) §9; an incompatible change waits for 2.0.
4. **Change the canonical source, reference it elsewhere.** Each concept and record shape is defined once; [`CANONICAL_CONCEPTS.md`](CANONICAL_CONCEPTS.md) names where. Edit that source and point to it rather than copying the definition ([`MAINTENANCE.md`](MAINTENANCE.md) §3–§4).
5. **Validate.** Run the required checks of [`MAINTENANCE.md`](MAINTENANCE.md) §2 from the AITM-SMB folder: `python3 tools/validate.py` and `python3 tools/validate.py --engagement examples/compact-scenario-b` pass with 0 errors. CI runs both on every change.
6. **Record the change.** Add a [`CHANGELOG.md`](CHANGELOG.md) entry for any user-visible change; a renamed field goes into the migration table ([`VERSIONING.md`](VERSIONING.md) §9).
7. **Material changes add an ADR.** A material methodology change (for example to a [`PUBLIC_API.md`](PUBLIC_API.md) item, a human gate, or an invariant) and every MAJOR change should be recorded as an ADR ([`MAINTENANCE.md`](MAINTENANCE.md) §2). Copy [`decisions/ADR-0000-template.md`](decisions/ADR-0000-template.md); index and numbering: [`decisions/README.md`](decisions/README.md).

Maintainers review and merge pull requests and cut releases ([`MAINTENANCE.md`](MAINTENANCE.md) §2, [`VERSIONING.md`](VERSIONING.md) §10).

While AITM-SMB is hosted in the Agentic Product Standard repository, that repository's [contribution rules](https://github.com/Moai-Team-LLC/agentic-product-standard/blob/main/CONTRIBUTING.md), including its commit-message convention and checks, and its [governance](https://github.com/Moai-Team-LLC/agentic-product-standard/blob/main/GOVERNANCE.md) apply as well.

## Domain neutrality and examples

The normative core does not depend on a specific company, industry, product, cloud, AI provider, software stack, or consulting engagement ([`STANDARD.md`](STANDARD.md) §13, [`SCOPE.md`](SCOPE.md)), and it promotes no vendor. Illustrations use abstract scenarios ([`validation/ABSTRACT_SCENARIOS.md`](validation/ABSTRACT_SCENARIOS.md)).

Do not add named company or project examples to the normative core. Worked examples live only in [`examples/`](examples/); they are fictional, built on an abstract scenario, and marked informative.

Real implementations belong outside the core methodology ([`SCOPE.md`](SCOPE.md) §3, [`EXTENSION_MODEL.md`](EXTENSION_MODEL.md)) and may only be used to test whether the method generalizes.

## Licensing of contributions

AITM-SMB is licensed under the [MIT License](LICENSE). Contributions are accepted under the same license (inbound = outbound). By opening a pull request you confirm that you have the right to submit the work under it. There is no separate contributor agreement.

## Conduct and security

Participation follows the [Code of Conduct](CODE_OF_CONDUCT.md). Report security or agent-safety problems privately as described in [`SECURITY.md`](SECURITY.md), not in a public issue.
