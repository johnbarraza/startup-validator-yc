import concurrent.futures
from typing import Any

from ..config import ValidationConfig
from ..llm_client import LLMClient

SIMULATION_GATE = 0.60


def _persona(
    persona_id: str,
    role: str,
    lens: str,
    success_metric: str,
    default_objection: str,
) -> dict[str, str]:
    return {
        "id": persona_id,
        "role": role,
        "lens": lens,
        "success_metric": success_metric,
        "default_objection": default_objection,
    }


def default_personas() -> list[dict[str, str]]:
    return [
        _persona(
            "P1",
            "End user",
            "Daily workflow pain, speed, usability, trust.",
            "The product saves time or reduces stress in a repeated task.",
            "This sounds useful, but I already have a workaround.",
        ),
        _persona(
            "P2",
            "Economic buyer",
            "Budget, ROI, risk, urgency, procurement friction.",
            "The product clearly pays for itself this quarter or protects a critical metric.",
            "Who owns the budget, and why would we buy now?",
        ),
        _persona(
            "P3",
            "Operations owner",
            "Implementation, process change, support load, reliability.",
            "The workflow fits existing operations without creating extra coordination cost.",
            "This may add another tool my team has to maintain.",
        ),
        _persona(
            "P4",
            "Incumbent competitor",
            "How the status quo or large vendors defend the account.",
            "The startup finds a wedge incumbents do not prioritize.",
            "We can add this feature or bundle it with our existing platform.",
        ),
        _persona(
            "P5",
            "YC partner",
            "Market size, founder insight, speed of learning, venture scale.",
            "The idea has a sharp initial wedge and a path to a large market.",
            "This may be a feature, not a company.",
        ),
        _persona(
            "P6",
            "Technical builder",
            "Data access, model quality, defensibility, COGS, failure modes.",
            "The system can be built cheaply, reliably, and with a learning loop.",
            "The demo may work, but edge cases and data access can break the product.",
        ),
    ]


def _simulate_persona(
    client: LLMClient,
    config: ValidationConfig,
    persona: dict[str, str],
    idea: str,
    gap: dict[str, Any],
    validation: dict[str, Any],
) -> dict[str, Any]:
    return client.json_completion(
        model=config.chat_model,
        temperature=0.3,
        system_prompt=(
            f"You are a {persona['role']} evaluating a startup idea. "
            f"Your lens: {persona['lens']} "
            f"Your success metric: {persona['success_metric']} "
            "Return only valid JSON. Be critical and specific."
        ),
        user_prompt=f"""Evaluate this startup idea strictly from your perspective.

Idea:
{idea}

Selected gap:
{gap}

YC validation decision:
{validation.get('go_no_go', 'unknown')} — {validation.get('decision', '')}

Return JSON with exactly these keys:
- persona_id: "{persona['id']}"
- role: "{persona['role']}"
- reaction: 2-3 sentence honest reaction from your specific lens
- concern: your single sharpest objection or risk
- evidence_request: the one concrete thing you need to see to raise your score
- score: float 0.0-1.0 (0=reject, 0.5=neutral, 1=strongly convinced), based only on your lens
- score_rationale: one sentence explaining your score
""",
        fallback=lambda: {
            "persona_id": persona["id"],
            "role": persona["role"],
            "reaction": (
                f"From the {persona['role']} view, the idea is interesting only if it proves "
                f"{persona['success_metric'].lower()}"
            ),
            "concern": persona["default_objection"],
            "evidence_request": "Show a real recent example from the target customer segment.",
            "score": 0.5,
            "score_rationale": "Fallback used — no LLM available.",
            "source": "deterministic_fallback",
        },
    )


def _run_parallel_simulation(
    client: LLMClient,
    config: ValidationConfig,
    personas: list[dict[str, str]],
    idea: str,
    gap: dict[str, Any],
    validation: dict[str, Any],
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(personas)) as executor:
        future_to_persona = {
            executor.submit(_simulate_persona, client, config, p, idea, gap, validation): p
            for p in personas
        }
        for future in concurrent.futures.as_completed(future_to_persona):
            persona = future_to_persona[future]
            try:
                results.append(future.result())
            except Exception as exc:
                results.append({
                    "persona_id": persona["id"],
                    "role": persona["role"],
                    "reaction": "Error during simulation.",
                    "concern": str(exc),
                    "evidence_request": "N/A",
                    "score": 0.5,
                    "score_rationale": f"Exception: {exc}",
                    "source": "error_fallback",
                })
    results.sort(key=lambda r: r.get("persona_id", ""))
    return results


def _aggregate(persona_results: list[dict[str, Any]]) -> float:
    scores = [r.get("score", 0.5) for r in persona_results if isinstance(r.get("score"), (int, float))]
    return round(sum(scores) / len(scores), 3) if scores else 0.0


def _build_consensus(
    persona_results: list[dict[str, Any]],
    validation: dict[str, Any],
    aggregate_score: float,
    gate_passed: bool,
) -> dict[str, Any]:
    return {
        "aggregate_score": aggregate_score,
        "gate_passed": gate_passed,
        "gate_threshold": SIMULATION_GATE,
        "top_concerns": [r.get("concern", "") for r in persona_results[:3]],
        "top_evidence_requests": [r.get("evidence_request", "") for r in persona_results[:3]],
        "strongest_signal": "Proceed only if target users describe a recent, repeated, expensive problem in their own words.",
        "weakest_assumption": "Simulation scores are LLM estimates; live interviews must confirm.",
        "adoption_path": "Start with a narrow concierge workflow, then productize the repeated steps.",
        "pricing_test": "Ask for a small paid pilot tied to the buyer's success metric.",
        "decision_pressure": validation.get("go_no_go", "GO_WITH_CONSTRAINTS"),
    }


def run_stage3b_simulation(
    client: LLMClient,
    config: ValidationConfig,
    idea: str,
    gap: dict[str, Any],
    validation: dict[str, Any],
    context: str,
) -> dict[str, Any]:
    personas = default_personas()
    persona_results = _run_parallel_simulation(client, config, personas, idea, gap, validation)
    aggregate_score = _aggregate(persona_results)
    gate_passed = aggregate_score >= SIMULATION_GATE

    return {
        "inspiration": (
            "MiroFish-style parallel simulation: 6 independent persona agents scored in parallel, "
            f"aggregate gate={SIMULATION_GATE}."
        ),
        "idea": idea,
        "selected_gap": gap,
        "personas": personas,
        "persona_results": persona_results,
        "aggregate_score": aggregate_score,
        "gate_passed": gate_passed,
        "gate_threshold": SIMULATION_GATE,
        "consensus": _build_consensus(persona_results, validation, aggregate_score, gate_passed),
        "recommended_interventions": [
            "Narrow the customer segment until the end user and buyer are obvious.",
            "Run interviews around recent behavior, not opinions about the idea.",
            "Prototype the outcome manually before building a scalable product.",
            "Track what data or workflow insight compounds with each use.",
        ],
        "source": "parallel_simulation",
    }
