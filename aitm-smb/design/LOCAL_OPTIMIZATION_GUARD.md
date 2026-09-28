# Local Optimization Guard

## 1. Purpose

AITM-SMB prevents local improvement from degrading the wider operating system.

This module makes INV-09 (`STANDARD.md` §3) checkable: local capability improvement MUST be checked for upstream, downstream, shared-resource, incentive, and Constraint Migration effects.

---

## 2. Required challenge

For every selected Initiative ask:

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

In the Compact profile, answering these questions per selected Initiative is the system-effect check (`APPLICATION_PROFILES.md` §3).

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

Record the §2 answers in a System Effect Assessment (`SFX-###`): record contract `artifacts/system-effect-assessment.md`.

One assessment per selected Initiative. A skill that finds an existing assessment for the same Initiative updates it instead of creating a second one.

---

## 5. Approval rule

A material Initiative SHOULD NOT be approved until the INV-09 effects (§2) are recorded.

If a recorded effect or the System Constraint changes a Phase 4 priority, the affected selection returns to the Phase 4 human gate (`methodology/05-target-system-design.md`).
