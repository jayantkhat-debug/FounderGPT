from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

from app.core.config import settings


class NvidiaClient:
    def __init__(self) -> None:
        if not settings.nvidia_api_key:
            self._client: OpenAI | None = None
            return

        self._client = OpenAI(
            api_key=settings.nvidia_api_key,
            base_url=str(settings.nvidia_base_url),
            timeout=settings.ai_timeout_seconds,
        )

    @retry(wait=wait_exponential(multiplier=1, min=1, max=8), stop=stop_after_attempt(3))
    def complete(self, *, system_prompt: str, user_message: str) -> str:
        if self._client is None:
            return (
                "NVIDIA_API_KEY is not configured. I can still validate product strategy locally, "
                "but live model responses require a server-side key in backend/.env."
            )

        response = self._client.chat.completions.create(
            model=settings.nvidia_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            temperature=0.35,
        )
        return response.choices[0].message.content or ""


nvidia_client = NvidiaClient()
