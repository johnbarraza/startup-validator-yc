"""Stage 0 — Idea classifier, devil's advocate, and country structural context.

Two parallel LLM calls:
  1. CLASSIFIER  — standard pit check (optimistic, finds green flags)
  2. DEVIL'S ADVOCATE — adversarial critic that MUST find at least 3 red flags

Results are merged. The stricter verdict wins unless both agents agree on PROCEED.

Also generates:
  country_structural_context — economic reality per country (informality,
    payment friction, buyer reality, distribution channel)
  freemium_recommendation — YES/NO/MAYBE with rationale
"""
import concurrent.futures
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

COUNTRY_STRUCTURAL_FACTS = {
    "Peru": (
        # Economy & informality (sources: ILO, World Bank, INEI 2024)
        "70-75% of workforce is informal. GDP per capita $8,400 (2024), high inequality (Gini 0.43). "
        "36% of population below $8.30/day PPP — large segment cannot pay for software subscriptions. "
        "Lima represents ~90% of the addressable SaaS market; outside Lima, smartphone penetration and WTP drop sharply. "

        # VC & funding (sources: PECAP 2023, Cuantico data)
        "VC ecosystem is early: Peru receives <3% of LATAM VC (Brazil ~50%, Mexico ~25%, Colombia ~10%). "
        "Only ~7 notable VC-backed deals in 2023. Typical seed checks: Wayra $50-75K, angel $50-300K. "
        "Series A ($500K-$5M) virtually requires an international co-investor — local capital dries up at growth stage. "
        "Opportunity: VC gap means less competition and better terms at seed, but must build for regional scale from day 1. "
        "Active funds: Wayra Peru, UTEC Ventures, Magma Partners (regional), Endeavor Peru, COFIDE (emerging co-investor). "
        "Non-dilutive options: StartupPeru grants S/100K-500K (~$27K-135K), CONCYTEC R&D grants. "

        # AI adoption (sources: McKinsey 2025, ENAI, sector reports)
        "AI adoption is very early — estimated 5-15% of businesses use AI in any capacity (3-5 years behind Brazil/Mexico). "
        "Early adopters: banking (BCP/Credicorp chatbots, fraud detection), mining (predictive maintenance), large retail. "
        "Barriers: severe ML/AI talent shortage, low digitalization baseline (many SMEs still on Excel/paper), "
        "no dedicated government AI fund, ENAI strategy published 2021 but implementation stalled. "
        "Opportunity: first-mover advantage in vertical AI is real — low local competition, international tools not localized. "

        # Payments & distribution
        "B2C payment rails: Yape (BCP, 10M+ users) and Plin (BBVA+Interbank, 8M+ users) — consumer SaaS must integrate these. "
        "B2B payment: CCI bank transfer standard; no widespread B2B credit card billing; no Stripe equivalent locally. "
        "Local payment processors: Culqi, PayU, Mercado Pago — all add friction vs international. "
        "Primary B2B sales channel: WhatsApp and face-to-face demo, not email campaigns or PLG. "

        # Procurement & regulatory
        "Government/public procurement: flows through OSCE/UGEL with 6-18 month cycles; public budgets are rigid. "
        "Regulatory mandates (MINEDU, OSINERGMIN, SUNAT) exist but enforcement lag is 6-18 months — mandate alone is not a forcing function. "
        "WTP for SaaS: S/50-200/month for SME, S/500-2000/month for mid-market — significantly below US/EU equivalents. "

        # Talent & internet
        "Internet penetration 74.7% (25.78M users, DataReportal 2024); mobile connections 109.8% of population. "
        "Senior ML/AI talent scarce and expensive relative to market; junior developers increasingly available from UTEC, UPC, PUCP, UP. "
        "TikTok reach 91.7% of adults — organic B2C distribution through short video is unusually accessible."
    ),
    "LATAM": (
        "Brazil (~50%), Mexico (~25%), Colombia (~10%) dominate LATAM VC — Peru, Chile, Argentina share the rest. "
        "Each country requires separate compliance, localization, and sales motion — do not assume one product fits all. "
        "B2B sales cycles 3-12 months; enterprise and government add complexity. "
        "Payment rails vary: PIX (Brazil, instant, near-universal), PSE (Colombia), SPEI (Mexico), Yape/Plin (Peru). "
        "WhatsApp is the primary B2B communication tool across all LATAM markets — email open rates are low. "
        "AI adoption is ahead of Peru in Brazil and Mexico but still early vs North America/Europe. "
        "Regional expansion requires local legal entity, local payment integration, and local GTM — budget accordingly."
    ),
    "USA": (
        "Higher WTP — SaaS B2B $100-500/month is standard for SMB; enterprise $1K-10K/month. "
        "Credit card billing and PLG (product-led growth) work well; Stripe is standard. "
        "AI adoption far ahead — most verticals already have well-funded AI incumbents; competition is fierce. "
        "Distribution through marketplaces (App Store, Shopify, Salesforce AppExchange), communities, and content. "
        "Regulatory varies by state; federal AI regulation still emerging (2024-2025). "
        "Talent is expensive ($150K-300K/year for senior ML engineers); offshore team required to control COGS. "
        "Venture scale requires TAM > $1B and a clear path to $100M ARR — Peru-only ideas rarely qualify."
    ),
}


