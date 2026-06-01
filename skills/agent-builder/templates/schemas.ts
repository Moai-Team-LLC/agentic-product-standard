// Typed input/output skeletons for one agent.
// Illustrative artifact-contract — keep it framework-light. Uses zod only as a
// widely-understood schema notation; swap for your own validator if you prefer.
//
//   npm i zod   (or:  bun add zod)

import { z } from "zod"

// ── Input ────────────────────────────────────────────────────────────────
// Derived from the Agent Contract §4 (Inputs). Validate at the runner boundary
// BEFORE any LLM call. Reject (don't coerce) malformed input.
export const AgentInputSchema = z.object({
  task: z.string().min(1),
  actor: z.object({
    id: z.string(),
    // Resolve the actor's permission tiers in code; never trust the prompt.
    permissions: z.array(z.string()).default([]),
  }),
  // Optional, task-specific fields go here.
})
export type AgentInput = z.infer<typeof AgentInputSchema>

// ── Output ───────────────────────────────────────────────────────────────
// Derived from the Agent Contract §9 (Output Schema). Validate the model's
// structured output against this; treat a parse failure as a task failure.
export const AgentOutputSchema = z.object({
  status: z.enum(["completed", "escalated", "failed"]),
  // The artifact this agent owns (Contract §2). Shape it for your domain.
  artifact: z.unknown().optional(),
  // True when an action needs human approval before it commits (P3+).
  approvalRequired: z.boolean().default(false),
  // Concrete reasons, used by assertions and eval cases.
  notes: z.array(z.string()).default([]),
})
export type AgentOutput = z.infer<typeof AgentOutputSchema>
