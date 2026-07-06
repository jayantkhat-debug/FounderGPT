from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_db_user
from app.db.session import get_db
from app.models import User
from app.schemas.conversation import ConversationCreate, ConversationRead, MessageRead
from app.schemas.memory import ProjectMemoryRead, ProjectMemoryUpdate
from app.schemas.project import ProjectCreate, ProjectRead, ProjectUpdate
from app.services.generator_service import generator_service
from app.services.nvidia_client import AIConfigurationError, AIProviderError
from app.services.project_service import (
    create_conversation,
    create_project,
    get_conversation_messages,
    get_or_create_project_memory,
    get_owned_conversation,
    get_owned_project,
    get_project_conversations,
    list_projects,
    serialize_project,
    update_project,
    update_project_memory,
)

router = APIRouter()


@router.get("", response_model=list[ProjectRead])
async def list_user_projects(
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
) -> list[ProjectRead]:
    return list_projects(db, user)


@router.post("", response_model=ProjectRead)
async def create_user_project(
    request: ProjectCreate,
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
) -> ProjectRead:
    return create_project(db, user, request)


@router.get("/{project_id}", response_model=ProjectRead)
async def get_user_project(
    project_id: UUID,
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
) -> ProjectRead:
    return serialize_project(get_owned_project(db, user, project_id))


@router.patch("/{project_id}", response_model=ProjectRead)
async def update_user_project(
    project_id: UUID,
    request: ProjectUpdate,
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
) -> ProjectRead:
    return update_project(db, user, project_id, request)


@router.get("/{project_id}/memory", response_model=ProjectMemoryRead)
async def get_user_project_memory(
    project_id: UUID,
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
) -> ProjectMemoryRead:
    project = get_owned_project(db, user, project_id)
    return get_or_create_project_memory(db, project)


@router.put("/{project_id}/memory", response_model=ProjectMemoryRead)
async def update_user_project_memory(
    project_id: UUID,
    request: ProjectMemoryUpdate,
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
) -> ProjectMemoryRead:
    project = get_owned_project(db, user, project_id)
    return update_project_memory(db, project, request)


@router.get("/{project_id}/conversations", response_model=list[ConversationRead])
async def list_user_project_conversations(
    project_id: UUID,
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
) -> list[ConversationRead]:
    project = get_owned_project(db, user, project_id)
    return get_project_conversations(db, project)


@router.post("/{project_id}/conversations", response_model=ConversationRead)
async def create_user_project_conversation(
    project_id: UUID,
    request: ConversationCreate,
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
) -> ConversationRead:
    project = get_owned_project(db, user, project_id)
    return create_conversation(db, project, request.title)


@router.get("/{project_id}/conversations/{conversation_id}/messages", response_model=list[MessageRead])
async def list_user_project_messages(
    project_id: UUID,
    conversation_id: UUID,
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
) -> list[MessageRead]:
    project = get_owned_project(db, user, project_id)
    conversation = get_owned_conversation(db, project, conversation_id)
    return get_conversation_messages(db, conversation)


@router.post("/{project_id}/generate-business-model")
async def generate_project_business_model(
    project_id: UUID,
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
):
    project = get_owned_project(db, user, project_id)
    memory = get_or_create_project_memory(db, project)
    try:
        business_model = generator_service.generate_business_model(memory)
    except AIConfigurationError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
    except AIProviderError:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="FounderGPT X could not get a response from NVIDIA Build API. Please retry.",
        )

    # Persist the generated business model to project memory
    memory.revenue_model = business_model
    db.commit()

    return {"business_model": business_model}


@router.post("/{project_id}/generate-financial-model")
async def generate_project_financial_model(
    project_id: UUID,
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
):
    project = get_owned_project(db, user, project_id)
    memory = get_or_create_project_memory(db, project)
    try:
        financial_model = generator_service.generate_financial_model(memory)
    except AIConfigurationError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
    except AIProviderError:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="FounderGPT X could not get a response from NVIDIA Build API. Please retry.",
        )

    # Persist the generated financial model to project memory
    memory.pricing = financial_model
    db.commit()

    return {"financial_model": financial_model}


@router.post("/{project_id}/generate-business-plan")
async def generate_project_business_plan(
    project_id: UUID,
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
):
    project = get_owned_project(db, user, project_id)
    memory = get_or_create_project_memory(db, project)
    try:
        business_plan = generator_service.generate_business_plan(memory)
    except AIConfigurationError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
    except AIProviderError:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="FounderGPT X could not get a response from NVIDIA Build API. Please retry.",
        )

    # Persist the generated business plan to project memory
    memory.business_plan = business_plan
    db.commit()

    return {"business_plan": business_plan}


@router.post("/{project_id}/generate-web3-strategy")
async def generate_project_web3_strategy(
    project_id: UUID,
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
):
    project = get_owned_project(db, user, project_id)
    memory = get_or_create_project_memory(db, project)
    try:
        web3_strategy = generator_service.generate_web3_strategy(memory)
    except AIConfigurationError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
    except AIProviderError:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="FounderGPT X could not get a response from NVIDIA Build API. Please retry.",
        )

    # Persist the generated Web3 strategy to project memory
    memory.web3_strategy = web3_strategy
    db.commit()

    return {"web3_strategy": web3_strategy}


@router.post("/{project_id}/generate-pitch-deck")
async def generate_project_pitch_deck(
    project_id: UUID,
    user: User = Depends(get_current_db_user),
    db: Session = Depends(get_db),
):
    project = get_owned_project(db, user, project_id)
    memory = get_or_create_project_memory(db, project)
    try:
        pitch_deck = generator_service.generate_pitch_deck(memory)
    except AIConfigurationError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
    except AIProviderError:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="FounderGPT X could not get a response from NVIDIA Build API. Please retry.",
        )

    # Persist the generated pitch deck to project memory
    memory.pitch_deck = pitch_deck
    db.commit()

    return {"pitch_deck": pitch_deck}
