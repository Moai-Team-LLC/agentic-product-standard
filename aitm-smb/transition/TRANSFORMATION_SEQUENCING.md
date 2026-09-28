# Transformation Sequencing

## 1. Purpose

AITM-SMB sequences transformation based on dependencies, learning, constraints, and risk.

---

## 2. Sequencing dimensions

Evaluate:

```text
Constraint relevance
Dependency order
Learning value
Reversibility
Risk
Time to evidence
Shared-platform leverage
Change burden
Economic exposure
```

---

## 3. Default sequencing logic

Prefer:

```text
1. establish observability
2. fix structural prerequisites
3. relax the system constraint
4. validate intervention effect
5. increase scope
6. increase authority only after evidence
7. optimize secondary capabilities
```

Also prefer high learning value, reversible decisions, bounded scope, short evidence loops, and vertical business slices (`execution/DELIVERY_SLICE.md`).

Avoid:

```text
big-bang migration
infrastructure-first work without capability effect
autonomy before observability
scale before proof
```

This is a default reasoning pattern, not a mandatory recipe. System Constraint as sequencing input: `design/CONSTRAINT_ANALYSIS.md` §6.

---

## 4. Dependency types

### Hard dependency

Initiative B cannot function before Initiative A.

### Information dependency

B requires data/knowledge produced by A.

### Governance dependency

B requires a control or decision model established by A.

### Learning dependency

B is possible, but A should be tested first to reduce uncertainty.

### Capacity dependency

B would overload a downstream capability until A changes capacity.

Initiative `dependencies` hold the INI-### ids an Initiative depends on (`CORE_MODEL.md` §7). Where the type matters for sequencing, record it in the Transformation Roadmap `dependency_types` (`artifacts/transformation-roadmap.md`). Capability dependencies are a different record (`DEP-###`, `design/CAPABILITY_NETWORK.md`).

---

## 5. Portfolio sequencing

An initiative SHOULD NOT be scheduled only because:

```text
it is easy
it is visible
it uses AI
stakeholders like it
```

It should be sequenced relative to:

```text
Outcome leverage
constraint
dependencies
risk
learning
```
