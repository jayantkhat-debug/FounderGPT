from uuid import UUID

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    conversation_id: UUID | None = None
    agent_key: str = Field(default="ceo", min_length=2, max_length=80)
    message: str = Field(min_length=2, max_length=20000)
    workflow: str = Field(default="founder_interview", max_length=120)


class ChatResponse(BaseModel):
    message_id: UUID | None = None
    agent_key: str
    content: str
    follow_up_questions: list[str] = Field(default_factory=list)
    memory_updates: list[dict] = Field(default_factory=list)
    suggested_tasks: list[dict] = Field(default_factory=list)
