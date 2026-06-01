// Structured envelope for agent-to-agent communication.
// Agents must talk through this — never free-form text when state matters.
// Sub-agents return CONDENSED findings in `payload`, never raw transcripts.

export type AgentMessage = {
  messageType:
    | "task_request"
    | "task_result"
    | "clarification_request"
    | "clarification_response"
    | "critique_request"
    | "critique_result"
    | "handoff_request"
    | "handoff_acceptance"
    | "handoff_rejection"
    | "approval_request"
    | "error_report"

  sender: string
  receiver: string
  runId: string
  taskId: string
  priority: "low" | "normal" | "high" | "urgent"

  payload: unknown // condensed findings / structured result — not a transcript
  contextRefs: string[] // references to large artifacts, not the artifacts themselves
  permissions: string[] // tiers the receiver is allowed to exercise
  expectedOutput?: unknown

  trace: {
    parentStepId?: string
    correlationId: string
  }
}
