"""Batch runner — two modes.

──────────────────────────────────────────────────────────────────────────
MODE 1: BATCH  (default)
  Run all ideas independently through the full pipeline.
  Each idea gets its own score. Final output: ranked leaderboard.

  python -m ai.validation_agents.run_batch
  python -m ai.validation_agents.run_batch --top 5

──────────────────────────────────────────────────────────────────────────
MODE 2: TOURNAMENT  (--tournament)
  3-round elimination bracket. Cheap stages first, expensive last.

  Round 1 — Stage 0 only (direct import, ~$0.01/idea, ALL ideas in parallel)
    Eliminates: proceed=ABORT and devil=FATAL (true pit ideas, no chance)
    Advances: PROCEED + WARN + ABORT with devil!=FATAL (weak ideas get a shot)

  Round 2 — Stage 1→3 via full pipeline (subprocess, survivors only)
    Runs research + gaps + 3 iterations + YC validation for each survivor.
    Eliminates: bottom N ideas by Stage 3 composite score.
    Advances: top --finalists (default 3)

  Round 3 (Final) — Stage 3B+3C (already ran in Round 2, just filters results)
    Compares finalists on MiroFish simulation score + Stage 3C dossier score.
    Declares winner and runner-up.

  python -m ai.validation_agents.run_batch --tournament
  python -m ai.validation_agents.run_batch --tournament --finalists 4

──────────────────────────────────────────────────────────────────────────
"""
import argparse
import concurrent.futures
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_IDEAS_FILE = Path(__file__).resolve().parents[2] / "docs" / "ideas_consolidadas_para_validacion.md"
LEADERBOARD_PATH = Path(__file__).resolve().parents[2] / "docs" / "leaderboard.md"
TOURNAMENT_PATH = Path(__file__).resolve().parents[2] / "docs" / "tournament.md"


# ── Markdown parser ──────────────────────────────────────────────────────────

def extract_ideas_from_md(md_path: Path) -> list[dict[str, str]]:
    text = md_path.read_text(encoding="utf-8", errors="ignore")
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
        for block in re.finditer(r"```text\s*\n(.*?)```", text, re.DOTALL):
            idea = block.group(1).strip()
            if idea and len(idea) > 20:
                ideas.append({"name": idea[:40], "idea": idea})
    return ideas


# ── Subprocess runner (full pipeline) ────────────────────────────────────────

def _read_state_artifacts(idea_text: str) -> dict[str, Any]:
    """Read pipeline artifacts from state.json on disk (more reliable than stdout parsing)."""
    from .config import DEFAULT_OUTPUT_DIR
    from .run_pipeline import idea_key
    run_key = idea_key(idea_text)
    state_path = DEFAULT_OUTPUT_DIR / run_key / "state.json"
    if not state_path.exists():
        return {}
    try:
        state_data = json.loads(state_path.read_text(encoding="utf-8"))
        return state_data.get("artifacts", {})
    except Exception:
        return {}


def _extract_summary(idea_text: str, returncode: int, artifacts: dict[str, Any]) -> dict[str, Any]:
    classify = artifacts.get("stage0_classify", {})
    dossier = artifacts.get("stage3c_dossier", {})
    simulation = artifacts.get("stage3b_simulation", {})
    winner = artifacts.get("stage3_winner_iteration", {})
    validation = artifacts.get("stage3_validation", {})

    total_score = dossier.get("total_score")
    if total_score is None:
        sc = dossier.get("scorecard", {})
        if isinstance(sc, dict):
            total_score = sum(v for v in sc.values() if isinstance(v, (int, float)))

    return {
        "idea": idea_text,
        "status": "ok" if returncode in (0, 1) else "error",
        "returncode": returncode,
        "problem_type": classify.get("problem_type", "?"),
        "proceed": classify.get("proceed_recommendation", "?"),
        "devil": classify.get("devil_verdict", "?"),
        "freemium": classify.get("freemium_recommendation", "?"),
        "vertical": classify.get("vertical", "?"),
        "hardest_assumption": classify.get("hardest_assumption", ""),
        "payment_blocker": classify.get("payment_blocker", ""),
        "free_sub_risk": classify.get("free_substitute_risk", ""),
        "winner_angle": winner.get("angle", "?"),
        "go_no_go": validation.get("go_no_go", "?"),
        "sim_score": simulation.get("aggregate_score"),
        "total_score": total_score,
        "max_score": dossier.get("max_score", 100),
        "rating": dossier.get("rating", ""),
    }


