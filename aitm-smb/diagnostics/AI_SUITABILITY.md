# AI Suitability Assessment

## 1. Purpose

AITM-SMB does not ask:

```text
Where can we use AI?
```

It asks:

```text
Where does probabilistic intelligence create more value
than process redesign, deterministic software, or automation?
```

---

## 2. Suitability dimensions

Assess each candidate Intervention of an `AI_*` type (`PUBLIC_API.md` §6) across:

```text
Semantic Load
Input Variability
Judgment Requirement
Knowledge Intensity
Interaction Requirement
Prediction Requirement
Generation Requirement
Tolerance for Probabilistic Output
Verification Feasibility
Error Recoverability
Context Availability
Data Sensitivity
Execution Risk
Economic Frequency
```

Rate each dimension `low | medium | high` with a short note; mark a dimension that does not apply as not relevant, with the reason. Each dimension has one field in the record (§6).

---

## 3. AI-positive signals

AI becomes more suitable when work requires:

```text
interpretation of unstructured input
semantic matching
classification under ambiguity
summarization
generation
natural-language interaction
knowledge retrieval
pattern recognition
contextual recommendations
prediction
reasoning across heterogeneous information
```

---

## 4. AI-negative signals

Prefer deterministic logic when work requires:

```text
exact arithmetic
strict rule execution
schema validation
known routing logic
transaction consistency
simple transformation
fully predictable output
```

---

## 5. AI suitability classes

### A — Strong AI Fit

AI is central to solving the Gap.

### B — Hybrid Fit

AI adds material value but deterministic logic remains substantial.

### C — Optional AI

AI may improve experience or efficiency but is not structurally necessary.

### D — Weak AI Fit

AI adds complexity without enough value.

### E — AI Contraindicated

Risk, determinism requirements, or verification limits make AI unsuitable.

### What each class implies for selection

- A — AI MAY be selected. Authority is assessed separately (`diagnostics/AUTONOMY_SUITABILITY.md`).
- B — AI MAY be selected for the part that needs it; the rest uses deterministic logic. Authority is assessed separately.
- C — AI MAY be selected only with a recorded rationale for why it beats the non-AI alternative; otherwise select the non-AI alternative.
- D — AI SHOULD NOT be selected; selecting it requires an explicit, recorded justification (`STANDARD.md` §17).
- E — AI MUST NOT be selected. Record the candidate as a rejected Intervention with the classification as its rationale.

A class is a finding about fit, not an approval. Interventions are selected in Phase 4 (material selection: `HG-INITIATIVE`); AI authority above L0 needs `HG-AUTHORITY` (`STANDARD.md` §8).

---

## 6. Assessment record

Record contract: `artifacts/ai-suitability-assessment.md`.

---

## 7. Hard rule

An AI intervention MUST NOT be selected only because:

```text
AI is fashionable
a vendor offers the feature
the model can technically perform the task
competitors mention AI
```
