---
artifact_type: target-architecture
status: deprecated
deprecated_since: 0.7.0
removal_target: 2.0.0
replacement:
  - artifacts/capability-target-state.md
  - artifacts/target-operating-architecture.md
---

# Target Architecture — Deprecated

This artifact previously mixed two different abstraction levels:

1. future behavior of one Capability;
2. integrated future operating architecture across Capabilities.

Use:

- `artifacts/capability-target-state.md` for a single Capability Target State;
- `artifacts/target-operating-architecture.md` for the integrated system-level architecture.

No new AITM-SMB execution should produce this artifact.
