from typing import Any

from ..config import ValidationConfig
from ..llm_client import LLMClient


PITCH_SECTIONS = [
    "one_liner",
    "problem",
    "solution_insight",
    "why_now",
    "market",
    "competition_moat",
    "business_model_pricing",
    "go_to_market",
    "traction_signals",
    "roadmap",
    "risks_mitigations",
    "the_ask",
    "product_demo_architecture",
]


SCORING_DIMENSIONS = [
    ("problem_validation", 15),
    ("solution_insight", 10),
    ("market_quality", 15),
    ("competition_moat", 10),
    ("business_model_pricing", 10),
    ("go_to_market", 10),
    ("traction_or_evidence", 10),
    ("execution_roadmap", 10),
    ("risk_control", 10),
]


def _score(name: str, max_points: int, points: int, note: str) -> dict[str, Any]:
    return {
        "dimension": name,
        "points": points,
        "max_points": max_points,
        "note": note,
    }


def _fallback_region(region: str) -> dict[str, Any]:
    if region.lower() == "peru":
        return {
            "region": "Peru",
            "validity": "Potentially strong for problems with local regulation, Spanish workflows, public data, or underserved SMEs.",
            "tam": "Estimate from national population, firms, households, sector output, or public expenditure.",
            "sam": "Start with reachable cities, industries, institutions, or customer segments where the founder can sell.",
            "som_12_months": "Use a bottom-up estimate: reachable leads x conversion rate x annual contract value.",
            "recommended_sources": [
                "INEI microdata and surveys",
                "MEF budget data",
                "BCRP statistics",
                "sector associations",
                "local interviews",
            ],
        }
    if region.lower() == "latam":
        return {
            "region": "LATAM",
            "validity": "Attractive if the problem repeats across Spanish-speaking markets and does not require heavy country-by-country integration.",
            "tam": "Estimate from regional sector size, number of firms, workers, students, patients, transactions, or institutions.",
            "sam": "Prioritize countries with similar language, regulation, distribution, and payment behavior.",
            "som_12_months": "Estimate expansion only after proving one repeatable channel in the first country.",
            "recommended_sources": [
                "World Bank",
                "IDB",
                "ECLAC/CEPAL",
                "national statistics offices",
                "industry reports",
            ],
        }
    return {
        "region": "USA",
        "validity": "Useful benchmark for market size and competitor density; attractive if willingness to pay is higher and distribution is reachable.",
        "tam": "Estimate from US sector spend, number of businesses, paid seats, transactions, or workflow volume.",
        "sam": "Narrow to a buyer segment the founder can actually reach through outbound, communities, or integrations.",
        "som_12_months": "Use a conservative founder-led sales or self-serve acquisition model.",
        "recommended_sources": [
            "US Census",
            "BLS",
            "World Bank",
            "Statista or industry reports",
            "academic papers",
        ],
    }


