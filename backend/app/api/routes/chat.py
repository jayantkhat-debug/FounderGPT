from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_db_user
from app.db.session import get_db
from app.models import MessageRole, User
from app.schemas.chat import ChatRequest, ChatResponse, StartupIdeaChatRequest, StartupIdeaChatResponse
from app.security.auth import AuthenticatedUser, get_current_user
from app.services.nvidia_client import AIConfigurationError, AIProviderError
from app.services.chat_service import chat_service
from app.services.project_service import (
    create_conversation,
    get_owned_conversation,
    get_owned_project,
    store_message,
)

project_router = APIRouter()
router = APIRouter()


@project_router.post("/{project_id}/chat", response_model=ChatResponse)
async def chat_with_agent(
    project_id: UUID,
    request: ChatRequest,
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
) -> ChatResponse:
    project = get_owned_project(db, user, project_id)
    conversation = (
        get_owned_conversation(db, project, request.conversation_id)
        if request.conversation_id
        else create_conversation(db, project, "Founder strategy session")
    )
    store_message(db, conversation, role=MessageRole.user, content=request.message, agent_key=request.agent_key)
    try:
        response = chat_service.respond(request)
    except AIConfigurationError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
    except AIProviderError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="FounderGPT X could not get a response from NVIDIA Build API. Please retry.",
        ) from exc
    assistant_message = store_message(
        db,
        conversation,
        role=MessageRole.assistant,
        content=response.content,
        agent_key=response.agent_key,
    )
    response.message_id = assistant_message.id
    response.conversation_id = conversation.id
    return response


@router.post("/startup-idea", response_model=StartupIdeaChatResponse)
async def chat_about_startup_idea(
    request: StartupIdeaChatRequest,
    _: AuthenticatedUser = Depends(get_current_user),
) -> StartupIdeaChatResponse:
    try:
        return chat_service.respond_to_startup_idea(request)
    except AIConfigurationError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
    except AIProviderError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="FounderGPT X could not get a response from NVIDIA Build API. Please retry.",
        ) from exc