def _run_classifier(
    client: LLMClient,
    config: ValidationConfig,
    idea: str,
    context: str,
) -> dict[str, Any]:
    """Pass 1: Standard optimistic classifier."""
    verticals_text = ", ".join(VERTICALS)
    problem_type_text = "\n".join(f"- {k}: {v}" for k, v in PROBLEM_TYPE_DEFS.items())
    country_context = "\n".join(f"\n{k}:\n{v}" for k, v in COUNTRY_STRUCTURAL_FACTS.items())

    return client.json_completion(
        model=config.classifier_model,
        temperature=0.1,
        system_prompt=(
            "You are a YC partner screening startup ideas. "
            "Classify honestly. Consider country-specific economic realities. "
            "Return only valid JSON."
        ),
        user_prompt=f"""Classify this startup idea.

IDEA: {idea}

PROBLEM TYPES:
{problem_type_text}

VERTICALS: {verticals_text}
CUSTOMER TYPES: B2B, B2C, B2G, B2B2C, Marketplace
PROBLEM SEVERITY: STRUCTURAL / RECURRING / CONVENIENCE / COSMETIC

COUNTRY STRUCTURAL REALITIES (apply to the relevant market):
{country_context}

PAINKILLER SIGNALS (need 3+ to PROCEED):
- Active workarounds exist (spreadsheets, manual labor, WhatsApp groups)
- Spending already happens on imperfect solutions
- Regulatory / compliance forcing function with real enforcement
- Recurring pain: weekly or more often
- Measurable cost: lost hours, revenue, or compliance risk
- B2B: buyer has a budget line that already covers this kind of cost
- Users search actively for solutions

PROCEED RULES:
- PROCEED: PAINKILLER, 3+ green flags, 0-1 red flags, buyer can actually pay given country context
- WARN: VITAMIN, or green flags exist but buyer payment path is unclear given country economics
- ABORT: PIT or CROWDED_COPYCAT with no wedge

Return JSON:
{{
  "problem_type": "PAINKILLER|VITAMIN|PIT|CROWDED_COPYCAT",
  "vertical": "<from list>",
  "customer_type": "B2B|B2C|B2G|B2B2C|Marketplace",
  "problem_severity": "STRUCTURAL|RECURRING|CONVENIENCE|COSMETIC",
  "pain_evidence": "<evidence present or missing>",
  "painkiller_signals_detected": ["<green flags that apply>"],
  "classification_rationale": "<2-3 sentences>",
  "proceed_recommendation": "PROCEED|WARN|ABORT",
  "freemium_recommendation": "YES|NO|MAYBE",
  "freemium_rationale": "<why free tier helps or hurts given buyer type and country economics>"
}}

YC context: {context[:2000]}
""",
        fallback=lambda: {
            "problem_type": "VITAMIN",
            "vertical": "Other",
            "customer_type": "B2C",
            "problem_severity": "RECURRING",
            "pain_evidence": "No LLM — assume VITAMIN.",
            "painkiller_signals_detected": [],
            "classification_rationale": "Deterministic fallback.",
            "proceed_recommendation": "WARN",
            "freemium_recommendation": "MAYBE",
            "freemium_rationale": "Cannot assess without LLM.",
            "source": "deterministic_fallback",
        },
    )


