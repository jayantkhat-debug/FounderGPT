from functools import cached_property

from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "FounderGPT X API"
    app_env: str = "development"
    api_v1_prefix: str = "/api/v1"
    frontend_origin: str = "http://localhost:3000"

    database_url: str = Field(default="postgresql+psycopg://foundergpt:foundergpt@localhost:5432/foundergpt")

    clerk_issuer: str = ""
    clerk_jwks_url: str = ""

    nvidia_api_key: str = ""
    nvidia_base_url: AnyUrl | str = "https://integrate.api.nvidia.com/v1"
    nvidia_model: str = "meta/llama-3.1-70b-instruct"
    ai_timeout_seconds: float = 45.0

    @cached_property
    def is_development(self) -> bool:
        return self.app_env.lower() == "development"


settings = Settings()
