from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.conversation import ConversationCreate, ConversationRead, MessageRead
from app.schemas.memory import ProjectMemoryRead, ProjectMemoryUpdate
from app.schemas.project import ProjectCreate, ProjectRead, ProjectUpdate
from app.security.auth import AuthenticatedUser, get_current_user
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
from app.services.user_service import get_or_create_user

router = APIRouter()


@router.get("", response_model=list[ProjectRead])
async def list_user_projects(
    auth_user: AuthenticatedUser = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[ProjectRead]:
    user = get_or_create_user(db, auth_user)
    return list_projects(db, user)


@router.post("", response_model=ProjectRead)
async def create_user_project(
    request: ProjectCreate,
    auth_user: AuthenticatedUser = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ProjectRead:
    user = get_or_create_user(db, auth_user)
    return create_project(db, user, request)


@router.get("/{project_id}", response_model=ProjectRead)
async def get_user_project(
    project_id: UUID,
    auth_user: AuthenticatedUser = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ProjectRead:
    user = get_or_create_user(db, auth_user)
    return serialize_project(get_owned_project(db, user, project_id))


@router.patch("/{project_id}", response_model=ProjectRead)
async def update_user_project(
    project_id: UUID,
    request: ProjectUpdate,
    auth_user: AuthenticatedUser = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ProjectRead:
    user = get_or_create_user(db, auth_user)
    return update_project(db, user, project_id, request)


@router.get("/{project_id}/memory", response_model=ProjectMemoryRead)
async def get_user_project_memory(
    project_id: UUID,
    auth_user: AuthenticatedUser = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ProjectMemoryRead:
    user = get_or_create_user(db, auth_user)
    project = get_owned_project(db, user, project_id)
    return get_or_create_project_memory(db, project)


@router.put("/{project_id}/memory", response_model=ProjectMemoryRead)
async def update_user_project_memory(
    project_id: UUID,
    request: ProjectMemoryUpdate,
    auth_user: AuthenticatedUser = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ProjectMemoryRead:
    user = get_or_create_user(db, auth_user)
    project = get_owned_project(db, user, project_id)
    return update_project_memory(db, project, request)


@router.get("/{project_id}/conversations", response_model=list[ConversationRead])
async def list_user_project_conversations(
    project_id: UUID,
    auth_user: AuthenticatedUser = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[ConversationRead]:
    user = get_or_create_user(db, auth_user)
    project = get_owned_project(db, user, project_id)
    return get_project_conversations(db, project)


@router.post("/{project_id}/conversations", response_model=ConversationRead)
async def create_user_project_conversation(
    project_id: UUID,
    request: ConversationCreate,
    auth_user: AuthenticatedUser = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ConversationRead:
    user = get_or_create_user(db, auth_user)
    project = get_owned_project(db, user, project_id)
    return create_conversation(db, project, request.title)


@router.get("/{project_id}/conversations/{conversation_id}/messages", response_model=list[MessageRead])
async def list_user_project_messages(
    project_id: UUID,
    conversation_id: UUID,
    auth_user: AuthenticatedUser = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> list[MessageRead]:
    user = get_or_create_user(db, auth_user)
    project = get_owned_project(db, user, project_id)
    conversation = get_owned_conversation(db, project, conversation_id)
    return get_conversation_messages(db, conversation)