def _run_full_pipeline(idea_text: str, args: argparse.Namespace) -> dict[str, Any]:
    cmd = [
        sys.executable, "-m", "ai.validation_agents.run_pipeline",
        "--idea", idea_text,
        "--auto",
        "--regions", args.regions,
    ]
    if args.force:
        cmd.append("--force")
    if args.no_llm:
        cmd.append("--no-llm")
    if args.force_pit:
        cmd.append("--force-pit")
    if getattr(args, "verbose", False):
        cmd.append("--verbose")

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True,
            cwd=str(Path(__file__).resolve().parents[2]),
            timeout=600,
        )
        # Read artifacts from state.json (written by pipeline regardless of flags)
        artifacts = _read_state_artifacts(idea_text)
        return _extract_summary(idea_text, result.returncode, artifacts)
    except subprocess.TimeoutExpired:
        return {"idea": idea_text, "status": "timeout", "returncode": -1}
    except Exception as exc:
        return {"idea": idea_text, "status": "error", "error": str(exc), "returncode": -1}


# ── Stage 0 direct (no subprocess) ───────────────────────────────────────────

def _run_stage0_direct(entry: dict[str, str], args: argparse.Namespace) -> dict[str, Any]:
    from .config import load_config
    from .llm_client import LLMClient
    from .run_pipeline import read_yc_context
    from .stages.stage0_classify import run_stage0_classify

    config = load_config(use_llm=not args.no_llm)
    client = LLMClient(config)
    context = read_yc_context()
    classification = run_stage0_classify(client, config, entry["idea"], context)
    return {
        "idea": entry["idea"],
        "_name": entry["name"],
        "problem_type": classification.get("problem_type", "?"),
        "proceed": classification.get("proceed_recommendation", "?"),
        "devil": classification.get("devil_verdict", "?"),
        "freemium": classification.get("freemium_recommendation", "?"),
        "vertical": classification.get("vertical", "?"),
        "hardest_assumption": classification.get("hardest_assumption", ""),
        "payment_blocker": classification.get("payment_blocker", ""),
        "free_sub_risk": classification.get("free_substitute_risk", ""),
        "market_reality": classification.get("market_size_reality_check", ""),
        "classification_rationale": classification.get("classification_rationale", ""),
        "devil_rationale": classification.get("devil_rationale", ""),
    }


# ── Scoring ───────────────────────────────────────────────────────────────────

def _composite_score(r: dict[str, Any]) -> float:
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


def _stage3_score(r: dict[str, Any]) -> float:
    """Score based only on Stage 3 YC validation for Round 2 elimination."""
    s = 0.0
    go = str(r.get("go_no_go", "")).upper()
    if go in ("TRUE", "GO", "YES"):
        s += 30
    elif go in ("FALSE", "NO_GO", "NO"):
        s -= 10
    if r.get("proceed") == "PROCEED":
        s += 15
    elif r.get("proceed") == "WARN":
        s += 5
    if r.get("devil") in ("STRONG", None):
        s += 5
    elif r.get("devil") == "FATAL":
        s -= 15
    return s


# ── Report builders ───────────────────────────────────────────────────────────

def _row(r: dict[str, Any], rank: int, extra: str = "") -> str:
    name = r.get("_name", r["idea"][:35])
    score_str = f"{r.get('total_score','?')}/{r.get('max_score','?')}"
    sim = r.get("sim_score")
    sim_str = f"{sim:.2f}" if isinstance(sim, float) else str(sim or "?")
    return (
        f"| {rank} | {name}{extra} | {r.get('problem_type','?')} "
        f"| {r.get('proceed','?')} | {r.get('devil','?')} "
        f"| {r.get('freemium','?')} | {r.get('winner_angle','?')} "
        f"| {score_str} | {sim_str} | {str(r.get('rating',''))[:35]} |"
    )


def _table_header() -> list[str]:
    return [
        "| Rank | Name | Type | Proceed | Devil | Freemium | Winner | Score | Sim | Rating |",
        "|---:|---|---|---|---|---|---|---:|---:|---|",
    ]


