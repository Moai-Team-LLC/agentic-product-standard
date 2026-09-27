# AITM-SMB Conformance

**Version:** 1.0.0

Conformance is semantic, not documentary.

---

## 1. Core conformance

An AITM-SMB application MUST:

1. define at least one measurable Outcome;
2. identify the relevant Capability or Capabilities;
3. represent Current State sufficiently for diagnosis;
4. identify a material Gap;
5. distinguish Cause from Symptom;
6. consider non-AI interventions;
7. justify AI where selected;
8. define Capability Target State;
9. connect Initiatives to Gaps and Outcomes;
10. define Metrics and Evidence;
11. define human/AI authority where AI acts;
12. preserve end-to-end traceability.

---

## 2. Non-conforming by themselves

These are not full AITM-SMB applications:

```text
AI maturity survey
AI use-case brainstorm
tool selection
automation backlog
agent architecture
cloud architecture
prompt library
AI policy document
```

They MAY be components inside a conforming application.

---

## 3. Profiles

An application SHOULD declare one or more profiles:

```text
Compact
Standard
Governed
Portfolio
Measured
```

See `APPLICATION_PROFILES.md`.

---

## 4. Artifact proportionality

Conformance does not require one file per artifact contract.

Artifacts MAY be merged or split if:

```text
semantic boundaries remain explicit
stable identifiers remain intact
traceability remains intact
ownership remains clear
agent parsing remains reliable
```

---

## 5. Conformance declaration

```yaml
aitm_conformance:
  framework_version: 1.0.0
  profiles: []
  validated_at:
  unresolved_exceptions: []
```

An AI agent MAY evaluate conformance.

An AI agent MUST NOT self-approve gated business decisions.

---

## 6. Exceptions

Any waived requirement SHOULD record:

```text
requirement
reason
risk
owner
review trigger
```
