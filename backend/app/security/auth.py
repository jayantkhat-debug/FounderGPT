from dataclasses import dataclass

import httpx
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

from app.core.config import settings

bearer_scheme = HTTPBearer(auto_error=False)
_jwks_cache: dict | None = None


@dataclass(frozen=True)
class AuthenticatedUser:
    clerk_user_id: str
    email: str | None = None
    full_name: str | None = None


def _get_jwks() -> dict:
    global _jwks_cache
    if _jwks_cache is None:
        response = httpx.get(settings.clerk_jwks_url, timeout=10)
        response.raise_for_status()
        _jwks_cache = response.json()
    return _jwks_cache


def _decode_clerk_token(token: str) -> AuthenticatedUser:
    if not settings.clerk_jwks_url:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Clerk JWKS is not configured.",
        )

    try:
        header = jwt.get_unverified_header(token)
        kid = header.get("kid")
        key = next((item for item in _get_jwks().get("keys", []) if item.get("kid") == kid), None)
        if key is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unknown Clerk signing key.")

        decode_kwargs = {
            "algorithms": ["RS256"],
            "options": {"verify_aud": bool(settings.clerk_audience)},
        }
        if settings.clerk_issuer:
            decode_kwargs["issuer"] = settings.clerk_issuer
        if settings.clerk_audience:
            decode_kwargs["audience"] = settings.clerk_audience
        claims = jwt.decode(token, key, **decode_kwargs)
    except HTTPException:
        raise
    except (JWTError, httpx.HTTPError) as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Clerk token.") from exc

    subject = claims.get("sub")
    if not subject:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Clerk token is missing subject.")

    email = claims.get("email") or claims.get("primary_email_address")
    full_name = claims.get("name") or claims.get("full_name")
    return AuthenticatedUser(clerk_user_id=subject, email=email, full_name=full_name)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
) -> AuthenticatedUser:
    if credentials is None or not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing bearer token.",
        )

    token = credentials.credentials
    if settings.is_development and token == "dev":
        return AuthenticatedUser(clerk_user_id="dev_user", email="dev@foundergpt.local", full_name="Development Founder")

    return _decode_clerk_token(token)