def build_leaderboard(results: list[dict[str, Any]]) -> str:
    ranked = sorted(results, key=_composite_score, reverse=True)
    rows = _table_header()
    for i, r in enumerate(ranked, 1):
        rows.append(_row(r, i))

    details = ["\n---\n## Detail\n"]
    for r in ranked:
        details.append(f"\n### {r.get('_name', r['idea'][:40])}")
        details.append(f"- **Type:** {r.get('problem_type')} | **Proceed:** {r.get('proceed')} | **Devil:** {r.get('devil')}")
        details.append(f"- **Payment blocker:** {r.get('payment_blocker','')}")
        details.append(f"- **Free substitute risk:** {r.get('free_sub_risk','')}")
        details.append(f"- **Hardest assumption:** {r.get('hardest_assumption','')}")
        details.append(f"- **Winner angle:** {r.get('winner_angle','?')} → YC: {r.get('go_no_go','?')}")
        details.append(f"- **Score:** {r.get('total_score','?')}/{r.get('max_score','?')} | Sim: {r.get('sim_score','?')} | {r.get('rating','')}")

    return (
        f"# Startup Idea Leaderboard\n\nGenerated: {datetime.now(timezone.utc).isoformat()}\n"
        f"Ideas: {len(results)}\n\n## Ranking\n\n"
        + "\n".join(rows) + "\n" + "\n".join(details) + "\n"
    )


def build_tournament_report(
    r1_all: list[dict[str, Any]],
    r1_eliminated: list[dict[str, Any]],
    r2_all: list[dict[str, Any]],
    r2_eliminated: list[dict[str, Any]],
    finalists: list[dict[str, Any]],
) -> str:
    winner = finalists[0] if finalists else {}
    runner_up = finalists[1] if len(finalists) > 1 else {}

    def _elim_rows(items: list[dict[str, Any]]) -> str:
        lines = []
        for r in items:
            lines.append(
                f"- **{r.get('_name', r['idea'][:40])}** — "
                f"{r.get('problem_type','?')} | devil={r.get('devil','?')} | "
                f"{r.get('devil_rationale', r.get('classification_rationale',''))[:100]}"
            )
        return "\n".join(lines) or "_(none)_"

    finalist_rows = _table_header()
    for i, r in enumerate(finalists, 1):
        mark = " 🏆" if i == 1 else (" 🥈" if i == 2 else "")
        finalist_rows.append(_row(r, i, mark))

    return f"""# Startup Idea Tournament

Generated: {datetime.now(timezone.utc).isoformat()}

---

## Round 1 — Pit Check (Stage 0, all {len(r1_all)} ideas)

Filter: ABORT + devil=FATAL → eliminated

### Eliminated ({len(r1_eliminated)})
{_elim_rows(r1_eliminated)}

### Advanced to Round 2 ({len(r1_all) - len(r1_eliminated)})
{_elim_rows([r for r in r1_all if r not in r1_eliminated])}

---

## Round 2 — YC Validation (Stage 1→3, {len(r2_all)} survivors)

Filter: bottom ideas by Stage 3 composite score → eliminated

### Eliminated ({len(r2_eliminated)})
{_elim_rows(r2_eliminated)}

### Finalists ({len(finalists)})
{chr(10).join(finalist_rows)}

---

## Final — MiroFish + Dossier (Stage 3B+3C)

{chr(10).join(finalist_rows)}

### 🏆 Winner: {winner.get('_name', '?')}
- Type: {winner.get('problem_type','?')} | Proceed: {winner.get('proceed','?')} | Devil: {winner.get('devil','?')}
- Winner iteration: {winner.get('winner_angle','?')} → YC: {winner.get('go_no_go','?')}
- Simulation score: {winner.get('sim_score','?')} / gate=0.60
- Dossier score: {winner.get('total_score','?')}/{winner.get('max_score','?')}
- {winner.get('rating','')}
- **Hardest assumption to validate next:** {winner.get('hardest_assumption','')}
- **Payment blocker to resolve:** {winner.get('payment_blocker','')}

### 🥈 Runner-up: {runner_up.get('_name', '?') if runner_up else 'N/A'}
{f"- Score: {runner_up.get('total_score','?')}/{runner_up.get('max_score','?')} | {runner_up.get('rating','')}" if runner_up else ""}

---

## Cost estimate
- Round 1 (Stage 0 × {len(r1_all)} parallel): ~${len(r1_all) * 0.01:.2f}
- Round 2 (full pipeline × {len(r2_all)}): ~${len(r2_all) * 0.10:.2f}
- Total: ~${len(r1_all) * 0.01 + len(r2_all) * 0.10:.2f} vs full batch ~${len(r1_all) * 0.15:.2f}
"""


