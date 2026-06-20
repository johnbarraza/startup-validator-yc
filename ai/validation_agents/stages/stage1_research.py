from typing import Any

from ..config import ValidationConfig
from ..llm_client import LLMClient


def _fallback_research(idea: str) -> dict[str, Any]:
    alternatives = [
        ("Manual workaround", "Spreadsheet, notes, or ad hoc process", "Cheap and flexible, but slow and inconsistent."),
        ("Generic horizontal SaaS", "Broad workflow software", "Easy to adopt, but weak on domain-specific outcomes."),
        ("Incumbent enterprise platform", "Large vendor suite", "Trusted by buyers, but expensive and slow to implement."),
        ("Internal build", "Company-owned custom tooling", "Fits local process, but competes with engineering priorities."),
        ("Consulting or agency service", "Human-led service provider", "High-touch expertise, but margins and scale are limited."),
        ("Open-source project", "Community-maintained tool", "Low software cost, but support and reliability vary."),
        ("AI wrapper", "Thin LLM interface", "Fast to build, but easy to copy if workflow depth is missing."),
        ("Marketplace or network", "Connects supply and demand", "Useful when liquidity exists, hard to start from zero."),
        ("Mobile-first app", "Lightweight point solution", "Good distribution surface, often too shallow for serious workflows."),
        ("No-code automation", "Zapier/Airtable/Notion-style stack", "Good for prototypes, brittle for core operations."),
        ("Legacy desktop software", "Installed tool or old vertical app", "Embedded in workflows, poor UX and integrations."),
        ("Data dashboard", "BI/reporting layer", "Makes status visible, but may not drive action."),
        ("Community and content", "Newsletter, course, forum, or templates", "Can validate demand, but may not be software defensible."),
        ("API infrastructure", "Developer-facing primitives", "Scales well if developers are the buyer, indirect otherwise."),
        ("Status quo", "Doing nothing", "Always a competitor when pain is tolerable or budget is unclear."),
    ]
    return {
        "idea": idea,
        "market": "Unknown market inferred from founder-provided idea",
        "solutions": [
            {
                "id": f"S{i:02d}",
                "name": name,
                "category": category,
                "observed_positioning": note,
            }
            for i, (name, category, note) in enumerate(alternatives, start=1)
        ],
        "research_summary": (
            "Fallback mode cannot perform live market research, so it maps the idea against the common "
            "alternative categories every startup must beat: manual work, internal builds, incumbents, "
            "consultants, generic SaaS, open-source, and doing nothing. Use live LLM mode or add external "
            "research artifacts for named competitors."
        ),
        "source": "deterministic_fallback",
    }


def run_stage1_research(client: LLMClient, config: ValidationConfig, idea: str, context: str) -> dict[str, Any]:
    return client.json_completion(
        model=config.research_model,
        temperature=0.3,
        system_prompt=(
            "You are a market researcher and competitive intelligence analyst for a YC-style founder. "
            "Return only valid JSON. Be concrete, skeptical, and evidence-based."
        ),
        user_prompt=f"""Research the top 15 current alternatives for this startup idea AND score each
competitor using the 6-signal deal-sourcing taxonomy from venture-capital-intelligence.

IDEA: {idea}

PROJECT CONTEXT: {context[:4000]}

━━━ PART 1: Competitive alternatives ━━━
List 15 alternatives (incumbents, workarounds, direct competitors, indirect substitutes, do-nothing).

━━━ PART 2: Signal scoring for top 5 competitors ━━━
For the 5 most dangerous competitors, score each of these 6 signals (1-10):
- HIRING: headcount growth, GTM/eng roles being filled
- FUNDING: recent raises, investor quality, runway signals
- PRODUCT: feature launches, integrations, review momentum
- TEAM: exec hires/departures, advisor additions
- MARKET: category growth, acquisitions, regulatory tailwinds
- TECH: stack sophistication, GitHub activity, API/dev adoption

Signal strength: 9-10=very strong, 7-8=strong, 5-6=moderate, 3-4=weak, 1-2=noise
Sentiment: POSITIVE / NEGATIVE / NEUTRAL
Overall deal score 0-100 → classification: MONITOR / ENGAGE / MOVE_FAST

Return JSON with keys:
idea, market, solutions, research_summary, competitor_signals.

solutions: list of {{id, name, category, observed_positioning}}
competitor_signals: list of {{
  competitor, hiring_score, funding_score, product_score,
  team_score, market_score, tech_score, overall_score,
  classification, sentiment, sourcing_brief
}}
""",
        fallback=lambda: _fallback_research(idea),
    )