def _fallback_dossier(
    idea: str,
    gap: dict[str, Any],
    validation: dict[str, Any],
    simulation: dict[str, Any],
    regions: list[str],
) -> dict[str, Any]:
    scorecard = [
        _score("problem_validation", 15, 8, "Promising only after 5 concrete user interviews prove recent painful behavior."),
        _score("solution_insight", 10, 6, "Insight needs sharper wording around what existing alternatives miss."),
        _score("market_quality", 15, 7, "Market sizing is not yet evidenced; compare Peru, LATAM, and USA before choosing focus."),
        _score("competition_moat", 10, 5, "Moat is weak until workflow data, distribution, or community compounds."),
        _score("business_model_pricing", 10, 6, "Pricing needs a concrete buyer metric and contribution margin assumptions."),
        _score("go_to_market", 10, 6, "First 10 users can be founder-led; first 100 and 1,000 need a repeatable channel."),
        _score("traction_or_evidence", 10, 3, "No traction provided in the input; require interviews, waitlist, pilots, or usage."),
        _score("execution_roadmap", 10, 7, "A 3/6/12 month roadmap is feasible if the first wedge is narrow."),
        _score("risk_control", 10, 6, "AI-platform substitution and weak demand are the main risks to control."),
    ]
    total = sum(item["points"] for item in scorecard)
    max_total = sum(item["max_points"] for item in scorecard)
    region_list = [_fallback_region(region.strip()) for region in regions if region.strip()]

    return {
        "source": "deterministic_fallback",
        "one_liner": f"We help a specific customer segment solve '{gap.get('title', 'a painful workflow')}' through a focused software/AI workflow.",
        "problem": {
            "who_suffers": "Define one specific user and one economic buyer. Avoid broad labels like 'everyone' or 'companies'.",
            "pain_level": "Quantify hours lost, money lost, risk, errors, or missed revenue per month.",
            "current_workaround": "Identify the real competitor: spreadsheet, WhatsApp, email, manual labor, incumbent, or doing nothing.",
            "evidence_needed": "At least 5 interviews, screenshots, public data, or workflow artifacts.",
        },
        "solution_insight": {
            "solution": "A narrow workflow that produces an outcome the buyer already values.",
            "insight": "The likely insight is not 'AI can do it'; it is that a repeated expert workflow can be compressed and standardized.",
            "non_stack_note": "This dossier intentionally avoids frontend/backend stack because the correct stack changes by idea.",
        },
        "why_now": [
            "LLMs and agents can now execute and explain multi-step workflows cheaply.",
            "Distribution through communities, outbound, and self-serve demos is faster for solo founders.",
            "Users are more willing to try AI-native tools when the workflow is narrow and auditable.",
        ],
        "market": {
            "recommended_focus": "Start where the founder has fastest access to users and evidence; compare Peru, LATAM, and USA before committing.",
            "regions": region_list,
            "source_strategy": [
                "Use INEI microdata for Peru when the market depends on households, employment, education, health, agriculture, firms, or municipalities.",
                "Use MEF/BCRP for public budgets, macro indicators, credit, sector output, and Peru-specific economic framing.",
                "Use World Bank/CEPAL/IDB for LATAM comparables.",
                "Use papers and industry reports when the market is technical, clinical, educational, or scientific.",
                "Use bottom-up SOM for the first 12 months; do not rely only on top-down TAM.",
            ],
        },
        "competition_moat": {
            "alternatives_to_compare": ["doing nothing", "spreadsheet/manual workflow", "horizontal SaaS", "incumbent platform", "AI assistant"],
            "moat_candidates": ["proprietary workflow data", "distribution/community", "integrations", "trust/brand", "regulatory or local-domain expertise"],
            "weak_moat_warning": "If Claude/OpenAI can solve the job with a prompt, the startup needs a workflow, data, distribution, or compliance layer.",
        },
        "business_model_pricing": {
            "model_options": ["monthly SaaS", "usage-based", "transaction fee", "marketplace take rate", "paid pilot", "enterprise license"],
            "pricing_rule": "Use no more than 3 plans and tie price to a buyer-visible outcome.",
            "contribution_margin": "Estimate tokens/API calls, storage, human review, support, and acquisition cost per customer.",
        },
        "go_to_market": {
            "first_10": "Founder-led outreach to people with the exact painful workflow.",
            "first_100": "Repeat the channel that produced the first paid or high-intent users.",
            "first_1000": "Add scalable distribution: partnerships, integrations, content, community, marketplace, or PLG.",
        },
        "traction_signals": [
            "5+ interviews with recent pain stories",
            "waitlist with qualified users",
            "letters of intent or paid pilots",
            "prototype usage by real users",
            "before/after workflow evidence",
        ],
        "roadmap": {
            "3_months": "Validate the wedge, ship concierge/prototype workflow, close first paying or high-intent users.",
            "6_months": "Productize repeated steps, measure retention, build first repeatable acquisition channel.",
            "12_months": "Expand to adjacent workflow or geography after proving retention and willingness to pay.",
        },
        "risks_mitigations": [
            {
                "risk": "Market risk: users like the idea but do not have urgent pain.",
                "mitigation": "Interview around recent behavior and require evidence of money/time/risk.",
            },
            {
                "risk": "AI substitution risk: Claude, OpenAI, or another foundation-model tool absorbs the feature.",
                "mitigation": "Own workflow data, distribution, integrations, evaluation harnesses, and domain trust beyond the prompt.",
            },
            {
                "risk": "Execution risk: solo founder overbuilds before validation.",
                "mitigation": "Run concierge tests and kill criteria before building broad product surface area.",
            },
        ],
        "the_ask": {
            "amount": "Define a specific amount or resource ask only after the first validation sprint.",
            "use_of_funds": ["customer discovery", "prototype", "data acquisition", "distribution experiments"],
            "milestone": "Unlock proof that one segment has repeated pain and will pay for the outcome.",
        },
        "product_demo_architecture": {
            "demo_url": "TODO: deploy a public demo (Streamlit, Vercel, Railway, or Hugging Face Spaces)",
            "demo_credentials": "TODO: add test user credentials once demo is live",
            "main_flow_screenshots": [
                "1. Landing / onboarding screen",
                "2. Core input form or conversation entry",
                "3. AI processing / loading state",
                "4. Result / output screen",
                "5. Export or share action",
                "6. Settings or profile (optional)",
            ],
            "architecture_diagram": (
                "Frontend (web/mobile) → API layer (FastAPI / Flask) → "
                "Orchestration (agent loop) → LLM API + domain data sources → "
                "Database (Postgres / SQLite) → Output / report"
            ),
            "repo_structure": [
                "frontend/  — UI (React / Streamlit / Vue)",
                "backend/   — API + agent logic",
                "ai/        — prompts, agents, pipelines",
                "data/      — seed data, validation sets",
                "notebooks/ — exploration and analysis",
                "docs/      — architecture diagram, pitch assets",
            ],
            "ai_models_used": [
                "deepseek-chat — fast, cheap inference for classification and structured extraction",
                "deepseek-reasoner — multi-step reasoning for validation and scoring",
            ],
        },
        "scorecard": scorecard,
        "total_score": total,
        "max_score": max_total,
        "rating": "Promising but unvalidated" if total >= 55 else "Needs sharper validation",
        "external_research_hooks": {
            "inei_microdatos": "Useful for Peru-specific TAM/SAM evidence from INEI surveys and variable search.",
            "paperdl": "Useful for finding academic papers when the idea needs scientific, health, education, or technical evidence.",
        },
        # Pressure-test scorecard (startup-pressure-test framework)
        "pressure_test_scorecard": {
            "pain_intensity": 3,
            "buyer_clarity": 2,
            "urgency": 3,
            "differentiation": 2,
            "speed_to_validate": 4,
            "founder_advantage": 2,
            "total": 16,
        },
        # Fatal flaws (pressure-test framework)
        "fatal_flaws": [
            {
                "risk": "Market risk: users like the idea but don't have urgent pain.",
                "severity": "HIGH",
                "why_it_matters": "No urgency = no switching from free alternatives.",
                "fast_test": "5 interviews asking about last time this pain cost them time or money.",
            },
            {
                "risk": "Payment blocker: buyer can't pay via SaaS subscription given Peru's informal economy.",
                "severity": "HIGH",
                "why_it_matters": "No recurring billing = no SaaS business model.",
                "fast_test": "Ask 3 target buyers if they have a credit card or Yape for business payments.",
            },
            {
                "risk": "Free substitute absorbs 80% of use case before product ships.",
                "severity": "MEDIUM",
                "why_it_matters": "WhatsApp + Excel + Google Forms are entrenched and free.",
                "fast_test": "Map every step of the workflow to existing free tools; identify the gap.",
            },
        ],
        # First 10 customers (pressure-test framework — manual, founder-led)
        "first_10_customers": [
            {
                "action": "Send 20 WhatsApp voice messages to target buyers with a 2-sentence problem statement.",
                "channel": "WhatsApp",
                "target_persona": "Decision-maker in the target segment",
                "how_to_reach": "Use LinkedIn to find names, then WhatsApp via shared group or mutual contact.",
            },
            {
                "action": "Run a 30-min Zoom demo for 5 warm contacts who already have this pain.",
                "channel": "LinkedIn",
                "target_persona": "Operators who currently use the manual workaround",
                "how_to_reach": "Search LinkedIn for job title + pain keyword, send a connection note referencing the exact problem.",
            },
            {
                "action": "Attend one industry event or WhatsApp group where target buyers gather.",
                "channel": "community",
                "target_persona": "Any buyer who attends sector events or online communities",
                "how_to_reach": "Join the WhatsApp group, post a pain-question (not a pitch), DM respondents.",
            },
        ],
        # MVP 2-week test (pressure-test framework)
        "mvp_2_week_test": {
            "build": "A single-workflow prototype: one input, one output — no dashboard, no settings.",
            "cut": "Authentication, billing, multi-user, reporting, and any feature beyond the core workflow.",
            "test_hypothesis": "If 3 of 5 demo users complete the workflow without help and ask 'when can I use this?', demand is real.",
            "success_signal": "At least 1 user offers to pay or signs a letter of intent within 2 weeks.",
        },
    }


