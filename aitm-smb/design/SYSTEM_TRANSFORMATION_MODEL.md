# AITM-SMB System Transformation Model

## 1. Purpose

AITM-SMB does not optimize isolated capabilities.

It redesigns an interconnected business system.

A capability may improve locally while the organization performs worse globally.

Therefore the target transformation model is:

```text
Outcome System
→ Capability Network
→ Dependency Structure
→ System Constraint
→ Coordinated Interventions
→ Target Operating Architecture
→ Transition States
→ Measured System Effect
```

---

## 2. Business as a capability network

Capabilities form a directed dependency network.

Example abstraction:

```text
Demand Generation
        ↓
Lead Qualification
        ↓
Solution Design
        ↓
Pricing
        ↓
Commitment
        ↓
Delivery
        ↓
Support
        ↓
Retention
```

But dependencies are not always linear.

A capability may depend on:

```text
Knowledge Management
Identity
Financial Control
Data Quality
Governance
Resource Allocation
```

across several value streams.

---

## 3. Local versus system optimization

Before improving a Capability ask:

```text
If this Capability improves,
where does the next constraint appear?
```

Examples of overload that may follow:

```text
Faster lead qualification
→ more opportunities
→ overloaded solution design

Faster content generation
→ more content
→ overloaded review

Automated support intake
→ more routed cases
→ overloaded expert escalation
```

When the overload passes the constraint test, the System Constraint has moved: Constraint Migration (`design/CONSTRAINT_ANALYSIS.md` §5). Otherwise it is a local bottleneck.

---

## 4. Transformation design object

A system transformation SHOULD make the following explicit. It is a view with no record of its own; each element is held by the record named:

```text
Outcomes                        Outcome (OUT)
Capabilities, critical
  dependencies                  Capability Network (CPN, DEP): artifacts/capability-network.md
current constraint, expected
  Constraint Migration          System Constraint (CST): artifacts/system-constraint.md
coordinated interventions       Initiatives (INI) and their Interventions (INT)
target operating architecture   TOA: artifacts/target-operating-architecture.md
transition states               Transition States (STA, type TRANSITION): artifacts/transition-state.md
system metrics                  Metrics (MET) in the TOA metric_ids
system effects                  System Effect Assessments (SFX): artifacts/system-effect-assessment.md
```

---

## 5. System design rule

Do not ask only:

```text
How can this capability be improved?
```

Also ask:

```text
What happens to the rest of the system if it improves?
```

---

## 6. Required system checks

Before approving a Target Operating Architecture (`HG-TOA`, `STANDARD.md` §8) verify:

1. downstream capacity;
2. upstream information quality;
3. decision-right consistency;
4. ownership consistency;
5. shared data dependencies;
6. shared knowledge dependencies;
7. shared application dependencies;
8. control dependencies;
9. metric interactions;
10. likely Constraint Migration.

---

## 7. System-level success

A transformation is successful when:

```text
local capability improvement
AND
no unacceptable downstream degradation
AND
target Outcome improves
AND
new constraint is understood
```