def _run_devil_advocate(
    client: LLMClient,
    config: ValidationConfig,
    idea: str,
    context: str,
) -> dict[str, Any]:
    """Pass 2: Adversarial critic — MUST find red flags and payment blockers."""
    country_context = "\n".join(f"\n{k}:\n{v}" for k, v in COUNTRY_STRUCTURAL_FACTS.items())

    return client.json_completion(
        model=config.classifier_model,
        temperature=0.4,
        system_prompt=(
            "You are a brutally skeptical YC partner who has seen 10,000 startup pitches fail. "
            "Your job is to FIND THE HOLES — not validate the idea. "
            "You MUST find at least 3 specific red flags even for good ideas. "
            "Consider country-specific economic realities. Return only valid JSON."
        ),
        user_prompt=f"""Find every reason this startup idea could FAIL or be a PIT.

IDEA: {idea}

COUNTRY STRUCTURAL REALITIES:
{country_context}

YOUR MISSION: Find the specific red flags, payment blockers, and structural risks.
Even if the idea seems good, find the 3-5 most likely reasons it fails.

PIT TRAPS TO CHECK:
- Does the regulatory mandate actually get enforced? Or do schools ignore it for years?
- Can the buyer actually pay? Or does the budget go through a slow bureaucracy?
- Is the workaround (Excel/WhatsApp) good enough that nobody will switch?
- Does the 70% informal economy mean the real market is much smaller than it looks?
- Will a government portal or free tool from MINEDU replace this before it scales?
- Is the founder underestimating the sales cycle to institutional buyers?
- Does this require changing teacher behavior — notoriously hard?
- Is the pain felt by the tutor (end user) but budget controlled by the director (buyer)?
- Are there enough private schools with budget to hit venture scale in Peru alone?
- Could a WhatsApp bot or Google Forms template eliminate 80% of the pain for free?

Return JSON:
{{
  "devil_verdict": "STRONG|WEAK|FATAL",
  "pit_signals_detected": [
    "<specific red flag 1 with concrete reasoning>",
    "<specific red flag 2>",
    "<specific red flag 3>",
    "<more if found>"
  ],
  "payment_blocker": "<the most likely reason the buyer doesn't pay, given country economics>",
  "free_substitute_risk": "<what free tool or workaround already covers 80% of this>",
  "market_size_reality_check": "<realistic paying market size given informality, procurement, WTP>",
  "hardest_assumption": "<the single most dangerous unvalidated assumption>",
  "devil_rationale": "<2-3 sentences on overall risk level>"
}}

YC context: {context[:1500]}
""",
        fallback=lambda: {
            "devil_verdict": "WEAK",
            "pit_signals_detected": ["Could not run devil's advocate without LLM."],
            "payment_blocker": "Unknown — run with LLM enabled.",
            "free_substitute_risk": "Unknown.",
            "market_size_reality_check": "Unknown.",
            "hardest_assumption": "Unknown.",
            "devil_rationale": "Deterministic fallback.",
            "source": "deterministic_fallback",
        },
    )


