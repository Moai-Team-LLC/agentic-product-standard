# Intervention Patterns

Canonical definitions of the intervention families. The identifiers are the stable tokens of `PUBLIC_API.md` §6; an Intervention's `type` (`CORE_MODEL.md` §6) is exactly one of them.

INV-05 (`STANDARD.md` §3) names the kinds of change; these families make them selectable. Challenge order over the families: `STANDARD.md` §5 (questions: `DECISION_MODEL.md` §1).

## 1. Rules

- Extensions MAY add subtypes but MUST NOT redefine these semantics (`PUBLIC_API.md` §6).
- Choose the family by what the Intervention primarily changes. Describe secondary changes in `description`. Split the Intervention when its parts can be selected independently.
- An `AI_*` family names the kind of AI contribution; authority is set only by the autonomy level (`diagnostics/AUTONOMY_SUITABILITY.md` §2), assessed per action class in an Autonomy Assessment (`artifacts/autonomy-assessment.md`).
- Every `AI_*` candidate needs an AI Suitability Assessment and an Autonomy Assessment before prioritization (`methodology/03-intervention-design.md`).

1.0 headings renamed in 1.1: Automate is `AUTOMATION`, Reallocate Authority is `DECISION`, Redesign Role is `ROLE`, Build Feedback Loop is `FEEDBACK`.

---

## 2. ELIMINATE

Remove work that should not exist.

Typical triggers:

```text
duplicate approval
unused report
manual reconciliation caused by bad system boundary
redundant data entry
```

---

## 3. SIMPLIFY

Reduce steps, rules, or decision complexity.

---

## 4. STANDARDIZE

Make recurring work explicit and consistent.

Useful before automation or AI.

---

## 5. INSTRUMENT

Add measurement where the system is currently opaque.

---

## 6. INTEGRATE

Remove fragmentation between systems or information sources.

---

## 7. PROCESS

Redesign a Process (`ontology/ONTOLOGY.md`): its sequence, handoffs, or coordination, where eliminating, simplifying, or standardizing steps is not enough.

---

## 8. ROLE

Change a human responsibility, for example after automation or AI takes over part of the work (`change/ROLE_TRANSITION_MODEL.md`).

---

## 9. DECISION

Change who or what is allowed to decide: the Decision Rights over a business decision (`design/DECISION_RIGHTS_ARCHITECTURE.md`).

Moving a decision to AI is also an authority increase: its level is the autonomy level (§1), granted only through `HG-AUTHORITY` (`STANDARD.md` §8).

---

## 10. DATA

Create, correct, or govern a Data Asset (`ontology/ONTOLOGY.md`): its structure, quality, ownership, or availability.

---

## 11. KNOWLEDGE

Capture, consolidate, or maintain a Knowledge Asset (`ontology/ONTOLOGY.md`): the rules, expertise, documents, or context required for competent action (`design/INFORMATION_KNOWLEDGE_ARCHITECTURE.md`).

---

## 12. SOFTWARE

Change Application behavior (`ontology/ONTOLOGY.md`) other than integration (`INTEGRATE`) or deterministic automation (`AUTOMATION`): functions, interfaces, validation, or system responsibilities (`design/APPLICATION_BOUNDARIES.md`).

---

## 13. AUTOMATION

Deterministic automation: use predefined logic for repetitive bounded work.

---

## 14. AI_ASSIST

AI improves human cognition or execution.

---

## 15. AI_AUTOMATE

AI completes a bounded probabilistic task inside a controlled workflow.

---

## 16. AI_AUGMENT

AI changes the capability by providing continuous intelligence, prediction, retrieval, or recommendation.

---

## 17. AI_AUTONOMIZE

AI pursues a bounded objective with tools, within the authority its autonomy level grants.

Requires explicit autonomy assessment. The family grants no authority by itself (§1).

---

## 18. CONTROL

Add or change a Control (`ontology/ONTOLOGY.md`): a mechanism constraining risk, authority, access, or behavior.

---

## 19. FEEDBACK

Connect outcome evidence back to operational behavior.

---

## 20. Pattern sequencing

The default challenge against premature AI complexity is the challenge order in `STANDARD.md` §5. It is a challenge heuristic, not a required sequence.

Increase autonomy only when justified, after evidence: `governance/AUTHORITY_ESCALATION_MODEL.md`.
