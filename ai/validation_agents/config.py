import os
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


@dataclass(frozen=True)
class ValidationConfig:
    api_key: str | None
    base_url: str
    chat_model: str
    reasoner_model: str
    output_dir: Path
    use_llm: bool


def load_dotenv(path: Path | None = None) -> None:
    """Tiny .env loader to avoid adding a dependency just for this CLI."""
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

    return ValidationConfig(
        api_key=api_key,
        base_url=base_url,
        chat_model=os.getenv("DEEPSEEK_CHAT_MODEL", "deepseek-chat"),
        reasoner_model=os.getenv("DEEPSEEK_REASONER_MODEL", "deepseek-reasoner"),
        output_dir=resolved_output_dir,
        use_llm=use_llm and bool(api_key),
    )
