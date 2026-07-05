from datetime import UTC, datetime
from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Conversation, Message, MessageRole, Project, ProjectMemory, User
from app.schemas.memory import ProjectMemoryUpdate
from app.schemas.project import ProjectCreate, ProjectRead, ProjectUpdate


def serialize_project(project: Project) -> ProjectRead:
    return ProjectRead(
        id=project.id,
        name=project.startup_name,
        description=project.description or project.idea,
        stage=project.stage,
        target_users=project.target_users,
        market=project.market,
        competitors=project.competitors,
        revenue_model=project.revenue_model,
        funding_stage=project.funding_stage,
        status=project.status.value,
        health_score=project.health_score,
        created_at=project.created_at,
        updated_at=project.updated_at,
    )


def get_owned_project(db: Session, user: User, project_id: UUID) -> Project:
    project = db.scalar(select(Project).where(Project.id == project_id, Project.owner_id == user.id))
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found.")
    return project


def list_projects(db: Session, user: User) -> list[ProjectRead]:
    projects = db.scalars(select(Project).where(Project.owner_id == user.id).order_by(Project.updated_at.desc())).all()
    return [serialize_project(project) for project in projects]


def create_project(db: Session, user: User, request: ProjectCreate) -> ProjectRead:
    project = Project(
        owner_id=user.id,
        startup_name=request.name,
        idea=request.description,
        description=request.description,
        stage=request.stage,
        target_users=request.target_users,
        market=request.market,
        competitors=request.competitors,
        revenue_model=request.revenue_model,
        funding_stage=request.funding_stage,
    )
    db.add(project)
    db.flush()

    memory = ProjectMemory(
        project_id=project.id,
        startup_name=request.name,
        revenue_model=request.revenue_model,
        competitors=request.competitors,
    )
    db.add(memory)
    db.commit()
    db.refresh(project)
    return serialize_project(project)


def update_project(db: Session, user: User, project_id: UUID, request: ProjectUpdate) -> ProjectRead:
    project = get_owned_project(db, user, project_id)
    updates = request.model_dump(exclude_unset=True)
    if "name" in updates:
        project.startup_name = updates["name"]
    if "description" in updates:
        project.description = updates["description"]
        project.idea = updates["description"]
    if "stage" in updates:
        project.stage = updates["stage"]
    for field in ("target_users", "market", "competitors", "revenue_model", "funding_stage"):
        if field in updates:
            setattr(project, field, updates[field])
    db.commit()
    db.refresh(project)
    return serialize_project(project)


def get_or_create_project_memory(db: Session, project: Project) -> ProjectMemory:
    memory = db.scalar(select(ProjectMemory).where(ProjectMemory.project_id == project.id))
    if memory is None:
        memory = ProjectMemory(project_id=project.id, startup_name=project.startup_name)
        db.add(memory)
        db.commit()
        db.refresh(memory)
    return memory


def update_project_memory(db: Session, project: Project, request: ProjectMemoryUpdate) -> ProjectMemory:
    memory = get_or_create_project_memory(db, project)
    updates = request.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(memory, field, value)
    db.commit()
    db.refresh(memory)
    return memory


def create_conversation(db: Session, project: Project, title: str) -> Conversation:
    conversation = Conversation(project_id=project.id, title=title)
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation


def get_project_conversations(db: Session, project: Project) -> list[Conversation]:
    return db.scalars(
        select(Conversation).where(Conversation.project_id == project.id).order_by(Conversation.updated_at.desc())
    ).all()


def get_owned_conversation(db: Session, project: Project, conversation_id: UUID) -> Conversation:
    conversation = db.scalar(
        select(Conversation).where(Conversation.id == conversation_id, Conversation.project_id == project.id)
    )
    if conversation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found.")
    return conversation


def get_conversation_messages(db: Session, conversation: Conversation) -> list[Message]:
    return db.scalars(
        select(Message).where(Message.conversation_id == conversation.id).order_by(Message.created_at.asc())
    ).all()


def store_message(
    db: Session,
    conversation: Conversation,
    *,
    role: MessageRole,
    content: str,
    agent_key: str | None = None,
) -> Message:
    message = Message(conversation_id=conversation.id, role=role, content=content, agent_key=agent_key)
    conversation.updated_at = datetime.now(UTC)
    db.add(message)
    db.add(conversation)
    db.commit()
    db.refresh(message)
    return message