# ── Batch mode ────────────────────────────────────────────────────────────────

def run_batch(args: argparse.Namespace) -> int:
    ideas_file = _require_ideas_file(args)
    ideas = extract_ideas_from_md(ideas_file)
    if not ideas:
        print(f"No validator_idea blocks found in {ideas_file}")
        return 1
    if args.top:
        ideas = ideas[: args.top]

    print(f"\nBATCH MODE — {len(ideas)} ideas from {ideas_file.name}")
    print("=" * 60)
    results = []
    for i, entry in enumerate(ideas, 1):
        print(f"\n[{i}/{len(ideas)}] {entry['name']}")
        r = _run_full_pipeline(entry["idea"], args)
        r["_name"] = entry["name"]
        results.append(r)
        print(f"  → {r.get('problem_type','?')} | proceed={r.get('proceed','?')} | devil={r.get('devil','?')} | score={r.get('total_score','?')}")

    report = build_leaderboard(results)
    LEADERBOARD_PATH.write_text(report, encoding="utf-8")
    print(f"\nLeaderboard → {LEADERBOARD_PATH}")
    print("\n" + report[:600])
    return 0


# ── Tournament mode ───────────────────────────────────────────────────────────

def run_tournament(args: argparse.Namespace) -> int:
    ideas_file = _require_ideas_file(args)
    ideas = extract_ideas_from_md(ideas_file)
    if not ideas:
        print(f"No validator_idea blocks found in {ideas_file}")
        return 1
    if args.top:
        ideas = ideas[: args.top]

    print(f"\nTOURNAMENT MODE — {len(ideas)} ideas | finalists={args.finalists}")
    print("=" * 60)

    # ── Round 1: Stage 0 in parallel ─────────────────────────────────────────
    print(f"\n[ROUND 1] Pit check — {len(ideas)} ideas (parallel Stage 0)...")
    r1_results: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(ideas), 5)) as ex:
        future_to_entry = {ex.submit(_run_stage0_direct, e, args): e for e in ideas}
        for future in concurrent.futures.as_completed(future_to_entry):
            entry = future_to_entry[future]
            try:
                r = future.result()
            except Exception as exc:
                r = {"idea": entry["idea"], "_name": entry["name"],
                     "proceed": "WARN", "devil": "WEAK", "error": str(exc)}
            r.setdefault("_name", entry["name"])
            r1_results.append(r)
            print(f"  {r['_name'][:35]:35} → {r.get('proceed','?'):7} devil={r.get('devil','?')}")

    # Eliminate: ABORT + FATAL devil (true pit — no redemption)
    eliminated_r1 = [
        r for r in r1_results
        if r.get("proceed") == "ABORT" and r.get("devil") == "FATAL"
    ]
    survivors_r1 = [r for r in r1_results if r not in eliminated_r1]

    print(f"\n  Eliminated R1: {len(eliminated_r1)} | Advancing: {len(survivors_r1)}")
    for e in eliminated_r1:
        print(f"  ✗ {e['_name']} — {e.get('classification_rationale','')[:80]}")

    if not survivors_r1:
        print("All ideas eliminated in Round 1. Refine your ideas.")
        return 1

    # ── Round 2: Full pipeline for survivors ─────────────────────────────────
    survivor_ideas = [
        next((e for e in ideas if e["idea"] == r["idea"]), {"idea": r["idea"], "name": r["_name"]})
        for r in survivors_r1
    ]
    print(f"\n[ROUND 2] Full pipeline — {len(survivor_ideas)} survivors...")
    r2_results: list[dict[str, Any]] = []
    for i, entry in enumerate(survivor_ideas, 1):
        print(f"  [{i}/{len(survivor_ideas)}] {entry['name']}")
        r = _run_full_pipeline(entry["idea"], args)
        # Merge Round 1 classification data
        r1_data = next((x for x in survivors_r1 if x["idea"] == entry["idea"]), {})
        r.update({k: v for k, v in r1_data.items() if k not in r or not r[k]})
        r["_name"] = entry["name"]
        r2_results.append(r)
        print(f"    → go_no_go={r.get('go_no_go','?')} | score={r.get('total_score','?')} | sim={r.get('sim_score','?')}")

    # Rank by Stage 3 composite, keep top finalists
    r2_ranked = sorted(r2_results, key=_stage3_score, reverse=True)
    n_finalists = min(args.finalists, len(r2_ranked))
    finalists = r2_ranked[:n_finalists]
    eliminated_r2 = r2_ranked[n_finalists:]

    print(f"\n  Eliminated R2: {len(eliminated_r2)} | Finalists: {len(finalists)}")

    # ── Final: rank finalists by full composite score ─────────────────────────
    finalists_ranked = sorted(finalists, key=_composite_score, reverse=True)

    print(f"\n[FINAL] {len(finalists_ranked)} finalists ranked by MiroFish + dossier score:")
    for i, r in enumerate(finalists_ranked, 1):
        print(f"  #{i} {r.get('_name','?')} — score={r.get('total_score','?')} sim={r.get('sim_score','?')}")

    report = build_tournament_report(
        r1_all=r1_results,
        r1_eliminated=eliminated_r1,
        r2_all=r2_results,
        r2_eliminated=eliminated_r2,
        finalists=finalists_ranked,
    )
    TOURNAMENT_PATH.write_text(report, encoding="utf-8")
    # Leaderboard only includes ideas that completed the full pipeline (R2 survivors).
    # Eliminated R1 ideas are documented in tournament.md with their elimination reason.
    leaderboard = build_leaderboard(r2_results)
    LEADERBOARD_PATH.write_text(leaderboard, encoding="utf-8")

    print(f"\nTournament report → {TOURNAMENT_PATH}  (all ideas + elimination reasons)")
    print(f"Leaderboard       → {LEADERBOARD_PATH}  (only ideas that ran full pipeline)")
    if finalists_ranked:
        winner = finalists_ranked[0]
        print(f"\n🏆 Winner: {winner.get('_name','?')} | score={winner.get('total_score','?')} | sim={winner.get('sim_score','?')}")
    return 0


