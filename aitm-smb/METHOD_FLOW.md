# AITM-SMB Canonical Method Flow

**Version:** 1.1.0

## 1. One-page method

AITM-SMB transforms an SMB in twelve steps. The steps are the one-page view; the executable phases are `EXECUTION_MODEL.md` §1.

| Step | Phase |
|---|---|
| 1. Frame Outcome | 0 Frame |
| 2. Discover Capabilities | 1 Observe |
| 3. Map Current System | 1 Observe |
| 4. Diagnose Gaps & Causes | 2 Diagnose |
| 5. Design Interventions | 3 Design Interventions |
| 6. Select & Prioritize | 4 Decide |
| 7. Design Target System | 5 Design Target System |
| 8. Design Transition | 6 Design Transition |
| 9. Pilot & Evaluate | 6 Design Transition (design) · 7 Operationalize (run, evaluate, promote) |
| 10. Roll Out & Govern | 7 Operationalize |
| 11. Measure Value | 8 Measure & Evolve |
| 12. Evolve | 8 Measure & Evolve |

---

## 2. Canonical reasoning chain

The canonical transformation chain is defined only in `STANDARD.md` §2.

The steps in §1 traverse that chain; they are not a second chain.

---

## 3. Minimum valid path

Every application, including Compact, MUST preserve the minimum valid path in `EXECUTION_MODEL.md` §6.

No profile may skip these semantic layers.

---

## 4. Mandatory human gates

Human approval is required at the gates in `STANDARD.md` §8 (`HG-*`), at whichever step their trigger occurs.

---

## 5. Mandatory challenge questions

At every major step ask:

### Outcome
What business result must change?

### Capability
What must the organization become capable of doing?

### Gap
What prevents that capability today?

### Cause
What explains the gap?

### Intervention
What is the simplest effective change? (full challenge: `DECISION_MODEL.md` §1)

### AI
What specifically requires probabilistic intelligence?

### Autonomy
Why are assistance and explicit human approval insufficient? (full challenge: `DECISION_MODEL.md` §3)

### System
What upstream, downstream, shared-resource, incentive, and Constraint Migration effects will this change create? (INV-09)

### Transition
How can we test this safely and reversibly?

### Value
What evidence proves that the business improved?
