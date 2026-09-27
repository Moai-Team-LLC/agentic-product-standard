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

Assess each candidate intervention across:

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

---

## 6. Assessment contract

```yaml
ai_suitability:
  intervention_id:
  semantic_load:
  input_variability:
  judgment_requirement:
  knowledge_intensity:
  probabilistic_tolerance:
  verification_feasibility:
  recoverability:
  context_readiness:
  risk:
  economics:
  classification: A | B | C | D | E
  rationale:
  non_ai_alternative:
```

---

## 7. Hard rule

An AI intervention MUST NOT be selected only because:

```text
AI is fashionable
a vendor offers the feature
the model can technically perform the task
competitors mention AI
```
