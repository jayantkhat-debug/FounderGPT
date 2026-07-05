from uuid import UUID

from fastapi import APIRouter, Depends

from app.schemas.chat import ChatRequest, ChatResponse
from app.security.auth import AuthenticatedUser, get_current_user
from app.services.chat_service import chat_service

router = APIRouter()


@router.post("/{project_id}/chat", response_model=ChatResponse)
async def chat_with_agent(
    project_id: UUID,
    request: ChatRequest,
    _: AuthenticatedUser = Depends(get_current_user),
) -> ChatResponse:
    _ = project_id
    return chat_service.respond(request)
