# Rollout Model

## 1. Purpose

Rollout expands a validated transformation while preserving control.

A rollout that follows a material pilot starts only after `HG-PROMOTION` (`STANDARD.md` §8). Record contract: `artifacts/rollout-plan.md` (`ROL-###`).

---

## 2. Rollout dimensions

Expansion may occur by:

```text
user group
customer segment
transaction class
geography
workflow scope
data scope
AI capability
autonomy level
```

Expanding by autonomy level is an authority increase: it follows `governance/AUTHORITY_ESCALATION_MODEL.md`, requires `HG-AUTHORITY`, and MUST NOT exceed the approved Authority Ceiling (`diagnostics/AUTONOMY_SUITABILITY.md` §6).

---

## 3. Rollout gates

Before expanding scope verify:

```text
pilot success criteria met
promotion approved (HG-PROMOTION) where a material pilot preceded the rollout
failure modes understood
monitoring active
ownership assigned
support path exists
role changes explicit
rollback/recovery exists
governance controls operate
autonomy level approved and within the Authority Ceiling
cost envelope acceptable
```

These gates are verified before each stage. Governed: this verification is Execution Gate E (`execution/EXECUTION_GATE_MODEL.md`).

---

## 4. Progressive rollout

Preferred pattern:

```text
small cohort
→ broader cohort
→ default path
→ legacy path retired
```

---

## 5. Rollback versus recovery

### Rollback

Return to the previous operating state.

### Recovery

Continue with the new system after correcting state or handling failure.

Every material rollout SHOULD know which is possible.

---

## 6. Rollout completion

Rollout is complete only when:

```text
target scope operates on new model
old temporary paths are retired or explicitly retained
ownership is transferred to operations
metrics are stable
known risks are accepted
```

Accepting a material known risk requires `HG-RISK` (`STANDARD.md` §8); the risk is a Risk record (`RSK-###`, `artifacts/decision-assumption-log.md`).
