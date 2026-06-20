"""YC-style startup idea validation pipeline.

FLOW
────
Stage 0   Classify idea → detect pit ideas, categorize vertical + problem type
          ABORT if PIT (unless --force-pit flag used)
Stage 1   Research current alternatives in the market
Stage 2   Identify market gaps from research
Stage 2B  Generate N idea iterations (default 3 angles: original / B2B pivot / wedge)
          Each iteration gets a quick score (problem acuity, market size, feasibility)
Stage 3   YC validation — runs in PARALLEL for all iterations
          → selects winning iteration by score
          Gate: go_no_go must not be hard NO on winner
Stage 3B  MiroFish-style stakeholder simulation on WINNING iteration
          6 personas in parallel → aggregate score gate (default 0.60)
Stage 3C  Full YC dossier + 100-pt scorecard + Demo & Architecture on winner
Stage 4   Markdown report

PROVIDERS SUPPORTED (set in .env)
──────────────────────────────────
DeepSeek  : DEEPSEEK_API_KEY      (default)
OpenRouter: OPENROUTER_API_KEY    → prefix model with openrouter/<model>
Qwen      : DASHSCOPE_API_KEY     → prefix model with qwen/<model>

USAGE
─────
python -m ai.validation_agents.run_pipeline \\
  --idea "..." --auto --verbose

python -m ai.validation_agents.run_pipeline \\
  --idea "..." --auto --verbose --iterations 3 --force

# Skip pit check (e.g., for testing):
  --force-pit

# Override models per stage:
  CLASSIFIER_MODEL=deepseek-chat
  ITERATION_MODEL=openrouter/qwen/qwen-plus
"""
import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
from typing import Any

from .config import PROJECT_ROOT, ValidationConfig, load_config
from .llm_client import LLMClient
from .state import PipelineState
from .stages.stage0_classify import run_stage0_classify
from .stages.stage1_research import run_stage1_research
from .stages.stage2_gaps import run_stage2_gaps
from .stages.stage2b_iterations import run_stage2b_iterations
from .stages.stage3_validation import run_stage3_validation
from .stages.stage3b_simulation import run_stage3b_simulation
from .stages.stage3c_dossier import run_stage3c_dossier
from .stages.stage4_report import build_markdown_report, write_report


DEFAULT_IDEA = (
    "A startup idea that helps a specific customer segment solve a painful repeated workflow "
    "with software or AI. Pass --idea to validate a concrete idea."
)

PITCH_DOSSIER_DOCTRINE = """
--- docs/Final_Project_Startup_principal.pdf distilled doctrine ---
Use a YC-style startup dossier with these general sections:
1. One-liner: "We do X for Y using Z"; one sentence only.
2. Founder-market fit: why this founder can win, but avoid assuming founder data if not provided.
3. Problem: who suffers, pain intensity, current workaround, and evidence.
4. Solution & insight: what is built and the non-obvious insight.
5. Why now: what changed recently that makes the idea possible or urgent.
6. Market: TAM, SAM, and SOM for the first 12 months, with sources.
7. Competition and moat: include do-nothing and manual/spreadsheet alternatives.
8. Business model and pricing: concrete model, max three plans, variable costs/contribution margin.
9. Go-to-market: first 10, 100, and 1,000 users.
10. Traction or early signals: interviews, waitlist, LOIs, pilots, usage, workflow evidence.
11. Roadmap: 3, 6, and 12 month milestones.
12. Risks and mitigations: market, technical, execution, regulatory when relevant, and AI substitution risk.
13. The ask: amount/resource, use, and milestone unlocked.
Do not hardcode product stack, architecture, demo URL, or course-tool requirements in the general framework.

--- YC 2025 400-startup analysis distilled doctrine ---
Use the January-2025 style YC cohort analysis as trend context, not as timeless truth.
Important priors:
1. AI is a default assumption in recent YC cohorts, but generic AI agents are crowded.
2. B2B has stronger monetization priors than broad B2C.
3. Vertical AI workflows are stronger than horizontal AI wrappers.
4. Domain expertise plus AI can become a moat when it creates workflow data, trust, or distribution.
5. Look for underserved large markets instead of copying crowded agent/copilot categories.
6. Education, legal, healthcare, financial services, developer infrastructure, retail, climate, manufacturing,
   agriculture, and logistics should be evaluated by saturation, buyer urgency, and distribution.
7. Treat the article's numbers as approximate, because the source itself says some analysis used LLMs.
"""


