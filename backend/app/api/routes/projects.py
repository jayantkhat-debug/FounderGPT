from uuid import UUID

from fastapi import APIRouter, Depends

from app.schemas.project import ProjectCreate, ProjectRead
from app.security.auth import AuthenticatedUser, get_current_user

router = APIRouter()


@router.get("", response_model=list[ProjectRead])
async def list_projects(_: AuthenticatedUser = Depends(get_current_user)) -> list[ProjectRead]:
    return []


@router.post("", response_model=ProjectRead)
async def create_project(
    request: ProjectCreate,
    _: AuthenticatedUser = Depends(get_current_user),
) -> ProjectRead:
    return ProjectRead(
        id=UUID("00000000-0000-0000-0000-000000000001"),
        startup_name=request.startup_name,
        idea=request.idea,
        target_users=request.target_users,
        market=request.market,
        competitors=request.competitors,
        revenue_model=request.revenue_model,
        funding_stage=request.funding_stage,
        status="draft",
        health_score=None,
    )
