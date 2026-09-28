# Transformation Economics

## 1. Purpose

AITM-SMB treats economics as part of architecture.

A technically successful transformation that destroys unit economics is not successful.

---

## 2. Economic lenses

Evaluate:

```text
Current cost
Implementation cost
Operating cost
AI inference cost
Human oversight cost
Failure cost
Delay cost
Opportunity cost
Switching cost
Lock-in cost
```

---

## 3. Economic value classes

Transformation value may come from:

```text
revenue growth
margin improvement
capacity creation
cycle-time reduction
error reduction
risk reduction
retention improvement
working-capital improvement
management leverage
knowledge retention
```

---

## 4. Cost-per-successful-outcome

For AI-enabled capabilities prefer:

```text
cost per successful business outcome
```

over:

```text
cost per token
cost per model call
```

Example:

```text
total operating cost of support capability
/
successfully resolved customer issues
```

---

## 5. Economic hypothesis

```yaml
economic_hypothesis:
  initiative_id:        # INI-###, set when the Initiative is selected (Phase 4)
  intervention_ids: []  # INT-### it concerns before an Initiative exists
  current_cost:
  expected_future_cost:
  expected_value:       # estimate and its §3 value class(es)
  implementation_cost:
  operational_cost:
  key_assumptions: []   # ASM-###
  downside_case:
  evidence_needed:
  metric_ids: []        # Economic Metrics (METRICS.md §8) that will test it, preferably cost per successful outcome (§4)
```

Use across the lifecycle:

```text
Phase 3  economic assumptions of candidate Interventions (ASM-###)
Phase 4  economic hypothesis of each material candidate, prepared before HG-BUDGET
Phase 8  hypothesis evaluated against measured cost and value
```

Before `HG-BUDGET` (`STANDARD.md` §8), every material candidate carries an economic hypothesis. The Decision closing `HG-BUDGET` cites it: the `INI-###` or `INT-###` it concerns in `subject_ids`, its `key_assumptions` in `assumption_ids`, and its `downside_case` in `rationale`.

---

## 6. Rule

AITM-SMB does not require precise ROI when uncertainty is high.

It requires economic assumptions to be visible.
