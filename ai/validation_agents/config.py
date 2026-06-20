import os
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


@dataclass(frozen=True)
class ValidationConfig:
    # Primary provider (DeepSeek by default, OpenAI-compatible)
    api_key: str | None
    base_url: str
    chat_model: str
    reasoner_model: str
    # Stage-specific model overrides
    classifier_model: str   # Stage 0: fast + cheap (pit detection)
    iteration_model: str    # Stage 2B: creative divergent framings
    research_model: str     # Stage 1+2: research + gap analysis
    # OpenRouter (optional — gives access to Claude, Qwen, Mistral, etc.)
    openrouter_api_key: str | None
    openrouter_base_url: str
    # Qwen / DashScope (optional — direct Alibaba API)
    qwen_api_key: str | None
    qwen_base_url: str
    output_dir: Path
    use_llm: bool


def load_dotenv(path: Path | None = None) -> None:
    env_path = path or PROJECT_ROOT / ".env"
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def load_config(output_dir: str | Path | None = None, use_llm: bool = True) -> ValidationConfig:
    load_dotenv()
    resolved_output_dir = Path(output_dir) if output_dir else DEFAULT_OUTPUT_DIR
    resolved_output_dir.mkdir(parents=True, exist_ok=True)

    api_key = os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    chat_model = os.getenv("DEEPSEEK_CHAT_MODEL", "deepseek-v4-flash")
    reasoner_model = os.getenv("DEEPSEEK_REASONER_MODEL", "deepseek-v4-flash")

    openrouter_key = os.getenv("OPENROUTER_API_KEY")
    qwen_key = os.getenv("DASHSCOPE_API_KEY") or os.getenv("QWEN_API_KEY")

    # Stage-specific models — can point to any OpenAI-compatible model string.
    # Examples:
    #   CLASSIFIER_MODEL=deepseek-chat               (default, cheap + fast)
    #   CLASSIFIER_MODEL=qwen-plus                   (if DASHSCOPE_API_KEY set)
    #   ITERATION_MODEL=anthropic/claude-3-haiku      (if OPENROUTER_API_KEY set)
    classifier_model = os.getenv("CLASSIFIER_MODEL", chat_model)
    iteration_model = os.getenv("ITERATION_MODEL", reasoner_model)
    research_model = os.getenv("RESEARCH_MODEL", reasoner_model)

    any_key = bool(api_key or openrouter_key or qwen_key)

    return ValidationConfig(
        api_key=api_key,
        base_url=base_url,
        chat_model=chat_model,
        reasoner_model=reasoner_model,
        classifier_model=classifier_model,
        iteration_model=iteration_model,
        research_model=research_model,
        openrouter_api_key=openrouter_key,
        openrouter_base_url=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
        qwen_api_key=qwen_key,
        qwen_base_url=os.getenv("QWEN_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1"),
        output_dir=resolved_output_dir,
        use_llm=use_llm and any_key,
    )
