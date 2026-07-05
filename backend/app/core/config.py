from functools import cached_property
from pathlib import Path

from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BACKEND_DIR / ".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "FounderGPT X API"
    app_env: str = "development"
    api_v1_prefix: str = "/api/v1"
    frontend_origin: str = "http://localhost:3000"
    frontend_origins: str = "http://localhost:3000,http://localhost:3001,http://localhost:3002"

    database_url: str = Field(default="postgresql+psycopg://foundergpt:foundergpt@localhost:5432/foundergpt")

    clerk_issuer: str = ""
    clerk_jwks_url: str = ""
    clerk_audience: str = ""

    nvidia_api_key: str = ""
    nvidia_base_url: AnyUrl | str = "https://integrate.api.nvidia.com/v1"
    nvidia_model: str = "meta/llama-3.1-70b-instruct"
    ai_timeout_seconds: float = 45.0
    ai_max_tokens: int = 900

    @cached_property
    def is_development(self) -> bool:
        return self.app_env.lower() == "development"

    @cached_property
    def cors_origins(self) -> list[str]:
        origins = [origin.strip() for origin in self.frontend_origins.split(",") if origin.strip()]
        if self.frontend_origin and self.frontend_origin not in origins:
            origins.append(self.frontend_origin)
        return origins


settings = Settings()
