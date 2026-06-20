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
        "70% informal economy — most economic activity happens outside registered firms. "
        "Public schools (80% of secondary schools) have zero discretionary budget; procurement flows through UGEL "
        "(regional education offices) with 6-18 month cycles. Private schools have budget but are small and fragmented. "
        "B2B payment is wire transfer or cash; no SaaS credit card billing by default. "
        "Primary B2B distribution channel is WhatsApp and face-to-face, not email. "
        "Regulatory mandates (MINEDU) exist but schools routinely ignore them for years without consequence. "
        "WTP for software is low — S/50-200/month is a stretch for most private schools. "
        "Trust in digital tools is built through referrals and demos, not marketing."
    ),
    "LATAM": (
        "High income inequality across all countries. Brazil, Colombia, Mexico have larger formal sectors. "
        "Each country requires separate compliance, localization, and sales motion. "
        "EdTech B2B sales cycles are long (3-12 months) and involve multiple stakeholders. "
        "Payment infrastructure varies — PIX in Brazil, PSE in Colombia, SPEI in Mexico. "
        "WhatsApp is the primary business communication tool across all LATAM markets."
    ),
    "USA": (
        "Higher WTP — SaaS B2B $100-500/month is normal for SMB. "
        "EdTech is regulated at state level; no single federal compliance mandate. "
        "Strong competition from Naviance, Handshake, Clever, and Google Classroom integrations. "
        "Distribution through school districts and state education agencies, not individual schools. "
        "Public schools funded through local property taxes — wide variance in budget by district. "
        "Credit card billing and PLG (product-led growth) work well for small schools."
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


def _merge_results(
    classifier: dict[str, Any],
    devil: dict[str, Any],
) -> dict[str, Any]:
    """Merge optimistic classifier + devil's advocate into final verdict."""
    devil_verdict = devil.get("devil_verdict", "WEAK")
    classifier_rec = classifier.get("proceed_recommendation", "WARN")

    # Stricter verdict wins when devil finds FATAL issues
    if devil_verdict == "FATAL":
        final_rec = "ABORT"
    elif devil_verdict == "WEAK" and classifier_rec == "PROCEED":
        final_rec = "WARN"
    else:
        final_rec = classifier_rec

    # Combine pit signals from both agents
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
        "source": "dual_agent_classification",
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

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        f_classifier = executor.submit(_run_classifier, client, config, idea, context)
        f_devil = executor.submit(_run_devil_advocate, client, config, idea, context)
        classifier = f_classifier.result()
        devil = f_devil.result()

    return _merge_results(classifier, devil)
