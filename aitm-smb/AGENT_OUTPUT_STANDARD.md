# AITM-SMB Agent Output Standard

**Version:** 1.1.0

Every skill handoff (`AGENTS.md` §4 step 10) MUST emit exactly one `aitm_output` block, as a single fenced `yaml` block:

```yaml
aitm_output:
  framework_version: 1.1.0
  profiles: []
  skill:                  # skill directory name, e.g. 13-assess-ai-suitability
  status:                 # PUBLIC_API.md §8
  status_reason:
  artifacts_changed: []   # "<instance path> <record IDs>"
  trace:                  # keys = TRACEABILITY.md §4 trace record
    outcome_ids: []
    capability_ids: []
    state_ids: []
    gap_ids: []
    hypothesis_ids: []
    intervention_ids: []
    initiative_ids: []
    metric_ids: []
    evidence_ids: []
    other_ids: []         # any other registered IDs (ontology/ONTOLOGY.md)
  findings: []            # audit / assessment skills
  assumptions: []         # ASM ids, or statements labeled [ASSUMPTION]
  decisions_needed: []    # items: {gate: HG-*, subject_ids: [], question: }
  open_gates: []          # HG-* not yet approved
  evidence_debt: []       # EVIDENCE_STANDARD.md §5 records
  risks: []
  next_skill:
```

## Fields

| Field | Content |
|---|---|
| `framework_version` | AITM-SMB version the skill followed (`MANIFEST.md`) |
| `profiles` | active profiles (`PUBLIC_API.md` §5 names) from the profile Decision; see `AGENT_CONTEXT_POLICY.md` |
| `skill` | skill directory name |
| `status` | one agent status from `PUBLIC_API.md` §8; when several apply, the first in its order |
| `status_reason` | why this status; names the other statuses that also apply |
| `artifacts_changed` | one item per changed instance: engagement-workspace path, then the record IDs created or changed |
| `trace` | registered IDs the output touches, under the `TRACEABILITY.md` §4 keys; `other_ids` holds IDs with any other registered prefix |
| `findings` | results of audit and assessment skills, each with the IDs it concerns |
| `assumptions` | ASM-### IDs, or statements labeled `[ASSUMPTION]` (`AGENTS.md` §3) |
| `decisions_needed` | decisions a human must take; `gate` is the `STANDARD.md` §8 gate, empty when none applies |
| `open_gates` | `STANDARD.md` §8 gates reached and not yet approved |
| `evidence_debt` | Evidence Debt records (`evidence/EVIDENCE_STANDARD.md` §5) |
| `risks` | RSK-### IDs (Risk record: `artifacts/decision-assumption-log.md`) or short risk statements |
| `next_skill` | directory name of the recommended next skill, or empty |

## Rules

- Keys are fixed. Leave a key empty when nothing applies; do not rename keys or add top-level keys. Skill-specific results belong in the artifact the skill produces; skills that persist no artifact use `findings`.
- Missing links follow `TRACEABILITY.md` §4: an empty list means no applicable link; a required link not yet established is shown as `MISSING:<reason>`, and missing Evidence is also listed in `evidence_debt`.
- A non-empty `open_gates` rules out `COMPLETE`.
- Agents SHOULD use stable identifiers and references rather than repeat upstream artifact content.
