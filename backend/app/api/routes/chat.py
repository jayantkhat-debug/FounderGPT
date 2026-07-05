from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.chat import ChatRequest, ChatResponse, StartupIdeaChatRequest, StartupIdeaChatResponse
from app.security.auth import AuthenticatedUser, get_current_user
from app.services.nvidia_client import AIConfigurationError, AIProviderError
from app.services.chat_service import chat_service

project_router = APIRouter()
router = APIRouter()


@project_router.post("/{project_id}/chat", response_model=ChatResponse)
async def chat_with_agent(
    project_id: UUID,
    request: ChatRequest,
    _: AuthenticatedUser = Depends(get_current_user),
) -> ChatResponse:
    _ = project_id
    return chat_service.respond(request)


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
