from typing import Any

from ..config import ValidationConfig
from ..llm_client import LLMClient


FRIEDMAN_QUESTIONS = [
    "Founder-market fit",
    "Market size",
    "Problem acuity",
    "Competition",
    "Personal pull",
    "Recently possible or necessary",
    "Successful proxies",
    "Years-long commitment",
    "Scalability",
    "Good idea space",
]


YC_RULES = [
    "Do not wait for the perfect idea",
    "Burn the boats",
    "Go deep into customer workflow",
    "Build at the edge of AI",
    "Sell outcomes, not tools",
    "Choose ambitious scope",
    "Treat failure as structured data",
    "Pick low-trust, high-expertise markets",
    "The process is the product",
    "Avoid early-demand trap",
    "Price per unit or result",
    "Obsess over COGS",
    "Do not bolt AI onto legacy",
    "Cover domain, model, and operations fluency",
]


def _score(label: str, score: int, note: str) -> dict[str, Any]:
    return {"criterion": label, "score": score, "note": note}


def _fallback_validation(idea: str, gap: dict[str, Any]) -> dict[str, Any]:
    friedman = [
        _score("Founder-market fit", 5, "Unknown until the founder proves unusual access or insight into the users."),
        _score("Market size", 5, "Unknown in fallback mode; estimate TAM/SAM/SOM with external evidence."),
        _score("Problem acuity", 6, "Potentially strong if the selected gap maps to urgent time, money, or risk."),
        _score("Competition", 6, "Alternatives probably exist; competition is validation if the wedge is sharper."),
        _score("Personal pull", 5, "Unknown until the founder states why they would work on this for years."),
        _score("Recently possible or necessary", 6, "Likely if AI, regulation, platform shifts, or cost changes enable it now."),
        _score("Successful proxies", 5, "Find adjacent companies, workflows, or budgets that prove willingness to pay."),
        _score("Years-long commitment", 5, "Unknown; validate whether the domain is deep enough for compounding insight."),
        _score("Scalability", 6, "Software can scale, but sales, service, and data access may constrain the model."),
        _score("Good idea space", 6, "Promising only if the first customer segment has repeated painful workflows."),
    ]
    yc = [
        _score(rule, 6 if i not in {2, 8, 11} else 7, "Provisional pass; replace assumptions with customer evidence.")
        for i, rule in enumerate(YC_RULES)
    ]
    return {
        "idea": idea,
        "selected_gap": gap,
        "friedman_scores": friedman,
        "yc_rule_scores": yc,
        "go_no_go": "GO_WITH_CONSTRAINTS",
        "decision": (
            "Proceed only as a validation sprint. Do not build more product surface area until at least "
            "5 target users confirm the selected gap is painful, frequent, and tied to a budget or urgent workflow."
        ),
        "next_experiments": [
            "Interview 5 target users about the last time they experienced this problem.",
            "Ask what they use today, how much it costs, and what happens if they do nothing.",
            "Run a concierge or fake-door test for the smallest paid outcome.",
            "Compare the idea against the strongest incumbent and the status quo.",
        ],
        "kill_criteria": [
            "Users cannot recall a recent painful instance of the problem.",
            "No one can identify a budget owner or urgent operational metric.",
            "The proposed workflow is only mildly better than the current workaround.",
        ],
        "source": "deterministic_fallback",
    }


def run_stage3_validation(
    client: LLMClient,
    config: ValidationConfig,
    idea: str,
    gap: dict[str, Any],
    context: str,
) -> dict[str, Any]:
    return client.json_completion(
        model=config.reasoner_model,
        temperature=0.1,
        system_prompt=(
            "You are a strict YC validation partner. Return only valid JSON. "
            "Score honestly and include explicit go/no-go criteria."
        ),
        user_prompt=f"""
Validate this startup idea and selected market gap.

Idea:
{idea}

Selected gap:
{gap}

Use these 10 Friedman questions:
{FRIEDMAN_QUESTIONS}

Use these 14 YC rules:
{YC_RULES}

Project context:
{context[:5000]}

Return JSON with keys: idea, selected_gap, friedman_scores, yc_rule_scores,
go_no_go, decision, next_experiments, kill_criteria.
""",
        fallback=lambda: _fallback_validation(idea, gap),
    )