# ── CLI ───────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Batch validate startup ideas (batch or tournament mode).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--ideas-file",
        default=None,
        metavar="PATH",
        help=(
            "Path to a markdown file with validator_idea blocks (required). "
            "Expected structure per idea:\n"
            "  ## N. Idea Name\n"
            "  ...\n"
            "  validator_idea:\n"
            "  ```text\n"
            "  One-paragraph idea description.\n"
            "  ```\n"
            "See docs/ideas_consolidadas_para_validacion.md for a full example."
        ),
    )
    parser.add_argument("--tournament", action="store_true",
                        help="Run 3-round elimination tournament instead of independent batch.")
    parser.add_argument("--finalists", type=int, default=3,
                        help="Number of finalists in tournament Round 2→Final (default 3).")
    parser.add_argument("--top", type=int, default=0, help="Only use top N ideas from file.")
    parser.add_argument("--regions", default="Peru,LATAM,USA")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--force-pit", action="store_true")
    parser.add_argument("--no-llm", action="store_true")
    parser.add_argument("--verbose", action="store_true",
                        help="Pass --verbose to each pipeline run.")
    return parser


def _require_ideas_file(args: argparse.Namespace) -> Path:
    if not args.ideas_file:
        print(
            "Error: --ideas-file is required.\n\n"
            "Usage:\n"
            "  python -m ai.validation_agents.run_batch "
            "--ideas-file docs/ideas_consolidadas_para_validacion.md --tournament\n\n"
            "Expected file structure (one block per idea):\n"
            "  ## 1. Idea Name\n"
            "  ...\n"
            "  validator_idea:\n"
            "  ```text\n"
            "  Your idea description here.\n"
            "  ```\n"
        )
        raise SystemExit(1)
    p = Path(args.ideas_file)
    if not p.exists():
        print(f"Error: file not found: {p}")
        raise SystemExit(1)
    return p


def main() -> int:
    args = build_parser().parse_args()
    if args.tournament:
        return run_tournament(args)
    return run_batch(args)


if __name__ == "__main__":
    raise SystemExit(main())
