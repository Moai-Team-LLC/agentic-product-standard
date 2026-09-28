# AITM-SMB Scope

## 1. Methodology boundary

AITM-SMB is a domain-neutral methodology for AI transformation of small and medium-sized businesses.

The core methodology MUST NOT depend on a specific company, industry, product, cloud, AI provider, software stack, or consulting engagement ([`STANDARD.md`](STANDARD.md) §13).

## 2. Normative core

The normative core is the Canonical Core ([`MANIFEST.md`](MANIFEST.md) `canonical_core`) plus the registered modules, artifact contracts, and skills; precedence: [`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md).

It defines:

```text
principles
ontology
method phases
artifact contracts
agent skills
decision gates
evaluation rules
governance rules
```

These elements must remain reusable across domains.

## 3. Non-normative extensions

Industry-specific or company-specific applications MAY exist outside the core repository as:

```text
adapters/
implementation-guides/
conformance-cases/
```

Such extensions MUST NOT redefine core concepts or phases. See [`EXTENSION_MODEL.md`](EXTENSION_MODEL.md).

"Profile" is reserved for the Application Profiles ([`APPLICATION_PROFILES.md`](APPLICATION_PROFILES.md)); extensions do not define profiles.

## 4. Validation without case dependence

The methodology should be validated through abstract scenarios and invariants rather than through named real projects ([`validation/ABSTRACT_SCENARIOS.md`](validation/ABSTRACT_SCENARIOS.md)).

Preferred:

```text
"a service business with a high manual qualification load"
"a product company with fragmented customer knowledge"
"a professional firm with expert-dependent delivery"
```

Avoid making named organizations or internal projects canonical examples.

A worked example MAY ship in [`examples/`](examples/) when it is fictional, built on an abstract scenario, and marked informative (e.g. [`examples/compact-scenario-b/`](examples/compact-scenario-b/)).

## 5. Design rule

If a concept only makes sense for one project, industry, or technology stack, it does not belong in the AITM-SMB core.
