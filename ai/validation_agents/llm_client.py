"""Multi-provider LLM client.

Provider routing by model name prefix:
  openrouter/<model>  → OpenRouter API  (OPENROUTER_API_KEY required)
  qwen/<model>        → DashScope/Qwen  (DASHSCOPE_API_KEY required)
  <anything else>     → Primary provider (DEEPSEEK_API_KEY / OPENAI_API_KEY)

Examples:
  deepseek-chat                         → DeepSeek (default)
  deepseek-reasoner                     → DeepSeek reasoner
  openrouter/anthropic/claude-3-haiku   → Claude via OpenRouter
  openrouter/qwen/qwen-plus             → Qwen via OpenRouter
  qwen/qwen-plus                        → Qwen direct (DashScope)
"""
import json
from typing import Any, Callable

from .config import ValidationConfig


FallbackFactory = Callable[[], dict[str, Any]]

_OPENROUTER_PREFIX = "openrouter/"
_QWEN_PREFIX = "qwen/"


def _resolve_provider(
    model: str, config: ValidationConfig
) -> tuple[str | None, str, str]:
    """Return (api_key, base_url, resolved_model_name)."""
    if model.startswith(_OPENROUTER_PREFIX):
        resolved = model[len(_OPENROUTER_PREFIX):]
        return config.openrouter_api_key, config.openrouter_base_url, resolved
    if model.startswith(_QWEN_PREFIX):
        resolved = model[len(_QWEN_PREFIX):]
        return config.qwen_api_key, config.qwen_base_url, resolved
    return config.api_key, config.base_url, model


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

    def _get_openai_client(self, model: str):
        """Return an openai.OpenAI client for the given model's provider."""
        import openai
        api_key, base_url, _ = _resolve_provider(model, self.config)
        if not api_key:
            return None
        return openai.OpenAI(api_key=api_key, base_url=base_url)

    def json_completion(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        model: str,
        temperature: float,
        fallback: FallbackFactory,
    ) -> dict[str, Any]:
        _, _, resolved_model = _resolve_provider(model, self.config)

        # Use provider-specific client if model has a prefix, else use primary
        if model.startswith((_OPENROUTER_PREFIX, _QWEN_PREFIX)):
            active_client = self._get_openai_client(model)
        else:
            active_client = self._client

        if not active_client:
            result = fallback()
            result.setdefault("source", "deterministic_fallback")
            if self.init_error:
                result["llm_error"] = self.init_error
            return result

        try:
            response = active_client.chat.completions.create(
                model=resolved_model,
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
