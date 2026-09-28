# AITM-SMB Conformance

**Version:** 1.1.0

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
11. define human/AI authority where AI acts, including how it is observed and reduced (INV-07);
12. preserve end-to-end traceability;
13. check selected Initiatives for upstream, downstream, shared-resource, incentive, and Constraint Migration effects (INV-09);
14. record each `STANDARD.md` §8 gate decision as an approved Decision (DEC-###) whose `approved_by` names the human approver.

The `STANDARD.md` §3 MUST invariants apply in full; the items above are their minimum checkable form. The smallest valid trace is the minimum valid path (`EXECUTION_MODEL.md` §6). "Material": `STANDARD.md` §16.

`rubrics/CONFORMANCE_CHECKLIST.md` is an informative aid; on conflict this file governs.

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

An application SHOULD declare one or more profiles (`PUBLIC_API.md` §5). Selection: `PROFILE_SELECTION.md`; the selected profiles are recorded as a Decision (skill 36).

Claiming a profile requires the content listed for it in `APPLICATION_PROFILES.md` (artifact mapping: `MINIMUM_ARTIFACT_SET.md`), unless waived per §6.

An application that declares no profile is evaluated as Compact.

---

## 4. Artifact proportionality

Conformance does not require one file per artifact contract.

Artifacts MAY be merged or split if:

```text
semantic boundaries remain explicit
stable identifiers remain intact
each record's type remains identifiable
traceability remains intact
ownership remains clear
agent parsing remains reliable
```

---

## 5. Conformance declaration

The declaration is persisted in the engagement's Transformation Intent (`artifacts/transformation-intent.md`) under `conformance:`. Skill 38 writes it.

```yaml
conformance:
  framework_version: 1.1.0
  profiles: []
  validated_at:
  validated_by:            # agent (skill) or named human that ran the check
  unresolved_exceptions: []  # §6 records
```

An AI agent MAY evaluate conformance.

An AI agent MUST NOT self-approve gated business decisions.

A conformance result is not approval of any gated decision.

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

Only an approved human decision (DEC-###) can waive a requirement (`NORMATIVE_INDEX.md` tier 1).

- SHOULD and profile requirements MAY be waived; the application still conforms.
- Waiving a MUST, including a `STANDARD.md` §3 invariant, makes the application non-conforming for that requirement. The waiver MUST be listed in `unresolved_exceptions`.
- Never waivable: a human, not an AI agent, makes each `STANDARD.md` §8 gate decision.
- Waivers a module provides for (e.g. Execution Gates, `execution/EXECUTION_GATE_MODEL.md` §4) follow that module and are not exceptions.