def run_stage3c_dossier(
    client: LLMClient,
    config: ValidationConfig,
    idea: str,
    gap: dict[str, Any],
    validation: dict[str, Any],
    simulation: dict[str, Any],
    regions: list[str],
    context: str,
) -> dict[str, Any]:
    persona_concerns = "\n".join(
        f"  - {r.get('role', '?')} (score={r.get('score','?')}): {r.get('concern', '')}"
        for r in simulation.get("persona_results", [])
    ) or "  (no simulation data)"

    sim_gate = simulation.get("aggregate_score", "?")
    primary_region = regions[0] if regions else "Peru"

    return client.json_completion(
        model=config.reasoner_model,
        temperature=0.1,
        system_prompt=(
            f"You are a brutally honest YC partner building a startup dossier. "
            f"Primary market: {primary_region}. Use local data sources (MINEDU, SUNEDU, MTPE, INEI, MEF, BCRP) "
            f"for Peru estimates. Return ONLY valid JSON with all required fields at root level."
        ),
        user_prompt=f"""Build a rigorous YC-style startup dossier. Be specific to the idea — no generic placeholders.

IDEA:
{idea}

SELECTED GAP:
{gap}

YC VALIDATION RESULT:
{validation.get('go_no_go')} — {validation.get('decision', '')}

STAKEHOLDER SIMULATION (MiroFish parallel agents, aggregate={sim_gate}):
Persona concerns to address in the dossier:
{persona_concerns}

REGIONS: {regions}
YC CONTEXT: {context[:4000]}

═══ STRICT FORMAT REQUIREMENTS ═══

market MUST use this exact structure (dual-method TAM per region):
{{
  "recommended_focus": "<which region and why>",
  "regions": [
    {{
      "region": "Peru",
      "validity": "<why Peru is or isn't the right starting market>",
      "tam_topdown": "<industry report estimate × addressable fraction, with source>",
      "tam_bottomup": "<potential customers × ARPU — validate against top-down>",
      "tam_consensus": "<agreed TAM range, flag if < $50M as sub-venture-scale>",
      "sam": "<TAM × 10-30% — reachable segment with rationale>",
      "som_12_months": "<SAM × 1-10% — bottom-up: leads × conversion × ACV>",
      "venture_threshold": "ABOVE_$1B / BELOW_$1B / BORDERLINE",
      "recommended_sources": ["MINEDU", "SUNEDU", "MTPE", "INEI", "MEF", ...]
    }},
    {{"region": "LATAM", "tam_topdown": "...", "tam_bottomup": "...", "tam_consensus": "...", "sam": "...", "som_12_months": "...", "venture_threshold": "...", "recommended_sources": [...]}},
    {{"region": "USA", "tam_topdown": "...", "tam_bottomup": "...", "tam_consensus": "...", "sam": "...", "som_12_months": "...", "venture_threshold": "...", "recommended_sources": [...]}}
  ],
  "source_strategy": ["<how to find each number>", ...]
}}

roadmap MUST be monthly with milestones and metrics:
{{
  "month_1": "<specific actions and metric target>",
  "month_2": "...",
  "month_3": "...",
  "month_6": "<state of product, users, revenue>",
  "month_9": "...",
  "month_12": "<ARR target, users, key partnerships>",
  "key_metrics_at_12m": {{
    "mrr_usd": <number>,
    "paying_customers": <number>,
    "churn_target": "<monthly %>",
    "cac_target_usd": <number>
  }}
}}

the_ask MUST justify every dollar with critical reasoning:
{{
  "amount_usd": <number>,
  "type": "pre-seed grant / angel / accelerator",
  "runway_months": <number>,
  "budget_breakdown": [
    {{"line": "<item>", "amount_usd": <number>, "rationale": "<why this amount, not more/less>"}},
    ...
  ],
  "milestone_unlocked": "<specific measurable outcome this funding achieves>",
  "critical_assumption_being_tested": "<the one thing this money proves or kills>",
  "why_not_less": "<why bootstrapping or a smaller amount would fail>",
  "why_not_more": "<why raising more before this milestone is premature>"
}}

scorecard: dict of {{dimension: score}} where all scores sum to total_score.
total_score and max_score MUST appear as separate integer fields at root level.

pressure_test_scorecard: score each dimension 1-5 (from startup-pressure-test framework):
{{
  "pain_intensity": <1-5>,
  "buyer_clarity": <1-5>,
  "urgency": <1-5>,
  "differentiation": <1-5>,
  "speed_to_validate": <1-5>,
  "founder_advantage": <1-5>,
  "total": <sum, max 30>
}}

fatal_flaws: the 3 most dangerous risks (from pressure-test framework):
[
  {{
    "risk": "<specific failure mode>",
    "severity": "HIGH|MEDIUM|LOW",
    "why_it_matters": "<one sentence>",
    "fast_test": "<cheapest way to prove or kill this risk in <2 weeks>"
  }},
  ...max 3...
]

first_10_customers: 3 most actionable manual traction moves (founder-led, no ads):
[
  {{
    "action": "<specific outreach or demo action>",
    "channel": "WhatsApp|LinkedIn|cold-call|event|referral|community|other",
    "target_persona": "<exact role and company type>",
    "how_to_reach": "<specific script or approach>"
  }},
  ...3 items...
]

mvp_2_week_test: smallest test that proves or kills the riskiest assumption:
{{
  "build": "<what to build in 2 weeks — one workflow, one output>",
  "cut": "<what NOT to build — features that don't test the core assumption>",
  "test_hypothesis": "<if X users do Y within 2 weeks, the assumption is validated>",
  "success_signal": "<the single metric that confirms demand>"
}}

Return JSON with exactly these root keys:
source, one_liner, problem, solution_insight, why_now, market, competition_moat,
business_model_pricing, go_to_market, traction_signals, roadmap, risks_mitigations,
the_ask, product_demo_architecture, scorecard, total_score, max_score, rating,
external_research_hooks, pressure_test_scorecard, fatal_flaws, first_10_customers,
mvp_2_week_test.

product_demo_architecture: concrete for this specific idea (no generic placeholders).
external_research_hooks: list of strings citing specific Peru data sources.
""",
        fallback=lambda: _fallback_dossier(idea, gap, validation, simulation, regions),
    )
