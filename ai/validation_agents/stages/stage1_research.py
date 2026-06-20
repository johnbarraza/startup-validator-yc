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
        model=config.chat_model,
        temperature=0.3,
        system_prompt=(
            "You are a market researcher for a YC-style founder. Return only valid JSON. "
            "Be concrete, skeptical, and focused on existing alternatives."
        ),
        user_prompt=f"""
Research the top 15 current alternatives for this startup idea. Do not assume any specific industry
unless it is explicitly present in the idea.

Idea:
{idea}

Project context:
{context[:5000]}

Return JSON with keys: idea, market, solutions, research_summary.
Each solution must include id, name, category, observed_positioning.
""",
        fallback=lambda: _fallback_research(idea),
    )
