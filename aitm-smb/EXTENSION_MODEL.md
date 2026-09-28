# AITM-SMB Extension Model

Framework governance ([`NORMATIVE_INDEX.md`](NORMATIVE_INDEX.md)). Versioning: [`VERSIONING.md`](VERSIONING.md).

## 1. Purpose

AITM-SMB Core remains domain-neutral ([`STANDARD.md`](STANDARD.md) §13).

Domain, industry, regulatory, and technical specialization belongs in Extensions.

---

## 2. Extension types

The named domains, regulations, and technologies below are illustrative extension targets, not endorsements or core dependencies.

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
AI regulation (e.g. EU AI Act)
operational-resilience regulation (e.g. DORA)
financial controls
privacy
sector-specific governance
```

### Technology Extension

Examples:

```text
cloud-platform implementation guide
AI-provider implementation guide
agent-framework implementation guide
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

It MUST NOT redefine, repurpose, or weaken:

```text
any stable item in PUBLIC_API.md §1–§8
  (objects incl. Outcome, Capability, Gap, Intervention, Initiative, Evidence;
   identifiers; core trace; profiles; intervention families; autonomy levels;
   agent statuses)
the invariants (STANDARD.md §3)
traceability rules (TRACEABILITY.md)
the human decision gates (STANDARD.md §8)
```

Extensions do not define Application Profiles; "profile" is reserved ([`SCOPE.md`](SCOPE.md) §3).

Names:

- Record ID prefixes added by an extension MUST NOT reuse a prefix registered in [`ontology/ONTOLOGY.md`](ontology/ONTOLOGY.md) (all are reserved, [`PUBLIC_API.md`](PUBLIC_API.md) §3). Declare them in `id_prefixes`. A core MINOR release can register new prefixes ([`VERSIONING.md`](VERSIONING.md) §3); on a collision, the extension MUST rename its prefix. Check an engagement that uses them with `python3 tools/validate.py --engagement <dir> --extra-prefixes <ABC,XYZ>`.
- Extension skills MUST NOT reuse core skill numbers ([`skills/INDEX.md`](skills/INDEX.md)) and SHOULD carry the extension name (e.g. `<extension>-<slug>`).
- Extension artifact types MUST NOT reuse a core `artifact_type` ([`artifacts/INDEX.md`](artifacts/INDEX.md)) and SHOULD carry the extension name.

---

## 4. Extension manifest

```yaml
extension:
  name:
  version:
  compatible_aitm_version:    # range, e.g. ">=1.1.0 <2.0.0" (VERSIONING.md)
  type:                       # domain | regulatory | technology | operating
  adds_modules: []
  adds_skills: []
  adds_artifacts: []
  adds_controls: []
  id_prefixes: []
  conflicts: []
```

---

## 5. Where extensions live

An extension lives outside the AITM root, in its own repository or directory ([`SCOPE.md`](SCOPE.md) §3), with its manifest at its root. It does not modify files in the AITM root; it references them by AITM-root-relative path.

Informative crosswalks are not extensions: [`docs/crosswalk-agentic-product-standard.md`](docs/crosswalk-agentic-product-standard.md) maps AITM-SMB terms to a related standard and adds no rules.

---

## 6. Core protection

If an extension requires changing core semantics, that is a proposal for a new AITM-SMB version, not an extension.
