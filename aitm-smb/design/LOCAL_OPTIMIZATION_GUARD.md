# Local Optimization Guard

## 1. Purpose

AITM-SMB prevents local improvement from degrading the wider operating system.

This module makes INV-09 ([`STANDARD.md`](../STANDARD.md) §3) checkable: local capability improvement MUST be checked for upstream, downstream, shared-resource, incentive, and Constraint Migration effects.

---

## 2. Required challenge

For every Initiative proposed for selection ask, before its selection is decided (Phase 4) and again at system level in Phase 5:

```text
upstream              Which upstream capability must support it?
downstream            What new demand will this create?
                      Which downstream capability receives it?
shared resource       What shared resource becomes more constrained?
incentive             Which metric may be gamed?
Constraint Migration  If this succeeds, where does the System Constraint move?
                      (design/CONSTRAINT_ANALYSIS.md §5)
exceptions            Which role absorbs new exceptions?
```

Also ask whether the change improves the target Outcome or only a local metric.

In the Compact profile, answering these questions per Initiative proposed for selection is the system-effect check ([`APPLICATION_PROFILES.md`](../APPLICATION_PROFILES.md) §3).

---

## 3. Common local-optimization failures

### Faster intake, unchanged delivery

```text
intake throughput ↑
delivery capacity unchanged
→ backlog ↑
```

### More AI-generated work, unchanged review

```text
generation throughput ↑
review capacity unchanged
→ queue ↑
```

### More automation, weaker exception handling

```text
routine work ↓
exception complexity ↑
expert burden ↑
```

### Better local KPI, worse system outcome

```text
support closes tickets faster
but repeat contact increases
```

---

## 4. System effect record

Record the §2 answers in a System Effect Assessment (`SFX-###`): record contract [`artifacts/system-effect-assessment.md`](../artifacts/system-effect-assessment.md).

One assessment per Initiative proposed for selection. A skill that finds an existing assessment for the same Initiative updates it instead of creating a second one.

Phase 4 (skill 05 invokes skill 19) records at least a draft: every §2 question answered from the Evidence available, an unknown effect marked `unknown` with Evidence Debt. Phase 5 (skill 06 invokes skills 19 and 24) refines it at system level, using the Capability Network and System Constraint where they exist.

---

## 5. Approval rule

A material Initiative SHOULD NOT be approved until its expected system effects (INV-09, §2) are recorded. `HG-INITIATIVE` decides with the System Effect Assessment in hand ([`methodology/04-prioritization.md`](../methodology/04-prioritization.md)).

If a refined effect or the System Constraint changes a Phase 4 priority, the affected selection returns to `HG-INITIATIVE` ([`methodology/05-target-system-design.md`](../methodology/05-target-system-design.md)).
