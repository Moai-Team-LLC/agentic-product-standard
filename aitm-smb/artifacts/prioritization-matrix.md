---
artifact_type: prioritization-matrix
framework_version: 1.0.0
status: canonical
---

# Prioritization Matrix

## Purpose

Select transformation initiatives based on explicit trade-offs.

## Evaluation dimensions

Use ordinal values with written rationale:

```text
Business Value
Strategic Relevance
Frequency / Volume
Evidence Strength
Data / Knowledge Readiness
Implementation Complexity
Change Burden
Operational Risk
Reversibility
Time to Evidence
```

## Rule

AITM-SMB does not require a universal weighted formula.

A numeric score MAY support discussion but MUST NOT conceal judgment.

## Required output

For each candidate:

```yaml
candidate:
  intervention_ids: []
  decision: select | defer | reject | investigate
  rationale:
  evidence:
  assumptions:
  major_risks:
  human_decision_owner:
```
