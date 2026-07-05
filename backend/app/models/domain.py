import enum
import uuid
from datetime import date, datetime
from typing import Any

from sqlalchemy import Date, DateTime, Enum, ForeignKey, Integer, Numeric, String, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class ProjectStatus(str, enum.Enum):
    draft = "draft"
    validating = "validating"
    building = "building"
    fundraising = "fundraising"
    scaling = "scaling"
    archived = "archived"


class MessageRole(str, enum.Enum):
    system = "system"
    user = "user"
    assistant = "assistant"
    tool = "tool"


class MemoryKind(str, enum.Enum):
    startup_profile = "startup_profile"
    customer = "customer"
    market = "market"
    competitor = "competitor"
    revenue = "revenue"
    goal = "goal"
    roadmap = "roadmap"
    risk = "risk"
    insight = "insight"


class DocumentKind(str, enum.Enum):
    business_plan = "business_plan"
    pitch_deck = "pitch_deck"
    market_research = "market_research"
    yc_application = "yc_application"
    financial_model = "financial_model"
    markdown = "markdown"
    json = "json"


class ExportStatus(str, enum.Enum):
    draft = "draft"
    queued = "queued"
    exported = "exported"
    failed = "failed"


class TaskPriority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class TaskStatus(str, enum.Enum):
    todo = "todo"
    doing = "doing"
    blocked = "blocked"
    done = "done"


class RoadmapHorizon(str, enum.Enum):
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"
    quarterly = "quarterly"


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    clerk_user_id: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(320), index=True)
    full_name: Mapped[str | None] = mapped_column(String(255))

    projects: Mapped[list["Project"]] = relationship(back_populates="owner")


class Project(Base, TimestampMixin):
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), index=True)
    startup_name: Mapped[str] = mapped_column(String(180))
    idea: Mapped[str] = mapped_column(Text)
    description: Mapped[str | None] = mapped_column(Text)
    target_users: Mapped[str | None] = mapped_column(Text)
    market: Mapped[str | None] = mapped_column(Text)
    competitors: Mapped[list[dict[str, Any]]] = mapped_column(JSONB, default=list)
    revenue_model: Mapped[str | None] = mapped_column(Text)
    funding_stage: Mapped[str | None] = mapped_column(String(80))
    stage: Mapped[str] = mapped_column(String(80), default="Idea")
    status: Mapped[ProjectStatus] = mapped_column(Enum(ProjectStatus), default=ProjectStatus.draft)
    health_score: Mapped[int | None] = mapped_column(Integer)

    owner: Mapped[User] = relationship(back_populates="projects")
    conversations: Mapped[list["Conversation"]] = relationship(back_populates="project")
    memory: Mapped["ProjectMemory | None"] = relationship(back_populates="project", uselist=False)


class ProjectMemory(Base, TimestampMixin):
    __tablename__ = "project_memories"
    __table_args__ = (UniqueConstraint("project_id", name="uq_project_memories_project_id"),)

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"), index=True)
    startup_name: Mapped[str | None] = mapped_column(String(180))
    problem: Mapped[str | None] = mapped_column(Text)
    solution: Mapped[str | None] = mapped_column(Text)
    customer: Mapped[str | None] = mapped_column(Text)
    revenue_model: Mapped[str | None] = mapped_column(Text)
    pricing: Mapped[str | None] = mapped_column(Text)
    competitors: Mapped[list[dict[str, Any]]] = mapped_column(JSONB, default=list)
    goals: Mapped[list[dict[str, Any]]] = mapped_column(JSONB, default=list)

    project: Mapped[Project] = relationship(back_populates="memory")


class Conversation(Base, TimestampMixin):
    __tablename__ = "conversations"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id"), index=True)
    title: Mapped[str] = mapped_column(String(180), default="Founder strategy session")

    project: Mapped[Project] = relationship(back_populates="conversations")
    messages: Mapped[list["Message"]] = relationship(back_populates="conversation")


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("conversations.id"), index=True)
    agent_key: Mapped[str | None] = mapped_column(String(80), index=True)
    role: Mapped[MessageRole] = mapped_column(Enum(MessageRole), index=True)
    content: Mapped[str] = mapped_column(Text)
    message_metadata: Mapped[dict[str, Any]] = mapped_column("metadata", JSONB, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), index=True)

    conversation: Mapped[Conversation] = relationship(back_populates="messages")


class Memory(Base, TimestampMixin):
    __tablename__ = "memories"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id"), index=True)
    kind: Mapped[MemoryKind] = mapped_column(Enum(MemoryKind), index=True)
    content: Mapped[dict[str, Any]] = mapped_column(JSONB)
    confidence: Mapped[float] = mapped_column(Numeric(3, 2), default=0.7)
    source_message_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))


class Document(Base, TimestampMixin):
    __tablename__ = "documents"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id"), index=True)
    kind: Mapped[DocumentKind] = mapped_column(Enum(DocumentKind), index=True)
    title: Mapped[str] = mapped_column(String(180))
    content: Mapped[dict[str, Any]] = mapped_column(JSONB)
    export_status: Mapped[ExportStatus] = mapped_column(Enum(ExportStatus), default=ExportStatus.draft)


class Task(Base, TimestampMixin):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id"), index=True)
    title: Mapped[str] = mapped_column(String(220))
    description: Mapped[str | None] = mapped_column(Text)
    priority: Mapped[TaskPriority] = mapped_column(Enum(TaskPriority), default=TaskPriority.medium)
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus), default=TaskStatus.todo)
    due_date: Mapped[date | None] = mapped_column(Date)


class Roadmap(Base, TimestampMixin):
    __tablename__ = "roadmaps"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id"), index=True)
    horizon: Mapped[RoadmapHorizon] = mapped_column(Enum(RoadmapHorizon), index=True)
    title: Mapped[str] = mapped_column(String(180))
    items: Mapped[list[dict[str, Any]]] = mapped_column(JSONB, default=list)
