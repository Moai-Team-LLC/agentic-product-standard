# Phase 1 — Observe (Current System)

## Objective

Build an evidence-based model of how the business currently produces value.

## Required inputs

- approved Transformation Intent (Outcomes approved through `HG-OUTCOME`);
- approved profile Decision;
- direct evidence where available;
- where evidence is absent, Assumptions a named business owner states or accepts ([`evidence/EVIDENCE_STANDARD.md`](../evidence/EVIDENCE_STANDARD.md) §7).

## Method

Use:

1. [`diagnostics/CAPABILITY_DISCOVERY.md`](../diagnostics/CAPABILITY_DISCOVERY.md)
2. [`CORE_MODEL.md`](../CORE_MODEL.md) §2–§3 (Capability, State)
3. [`ontology/ONTOLOGY.md`](../ontology/ONTOLOGY.md) (business-system entities)
4. [`evidence/EVIDENCE_STANDARD.md`](../evidence/EVIDENCE_STANDARD.md)

## Activities

1. map value streams that materially affect the approved Outcomes;
2. discover Capabilities (skill 11) and apply the granularity test;
3. describe each relevant Capability's CURRENT State across the relevant [`STANDARD.md`](../STANDARD.md) §4 dimensions;
4. connect roles, decisions, processes, data, knowledge, and applications (Business System Map `relations`, where the profile requires it);
5. identify handoffs and dependencies;
6. record failure modes and workarounds;
7. record Evidence and Evidence Debt.

## Outputs

- Capability Map ([`artifacts/capability-map.md`](../artifacts/capability-map.md)): Capability records (`CAP-###`) and their CURRENT States (`STA-###`, `type: CURRENT`);
- Business System Map ([`artifacts/business-system-map.md`](../artifacts/business-system-map.md)), where the profile requires it;
- Evidence Register ([`artifacts/evidence-register.md`](../artifacts/evidence-register.md)): Evidence (`EVD-###`) and Evidence Debt;
- Decision & Assumption Log updates (Assumptions).

## Human gates

None typically. Any [`STANDARD.md`](../STANDARD.md) §8 gate applies whenever its trigger occurs.

## Exit condition

Matches [`EXECUTION_MODEL.md`](../EXECUTION_MODEL.md) §2:

```text
each relevant Capability (CAP) has a CURRENT State (STA)
  backed by Evidence (EVD) or by Assumptions (ASM) a named business owner
  stated or accepted
AND the Business System Map with its required relations, where the profile requires it
```

A CURRENT State resting only on agent inference does not satisfy this exit; stop with `INSUFFICIENT_EVIDENCE` and record the Evidence Debt ([`AGENTS.md`](../AGENTS.md) §3).

In addition, as in every phase: facts and assumptions are separated; every material conclusion is traceable to Evidence (`EVD-###`) or labeled `[ASSUMPTION]` or `[HYPOTHESIS]` ([`AGENTS.md`](../AGENTS.md) §3); unresolved critical uncertainty is visible.

## Prohibited shortcut

Target-state solutions inside the current-state model.
