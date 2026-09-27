# AITM-SMB Scope

## 1. Methodology boundary

AITM-SMB is a domain-neutral methodology for AI transformation of small and medium-sized businesses.

The core methodology MUST NOT depend on:

- a specific company;
- a specific industry;
- a specific product;
- a specific cloud;
- a specific AI vendor;
- a specific software stack;
- a specific consulting engagement.

## 2. Normative core

The normative core defines:

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
profiles/
implementation-guides/
conformance-cases/
```

Such extensions MUST NOT redefine core concepts or phases.

## 4. Validation without case dependence

The methodology should be validated through abstract scenarios and invariants rather than through named real projects.

Preferred:

```text
"a service business with a high manual qualification load"
"a product company with fragmented customer knowledge"
"a professional firm with expert-dependent delivery"
```

Avoid making named organizations or internal projects canonical examples.

## 5. Design rule

If a concept only makes sense for one project, industry, or technology stack, it does not belong in the AITM-SMB core.
