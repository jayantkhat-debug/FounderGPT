from typing import Any
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ProjectCreate(BaseModel):
    name: str = Field(min_length=2, max_length=180)
    description: str = Field(min_length=2, max_length=12000)
    stage: str = Field(default="Idea", min_length=2, max_length=80)
    target_users: str | None = Field(default=None, max_length=8000)
    market: str | None = Field(default=None, max_length=8000)
    competitors: list[dict[str, Any]] = Field(default_factory=list)
    revenue_model: str | None = Field(default=None, max_length=4000)
    funding_stage: str | None = Field(default=None, max_length=80)


class ProjectUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=180)
    description: str | None = Field(default=None, min_length=2, max_length=12000)
    stage: str | None = Field(default=None, min_length=2, max_length=80)
    target_users: str | None = Field(default=None, max_length=8000)
    market: str | None = Field(default=None, max_length=8000)
    competitors: list[dict[str, Any]] | None = None
    revenue_model: str | None = Field(default=None, max_length=4000)
    funding_stage: str | None = Field(default=None, max_length=80)


class ProjectRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    description: str
    stage: str
    target_users: str | None
    market: str | None
    competitors: list[dict[str, Any]]
    revenue_model: str | None
    funding_stage: str | None
    status: str
    health_score: int | None
    created_at: datetime
    updated_at: datetime
