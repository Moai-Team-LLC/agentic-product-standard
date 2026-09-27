---
artifact_type: transformation-intent
framework_version: 1.0.0
status: canonical
---

# Transformation Intent

## Purpose

Define the transformation problem before designing solutions.

## Required content

```yaml
artifact:
  type: transformation-intent
  id: ATI-###
  status: draft | reviewed | approved

intent:
  problem_statement:
  business_context:
  outcome_ids: []
  owner:
  horizon:
  constraints: []
  non_goals: []
  known_risks: []
```

## Required questions

1. What business result must change?
2. Why now?
3. What evidence shows the current state?
4. Who owns the result?
5. What is explicitly out of scope?
6. What constraints cannot be ignored?

## Invalid completion

This artifact is incomplete if the stated goal is only:

```text
introduce AI
automate processes
build agents
increase AI adoption
```
