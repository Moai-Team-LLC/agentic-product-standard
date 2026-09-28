# AITM-SMB Decision Model

**Version:** 1.1.0

AITM-SMB separates three decisions:

```text
1. Should the Capability change?
2. Should AI be part of that change?
3. If AI is used, what authority should it receive?
```

These decisions MUST NOT be collapsed into one.

---

## 1. Intervention challenge

For a diagnosed Gap, evaluate in this order (challenge order: `STANDARD.md` §5; families: `design/INTERVENTION_PATTERNS.md`):

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

Autonomy levels L0–L5 (labels and authority per level): `diagnostics/AUTONOMY_SUITABILITY.md` §2.

Authority is a business architecture decision, not a technical consequence.

Before recommending autonomy, ask:

```text
Why is assistance insufficient?
Why is explicit approval insufficient?
What is the maximum safe authority (Authority Ceiling)?
How is authority bounded?
How is failure detected?
How is action recovered?
```

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

Granting such permission to AI is an authority increase (HG-AUTHORITY, `STANDARD.md` §8).

---

## 5. Decision record

Material decisions SHOULD be recorded as Decisions (`DEC-###`). Record contract: `artifacts/decision-assumption-log.md`.

`DEC-###` records engagement decisions about the transformation. Decision rights over operational business decisions are `BDS-###` (`design/DECISION_RIGHTS_ARCHITECTURE.md`).
