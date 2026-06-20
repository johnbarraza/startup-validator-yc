"""Batch runner — validates all ideas from a markdown file or inline list.

Parses ``validator_idea`` code blocks from an ideas markdown file, runs each
through the full pipeline, and writes a ranked leaderboard report.

Usage
─────
# Run all ideas from the consolidated file (LLM enabled)
python -m ai.validation_agents.run_batch

# Dry run without LLM (fast, uses deterministic fallbacks)
python -m ai.validation_agents.run_batch --no-llm

# Run only the top N ideas by rank
python -m ai.validation_agents.run_batch --top 3

# Custom ideas file
python -m ai.validation_agents.run_batch --ideas-file docs/my_ideas.md

# Force recompute all (ignore cached state)
python -m ai.validation_agents.run_batch --force
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import PROJECT_ROOT, DEFAULT_OUTPUT_DIR, load_config
from .run_pipeline import idea_key

DEFAULT_IDEAS_FILE = PROJECT_ROOT / "docs" / "ideas_consolidadas_para_validacion.md"
LEADERBOARD_PATH = PROJECT_ROOT / "docs" / "leaderboard.md"


def extract_ideas_from_md(md_path: Path) -> list[dict[str, str]]:
    """Extract validator_idea code blocks from a markdown file."""
    text = md_path.read_text(encoding="utf-8", errors="ignore")

    # Match sections: ## N. Name ... validator_idea: ```text ... ```
    section_pattern = re.compile(
        r"^## \d+\.\s+(.+?)$.*?validator_idea.*?```(?:text)?\s*\n(.*?)```",
        re.MULTILINE | re.DOTALL,
    )
    ideas = []
    for match in section_pattern.finditer(text):
        name = match.group(1).strip()
        idea = match.group(2).strip()
        if idea:
            ideas.append({"name": name, "idea": idea})

    if not ideas:
        # Fallback: extract any ```text blocks
        for block in re.finditer(r"```text\s*\n(.*?)```", text, re.DOTALL):
            idea = block.group(1).strip()
            if idea and len(idea) > 20:
                ideas.append({"name": idea[:40], "idea": idea})

    return ideas


def run_single(idea_text: str, args: argparse.Namespace) -> dict[str, Any]:
    """Run pipeline for one idea via subprocess, return parsed summary."""
    cmd = [
        sys.executable, "-m", "ai.validation_agents.run_pipeline",
        "--idea", idea_text,
        "--auto", "--json",
        "--regions", args.regions,
    ]
    if args.force:
        cmd.append("--force")
    if args.no_llm:
        cmd.append("--no-llm")
    if args.force_pit:
        cmd.append("--force-pit")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(PROJECT_ROOT),
            timeout=600,
        )
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        # Extract JSON artifact dump (last JSON object in stdout)
        artifacts: dict[str, Any] = {}
        for line in reversed(stdout.splitlines()):
            line = line.strip()
            if line.startswith("{"):
                try:
                    artifacts = json.loads(line)
                    break
                except json.JSONDecodeError:
                    pass

        # Also try last { ... } block spanning multiple lines
        if not artifacts:
            json_match = re.search(r"\{.*\}", stdout, re.DOTALL)
            if json_match:
                try:
                    artifacts = json.loads(json_match.group())
                except json.JSONDecodeError:
                    pass

        # Extract key signals from artifacts
        classify = artifacts.get("stage0_classify", {})
        dossier = artifacts.get("stage3c_dossier", {})
        simulation = artifacts.get("stage3b_simulation", {})
        winner = artifacts.get("stage3_winner_iteration", {})
        validation = artifacts.get("stage3_validation", {})

        total_score = dossier.get("total_score")
        max_score = dossier.get("max_score", 100)
        if total_score is None:
            sc = dossier.get("scorecard", {})
            if isinstance(sc, dict):
                total_score = sum(v for v in sc.values() if isinstance(v, (int, float)))

        return {
            "idea": idea_text,
            "status": "ok" if result.returncode in (0, 1) else "error",
            "returncode": result.returncode,
            "problem_type": classify.get("problem_type", "?"),
            "proceed": classify.get("proceed_recommendation", "?"),
            "devil": classify.get("devil_verdict", "?"),
            "freemium": classify.get("freemium_recommendation", "?"),
            "vertical": classify.get("vertical", "?"),
            "hardest_assumption": classify.get("hardest_assumption", ""),
            "payment_blocker": classify.get("payment_blocker", ""),
            "winner_angle": winner.get("angle", "?"),
            "go_no_go": validation.get("go_no_go", "?"),
            "sim_score": simulation.get("aggregate_score", "?"),
            "total_score": total_score,
            "max_score": max_score,
            "rating": dossier.get("rating", ""),
            "stderr_tail": stderr[-300:] if stderr else "",
        }
    except subprocess.TimeoutExpired:
        return {"idea": idea_text, "status": "timeout", "returncode": -1}
    except Exception as exc:
        return {"idea": idea_text, "status": "error", "error": str(exc), "returncode": -1}


def _score_for_rank(r: dict[str, Any]) -> float:
    """Compute ranking score for leaderboard sort."""
    s = float(r.get("total_score") or 0)
    if r.get("proceed") == "PROCEED":
        s += 20
    elif r.get("proceed") == "WARN":
        s += 5
    if r.get("devil") == "STRONG":
        s += 10
    elif r.get("devil") == "FATAL":
        s -= 20
    if str(r.get("go_no_go", "")).upper() in ("TRUE", "GO", "YES"):
        s += 10
    sim = r.get("sim_score")
    if isinstance(sim, (int, float)):
        s += sim * 10
    return s


def build_leaderboard(results: list[dict[str, Any]], ideas: list[dict[str, str]]) -> str:
    ranked = sorted(results, key=_score_for_rank, reverse=True)
    name_map = {r["idea"]: r.get("_name", r["idea"][:40]) for r in results}

    rows = ["| Rank | Name | Type | Proceed | Devil | Freemium | Winner | Score | Sim | Rating |",
            "|---:|---|---|---|---|---|---|---:|---:|---|"]

    for i, r in enumerate(ranked, 1):
        name = name_map.get(r["idea"], r["idea"][:35])
        score_str = f"{r.get('total_score','?')}/{r.get('max_score','?')}"
        sim = r.get("sim_score")
        sim_str = f"{sim:.2f}" if isinstance(sim, float) else str(sim)
        rows.append(
            f"| {i} | {name} | {r.get('problem_type','?')} "
            f"| {r.get('proceed','?')} | {r.get('devil','?')} "
            f"| {r.get('freemium','?')} | {r.get('winner_angle','?')} "
            f"| {score_str} | {sim_str} | {str(r.get('rating',''))[:40]} |"
        )

    detail_lines = ["\n---\n## Detail per idea\n"]
    for r in ranked:
        name = name_map.get(r["idea"], r["idea"][:40])
        detail_lines.append(f"\n### {name}")
        detail_lines.append(f"- **Type:** {r.get('problem_type')} | **Proceed:** {r.get('proceed')} | **Devil:** {r.get('devil')}")
        detail_lines.append(f"- **Freemium:** {r.get('freemium')} — {r.get('payment_blocker','')}")
        detail_lines.append(f"- **Hardest assumption:** {r.get('hardest_assumption','')}")
        detail_lines.append(f"- **Winner angle:** {r.get('winner_angle')} → YC: {r.get('go_no_go')}")
        detail_lines.append(f"- **Score:** {r.get('total_score')}/{r.get('max_score')} — {r.get('rating','')}")
        if r.get("status") != "ok":
            detail_lines.append(f"- **Status:** {r.get('status')} rc={r.get('returncode')}")

    return f"""# Startup Idea Leaderboard

