# AITM-SMB Agent Diagnostic Protocol

**Version:** 1.1.0

## 1. Purpose

This protocol defines how an AI agent performs diagnosis without inventing organizational reality.

It applies whenever an agent diagnoses (Phase 2; skills 03, 12, 16). Concepts: `diagnostics/DIAGNOSTIC_MODEL.md`, `diagnostics/ROOT_CAUSE_ANALYSIS.md`. Labels: `AGENTS.md` §3.

---

## 2. Diagnostic sequence

An agent MUST follow:

```text
1. Extract evidence                       EVD records
2. Extract observations
3. Identify symptoms
4. Link symptoms to Outcomes              OUT
5. Identify affected Capabilities         CAP
6. Describe Current State                 STA, type CURRENT
7. Define required behavior
8. Form Gaps                              GAP
9. Generate competing cause hypotheses    HYP, kind: cause, with cause_class
10. Test hypotheses against evidence      evidence_for / evidence_against
11. Mark confidence and status            confidence: low | medium | high
12. Only then generate intervention candidates
```

Confidence describes evidence strength (`diagnostics/DIAGNOSTIC_MODEL.md` §5). Cause classes and the evidence test: `diagnostics/ROOT_CAUSE_ANALYSIS.md`. A Gap is ready for intervention design only when it passes the diagnosis completion test (`diagnostics/DIAGNOSTIC_MODEL.md` §6).

---

## 3. Competing hypothesis rule

For every material Gap, generate at least two plausible cause hypotheses unless evidence makes alternatives unreasonable.

Record each as a Hypothesis record (`artifacts/decision-assumption-log.md`) and link the competitors through `alternative_hypothesis_ids`. When alternatives are unreasonable, record why.

The purpose is to resist premature closure.

---

## 4. Counterfactual challenge

Before accepting a cause ask:

```text
If this cause disappeared tomorrow,
would the Gap materially improve?
```

Before accepting an intervention ask:

```text
If this intervention worked perfectly,
would the Outcome materially improve?
```

If no, revise the model.

---

## 5. AI challenge

Before recommending AI, apply the intervention challenge in `DECISION_MODEL.md` §1.

---

## 6. Autonomy challenge

Before recommending agentic execution, apply the autonomy challenge in `DECISION_MODEL.md` §3.

---

## 7. Agent output

Hand off with the `aitm_output` block (`AGENT_OUTPUT_STANDARD.md`). Diagnostic content is recorded in the engagement's artifacts and referenced by ID:

| Diagnostic content | Recorded in | `aitm_output` |
|---|---|---|
| observations, symptoms | Diagnostic Record (`artifacts/diagnostic-record.md`) | `trace.other_ids` (DIA-###) |
| affected Outcomes | Transformation Intent (Phase 0) | `trace.outcome_ids` |
| affected Capabilities, Current State | Capability Map (Phase 1) | `trace.capability_ids`, `trace.state_ids` |
| Gaps | Capability Diagnosis | `trace.gap_ids` |
| cause hypotheses, validated causes | Hypothesis records; `status` tells them apart | `trace.hypothesis_ids` |
| evidence gaps | Evidence Debt (`evidence/EVIDENCE_STANDARD.md` §5) | `evidence_debt` |
| intervention candidates | Intervention Map (Phase 3) | `trace.intervention_ids` |
| unresolved questions | artifact `open_questions`, labeled `[OPEN]` | `decisions_needed` when a human must answer |

Records marked with another phase are written by that phase's skills (producers: `artifacts/INDEX.md`); diagnosis only references them by ID. A missing or wrong upstream record returns work to its phase (`EXECUTION_MODEL.md` §3).

---

## 8. Prohibited behavior

The agent MUST NOT:

- infer a root cause from one interview statement without labeling it `[HYPOTHESIS]`;
- treat a stakeholder request for a tool as proof of need;
- infer ROI without visible assumptions;
- infer authority from technical access;
- infer process correctness from documentation alone;
- declare AI fit without considering deterministic alternatives;
- mark a Hypothesis `validated` without Evidence recorded in `evidence_for`.
