from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import User
from app.security.auth import AuthenticatedUser, get_current_user
from app.services.user_service import get_or_create_user


def get_current_db_user(
    auth_user: Annotated[AuthenticatedUser, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
) -> User:
    return get_or_create_user(db, auth_user)
