import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from .config import PROJECT_ROOT, load_config
from .llm_client import LLMClient
from .state import PipelineState
from .stages.stage1_research import run_stage1_research
from .stages.stage2_gaps import run_stage2_gaps
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
    raise ValueError(f"Gap '{gap_id}' was not found. Available gaps: {available}")


def idea_key(idea: str) -> str:
    digest = hashlib.sha1(idea.encode("utf-8")).hexdigest()[:10]
    words = "".join(char.lower() if char.isalnum() else "-" for char in idea[:40])
    slug = "-".join(part for part in words.split("-") if part)[:32] or "startup-idea"
    return f"{slug}-{digest}"


def parse_regions(raw_regions: str) -> list[str]:
    regions = [region.strip() for region in raw_regions.split(",") if region.strip()]
    return regions or ["Peru", "LATAM", "USA"]


def resolve_run_paths(args: argparse.Namespace, output_root: Path, run_key: str) -> tuple[Path, Path]:
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
    if error:
        print(f"{stage}: {source} ({error})", flush=True)
    else:
        print(f"{stage}: {source}", flush=True)


def print_checkpoint_gaps(gaps: dict[str, Any]) -> None:
    print("\nCHECKPOINT 1 - choose a gap")
    for gap in gaps.get("gaps", []):
        print(f"{gap.get('id')}: {gap.get('title')} (priority {gap.get('priority')})")
        print(f"  Pain: {gap.get('pain')}")
        print(f"  Evidence: {gap.get('evidence_needed')}")
    print(f"\nRecommended: {gaps.get('recommended_gap_id')}")
    print("Resume with: python -m ai.validation_agents.run_pipeline --gap-id G1")
    print("Or run full demo with: python -m ai.validation_agents.run_pipeline --auto")


def print_checkpoint_validation(validation: dict[str, Any]) -> None:
    print("\nCHECKPOINT 2 - approve strategy")
    print(f"Decision: {validation.get('go_no_go')}")
    print(validation.get("decision"))
    print("\nNext experiments:")
    for item in validation.get("next_experiments", []):
        print(f"- {item}")
    print("\nResume with: python -m ai.validation_agents.run_pipeline --gap-id "
          f"{validation.get('selected_gap', {}).get('id')} --approve")


