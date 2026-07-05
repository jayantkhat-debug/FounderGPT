from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import User
from app.security.auth import AuthenticatedUser


def get_or_create_user(db: Session, auth_user: AuthenticatedUser) -> User:
    user = db.scalar(select(User).where(User.clerk_user_id == auth_user.clerk_user_id))
    if user is None:
        user = User(
            clerk_user_id=auth_user.clerk_user_id,
            email=auth_user.email or f"{auth_user.clerk_user_id}@unknown.local",
            full_name=auth_user.full_name,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    changed = False
    if auth_user.email and user.email != auth_user.email:
        user.email = auth_user.email
        changed = True
    if auth_user.full_name and user.full_name != auth_user.full_name:
        user.full_name = auth_user.full_name
        changed = True
    if changed:
        db.commit()
        db.refresh(user)
    return user
