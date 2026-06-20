import json
from typing import Any, Callable

from .config import ValidationConfig


FallbackFactory = Callable[[], dict[str, Any]]


class LLMClient:
    def __init__(self, config: ValidationConfig):
        self.config = config
        self._client = None
        self.init_error: str | None = None
        if config.use_llm:
            try:
                import openai

                self._client = openai.OpenAI(
                    api_key=config.api_key,
                    base_url=config.base_url,
                )
            except Exception as exc:
                self.init_error = str(exc)
                self._client = None

    @property
    def enabled(self) -> bool:
        return self._client is not None

    def json_completion(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        model: str,
        temperature: float,
        fallback: FallbackFactory,
    ) -> dict[str, Any]:
        if not self._client:
            result = fallback()
            result.setdefault("source", "deterministic_fallback")
            if self.init_error:
                result["llm_error"] = self.init_error
            return result

        try:
            response = self._client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                response_format={"type": "json_object"},
                temperature=temperature,
            )
            content = response.choices[0].message.content or "{}"
            result = json.loads(content)
            result.setdefault("source", "llm")
            return result
        except Exception as exc:
            result = fallback()
            result.setdefault("source", "deterministic_fallback")
            result["llm_error"] = str(exc)
            return result