def read_yc_context() -> str:
    paths = [
        PROJECT_ROOT / "docs" / "ycombinator" / "rules_summary.md",
        PROJECT_ROOT / "docs" / "ycombinator" / "Analyzing Latest 400 Business Ideas funded by YCombinator  by Harshit Tyagi  Medium.md",
        PROJECT_ROOT / "docs" / "ycombinator" / "video_HowtGetandEvaluateStartupIdeas.md",
        PROJECT_ROOT / "docs" / "ycombinator" / "video_How to Build an AI-Native Services Company.md",
        PROJECT_ROOT / "docs" / "ycombinator" / "video_Pick_One_Idea_and_Go_Deep.md",
    ]
    chunks: list[str] = [PITCH_DOSSIER_DOCTRINE]
    for path in paths:
        if path.exists():
            chunks.append(f"\n--- {path.relative_to(PROJECT_ROOT)} ---\n")
            chunks.append(path.read_text(encoding="utf-8", errors="ignore")[:8000])
    return "\n".join(chunks)


def find_gap(gaps: dict[str, Any], gap_id: str) -> dict[str, Any]:
    for gap in gaps.get("gaps", []):
        if str(gap.get("id")).lower() == gap_id.lower():
            return gap
    available = ", ".join(str(gap.get("id")) for gap in gaps.get("gaps", []))
    raise ValueError(f"Gap '{gap_id}' not found. Available: {available}")


def idea_key(idea: str) -> str:
    digest = hashlib.sha1(idea.encode("utf-8")).hexdigest()[:10]
    words = "".join(char.lower() if char.isalnum() else "-" for char in idea[:40])
    slug = "-".join(part for part in words.split("-") if part)[:32] or "startup-idea"
    return f"{slug}-{digest}"


def parse_regions(raw_regions: str) -> list[str]:
    regions = [r.strip() for r in raw_regions.split(",") if r.strip()]
    return regions or ["Peru", "LATAM", "USA"]


def resolve_run_paths(
    args: argparse.Namespace, output_root: Path, run_key: str
) -> tuple[Path, Path]:
    if args.state:
        state_path = Path(args.state)
        run_dir = state_path.parent
    else:
        run_dir = output_root / run_key
        state_path = run_dir / "state.json"
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir, state_path


