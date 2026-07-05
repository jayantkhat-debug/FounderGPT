from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserRead
from app.security.auth import AuthenticatedUser, get_current_user
from app.services.user_service import get_or_create_user

router = APIRouter()


@router.get("/me", response_model=UserRead)
async def get_me(
    auth_user: AuthenticatedUser = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> UserRead:
    return get_or_create_user(db, auth_user)
