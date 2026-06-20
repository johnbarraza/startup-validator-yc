"""Stage 0 — Idea classifier and pit-idea detector.

Runs before any expensive research. Classifies the idea by:
- problem_type: PAINKILLER / VITAMIN / PIT / CROWDED_COPYCAT
- vertical: EdTech / FinTech / HealthTech / etc.
- customer_type: B2B / B2C / B2G / B2B2C / Marketplace
- problem_severity: STRUCTURAL / RECURRING / CONVENIENCE / COSMETIC
- proceed_recommendation: PROCEED / WARN / ABORT

A PIT idea fails one or more of:
  1. Problem is imagined by the founder, not reported by target users
  2. Only the founder is the customer
  3. It is a feature of an existing free product (Gmail, Notion, etc.)
  4. The user describes the problem abstractly ("people waste time") not behaviorally
  5. Nobody actively searches for a solution today
"""
from typing import Any

from ..config import ValidationConfig
from ..llm_client import LLMClient

PROBLEM_TYPE_DEFS = {
    "PAINKILLER": "Solves a real, urgent, structural problem. Users actively seek solutions and would pay today.",
    "VITAMIN": "Nice-to-have. Users like it but don't urgently need it; adoption is slow.",
    "PIT": "Solves a non-problem: the founder is the only customer, or the problem is abstract/imagined.",
    "CROWDED_COPYCAT": "Real problem, but dominated by large incumbents with no clear differentiated wedge.",
}

VERTICALS = [
    "EdTech", "FinTech", "HealthTech", "AgriTech", "GovTech",
    "LogisticsTech", "HRTech", "LegalTech", "PropTech", "RetailTech",
    "DevTools", "CleanTech", "FoodTech", "InsurTech", "MarketingTech", "Other",
]

PIT_SIGNALS = [
    "founder describes problem abstractly ('people waste time') not behaviorally ('I spend 3h/day on X')",
    "no evidence of users actively seeking a solution (no searches, no forums, no workarounds)",
    "problem only exists for the founder or a very small group",
    "existing free tool already solves this (Gmail filter, Excel macro, Notion template, ChatGPT prompt)",
    "the 'pain' is convenience, not cost/risk/time/compliance",
    "users say 'interesting' but have no current workaround — means pain is not urgent",
    "the solution requires changing user behavior with no strong forcing function",
    "market is too small even at 100% penetration to build a venture-scale business",
]

PAINKILLER_SIGNALS = [
    "users describe a specific recent incident and what they did to cope",
    "active workarounds exist (spreadsheets, WhatsApp groups, manual labor, consultants)",
    "spending already happens on imperfect solutions",
    "regulatory, compliance, or safety forcing function creates urgency",
    "recurring pain: happens weekly or more often",
    "measurable cost: lost hours, lost revenue, risk of fine or accident",
    "users search actively for solutions (Google, Reddit, LinkedIn groups)",
    "B2B: a buyer can charge it to a budget line already in use",
]


def _fallback_classify(idea: str) -> dict[str, Any]:
    return {
        "problem_type": "VITAMIN",
        "vertical": "Other",
        "customer_type": "B2C",
        "problem_severity": "RECURRING",
        "pain_evidence": "Could not assess without LLM — assume VITAMIN until live interviews confirm urgency.",
        "pit_signals_detected": [
            "Classification ran without LLM; treat as unverified.",
        ],
        "painkiller_signals_detected": [],
        "classification_rationale": "Deterministic fallback. Run with LLM enabled for real classification.",
        "proceed_recommendation": "WARN",
        "suggested_pivot": "Conduct 5 user interviews focused on recent behavior, not opinions about the idea.",
        "source": "deterministic_fallback",
    }


def run_stage0_classify(
    client: LLMClient,
    config: ValidationConfig,
    idea: str,
    context: str,
) -> dict[str, Any]:
    pit_signals_text = "\n".join(f"- {s}" for s in PIT_SIGNALS)
    painkiller_signals_text = "\n".join(f"- {s}" for s in PAINKILLER_SIGNALS)
    verticals_text = ", ".join(VERTICALS)
    problem_type_text = "\n".join(f"- {k}: {v}" for k, v in PROBLEM_TYPE_DEFS.items())

    return client.json_completion(
        model=config.classifier_model,
        temperature=0.1,
        system_prompt=(
            "You are a brutally honest YC partner screening startup ideas for structural pain. "
            "Your job is to detect pit ideas before wasting resources on them. "
            "Be skeptical. Return only valid JSON."
        ),
        user_prompt=f"""Classify this startup idea strictly and honestly.

IDEA:
{idea}

PROBLEM TYPES:
{problem_type_text}

PIT SIGNALS (red flags — idea fails if 2+ apply):
{pit_signals_text}

PAINKILLER SIGNALS (green flags — idea needs 3+ to proceed):
{painkiller_signals_text}

VERTICALS (pick one): {verticals_text}
CUSTOMER TYPES: B2B, B2C, B2G, B2B2C, Marketplace
PROBLEM SEVERITY: STRUCTURAL (systemic, affects many), RECURRING (happens often), CONVENIENCE (minor friction), COSMETIC (aesthetic only)
PROCEED RECOMMENDATIONS:
- PROCEED: PAINKILLER with 3+ green flags and 0-1 red flags
- WARN: VITAMIN or PAINKILLER with weak evidence (1-2 green flags or 2+ red flags)
- ABORT: PIT or CROWDED_COPYCAT with no clear wedge

YC context (for calibration):
{context[:3000]}

Return JSON with exactly these keys:
{{
  "problem_type": "PAINKILLER|VITAMIN|PIT|CROWDED_COPYCAT",
  "vertical": "<one from the verticals list>",
  "customer_type": "B2B|B2C|B2G|B2B2C|Marketplace",
  "problem_severity": "STRUCTURAL|RECURRING|CONVENIENCE|COSMETIC",
  "pain_evidence": "<what evidence exists or is missing>",
  "pit_signals_detected": ["<list of red flags that apply>"],
  "painkiller_signals_detected": ["<list of green flags that apply>"],
  "classification_rationale": "<2-3 sentences explaining the verdict>",
  "proceed_recommendation": "PROCEED|WARN|ABORT",
  "suggested_pivot": "<if WARN or ABORT: one concrete change that would make this a stronger painkiller>"
}}
""",
        fallback=lambda: _fallback_classify(idea),
    )
