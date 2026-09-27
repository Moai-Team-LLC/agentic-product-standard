# AITM-SMB Agent Diagnostic Protocol

## 1. Purpose

This protocol defines how an AI agent performs diagnosis without inventing organizational reality.

---

## 2. Diagnostic sequence

An agent MUST follow:

```text
1. Extract evidence
2. Extract observations
3. Identify symptoms
4. Link symptoms to Outcomes
5. Identify affected Capabilities
6. Describe Current State
7. Define required behavior
8. Form Gaps
9. Generate competing cause hypotheses
10. Test hypotheses against evidence
11. Mark confidence
12. Only then generate intervention candidates
```

---

## 3. Competing hypothesis rule

For every material Gap, generate at least two plausible cause hypotheses unless evidence makes alternatives unreasonable.

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

Before recommending AI ask:

```text
Can this be eliminated?
Can this be simplified?
Can this be standardized?
Can deterministic automation solve it?
What specifically requires probabilistic intelligence?
```

---

## 6. Autonomy challenge

Before recommending agentic execution ask:

```text
Why is assistance insufficient?
Why is explicit approval insufficient?
What is the maximum safe authority?
How is failure detected?
How is action recovered?
```

---

## 7. Agent output structure

```yaml
diagnosis:
  observations: []
  symptoms: []
  affected_outcomes: []
  affected_capabilities: []
  gaps: []
  cause_hypotheses: []
  validated_causes: []
  evidence_gaps: []
  intervention_candidates: []
  unresolved_questions: []
```

---

## 8. Prohibited behavior

The agent MUST NOT:

- infer a root cause from one interview statement without labeling it a hypothesis;
- treat a stakeholder request for a tool as proof of need;
- infer ROI without visible assumptions;
- infer authority from technical access;
- infer process correctness from documentation alone;
- declare AI fit without considering deterministic alternatives.
