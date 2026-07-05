from fastapi import APIRouter

from app.api.routes import agents, chat, health, projects

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(chat.project_router, prefix="/projects", tags=["chat"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