def _run_preflight(
    client: LLMClient,
    config: ValidationConfig,
    idea: str,
) -> dict[str, Any]:
    """Pass 3: Pre-flight 3-check (from startup-skill) + deal-signal taxonomy (from vc-intelligence).

    3 fast sanity checks before investing pipeline time:
      1. Dominant solution — is there already a well-funded winner?
      2. Precedent failure — has a startup tried this and publicly failed?
      3. Regulatory kill — obvious legal/compliance blocker?

    Plus deal-signal scan (Hiring / Funding / Product / Team / Market / Tech)
    based on what the LLM knows about the space.
    """
    return client.json_completion(
        model=config.classifier_model,
        temperature=0.2,
        system_prompt=(
            "You are a startup pre-flight analyst. Run fast sanity checks to surface "
            "instant-kill signals before the team invests validation time. "
            "Be specific and honest. Return only valid JSON."
        ),
        user_prompt=f"""Run a 3-point pre-flight check on this startup idea.

IDEA: {idea}

PRE-FLIGHT CHECK 1 — DOMINANT SOLUTION:
Is there already a well-funded, widely-adopted solution to this EXACT problem?
Name it. If multiple, name the strongest one.
Score: CLEAR (no dominant player) / CROWDED (strong incumbent exists) / WINNER_TAKES_ALL (monopoly)

PRE-FLIGHT CHECK 2 — PRECEDENT FAILURE:
Has a notable startup tried this exact idea and publicly failed or pivoted away?
If yes: name it, the year, and the key failure reason in one sentence.
Score: NO_KNOWN_FAILURE / KNOWN_FAILURE / MULTIPLE_FAILURES

PRE-FLIGHT CHECK 3 — REGULATORY KILL:
Is there an obvious legal, licensing, or compliance reason this idea CANNOT exist
or would be extremely hard to launch in Peru/LATAM without special permits?
Score: NO_BLOCKER / SOFT_BLOCKER (manageable with effort) / HARD_KILL (fatal)

DEAL-SIGNAL SCAN (from vc-intelligence taxonomy — Hiring/Funding/Product/Team/Market/Tech):
Based on the category this idea is in, identify which signals a founder should
watch to know if the space is heating up or cooling down.

Return JSON:
{{
  "preflight_dominant_solution": {{
    "score": "CLEAR|CROWDED|WINNER_TAKES_ALL",
    "competitor_name": "<name or 'none found'>",
    "threat_level": "LOW|MEDIUM|HIGH",
    "note": "<one sentence>"
  }},
  "preflight_precedent_failure": {{
    "score": "NO_KNOWN_FAILURE|KNOWN_FAILURE|MULTIPLE_FAILURES",
    "example": "<company name + year + key failure reason, or 'none'>",
    "learning": "<what the failure reveals about the space>"
  }},
  "preflight_regulatory_kill": {{
    "score": "NO_BLOCKER|SOFT_BLOCKER|HARD_KILL",
    "regulation": "<specific law or requirement if any>",
    "mitigation": "<how to handle it, or 'n/a'>"
  }},
  "deal_signals": {{
    "hiring": "<what hiring patterns in the space indicate>",
    "funding": "<recent funding activity in this category, if known>",
    "product": "<key product launches or milestones to watch>",
    "market": "<macro trend or market signal driving this space>",
    "tech": "<technology shift enabling or threatening this idea>",
    "momentum": "ACCELERATING|STABLE|DECLINING"
  }},
  "preflight_summary": "<1 sentence: proceed / caution / kill and why>"
}}
""",
        fallback=lambda: {
            "preflight_dominant_solution": {
                "score": "CLEAR",
                "competitor_name": "unknown",
                "threat_level": "MEDIUM",
                "note": "Could not run preflight without LLM.",
            },
            "preflight_precedent_failure": {
                "score": "NO_KNOWN_FAILURE",
                "example": "none",
                "learning": "Unknown.",
            },
            "preflight_regulatory_kill": {
                "score": "NO_BLOCKER",
                "regulation": "unknown",
                "mitigation": "n/a",
            },
            "deal_signals": {
                "hiring": "unknown",
                "funding": "unknown",
                "product": "unknown",
                "market": "unknown",
                "tech": "unknown",
                "momentum": "STABLE",
            },
            "preflight_summary": "Preflight ran without LLM — treat as unverified.",
            "source": "deterministic_fallback",
        },
    )


_PREFLIGHT_FALLBACK: dict[str, Any] = {
    "preflight_dominant_solution": {"score": "CLEAR", "competitor_name": "unknown", "threat_level": "MEDIUM", "note": "No LLM."},
    "preflight_precedent_failure": {"score": "NO_KNOWN_FAILURE", "example": "none", "learning": "Unknown."},
    "preflight_regulatory_kill": {"score": "NO_BLOCKER", "regulation": "unknown", "mitigation": "n/a"},
    "deal_signals": {"hiring": "unknown", "funding": "unknown", "product": "unknown", "market": "unknown", "tech": "unknown", "momentum": "STABLE"},
    "preflight_summary": "Preflight unavailable without LLM.",
}


