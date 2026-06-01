"""Typed input/output skeletons for one agent.

Illustrative artifact-contract — keep it framework-light. Uses pydantic only as a
widely-understood schema notation; swap for your own validator if you prefer.

    pip install pydantic
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


# ── Input ──────────────────────────────────────────────────────────────────
# Derived from the Agent Contract §4 (Inputs). Validate at the runner boundary
# BEFORE any LLM call. Reject (don't coerce) malformed input.
class Actor(BaseModel):
    id: str
    # Resolve the actor's permission tiers in code; never trust the prompt.
    permissions: list[str] = Field(default_factory=list)


class AgentInput(BaseModel):
    task: str = Field(min_length=1)
    actor: Actor
    # Optional, task-specific fields go here.


# ── Output ─────────────────────────────────────────────────────────────────
# Derived from the Agent Contract §9 (Output Schema). Validate the model's
# structured output against this; treat a parse failure as a task failure.
class Status(str, Enum):
    completed = "completed"
    escalated = "escalated"
    failed = "failed"


class AgentOutput(BaseModel):
    status: Status
    # The artifact this agent owns (Contract §2). Shape it for your domain.
    artifact: Any | None = None
    # True when an action needs human approval before it commits (P3+).
    approval_required: bool = False
    # Concrete reasons, used by assertions and eval cases.
    notes: list[str] = Field(default_factory=list)