def run(args: argparse.Namespace) -> int:
    config = load_config(output_dir=args.output_dir, use_llm=not args.no_llm)
    client = LLMClient(config)
    run_key = idea_key(args.idea)
    run_dir, state_path = resolve_run_paths(args, config.output_dir, run_key)
    state = PipelineState.load_or_create(state_path, args.idea, force=args.force)
    context = read_yc_context()
    log_step(args, f"Run folder: {run_dir}")
    log_step(args, f"LLM enabled: {client.enabled} | base_url: {config.base_url} | chat_model: {config.chat_model} | reasoner_model: {config.reasoner_model}")

    if args.force or "stage1_research" not in state.artifacts:
        log_step(args, "Stage 1: researching alternatives...")
        research = run_stage1_research(client, config, state.idea, context)
        state.put_artifact("stage1_research", research)
        write_stage_artifact(run_dir, "stage1_research.json", research)
        log_artifact(args, "Stage 1", research)
    else:
        research = state.require_artifact("stage1_research")
        log_artifact(args, "Stage 1 cached", research)

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

    if args.force or "stage3_validation" not in state.artifacts:
        log_step(args, "Stage 3: running YC validation...")
        validation = run_stage3_validation(client, config, state.idea, selected_gap, context)
        state.put_artifact("stage3_validation", validation)
        write_stage_artifact(run_dir, "stage3_yc_validation.json", validation)
        log_artifact(args, "Stage 3", validation)
    else:
        validation = state.require_artifact("stage3_validation")
        log_artifact(args, "Stage 3 cached", validation)

    if args.force or "stage3b_simulation" not in state.artifacts:
        log_step(args, "Stage 3B: simulating stakeholders...")
        simulation = run_stage3b_simulation(client, config, state.idea, selected_gap, validation, context)
        state.put_artifact("stage3b_simulation", simulation)
        write_stage_artifact(run_dir, "stage3b_simulation.json", simulation)
        log_artifact(args, "Stage 3B", simulation)
    else:
        simulation = state.require_artifact("stage3b_simulation")
        log_artifact(args, "Stage 3B cached", simulation)

    gate_score = simulation.get("aggregate_score", 1.0)
    gate_passed = simulation.get("gate_passed", True)
    gate_threshold = simulation.get("gate_threshold", 0.60)
    log_step(args, f"Stage 3B gate: {gate_score:.2f} / {gate_threshold} — {'PASS' if gate_passed else 'WARN: low conviction'}")
    if not gate_passed:
        print(
            f"\nSIMULATION GATE: aggregate persona score {gate_score:.2f} < {gate_threshold}. "
            "Low stakeholder conviction detected. Review persona_results before proceeding.\n"
        )

    regions = parse_regions(args.regions)
    if args.force or "stage3c_dossier" not in state.artifacts:
        log_step(args, "Stage 3C: building YC dossier and scorecard...")
        dossier = run_stage3c_dossier(
            client,
            config,
            state.idea,
            selected_gap,
            validation,
            simulation,
            regions,
            context,
        )
        state.put_artifact("stage3c_dossier", dossier)
        write_stage_artifact(run_dir, "stage3c_dossier.json", dossier)
        log_artifact(args, "Stage 3C", dossier)
        log_step(args, f"Stage 3C score: {dossier.get('total_score')}/{dossier.get('max_score')} - {dossier.get('rating')}")
    else:
        dossier = state.require_artifact("stage3c_dossier")
        log_artifact(args, "Stage 3C cached", dossier)

    approved = args.approve or args.auto or state.strategy_approved
    if not approved:
        state.record("checkpoint_2", "Waiting for human strategy approval.")
        state.save()
        print_checkpoint_validation(validation)
        return 0

    state.strategy_approved = True
    report = build_markdown_report(
        idea=state.idea,
        research=research,
        gaps=gaps,
        validation=validation,
        simulation=simulation,
        dossier=dossier,
    )
    report_path = write_report(run_dir, report, filename="report.md")
    state.put_artifact("stage4_report", {"path": str(report_path), "markdown": report})
    write_stage_artifact(run_dir, "stage4_report.json", {"path": str(report_path), "markdown": report})
    state.record("complete", f"Validation report written to {report_path}")
    state.save()
    log_step(args, "Stage 4: report written.")

    if args.json:
        print(json.dumps(state.artifacts, indent=2, ensure_ascii=False))
    else:
        print(f"Validation pipeline complete: {report_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the YC-style startup idea validation agent pipeline.")
    parser.add_argument("--idea", default=DEFAULT_IDEA, help="Startup idea to validate.")
    parser.add_argument("--state", help="Path to pipeline state JSON.")
    parser.add_argument("--output-dir", help="Directory for state and reports.")
    parser.add_argument("--regions", default="Peru,LATAM,USA", help="Comma-separated market regions to compare.")
    parser.add_argument("--gap-id", help="Human-selected gap id from checkpoint 1, for example G1.")
    parser.add_argument("--approve", action="store_true", help="Approve checkpoint 2 and generate report.")
    parser.add_argument("--auto", action="store_true", help="Auto-select recommended gap and approve strategy.")
    parser.add_argument("--force", action="store_true", help="Recompute all stages from scratch.")
    parser.add_argument("--no-llm", action="store_true", help="Disable LLM calls and use deterministic fallbacks.")
    parser.add_argument("--json", action="store_true", help="Print artifacts as JSON after completion.")
    parser.add_argument("--verbose", action="store_true", help="Print each agent stage and whether it used LLM or fallback.")
    return parser


def main() -> int:
    return run(build_parser().parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