def _merge_results(
    classifier: dict[str, Any],
    devil: dict[str, Any],
    preflight: dict[str, Any],
) -> dict[str, Any]:
    """Merge classifier + devil's advocate + preflight into final verdict."""
    devil_verdict = devil.get("devil_verdict", "WEAK")
    classifier_rec = classifier.get("proceed_recommendation", "WARN")

    # Hard kill from preflight overrides everything
    reg_kill = preflight.get("preflight_regulatory_kill", {}).get("score", "NO_BLOCKER")
    if reg_kill == "HARD_KILL":
        devil_verdict = "FATAL"

    # Stricter verdict wins when devil finds FATAL issues
    if devil_verdict == "FATAL":
        final_rec = "ABORT"
    elif devil_verdict == "WEAK" and classifier_rec == "PROCEED":
        final_rec = "WARN"
    else:
        final_rec = classifier_rec

    pit_signals = list(dict.fromkeys(
        devil.get("pit_signals_detected", []) +
        classifier.get("pit_signals_detected", [])
    ))

    return {
        "problem_type": classifier.get("problem_type", "VITAMIN"),
        "vertical": classifier.get("vertical", "Other"),
        "customer_type": classifier.get("customer_type", "B2C"),
        "problem_severity": classifier.get("problem_severity", "RECURRING"),
        "pain_evidence": classifier.get("pain_evidence", ""),
        "pit_signals_detected": pit_signals,
        "painkiller_signals_detected": classifier.get("painkiller_signals_detected", []),
        "classification_rationale": classifier.get("classification_rationale", ""),
        "proceed_recommendation": final_rec,
        "suggested_pivot": classifier.get("suggested_pivot", ""),
        "freemium_recommendation": classifier.get("freemium_recommendation", "MAYBE"),
        "freemium_rationale": classifier.get("freemium_rationale", ""),
        # Devil's advocate findings
        "devil_verdict": devil_verdict,
        "payment_blocker": devil.get("payment_blocker", ""),
        "free_substitute_risk": devil.get("free_substitute_risk", ""),
        "market_size_reality_check": devil.get("market_size_reality_check", ""),
        "hardest_assumption": devil.get("hardest_assumption", ""),
        "devil_rationale": devil.get("devil_rationale", ""),
        # Pre-flight checks (startup-skill pattern)
        "preflight_dominant_solution": preflight.get("preflight_dominant_solution", {}),
        "preflight_precedent_failure": preflight.get("preflight_precedent_failure", {}),
        "preflight_regulatory_kill": preflight.get("preflight_regulatory_kill", {}),
        "preflight_summary": preflight.get("preflight_summary", ""),
        # Deal-signal taxonomy (vc-intelligence pattern)
        "deal_signals": preflight.get("deal_signals", {}),
        "source": "triple_agent_classification",
    }


def _fallback_classify(idea: str) -> dict[str, Any]:
    return {
        "problem_type": "VITAMIN",
        "vertical": "Other",
        "customer_type": "B2C",
        "problem_severity": "RECURRING",
        "pain_evidence": "No LLM — assume VITAMIN until interviews confirm urgency.",
        "pit_signals_detected": ["Classification ran without LLM; treat as unverified."],
        "painkiller_signals_detected": [],
        "classification_rationale": "Deterministic fallback.",
        "proceed_recommendation": "WARN",
        "suggested_pivot": "Conduct 5 user interviews focused on recent behavior.",
        "freemium_recommendation": "MAYBE",
        "freemium_rationale": "Cannot assess without LLM.",
        "devil_verdict": "WEAK",
        "payment_blocker": "Unknown.",
        "free_substitute_risk": "Unknown.",
        "market_size_reality_check": "Unknown.",
        "hardest_assumption": "Unknown.",
        "devil_rationale": "Fallback — no LLM.",
        **_PREFLIGHT_FALLBACK,
        "source": "deterministic_fallback",
    }


def run_stage0_classify(
    client: LLMClient,
    config: ValidationConfig,
    idea: str,
    context: str,
) -> dict[str, Any]:
    if not client.enabled:
        return _fallback_classify(idea)

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        f_classifier = executor.submit(_run_classifier, client, config, idea, context)
        f_devil = executor.submit(_run_devil_advocate, client, config, idea, context)
        f_preflight = executor.submit(_run_preflight, client, config, idea)
        classifier = f_classifier.result()
        devil = f_devil.result()
        preflight = f_preflight.result()

    return _merge_results(classifier, devil, preflight)
