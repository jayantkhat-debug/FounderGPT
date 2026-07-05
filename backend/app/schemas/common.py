from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ApiError(BaseModel):
    code: str
    message: str
    request_id: str | None = None


class TimestampedSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
    updated_at: datetime
