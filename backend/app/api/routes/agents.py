from fastapi import APIRouter, Depends

from app.agents.registry import AGENTS
from app.schemas.agent import AgentRead
from app.security.auth import AuthenticatedUser, get_current_user

router = APIRouter()


@router.get("", response_model=list[AgentRead])
async def list_agents(_: AuthenticatedUser = Depends(get_current_user)) -> list[AgentRead]:
    return [
        AgentRead(
            key=agent.key,
            name=agent.name,
            specialty=agent.specialty,
            personality=agent.personality,
        )
        for agent in AGENTS.values()
    ]
