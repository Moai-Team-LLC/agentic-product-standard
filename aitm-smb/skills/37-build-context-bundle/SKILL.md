---
name: 37-build-context-bundle
description: "Builds the bounded context an agent needs for one skill: the Core bundle, the active profiles from the profile Decision (provisional while HG-OUTCOME is open), the relevant phase file, the skill with its normative sources and artifact contracts, the modules the profiles activate for it, and only the upstream engagement records and Evidence the task needs, with personal data minimized. Use before any orchestrator or specialist step that needs context, and when a new agent session joins an engagement. Produces no persistent artifact; returns the loaded files, the active profiles, and any missing normative dependency in findings. Part of AITM-SMB; paths are relative to the AITM-SMB root."
metadata:
  framework: AITM-SMB
  version: "1.1.0"
  minimum_framework_version: "1.1.0"
  status: active
  category: framework-operations
  phase: "any"
  human_gate: "false"
---

# Skill 37: Build Agent Context Bundle

## Purpose

Load enough to follow the methodology, and no more: excess context causes instruction conflict, semantic drift, and invented dependencies. Invoked by [`skills/01-discover-transformation/SKILL.md`](../01-discover-transformation/SKILL.md) and before any step that needs context.

## Required inputs

- the requested skill (directory name) and task;
- the engagement workspace location;
- the profile Decision, if one exists.

## Normative sources

- [`AGENT_CONTEXT_POLICY.md`](../../AGENT_CONTEXT_POLICY.md)
- [`NORMATIVE_INDEX.md`](../../NORMATIVE_INDEX.md) (Canonical Core)
- [`MODULE_CATALOG.md`](../../MODULE_CATALOG.md) (modules each profile activates)

## Produces

- no persistent artifact; `findings` lists the files loaded, the active profiles and whether they are provisional, and any missing normative dependency.

## Procedure

1. Load the Core bundle ([`AGENT_CONTEXT_POLICY.md`](../../AGENT_CONTEXT_POLICY.md)); load further Canonical Core files ([`NORMATIVE_INDEX.md`](../../NORMATIVE_INDEX.md)) only when the requested skill depends on them.
2. Load the active profiles as [`AGENT_CONTEXT_POLICY.md`](../../AGENT_CONTEXT_POLICY.md) (Profile) prescribes; if no profile Decision exists, run [`skills/36-select-application-profile/SKILL.md`](../36-select-application-profile/SKILL.md) first.
3. Load the phase file ([`EXECUTION_MODEL.md`](../../EXECUTION_MODEL.md) §1), the requested skill, its Normative sources, the artifact contracts it produces, and the modules the active profiles activate for it ([`MODULE_CATALOG.md`](../../MODULE_CATALOG.md) §3).
4. Load approved upstream records, required Evidence, the proposed gate Decisions (open gates), and open Evidence Debt from the engagement workspace by reference ([`AGENT_CONTEXT_POLICY.md`](../../AGENT_CONTEXT_POLICY.md)); minimize and redact personal data.
5. Verify every normative dependency named by the loaded files is present; load a missing one rather than infer it.
6. Stop with `BLOCKED` when a required file or record cannot be found.

## MUST NOT

- load the full repository merely because it exists;
- load engagement data beyond the task, or copy personal or confidential content into context;
- write anything into the AITM root.

## Handoff

Emit the `aitm_output` block defined in [`AGENT_OUTPUT_STANDARD.md`](../../AGENT_OUTPUT_STANDARD.md).
