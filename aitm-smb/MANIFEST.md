# AITM-SMB Manifest

All paths are relative to the AITM root (the directory containing this file).

```yaml
framework:
  name: AITM-SMB
  expansion: AI Transformation Methodology for Small and Medium-Sized Businesses
  version: 1.1.0
  status: stable
  type: open-methodology
  license: MIT                     # LICENSE
  primary_unit: business-capability
  execution_model: artifact-driven
  agent_readable: true

canonical_core:
  - README.md
  - MANIFEST.md
  - STANDARD.md
  - SCOPE.md
  - NORMATIVE_INDEX.md
  - PUBLIC_API.md
  - CANONICAL_CONCEPTS.md
  - CORE_MODEL.md
  - METHOD_FLOW.md
  - TRACEABILITY.md
  - EXECUTION_MODEL.md
  - DECISION_MODEL.md
  - CONFORMANCE.md
  - APPLICATION_PROFILES.md
  - AGENTS.md
  - AGENT_CONTEXT_POLICY.md
  - AGENT_OUTPUT_STANDARD.md
  - ontology/ONTOLOGY.md

registries:
  - MODULE_CATALOG.md
  - artifacts/INDEX.md
  - skills/INDEX.md

distributions:                     # NORMATIVE_INDEX.md; built by tools/build_dist.py
  core:
    - canonical_core
    - registries
    - LICENSE
    - CHANGELOG.md
  full:
    - .                            # the whole AITM root

adapters:
  - SKILL.md                       # Claude Code / Agent Skills router; skill name aitm-smb

normative_keywords:
  MUST: mandatory
  MUST_NOT: prohibited
  SHOULD: recommended_unless_justified
  MAY: optional

core_invariants:                   # STANDARD.md §3
  - INV-01 — Outcome before technology
  - INV-02 — Capability over use case
  - INV-03 — Diagnosis before solution
  - INV-04 — Evidence over assumption
  - INV-05 — AI is optional
  - INV-06 — AI usefulness is separate from AI authority
  - INV-07 — Authority is explicit and revocable
  - INV-08 — Architecture before vendors
  - INV-09 — Optimize the system
  - INV-10 — Transition states are operable
  - INV-11 — Evidence before scale
  - INV-12 — Deployment is not transformation
  - INV-13 — AI quality is not business value
  - INV-14 — Every material decision is traceable
  - INV-15 — Proportionality over bureaucracy

scope_rules:
  - core_is_domain_neutral                   # STANDARD.md §13, SCOPE.md §1
  - engagement_instances_outside_aitm_root   # AGENT_CONTEXT_POLICY.md
```