def write_stage_artifact(run_dir: Path, filename: str, artifact: Any) -> Path:
    path = run_dir / filename
    path.write_text(json.dumps(artifact, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def log_step(args: argparse.Namespace, message: str) -> None:
    if args.verbose:
        print(message, flush=True)


def log_artifact(args: argparse.Namespace, stage: str, artifact: dict[str, Any]) -> None:
    if not args.verbose:
        return
    source = artifact.get("source", "unknown")
    error = artifact.get("llm_error")
    suffix = f" ({error})" if error else ""
    print(f"{stage}: {source}{suffix}", flush=True)


def print_checkpoint_gaps(gaps: dict[str, Any]) -> None:
    print("\nCHECKPOINT 1 — choose a gap")
    for gap in gaps.get("gaps", []):
        print(f"  {gap.get('id')}: {gap.get('title')} (priority {gap.get('priority')})")
        print(f"    Pain: {gap.get('pain')}")
    print(f"\nRecommended: {gaps.get('recommended_gap_id')}")
    print("Resume: python -m ai.validation_agents.run_pipeline --gap-id G1 --auto")


def print_checkpoint_validation(validation: dict[str, Any]) -> None:
    print("\nCHECKPOINT 2 — approve strategy")
    print(f"Decision: {validation.get('go_no_go')}")
    print(validation.get("decision"))
    print("\nNext experiments:")
    for item in validation.get("next_experiments", []):
        print(f"  - {item}")


def _validate_iteration(
    client: LLMClient,
    config: ValidationConfig,
    iteration: dict[str, Any],
    gap: dict[str, Any],
    context: str,
) -> dict[str, Any]:
    """Run Stage 3 validation for a single iteration framing."""
    idea_text = iteration.get("idea_refined", iteration.get("one_liner", ""))
    result = run_stage3_validation(client, config, idea_text, gap, context)
    result["_iteration_id"] = iteration.get("id", "I1")
    result["_iteration_angle"] = iteration.get("angle", "ORIGINAL")
    result["_iteration_one_liner"] = iteration.get("one_liner", "")
    return result


def _select_winning_iteration(
    validations: list[dict[str, Any]],
    iterations: list[dict[str, Any]],
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Pick the iteration with the best YC validation score."""
    def _score(v: dict[str, Any]) -> float:
        go = str(v.get("go_no_go", "")).upper()
        if go in ("TRUE", "GO", "YES", "PROCEED"):
            base = 2.0
        elif go in ("FALSE", "NO_GO", "NO", "ABORT"):
            base = 0.0
        else:
            base = 1.0
        friedman = sum(
            r.get("score", 0) if isinstance(r, dict) else 0
            for r in v.get("friedman_scores", [])
        )
        yc = sum(
            r.get("score", 0) if isinstance(r, dict) else 0
            for r in v.get("yc_rule_scores", [])
        )
        return base * 100 + friedman + yc

    best_validation = max(validations, key=_score)
    best_id = best_validation.get("_iteration_id", "I1")
    best_iteration = next(
        (it for it in iterations if it.get("id") == best_id),
        iterations[0],
    )
    return best_iteration, best_validation


def run(args: argparse.Namespace) -> int:
    from .config import ValidationConfig
    config = load_config(output_dir=args.output_dir, use_llm=not args.no_llm)
    client = LLMClient(config)
    run_key = idea_key(args.idea)
    run_dir, state_path = resolve_run_paths(args, config.output_dir, run_key)
    state = PipelineState.load_or_create(state_path, args.idea, force=args.force)
    context = read_yc_context()

    log_step(args, f"Run folder: {run_dir}")
    log_step(
        args,
        f"LLM: {client.enabled} | {config.base_url} | chat={config.chat_model} "
        f"| reasoner={config.reasoner_model} | classifier={config.classifier_model} "
        f"| iteration={config.iteration_model}",
    )

    # ── Stage 0: Classify ────────────────────────────────────────────────────
    if args.force or "stage0_classify" not in state.artifacts:
        log_step(args, "Stage 0: classifying idea (pit check)...")
        classification = run_stage0_classify(client, config, state.idea, context)
        state.put_artifact("stage0_classify", classification)
        write_stage_artifact(run_dir, "stage0_classify.json", classification)
        log_artifact(args, "Stage 0", classification)
    else:
        classification = state.require_artifact("stage0_classify")
        log_artifact(args, "Stage 0 cached", classification)

    problem_type = classification.get("problem_type", "UNKNOWN")
    proceed = classification.get("proceed_recommendation", "PROCEED")
    devil = classification.get("devil_verdict", "?")
    freemium = classification.get("freemium_recommendation", "?")
    log_step(
        args,
        f"Stage 0 verdict: {problem_type} → {proceed} | devil={devil} | freemium={freemium} "
        f"| vertical={classification.get('vertical')} | severity={classification.get('problem_severity')}",
    )

    if proceed == "ABORT" and not args.force_pit:
        print(f"\n[ABORT] Idea classified as {problem_type} (devil={devil}).")
        print(f"Rationale: {classification.get('classification_rationale')}")
        print(f"Payment blocker: {classification.get('payment_blocker')}")
        print(f"Hardest assumption: {classification.get('hardest_assumption')}")
        print(f"Pivot suggestion: {classification.get('suggested_pivot')}")
        print("\nFix the idea and re-run. Use --force-pit to override.\n")
        return 1

    if proceed == "WARN":
        print(f"\n[WARN] Idea classified as {problem_type} (devil={devil}).")
        for sig in classification.get("pit_signals_detected", []):
            print(f"  ⚠ {sig}")
        print(f"Payment blocker: {classification.get('payment_blocker')}")
        print(f"Free substitute risk: {classification.get('free_substitute_risk')}")
        print(f"Freemium: {freemium} — {classification.get('freemium_rationale')}")
        print("Continuing...\n")

    # ── Stage 1: Research ────────────────────────────────────────────────────
    if args.force or "stage1_research" not in state.artifacts:
        log_step(args, "Stage 1: researching alternatives...")
        research = run_stage1_research(client, config, state.idea, context)
        state.put_artifact("stage1_research", research)
        write_stage_artifact(run_dir, "stage1_research.json", research)
        log_artifact(args, "Stage 1", research)
    else:
        research = state.require_artifact("stage1_research")
        log_artifact(args, "Stage 1 cached", research)

    # ── Stage 2: Gaps ────────────────────────────────────────────────────────
    if args.force or "stage2_gaps" not in state.artifacts:
        log_step(args, "Stage 2: analyzing market gaps...")
        gaps = run_stage2_gaps(client, config, research)
        state.put_artifact("stage2_gaps", gaps)
        write_stage_artifact(run_dir, "stage2_gaps.json", gaps)
        log_artifact(args, "Stage 2", gaps)
    else:
        gaps = state.require_artifact("stage2_gaps")
        log_artifact(args, "Stage 2 cached", gaps)

    selected_gap_id = args.gap_id or state.selected_gap_id
    if args.auto and not selected_gap_id:
        selected_gap_id = gaps.get("recommended_gap_id")

    if not selected_gap_id:
        state.record("checkpoint_1", "Waiting for human gap selection.")
        state.save()
        print_checkpoint_gaps(gaps)
        return 0

    selected_gap = find_gap(gaps, str(selected_gap_id))
    state.selected_gap_id = selected_gap_id
    state.save()

    # ── Stage 2B: Idea Iterations ────────────────────────────────────────────
    if args.force or "stage2b_iterations" not in state.artifacts:
        log_step(args, f"Stage 2B: generating {args.iterations} idea iterations in parallel...")
        iterations_result = run_stage2b_iterations(client, config, state.idea, research, gaps, context)
        state.put_artifact("stage2b_iterations", iterations_result)
        write_stage_artifact(run_dir, "stage2b_iterations.json", iterations_result)
        log_artifact(args, "Stage 2B", iterations_result)
        for it in iterations_result.get("iterations", []):
            sc = it.get("quick_score", {})
            log_step(args, f"  {it.get('id')} {it.get('angle')}: {sc.get('total', '?')}/30 — {it.get('one_liner', '')[:60]}")
    else:
        iterations_result = state.require_artifact("stage2b_iterations")
        log_artifact(args, "Stage 2B cached", iterations_result)

    iterations = iterations_result.get("iterations", [])

    # ── Stage 3: YC Validation (parallel for all iterations) ─────────────────
    if args.force or "stage3_validations" not in state.artifacts:
        log_step(args, f"Stage 3: validating {len(iterations)} iterations in parallel...")
        validations: list[dict[str, Any]] = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(iterations)) as executor:
            future_to_it = {
                executor.submit(_validate_iteration, client, config, it, selected_gap, context): it
                for it in iterations
            }
            for future in concurrent.futures.as_completed(future_to_it):
                it = future_to_it[future]
                try:
                    validations.append(future.result())
                except Exception as exc:
                    validations.append({
                        "_iteration_id": it.get("id", "?"),
                        "_iteration_angle": it.get("angle", "?"),
                        "go_no_go": "ERROR",
                        "llm_error": str(exc),
                    })
        validations.sort(key=lambda v: v.get("_iteration_id", ""))
        state.put_artifact("stage3_validations", validations)
        write_stage_artifact(run_dir, "stage3_validations.json", validations)
        for v in validations:
            log_step(args, f"  Stage 3 {v.get('_iteration_id')} {v.get('_iteration_angle')}: {v.get('go_no_go')}")
    else:
        validations = state.require_artifact("stage3_validations")
        log_artifact(args, "Stage 3 cached", {"source": "cache"})

    # Select winning iteration
    winning_iteration, winning_validation = _select_winning_iteration(validations, iterations)
    log_step(
        args,
        f"Stage 3 winner: {winning_iteration.get('id')} {winning_iteration.get('angle')} "
        f"→ {winning_validation.get('go_no_go')}",
    )
    state.put_artifact("stage3_winner_iteration", winning_iteration)
    state.put_artifact("stage3_validation", winning_validation)
    write_stage_artifact(run_dir, "stage3_yc_validation.json", winning_validation)
    state.save()

    winning_idea = winning_iteration.get("idea_refined", state.idea)

    # ── Stage 3B: Stakeholder Simulation on winner ────────────────────────────
    if args.force or "stage3b_simulation" not in state.artifacts:
        log_step(args, "Stage 3B: simulating stakeholders on winning iteration...")
        simulation = run_stage3b_simulation(
            client, config, winning_idea, selected_gap, winning_validation, context
        )
        state.put_artifact("stage3b_simulation", simulation)
        write_stage_artifact(run_dir, "stage3b_simulation.json", simulation)
        log_artifact(args, "Stage 3B", simulation)
    else:
        simulation = state.require_artifact("stage3b_simulation")
        log_artifact(args, "Stage 3B cached", simulation)

    gate_score = simulation.get("aggregate_score", 1.0)
    gate_passed = simulation.get("gate_passed", True)
    gate_threshold = simulation.get("gate_threshold", 0.60)
    log_step(
        args,
        f"Stage 3B gate: {gate_score:.2f} / {gate_threshold} — "
        f"{'PASS' if gate_passed else 'WARN: low conviction'}",
    )
    if not gate_passed:
        print(
            f"\nSIMULATION GATE: aggregate persona score {gate_score:.2f} < {gate_threshold}. "
            "Low stakeholder conviction detected. Review persona_results before proceeding.\n"
        )

    # ── Stage 3C: Full Dossier ────────────────────────────────────────────────
    regions = parse_regions(args.regions)
    if args.force or "stage3c_dossier" not in state.artifacts:
        log_step(args, "Stage 3C: building YC dossier and scorecard...")
        dossier = run_stage3c_dossier(
            client, config, winning_idea, selected_gap,
            winning_validation, simulation, regions, context,
        )
        state.put_artifact("stage3c_dossier", dossier)
        write_stage_artifact(run_dir, "stage3c_dossier.json", dossier)
        log_artifact(args, "Stage 3C", dossier)
        log_step(
            args,
            f"Stage 3C score: {dossier.get('total_score')}/{dossier.get('max_score')} — {dossier.get('rating')}",
        )
    else:
        dossier = state.require_artifact("stage3c_dossier")
        log_artifact(args, "Stage 3C cached", dossier)

    # ── Checkpoint 2 ─────────────────────────────────────────────────────────
    approved = args.approve or args.auto or state.strategy_approved
    if not approved:
        state.record("checkpoint_2", "Waiting for human strategy approval.")
        state.save()
        print_checkpoint_validation(winning_validation)
        return 0

    state.strategy_approved = True

    # ── Stage 4: Report ───────────────────────────────────────────────────────
    report = build_markdown_report(
        idea=state.idea,
        classification=classification,
        research=research,
        gaps=gaps,
        iterations_result=iterations_result,
        winning_iteration=winning_iteration,
        validations=validations,
        validation=winning_validation,
        simulation=simulation,
        dossier=dossier,
    )
    report_path = write_report(run_dir, report, filename="report.md")
    state.put_artifact("stage4_report", {"path": str(report_path), "markdown": report})
    write_stage_artifact(run_dir, "stage4_report.json", {"path": str(report_path), "markdown": report})
    state.record("complete", f"Report written to {report_path}")
    state.save()
    log_step(args, "Stage 4: report written.")

    if args.json:
        print(json.dumps(state.artifacts, indent=2, ensure_ascii=False))
    else:
        print(f"Validation pipeline complete: {report_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="YC-style startup idea validation pipeline (Stage 0-4).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--idea", default=DEFAULT_IDEA, help="Startup idea to validate.")
    parser.add_argument("--state", help="Path to existing pipeline state JSON (resume).")
    parser.add_argument("--output-dir", help="Output directory for state and reports.")
    parser.add_argument("--regions", default="Peru,LATAM,USA", help="Comma-separated regions.")
    parser.add_argument("--gap-id", help="Gap id from checkpoint 1 (e.g. G2).")
    parser.add_argument("--iterations", type=int, default=3, help="Number of idea iterations (default 3).")
    parser.add_argument("--approve", action="store_true", help="Approve checkpoint 2.")
    parser.add_argument("--auto", action="store_true", help="Auto-select gap and approve.")
    parser.add_argument("--force", action="store_true", help="Recompute all stages.")
    parser.add_argument("--force-pit", action="store_true", help="Continue even if classified as PIT.")
    parser.add_argument("--no-llm", action="store_true", help="Use deterministic fallbacks (no API calls).")
    parser.add_argument("--json", action="store_true", help="Print artifacts as JSON on completion.")
    parser.add_argument("--verbose", action="store_true", help="Print stage-by-stage progress.")
    return parser


def main() -> int:
    return run(build_parser().parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