Generated: {datetime.now(timezone.utc).isoformat()}
Ideas evaluated: {len(results)}

## Ranking

{chr(10).join(rows)}

{chr(10).join(detail_lines)}
"""


def run_batch(args: argparse.Namespace) -> int:
    ideas_file = Path(args.ideas_file)
    if not ideas_file.exists():
        print(f"Ideas file not found: {ideas_file}")
        return 1

    ideas = extract_ideas_from_md(ideas_file)
    if not ideas:
        print(f"No validator_idea blocks found in {ideas_file}")
        return 1

    if args.top:
        ideas = ideas[: args.top]

    print(f"\nBatch validation: {len(ideas)} ideas from {ideas_file.name}")
    print("=" * 60)

    results = []
    for i, entry in enumerate(ideas, 1):
        name = entry["name"]
        idea_text = entry["idea"]
        print(f"\n[{i}/{len(ideas)}] {name}")
        print(f"  {idea_text[:80]}...")
        r = run_single(idea_text, args)
        r["_name"] = name
        results.append(r)
        print(
            f"  → {r.get('problem_type','?')} | proceed={r.get('proceed','?')} "
            f"| devil={r.get('devil','?')} | score={r.get('total_score','?')}"
        )

    leaderboard = build_leaderboard(results, ideas)
    LEADERBOARD_PATH.write_text(leaderboard, encoding="utf-8")
    print(f"\nLeaderboard written: {LEADERBOARD_PATH}")
    print("\n" + leaderboard[:800])
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Batch validate multiple startup ideas.")
    parser.add_argument(
        "--ideas-file",
        default=str(DEFAULT_IDEAS_FILE),
        help="Markdown file with validator_idea blocks.",
    )
    parser.add_argument("--top", type=int, default=0, help="Only run top N ideas.")
    parser.add_argument("--regions", default="Peru,LATAM,USA")
    parser.add_argument("--force", action="store_true", help="Force recompute all stages.")
    parser.add_argument("--force-pit", action="store_true", help="Continue even on PIT/ABORT.")
    parser.add_argument("--no-llm", action="store_true", help="Use deterministic fallbacks.")
    return parser


def main() -> int:
    return run_batch(build_parser().parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
