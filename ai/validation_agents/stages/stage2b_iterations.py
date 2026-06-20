"""Stage 2B — Idea iteration generator.

Inspired by Top_papers_creator's pivot loop (up to 2 pivots on low score).
Generates 3 meaningfully different framings of the same core problem space:

  I1 ORIGINAL   — Refined version of what the founder submitted.
  I2 PIVOT_B2B  — Same pain, reframed for an institutional/B2B buyer
                  (employer, university, government, distributor).
  I3 PIVOT_WEDGE — Narrowest slice that can prove demand fastest;
                   minimum viable customer and minimum viable problem.

All 3 are then validated in parallel by Stage 3. The highest-scoring
framing advances to Stage 3B + 3C.
"""
import concurrent.futures
from typing import Any

from ..config import ValidationConfig
from ..llm_client import LLMClient

ITERATION_ANGLES = [
    {
        "id": "I1",
        "angle": "ORIGINAL",
        "instruction": (
            "Refine and sharpen the founder's original idea. Keep the same customer and problem "
            "but make the one-liner crisper, the pain more behavioral, and the wedge narrower."
        ),
    },
    {
        "id": "I2",
        "angle": "PIVOT_B2B",
        "instruction": (
            "Reframe the same core problem for an institutional or B2B buyer: a university, employer, "
            "government agency, trade association, or distributor who has budget and urgency. "
            "The end user may be the same but the buyer and pricing model should change."
        ),
    },
    {
        "id": "I3",
        "angle": "PIVOT_WEDGE",
        "instruction": (
            "Find the narrowest, sharpest slice of the problem that one specific micro-segment "
            "suffers most acutely right now. Ignore scale — optimize for fastest evidence of "
            "willingness to pay from 10 real users in the next 30 days."
        ),
    },
]


def _fallback_iteration(idea: str, angle: dict[str, str]) -> dict[str, Any]:
    return {
        "id": angle["id"],
        "angle": angle["angle"],
        "idea_refined": f"[{angle['angle']}] {idea}",
        "target_customer": "To be defined through user interviews.",
        "core_problem": "To be validated through behavioral interviews.",
        "solution_hook": "To be determined after problem validation.",
        "why_this_angle": angle["instruction"],
        "quick_score": {
            "problem_acuity": 5,
            "market_size": 5,
            "founder_feasibility": 5,
            "total": 15,
        },
        "source": "deterministic_fallback",
    }


def _generate_single_iteration(
    client: LLMClient,
    config: ValidationConfig,
    idea: str,
    research: dict[str, Any],
    gaps: dict[str, Any],
    context: str,
    angle: dict[str, str],
) -> dict[str, Any]:
    recommended_gap = gaps.get("recommended_gap_id", "")
    gap_titles = [
        f"{g.get('id')}: {g.get('title')}"
        for g in gaps.get("gaps", [])[:5]
    ]
    alternatives_summary = research.get("research_summary", "")[:1500]

    return client.json_completion(
        model=config.iteration_model,
        temperature=0.7,
        system_prompt=(
            "You are a YC startup coach generating a concrete, differentiated framing of a startup idea. "
            "Be creative but grounded. Focus on structural pain, not vitamins. "
            "Return only valid JSON."
        ),
        user_prompt=f"""Generate a startup idea framing using the angle below.

ORIGINAL IDEA:
{idea}

ANGLE TO APPLY:
{angle['instruction']}

MARKET GAPS IDENTIFIED (for context):
{chr(10).join(gap_titles)}
Recommended gap: {recommended_gap}

ALTERNATIVES IN MARKET (for context):
{alternatives_summary}

Score each framing honestly (0-10 per dimension):
- problem_acuity: How urgent and structural is the pain? (10 = people lose money/time/risk daily)
- market_size: How many potential customers exist? (10 = millions of potential payers)
- founder_feasibility: How easy is this to validate in 30 days with zero budget? (10 = can interview 10 users tomorrow)

Return JSON with exactly these keys:
{{
  "id": "{angle['id']}",
  "angle": "{angle['angle']}",
  "idea_refined": "<one crisp paragraph describing this version of the idea>",
  "one_liner": "<We do X for Y using Z — one sentence>",
  "target_customer": "<specific person with job title or life situation, not 'students' or 'companies'>",
  "core_problem": "<behavioral description: what they do today that is painful, how often, what it costs>",
  "solution_hook": "<the one thing that makes this version different from generic alternatives>",
  "why_this_angle": "<why this framing might outperform the original>",
  "quick_score": {{
    "problem_acuity": <0-10>,
    "market_size": <0-10>,
    "founder_feasibility": <0-10>,
    "total": <sum>
  }}
}}
""",
        fallback=lambda: _fallback_iteration(idea, angle),
    )


def run_stage2b_iterations(
    client: LLMClient,
    config: ValidationConfig,
    idea: str,
    research: dict[str, Any],
    gaps: dict[str, Any],
    context: str,
) -> dict[str, Any]:
    results: list[dict[str, Any]] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(ITERATION_ANGLES)) as executor:
        future_to_angle = {
            executor.submit(
                _generate_single_iteration, client, config, idea, research, gaps, context, angle
            ): angle
            for angle in ITERATION_ANGLES
        }
        for future in concurrent.futures.as_completed(future_to_angle):
            angle = future_to_angle[future]
            try:
                results.append(future.result())
            except Exception as exc:
                results.append(_fallback_iteration(idea, angle) | {"error": str(exc)})

    results.sort(key=lambda r: r.get("id", ""))

    best = max(results, key=lambda r: r.get("quick_score", {}).get("total", 0))

    return {
        "iterations": results,
        "recommended_iteration_id": best.get("id", "I1"),
        "recommended_one_liner": best.get("one_liner", ""),
        "source": "parallel_iteration",
    }
