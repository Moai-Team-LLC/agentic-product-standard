# AITM-SMB Decision Model

**Version:** 1.0.0

AITM-SMB separates three decisions:

```text
1. Should the Capability change?
2. Should AI be part of that change?
3. If AI is used, what authority should it receive?
```

These decisions MUST NOT be collapsed into one.

---

## 1. Intervention challenge

For a diagnosed Gap, evaluate in this order:

```text
Can the work be eliminated?
Can the system be simplified?
Can the work be standardized?
Is missing measurement the real problem?
Can systems/information be integrated?
Can deterministic automation solve it?
Does probabilistic AI add material value?
Does autonomy add material value beyond assistance?
```

---

## 2. AI suitability

AI becomes more suitable when work depends on:

```text
unstructured information
semantic interpretation
generation
classification under ambiguity
prediction
knowledge retrieval
contextual reasoning
natural-language interaction
```

AI becomes less suitable when work requires:

```text
exact arithmetic
strict deterministic rules
transaction consistency
simple validation
fully reproducible output
```

Detailed assessment: `diagnostics/AI_SUITABILITY.md`.

---

## 3. Autonomy

```text
L0 No AI
L1 Suggest
L2 Draft
L3 Execute with approval
L4 Execute within bounded policy
L5 Pursue bounded objective
```

Authority is a business architecture decision, not a technical consequence.

Detailed assessment: `diagnostics/AUTONOMY_SUITABILITY.md`.

---

## 4. Human authority rule

A system being technically capable of:

```text
send
approve
price
refund
publish
delete
purchase
commit
```

does not grant permission to do so.

---

## 5. Decision record

Material decisions SHOULD record:

```yaml
decision:
  id: DEC-###
  statement:
  owner:
  alternatives: []
  rationale:
  evidence_ids: []
  assumptions: []
  consequences: []
  review_trigger:
```
