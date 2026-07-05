from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ProjectMemoryUpdate(BaseModel):
    startup_name: str | None = Field(default=None, max_length=180)
    problem: str | None = Field(default=None, max_length=12000)
    solution: str | None = Field(default=None, max_length=12000)
    customer: str | None = Field(default=None, max_length=12000)
    revenue_model: str | None = Field(default=None, max_length=12000)
    pricing: str | None = Field(default=None, max_length=12000)
    competitors: list[dict[str, Any]] | None = None
    goals: list[dict[str, Any]] | None = None


class ProjectMemoryRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    project_id: UUID
    startup_name: str | None
    problem: str | None
    solution: str | None
    customer: str | None
    revenue_model: str | None
    pricing: str | None
    competitors: list[dict[str, Any]]
    goals: list[dict[str, Any]]
