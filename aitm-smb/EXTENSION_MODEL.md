# AITM-SMB Extension Model

## 1. Purpose

AITM-SMB Core remains domain-neutral.

Domain, industry, regulatory, and technical specialization belongs in Extensions.

---

## 2. Extension types

### Domain Extension

Examples:

```text
professional services
retail
manufacturing
health operations
financial services
community networks
```

### Regulatory Extension

Examples:

```text
EU AI Act
DORA
financial controls
privacy
sector-specific governance
```

### Technology Extension

Examples:

```text
AWS implementation profile
GCP implementation profile
Azure implementation profile
OpenAI implementation profile
Anthropic implementation profile
```

### Operating Extension

Examples:

```text
high-volume support
knowledge-intensive delivery
agentic back office
```

---

## 3. Extension rule

An Extension MAY:

```text
add artifacts
add controls
add skills
add evaluation criteria
add reference architectures
add constraints
```

It MUST NOT redefine:

```text
Outcome
Capability
Gap
Intervention
Initiative
Evidence
Traceability
Human Decision Gates
```

---

## 4. Extension manifest

```yaml
extension:
  name:
  version:
  compatible_aitm_version:
  type:
  adds_modules: []
  adds_skills: []
  adds_artifacts: []
  adds_controls: []
  conflicts: []
```

---

## 5. Core protection

If an extension requires changing core semantics, that is a proposal for a new AITM-SMB version, not an extension.
