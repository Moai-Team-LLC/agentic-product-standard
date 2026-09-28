# AITM-SMB Versioning Policy

Framework governance (`NORMATIVE_INDEX.md`). Compatibility promise: `PUBLIC_API.md` §9.

## 1. Version format

AITM-SMB uses semantic versioning:

```text
MAJOR.MINOR.PATCH
```

---

## 2. Major version

Increment MAJOR when:

```text
core ontology changes incompatibly
canonical method flow changes materially
required traceability changes
artifact semantics become incompatible
skill contracts require migration
a stable PUBLIC_API.md item changes meaning or is removed
a value is added to an enumeration agents must handle exhaustively
  (agent statuses PUBLIC_API.md §8, autonomy levels §7)
```

Example:

```text
1.x → 2.0
```

---

## 3. Minor version

Increment MINOR when:

```text
new module added
new skill added
new artifact added
new optional control or field added
diagnostic/design method expanded compatibly
new identifier prefix registered (ontology/ONTOLOGY.md)
new intervention family or subtype added
field renamed to match its canonical record contract (§9)
```

---

## 4. Patch version

Increment PATCH when:

```text
clarification
typo
non-semantic restructuring
example improvement
non-breaking agent instruction correction
```

---

## 5. Deprecated content

A deprecated file keeps its path and carries in its frontmatter:

```yaml
status: deprecated
deprecated_since:        # version, e.g. 0.7.0
replacement: []          # AITM-root-relative paths
removal_target:          # next MAJOR, e.g. 2.0.0
```

Deprecated artifact contracts MUST carry all four; other deprecated files SHOULD. Redirect guidance stays for the whole major line (`PUBLIC_API.md` §9); removal happens no earlier than `removal_target`.

---

## 6. Compatibility

Skills and artifacts declare the framework version they target:

```yaml
# skill frontmatter (skills/_SKILL_TEMPLATE.md)
framework: AITM-SMB
version: 1.1.0                     # the skill's own version
minimum_framework_version: 1.1.0   # oldest framework version the skill works with

# artifact contract frontmatter (artifacts/_ARTIFACT_CONTRACT.md)
framework_version: 1.1.0

# extension manifest (EXTENSION_MODEL.md §4)
compatible_aitm_version: ">=1.1.0 <2.0.0"
```

Engagement records carry the framework version they were produced under (`artifact` block, `aitm_output`, `conformance`).

---

## 7. Stable identifiers

Entity IDs such as:

```text
OUT-###
CAP-###
GAP-###
INT-###
INI-###
MET-###
```

must remain stable across document revisions.

Framework version changes do not invalidate engagement identifiers.

Full registry and rules: `ontology/ONTOLOGY.md`; stable subset: `PUBLIC_API.md` §3.

---

## 8. Version alignment

`MANIFEST.md` `framework.version` is the release version. These MUST equal it:

```text
every **Version:** header
framework_version in every canonical artifact contract
version in CITATION.cff
the current version named in README.md
```

CHANGELOG.md MUST have a section for it. Skill `minimum_framework_version` MUST NOT exceed it. `python3 tools/validate.py` checks all of this.

---

## 9. Field renames in a MINOR release

A MINOR release MAY rename a field only to align it with its canonical record contract (`CANONICAL_CONCEPTS.md`). Each rename is listed in the migration table of the release notes (`releases/<version>.md`, linked from `CHANGELOG.md`): record, old name, new name. No alias fields are kept; the table is the compatibility path. Meanings of `PUBLIC_API.md` items never change in a MINOR release.

---

## 10. Release tags

```text
inside the host repository   aitm-smb-vX.Y.Z
standalone (after a split)   vX.Y.Z
```

The tag MUST match `MANIFEST.md`. Pushing it publishes a GitHub release whose notes are the matching CHANGELOG.md section and which attaches the Core and Full distributions (`tools/build_dist.py`, `NORMATIVE_INDEX.md` §Distributions). Release procedure: `MAINTENANCE.md` §2.

---

## 11. Current stable major

`1.x`
