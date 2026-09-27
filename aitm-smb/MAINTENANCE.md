# AITM-SMB Repository Maintenance

## 1. Purpose

AITM-SMB is agent-readable.

Documentation drift is therefore a methodology defect.

---

## 2. Repository maintenance rules

Every release SHOULD verify:

```text
all normative links resolve
all skill references resolve
all artifact references resolve
no duplicate canonical definition exists
deprecated rules are marked
MANIFEST version matches release
CHANGELOG updated
```

---

## 3. Single-definition rule

A core concept SHOULD have one canonical definition.

Other files SHOULD reference it.

Examples:

```text
Capability → ontology/ONTOLOGY.md + CORE_MODEL.md
Traceability → TRACEABILITY.md
AI Suitability → diagnostics/AI_SUITABILITY.md
Autonomy → diagnostics/AUTONOMY_SUITABILITY.md
Transition State → transition/TRANSITION_STATE_MODEL.md
```

---

## 4. Duplication classes

### Acceptable duplication

Short reminders or summaries.

### Dangerous duplication

Two normative definitions that may diverge.

Dangerous duplication SHOULD be removed or replaced with links.

---

## 5. Release audit

Before a 1.0 release perform:

```text
semantic consistency audit
broken-reference audit
duplicate-definition audit
profile completeness audit
skill dependency audit
artifact completeness audit
```
