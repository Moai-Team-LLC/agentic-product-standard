---
artifact_type: template
framework_version: 1.1.0
status: canonical
---

# AITM-SMB Artifact Contract

Defines the shape of every artifact contract in `artifacts/`, the metadata of every engagement instance, and where instances live. Registry: `artifacts/INDEX.md`.

## 1. Single-record rule

Each record shape is defined exactly once; `CANONICAL_CONCEPTS.md` names where.

Modules own meaning and rules; the record contract owns field names.

Files that hold instances reference the record contract and MAY add fields only where they say so explicitly ("extends <record> with: …").

An artifact contract whose records are defined elsewhere writes "Record contract: `<path>` §n" and lists only its extension fields; it does not restate the record.

---

## 2. Contract frontmatter

```yaml
---
artifact_type:            # file stem
framework_version: 1.1.0
status: canonical         # or deprecated
entity:                   # only when the primary record is a registered entity
id_prefix:                # only with entity; registered in ontology/ONTOLOGY.md
owner_module:             # module that owns the semantics; omit for core-only records
produced_by: []           # skill directory names
---
```

`status` is the registry status of the contract, not the lifecycle of an instance (§4) or of a record (its record contract).

`produced_by`, the "Produced by" column of `artifacts/INDEX.md`, and the skills whose `## Produces` names the contract MUST be the same set. Orchestrators are listed where they write records directly or merge specialist output. A skill MAY also append to a contract it does not name in `## Produces` where the contract's prose allows it (Evidence, Evidence Debt, Assumptions, Metric records: `skills/INDEX.md` §4; gate Decisions: `STANDARD.md` §8); such skills are not listed.

A deprecated contract keeps its path and adds `deprecated_since`, `replacement` and `removal_target: 2.0.0` (`VERSIONING.md` §5).

---

## 3. Contract body

```text
# <Title>
## Purpose               1–3 sentences
## Record                YAML; or "Record contract: <path> §n" plus any explicit extension fields
## Rules                 optional
## Required questions    optional
## Validation            3–7 checkbox lines, derived from the owning module; no new semantics
```

A deprecated stub keeps its title and redirect text.

---

## 4. Instance metadata

Defined only here; contracts do not repeat it.

Every engagement instance file SHOULD start with:

```yaml
artifact:
  type:                   # artifact_type of the contract; a list when contracts are merged
  id:                     # file identifier (free text); record IDs belong to the records
  framework_version: 1.1.0
  status: draft | reviewed | approved | superseded
  owner:
  upstream: []
  downstream: []
  evidence: []            # EVD-###
  assumptions: []         # ASM-###, HYP-###
  decisions: []           # DEC-###
  open_questions: []
```

`artifact.status` is the instance lifecycle. Record `status` values follow each record contract; any record MAY also be `superseded` (`ontology/ONTOLOGY.md`).

An AI-generated artifact is not approved merely because it exists. `status: approved` alone is not approval: gated content is approved only by a Decision (`AGENTS.md` §4, `STANDARD.md` §8).

Where relevant, an instance also covers: purpose and scope; inputs; the records; Evidence; Assumptions / Hypotheses; Decisions; Open Questions; validation result; change history.

---

## 5. Provenance of material claims

Any record MAY carry, for a material claim, even where its record contract does not list them:

```yaml
evidence_ids: []          # EVD-###
assumption_ids: []        # ASM-###
confidence: low | medium | high
```

This is the explicit extension §1 requires; contracts need not repeat it. Inline text uses the `AGENTS.md` §3 labels. Missing links: `TRACEABILITY.md` §4.

---

## 6. Engagement workspace

The engagement workspace is the location, outside the AITM root, where one engagement's instances are written: filled artifacts, Evidence, Decisions, and the conformance declaration. Instances are never written into the AITM root; `artifacts/` holds contracts only. Loading and data handling: `AGENT_CONTEXT_POLICY.md`.

The layout is free. A common one is one directory per engagement with one file per contract, named by `artifact_type`. `python3 tools/validate.py --engagement <dir>` checks its trace integrity.

---

## 7. Merging and splitting

Contracts MAY be merged into fewer instance files, or split (`CONFORMANCE.md` §4, `MINIMUM_ARTIFACT_SET.md` §3–§4), as long as each record keeps its ID and its record type stays identifiable (its YAML key, e.g. `gap:`, or a section heading).

ID format, uniqueness and supersession: `ontology/ONTOLOGY.md`.
