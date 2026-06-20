"""Stage 3 — YC validation + VC hard-screening rubric.

Scoring layers:
1. Friedman 10 questions (YC-style founder/market fit)
2. YC 14 rules (operational/strategic fit)
3. VC hard-screening rubric (8 dimensions, weighted — from venture-capital-intelligence)
   Team 25% · Market 20% · Product 15% · Traction 15% · Business Model 10%
   Competition 8% · Financials 5% · Risk 2%
   → Weighted composite → PASS / CONDITIONAL_PASS / DECLINE
"""
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

# VC hard-screening rubric (venture-capital-intelligence, isanthoshgandhi)
VC_RUBRIC = [
    {"dimension": "Team",           "weight": 0.25, "question": "Why is this team uniquely positioned to win?"},
    {"dimension": "Market",         "weight": 0.20, "question": "Is TAM > $1B? Growing? Right timing?"},
    {"dimension": "Product",        "weight": 0.15, "question": "What is the defensible moat?"},
    {"dimension": "Traction",       "weight": 0.15, "question": "What evidence exists that the market wants this?"},
    {"dimension": "Business Model", "weight": 0.10, "question": "LTV:CAC > 3x? Margins > 60% for SaaS?"},
    {"dimension": "Competition",    "weight": 0.08, "question": "Why does this win vs funded incumbents?"},
    {"dimension": "Financials",     "weight": 0.05, "question": "Is burn rate reasonable? 18+ months runway?"},
    {"dimension": "Risk Profile",   "weight": 0.02, "question": "What is the realistic failure mode?"},
]


def _score(label: str, score: int, note: str) -> dict[str, Any]:
    return {"criterion": label, "score": score, "note": note}


def _vc_score(dimension: str, weight: float, score: int, rationale: str) -> dict[str, Any]:
    return {
        "dimension": dimension,
        "weight": weight,
        "score": score,
        "weighted": round(score * weight, 2),
        "rationale": rationale,
    }


def _compute_vc_verdict(vc_scores: list[dict[str, Any]]) -> dict[str, Any]:
    composite = sum(r.get("weighted", 0) for r in vc_scores)
    if composite >= 7.0:
        verdict = "PASS"
    elif composite >= 5.0:
        verdict = "CONDITIONAL_PASS"
    else:
        verdict = "DECLINE"
    return {"composite_score": round(composite, 2), "verdict": verdict}


def _fallback_validation(idea: str, gap: dict[str, Any]) -> dict[str, Any]:
    friedman = [
        _score("Founder-market fit", 5, "Unknown until founder proves access or insight."),
        _score("Market size", 5, "Estimate TAM/SAM/SOM with external evidence."),
        _score("Problem acuity", 6, "Strong if gap maps to urgent time, money, or risk."),
        _score("Competition", 6, "Alternatives exist; wedge must be sharper."),
        _score("Personal pull", 5, "Unknown until founder states years-long commitment."),
        _score("Recently possible or necessary", 6, "AI/regulation/cost shifts may enable now."),
        _score("Successful proxies", 5, "Find adjacent companies proving willingness to pay."),
        _score("Years-long commitment", 5, "Validate domain depth for compounding insight."),
        _score("Scalability", 6, "Software scales; sales/data access may constrain."),
        _score("Good idea space", 6, "Promising if segment has repeated painful workflows."),
    ]
    yc = [
        _score(rule, 6 if i not in {2, 8, 11} else 7, "Provisional; replace with customer evidence.")
        for i, rule in enumerate(YC_RULES)
    ]
    vc_scores = [
        _vc_score(r["dimension"], r["weight"], 5, "Fallback — requires LLM for real assessment.")
        for r in VC_RUBRIC
    ]
    return {
        "idea": idea,
        "selected_gap": gap,
        "friedman_scores": friedman,
        "yc_rule_scores": yc,
        "vc_rubric_scores": vc_scores,
        "vc_verdict": _compute_vc_verdict(vc_scores),
        "go_no_go": "GO_WITH_CONSTRAINTS",
        "decision": (
            "Proceed as validation sprint only. Do not build until 5 target users confirm "
            "the gap is painful, frequent, and tied to a budget or urgent workflow."
        ),
        "next_experiments": [
            "Interview 5 target users about the last time they experienced this problem.",
            "Ask what they use today, cost, and what happens if they do nothing.",
            "Run a concierge test for the smallest paid outcome.",
        ],
        "kill_criteria": [
            "Users cannot recall a recent painful instance.",
            "No budget owner or urgent operational metric identified.",
            "Workflow only mildly better than current workaround.",
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
    rubric_text = "\n".join(
        f"  {r['dimension']} (weight={int(r['weight']*100)}%): {r['question']}"
        for r in VC_RUBRIC
    )
    return client.json_completion(
        model=config.chat_model,
        temperature=0.1,
        system_prompt=(
            "You are a strict YC partner AND a VC analyst applying a hard-screening rubric. "
            "Return only valid JSON. Score honestly — low scores are useful, not failures."
        ),
        user_prompt=f"""Validate this startup idea against three scoring frameworks.

IDEA: {idea}

SELECTED GAP: {gap}

━━━ FRAMEWORK 1: Friedman 10 questions (score 1-10 each) ━━━
{FRIEDMAN_QUESTIONS}

━━━ FRAMEWORK 2: YC 14 rules (score 1-10 each) ━━━
{YC_RULES}

━━━ FRAMEWORK 3: VC Hard-Screening Rubric (8 dimensions, weighted) ━━━
Score each 1-10 with one-sentence rationale. Weights shown.
{rubric_text}

Verdict logic:
- PASS: weighted composite >= 7.0
- CONDITIONAL_PASS: composite 5.0–6.9 (specify milestones required)
- DECLINE: composite < 5.0

YC context:
{context[:4000]}

Return JSON with keys:
idea, selected_gap,
friedman_scores (list of {{criterion, score, note}}),
yc_rule_scores (list of {{criterion, score, note}}),
vc_rubric_scores (list of {{dimension, weight, score, weighted, rationale}}),
vc_verdict ({{composite_score, verdict, conditions_if_conditional}}),
go_no_go, decision, next_experiments, kill_criteria.
""",
        fallback=lambda: _fallback_validation(idea, gap),
    )
