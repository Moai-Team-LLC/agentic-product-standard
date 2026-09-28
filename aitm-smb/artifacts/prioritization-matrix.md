---
artifact_type: prioritization-matrix
framework_version: 1.1.0
status: canonical
owner_module: methodology/04-prioritization.md
produced_by: [05-prioritize-initiatives]
---

# Prioritization Matrix

## Purpose

Select transformation Initiatives from candidate Interventions based on explicit trade-offs, and record the decision on every candidate.

## Record

For each candidate:

```yaml
candidate:
  intervention_ids: []        # INT-### assessed together as one candidate
  initiative_id:              # INI-###, created when decision is select (CORE_MODEL.md §7)
  assessment: {}              # dimension → {value, rationale}; ordinal values, only the dimensions used
  decision: select | defer | reject | investigate
  rationale:
  evidence_ids: []
  assumption_ids: []
  major_risks:                # material ones also as Risk records (RSK-###, artifacts/decision-assumption-log.md)
  human_decision_owner:
  decision_id:                # DEC-### recording the selection; closes HG-INITIATIVE when material
```

Dimensions (`assessment` keys):

```text
Business Value            cite the economic hypothesis where one exists (economics/TRANSFORMATION_ECONOMICS.md §5)
Strategic Relevance
Frequency / Volume
Evidence Strength
Data / Knowledge Readiness
Implementation Complexity
Change Burden
Operational Risk
Reversibility
Time to Evidence
Constraint Relevance      where a System Constraint exists (design/CONSTRAINT_ANALYSIS.md §6)
portfolio criteria        Portfolio profile (portfolio/PORTFOLIO_PRIORITIZATION.md §2)
```

## Rules

AITM-SMB does not require a universal weighted formula.

Every material candidate carries an economic hypothesis (`economics/TRANSFORMATION_ECONOMICS.md` §5) before `HG-BUDGET`; its Business Value rationale cites it.

A numeric score MAY support discussion but MUST NOT conceal judgment.

`investigate` means the evidence is insufficient to decide; the rationale names the Evidence Debt or Experiment that will resolve it.

## Validation

- [ ] every candidate names its Interventions and a `decision` with written rationale
- [ ] assessed dimensions carry ordinal values with rationale; no score replaces judgment
- [ ] every `select` has an Initiative record (`initiative_id`) and, when material, an approved `HG-INITIATIVE` Decision (`decision_id`)
- [ ] every `investigate` names the Evidence Debt or Experiment that resolves it
- [ ] before `HG-BUDGET`, every material candidate has an economic hypothesis, cited in its Business Value rationale
- [ ] Constraint Relevance assessed where a System Constraint exists; Portfolio: stop condition checked (`portfolio/PORTFOLIO_PRIORITIZATION.md` §5)
