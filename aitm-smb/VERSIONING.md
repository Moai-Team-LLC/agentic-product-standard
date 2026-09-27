# AITM-SMB Versioning Policy

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
new optional control added
diagnostic/design method expanded compatibly
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

Deprecated files SHOULD contain:

```yaml
status: deprecated
deprecated_since:
replacement:
removal_target:
```

---

## 6. Compatibility

Skills and artifacts SHOULD declare the minimum compatible framework version.

Example:

```yaml
framework: AITM-SMB
minimum_version: 1.0.0
```

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


## Current stable major

`1.x`
