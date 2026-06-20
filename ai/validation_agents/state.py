import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class PipelineState:
    idea: str
    state_path: Path
    current_stage: str = "created"
    selected_gap_id: str | None = None
    strategy_approved: bool = False
    artifacts: dict[str, Any] = field(default_factory=dict)
    history: list[dict[str, str]] = field(default_factory=list)

    @classmethod
    def load_or_create(cls, path: Path, idea: str, force: bool = False) -> "PipelineState":
        if path.exists() and not force:
            data = json.loads(path.read_text(encoding="utf-8"))
            return cls(
                idea=data.get("idea", idea),
                state_path=path,
                current_stage=data.get("current_stage", "created"),
                selected_gap_id=data.get("selected_gap_id"),
                strategy_approved=data.get("strategy_approved", False),
                artifacts=data.get("artifacts", {}),
                history=data.get("history", []),
            )
        state = cls(idea=idea, state_path=path)
        state.record("created", "Pipeline state initialized.")
        state.save()
        return state

    def record(self, stage: str, message: str) -> None:
        self.current_stage = stage
        self.history.append({"at": utc_now(), "stage": stage, "message": message})

    def save(self) -> None:
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "idea": self.idea,
            "current_stage": self.current_stage,
            "selected_gap_id": self.selected_gap_id,
            "strategy_approved": self.strategy_approved,
            "artifacts": self.artifacts,
            "history": self.history,
        }
        self.state_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    def put_artifact(self, name: str, value: Any) -> None:
        self.artifacts[name] = value
        self.record(name, f"Artifact '{name}' updated.")
        self.save()

    def require_artifact(self, name: str) -> Any:
        if name not in self.artifacts:
            raise RuntimeError(f"Missing required artifact: {name}")
        return self.artifacts[name]
