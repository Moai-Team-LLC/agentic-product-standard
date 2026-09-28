# Role Transition Model

## 1. Purpose

AI transformation can remove tasks without removing the need for a role, and can create new responsibilities.

---

## 2. Task disposition

For each affected task classify:

```text
RETAIN
ASSIST
AUTOMATE
TRANSFER
ELIMINATE
CREATE_NEW
```

---

## 3. Role transition record

Record contract: the `role_transitions` section of `artifacts/adoption-plan.md`.

A role transition record states, per affected role, current and target responsibilities, the §2 disposition of each affected task, removed and new tasks, decision-right changes, skill changes, performance-metric changes, and risks.

---

## 4. New responsibilities commonly created by AI

```text
exception handling
knowledge curation
evaluation
policy ownership
AI quality review
workflow improvement
incident response
```

---

## 5. Rule

AITM-SMB SHOULD make role changes explicit before rollout.

Hidden role redesign creates adoption failure.

Decision-right changes MUST match the Decision Rights Map (`artifacts/decision-rights-map.md`) where one exists; changing material Decision Rights requires `HG-DECISION-RIGHTS` (`STANDARD.md` §8).
