# AITM-SMB Agent Output Standard

**Version:** 1.0.0

Substantial skill execution SHOULD emit:

```yaml
aitm_output:
  framework_version: 1.0.0
  profiles: []
  skill:
  status:
  artifacts_changed: []
  trace:
    outcomes: []
    capabilities: []
    states: []
    gaps: []
    hypotheses: []
    interventions: []
    initiatives: []
    metrics: []
    evidence: []
  assumptions: []
  decisions_needed: []
  evidence_debt: []
  risks: []
  next_skill:
```

Allowed status values:

```text
COMPLETE
PARTIAL
BLOCKED
HUMAN_DECISION_REQUIRED
INSUFFICIENT_EVIDENCE
```

Agents SHOULD use stable identifiers and references rather than repeat upstream artifact content.
