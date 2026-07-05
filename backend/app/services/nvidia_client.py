from openai import OpenAI
from openai import OpenAIError
from tenacity import retry, stop_after_attempt, wait_exponential

from app.core.config import settings


class AIConfigurationError(RuntimeError):
    pass


class AIProviderError(RuntimeError):
    pass


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

    def _ensure_client(self) -> OpenAI:
        if self._client is None:
            raise AIConfigurationError(
                "NVIDIA_API_KEY is not configured. Add it to backend/.env and restart the API server."
            )
        return self._client

    @retry(wait=wait_exponential(multiplier=1, min=1, max=8), stop=stop_after_attempt(3), reraise=True)
    def complete_messages(self, *, messages: list[dict[str, str]], temperature: float = 0.35) -> str:
        client = self._ensure_client()

        try:
            response = client.chat.completions.create(
                model=settings.nvidia_model,
                messages=messages,
                temperature=temperature,
                max_tokens=settings.ai_max_tokens,
            )
        except OpenAIError as exc:
            raise AIProviderError("NVIDIA Build API request failed.") from exc

        content = response.choices[0].message.content
        if not content:
            raise AIProviderError("NVIDIA Build API returned an empty response.")
        return content

    def complete(self, *, system_prompt: str, user_message: str) -> str:
        return self.complete_messages(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ]
        )


nvidia_client = NvidiaClient()
