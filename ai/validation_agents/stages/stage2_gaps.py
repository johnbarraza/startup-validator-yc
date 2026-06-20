from typing import Any

from ..config import ValidationConfig
from ..llm_client import LLMClient


def _fallback_gaps(research: dict[str, Any]) -> dict[str, Any]:
    gaps = [
        {
            "id": "G1",
            "title": "Narrow painful workflow",
            "pain": "The idea needs one urgent job-to-be-done, not a broad feature set.",
            "why_now": "AI and modern software can compress expert work, but only if the workflow is specific.",
            "evidence_needed": "Interview 5 target users and capture the exact task they already spend time or money on.",
            "priority": 1,
            "risk": "If the workflow is vague, the product becomes a solution looking for a problem.",
        },
        {
            "id": "G2",
            "title": "Buyer-visible outcome",
            "pain": "Users may like the product, but the buyer needs a measurable business result.",
            "why_now": "Founders can now instrument usage, cost, and time saved from the first prototype.",
            "evidence_needed": "Ask who owns the budget and what metric would justify payment this month.",
            "priority": 2,
            "risk": "Without a buyer metric, adoption can stall at free-user enthusiasm.",
        },
        {
            "id": "G3",
            "title": "Distribution wedge",
            "pain": "A useful product still fails if reaching users is too slow or expensive.",
            "why_now": "Communities, outbound, integrations, and content can reveal a repeatable first channel.",
            "evidence_needed": "Run 3 small acquisition tests and measure replies, demos, or waitlist conversion.",
            "priority": 3,
            "risk": "A channel that works once may not repeat without founder-led effort.",
        },
        {
            "id": "G4",
            "title": "Trust and switching friction",
            "pain": "Users keep existing tools unless the new workflow is clearly safer, faster, or cheaper.",
            "why_now": "Agentic workflows can generate strong first drafts, but users need proof and control.",
            "evidence_needed": "Ask users what would make them trust the product with a real task.",
            "priority": 4,
            "risk": "Trust gaps can turn an impressive demo into a non-critical side tool.",
        },
        {
            "id": "G5",
            "title": "Defensible workflow data",
            "pain": "A generic AI interface is easy to copy unless usage creates proprietary process insight.",
            "why_now": "Every interaction can teach the system where users hesitate, correct, or approve.",
            "evidence_needed": "Define what unique data the product captures after 30 days of usage.",
            "priority": 5,
            "risk": "If no proprietary learning loop exists, incumbents can clone the surface area.",
        },
    ]
    return {
        "research_source": research.get("source", "unknown"),
        "gaps": gaps,
        "recommended_gap_id": "G1",
        "checkpoint_instruction": "Choose one gap with --gap-id G1, or run --auto to select the recommended gap.",
        "source": "deterministic_fallback",
    }


def run_stage2_gaps(client: LLMClient, config: ValidationConfig, research: dict[str, Any]) -> dict[str, Any]:
    return client.json_completion(
        model=config.research_model,
        temperature=0.2,
        system_prompt=(
            "You are a skeptical market-gap analyst. Return only valid JSON. "
            "Rank gaps by customer pain, speed to validate, and defensibility."
        ),
        user_prompt=f"""
Given this competitive research, identify 5 to 8 market gaps for the startup idea.
Do not assume any specific industry unless it is explicitly present in the research.

Research JSON:
{research}

Return JSON with keys: research_source, gaps, recommended_gap_id, checkpoint_instruction.
Each gap must include id, title, pain, why_now, evidence_needed, priority, risk.
""",
        fallback=lambda: _fallback_gaps(research),
    )
