"""Discover, Pain-Finder, and Sharpen modes for the startup validation pipeline.

Mode 1 - Discover: problem domain -> N ideas -> Stage 0 ranked output.
  python -m ai.validation_agents.run_discover --discover --domain "mineria peruana"
  python -m ai.validation_agents.run_discover --discover --domain "salud mental LATAM" --n 8

Mode 2 - Pain Finder: web scrape real pain signals -> themes -> ideas -> Stage 0.
  python -m ai.validation_agents.run_discover --pain-finder --domain "mineria peruana"
  python -m ai.validation_agents.run_discover --pain-finder --domain "restaurantes Lima" --web

Mode 3 - Sharpen: vague idea -> 3 specific problem hypotheses -> sharpened ideas.
  python -m ai.validation_agents.run_discover --sharpen --idea "algo para hospitales con IA"
  python -m ai.validation_agents.run_discover --sharpen --idea "app para estudiantes" --validate
"""
import argparse
import concurrent.futures
import json
import subprocess
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DISCOVER_OUTPUT = PROJECT_ROOT / "docs" / "discover_results.json"


# ─────────────────────────────────────────────────────────────────────────────
# Shared: Stage 0 runner + display
# ─────────────────────────────────────────────────────────────────────────────

def _stage0_rank_key(r: dict[str, Any]) -> tuple[int, int, int]:
    proceed_score = {"PROCEED": 2, "WARN": 1, "ABORT": 0}.get(r.get("proceed_recommendation", "WARN"), 1)
    type_score = {"PAINKILLER": 2, "VITAMIN": 1, "PIT": 0, "CROWDED_COPYCAT": 0}.get(r.get("problem_type", "VITAMIN"), 1)
    devil_score = {"STRONG": 2, "WEAK": 1, "FATAL": 0}.get(r.get("devil_verdict", "WEAK"), 1)
    return (proceed_score, type_score, devil_score)


def _run_stage0_on_ideas(
    ideas: list[dict[str, str]], client: Any, config: Any, context: str
) -> list[dict[str, Any]]:
    from .stages.stage0_classify import run_stage0_classify

    results: list[dict[str, Any]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(ideas), 8)) as ex:
        future_map = {
            ex.submit(run_stage0_classify, client, config, e["idea"], context): e
            for e in ideas
        }
        for future in concurrent.futures.as_completed(future_map):
            entry = future_map[future]
            try:
                clf = future.result()
            except Exception as exc:
                clf = {
                    "proceed_recommendation": "WARN",
                    "devil_verdict": "WEAK",
                    "problem_type": "VITAMIN",
                    "llm_error": str(exc),
                }
            results.append({"_name": entry["name"], "_idea": entry["idea"], **clf})

    return sorted(results, key=_stage0_rank_key, reverse=True)


def _print_stage0_table(results: list[dict[str, Any]], title: str) -> None:
    print(f"\n{'='*60}")
    print(title)
    print(f"{'='*60}")
    print(f"{'#':<4} {'Name':<32} {'Type':<16} {'Proceed':<9} {'Devil'}")
    print("-" * 70)
    for i, r in enumerate(results, 1):
        print(
            f"  {i:<3} {r.get('_name', '?')[:30]:<32}"
            f"{r.get('problem_type', '?'):<16}"
            f"{r.get('proceed_recommendation', '?'):<9}"
            f"{r.get('devil_verdict', '?')}"
        )
    print()
    for i, r in enumerate(results, 1):
        print(f"#{i} {r.get('_name', '?')}")
        print(f"   {r.get('_idea', '')[:100]}")
        print(f"   Blocker:  {r.get('payment_blocker', '')[:90]}")
        print(f"   Riskiest: {r.get('hardest_assumption', '')[:90]}")
        print()


def _load_client_and_context(args: argparse.Namespace):
    from .config import load_config
    from .llm_client import LLMClient
    from .run_pipeline import read_yc_context

    config = load_config(use_llm=not args.no_llm)
    client = LLMClient(config)
    context = read_yc_context()
    return client, config, context


# ─────────────────────────────────────────────────────────────────────────────
# Modo 1 — Discover
# ─────────────────────────────────────────────────────────────────────────────

def _generate_ideas_from_domain(
    client: Any, config: Any, domain: str, context: str, n: int
) -> list[dict[str, str]]:
    result = client.json_completion(
        model=config.iteration_model,
        temperature=0.7,
        system_prompt=(
            "You are a startup idea generator specializing in Latin America and Peru. "
            "Generate concrete, actionable startup ideas — specific customer, specific pain, specific solution. "
            "Return only valid JSON."
        ),
        user_prompt=f"""Generate exactly {n} startup ideas for this problem domain.

DOMAIN: {domain}

REQUIREMENTS PER IDEA:
- Specific customer segment (not generic 'companies' or 'users')
- Real recurring pain that already causes workarounds (spreadsheets, WhatsApp, manual labor)
- Peru/LATAM reality: 70%+ informal economy, low B2C WTP, WhatsApp-first distribution
- Include mix of B2B and B2C — B2B gets stronger monetization priors in LATAM
- Each idea ~3 sentences: who suffers, what pain, what the solution does, why now

YC CONTEXT:
{context[:2500]}

Return JSON:
{{
  "ideas": [
    {{"name": "<short memorable name>", "idea": "<3-sentence description>"}},
    ...exactly {n} items...
  ]
}}
""",
        fallback=lambda: {
            "ideas": [
                {"name": f"Idea {i} — {domain[:20]}", "idea": f"Startup idea #{i} for {domain}."}
                for i in range(1, n + 1)
            ]
        },
    )
    return result.get("ideas", [])[:n]


def run_discover(args: argparse.Namespace) -> int:
    client, config, context = _load_client_and_context(args)

    print(f"\nDISCOVER MODE — domain: {args.domain} | n={args.n}")
    print("Generating ideas from domain...")

    ideas = _generate_ideas_from_domain(client, config, args.domain, context, args.n)
    if not ideas:
        print("No ideas generated. Check LLM connectivity.")
        return 1

    print(f"  {len(ideas)} ideas generated. Running Stage 0 in parallel...")
    ranked = _run_stage0_on_ideas(ideas, client, config, context)
    _print_stage0_table(ranked, f"DISCOVER — {args.domain}")

    out = Path(args.output) if args.output else DISCOVER_OUTPUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps({"mode": "discover", "domain": args.domain, "results": ranked}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Saved → {out}")
    return 0


# ─────────────────────────────────────────────────────────────────────────────
# Modo 2 — Pain Finder
# ─────────────────────────────────────────────────────────────────────────────

def _web_search_pains(domain: str) -> str:
    """Try firecrawl CLI for real web search. Returns raw content or empty string."""
    queries = [
        f"{domain} problems complaints reddit forum",
        f"{domain} pain points challenges linkedin",
        f"{domain} dificultades quejas problemas",
    ]
    parts: list[str] = []
    for q in queries:
        try:
            result = subprocess.run(
                ["firecrawl", "search", q, "--limit", "3"],
                capture_output=True, text=True, timeout=20, encoding="utf-8",
            )
            if result.returncode == 0 and result.stdout.strip():
                parts.append(result.stdout[:2000])
        except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
            break
    return "\n\n".join(parts)


def _extract_pain_themes(
    client: Any, config: Any, domain: str, web_content: str, context: str
) -> list[dict[str, Any]]:
    simulation_note = (
        f"Based on real web search results below:\n{web_content[:4000]}"
        if web_content
        else (
            "Simulate what you would find searching Reddit, LinkedIn, and industry forums for this domain. "
            "Be specific — use quote-like pain signals, not generic 'challenges'."
        )
    )
    result = client.json_completion(
        model=config.research_model,
        temperature=0.3,
        system_prompt=(
            "You are a startup researcher identifying real pain points from community discussions. "
            "Focus on specific, recurring problems — not vague challenges. Return only valid JSON."
        ),
        user_prompt=f"""Identify the top 5 pain themes in this domain from real user complaints.

DOMAIN: {domain}
{simulation_note}

COUNTRY CONTEXT: Peru/LATAM — 70%+ informal economy, WhatsApp-first comms, low WTP for B2C SaaS.

For each pain theme identify:
- A specific recurring complaint (not a generic challenge)
- Who suffers (specific job title or segment)
- Their current workaround (Excel, WhatsApp, manual labor, doing nothing)
- Whether they would pay for a solution and how much

Return JSON:
{{
  "pain_themes": [
    {{
      "theme": "<short theme name>",
      "pain_signal": "<specific complaint — quote-like>",
      "evidence_type": "<Reddit thread / LinkedIn post / job posting / field observation>",
      "who_suffers": "<specific role or segment>",
      "workaround": "<what they use instead>",
      "payment_signal": "<WTP estimate and rationale>"
    }},
    ...exactly 5 themes...
  ]
}}
""",
        fallback=lambda: {
            "pain_themes": [
                {
                    "theme": f"Pain {i} — {domain[:20]}",
                    "pain_signal": "LLM unavailable — run without --no-llm.",
                    "evidence_type": "unknown",
                    "who_suffers": "unknown",
                    "workaround": "unknown",
                    "payment_signal": "unknown",
                }
                for i in range(1, 6)
            ]
        },
    )
    return result.get("pain_themes", [])


def _ideas_from_pain_themes(
    client: Any, config: Any, domain: str, themes: list[dict], context: str
) -> list[dict[str, str]]:
    themes_text = json.dumps(themes, indent=2, ensure_ascii=False)
    result = client.json_completion(
        model=config.iteration_model,
        temperature=0.6,
        system_prompt=(
            "You are a startup idea generator. Each pain theme maps to exactly one startup idea. "
            "Ideas must be specific and grounded in the pain signal. Return only valid JSON."
        ),
        user_prompt=f"""Generate one startup idea per pain theme. Each idea addresses the specific pain.

DOMAIN: {domain}
PAIN THEMES:
{themes_text}

YC CONTEXT:
{context[:2000]}

Return JSON:
{{
  "ideas": [
    {{
      "name": "<startup name>",
      "pain_theme": "<theme name this addresses>",
      "idea": "<3-sentence description: specific customer, specific pain, specific solution, why now>"
    }},
    ...one per theme...
  ]
}}
""",
        fallback=lambda: {
            "ideas": [
                {
                    "name": t.get("theme", f"Idea {i}"),
                    "pain_theme": t.get("theme", ""),
                    "idea": t.get("pain_signal", "No description."),
                }
                for i, t in enumerate(themes, 1)
            ]
        },
    )
    return result.get("ideas", [])


def run_pain_finder(args: argparse.Namespace) -> int:
    client, config, context = _load_client_and_context(args)

    print(f"\nPAIN FINDER MODE — domain: {args.domain} | web={args.web}")
    print("=" * 60)

    web_content = ""
    if args.web:
        print("  Searching web for pain signals (firecrawl)...")
        web_content = _web_search_pains(args.domain)
        if web_content:
            print(f"  Got {len(web_content)} chars from web.")
        else:
            print("  firecrawl not found — falling back to LLM simulation.")
    else:
        print("  LLM simulating pain research (add --web for real search).")

    print("  Extracting pain themes...")
    themes = _extract_pain_themes(client, config, args.domain, web_content, context)
    if not themes:
        print("No pain themes extracted.")
        return 1

    print(f"\n--- Pain Themes ({args.domain}) ---")
    for i, t in enumerate(themes, 1):
        print(f"  {i}. [{t.get('theme', '?')}]  {t.get('pain_signal', '')[:80]}")
        print(f"     Who: {t.get('who_suffers', '?')}  |  Workaround: {t.get('workaround', '?')}")

    print(f"\n  Generating {len(themes)} ideas from themes...")
    raw_ideas = _ideas_from_pain_themes(client, config, args.domain, themes, context)
    ideas = [{"name": e.get("name", "?"), "idea": e.get("idea", "?")} for e in raw_ideas]

    if not ideas:
        print("No ideas generated.")
        return 1

    print(f"  Running Stage 0 on {len(ideas)} ideas in parallel...")
    ranked = _run_stage0_on_ideas(ideas, client, config, context)

    theme_map = {e.get("name", ""): e.get("pain_theme", "") for e in raw_ideas}
    for r in ranked:
        r["_pain_theme"] = theme_map.get(r.get("_name", ""), "")

    _print_stage0_table(ranked, f"PAIN FINDER — {args.domain}")

    out = Path(args.output) if args.output else DISCOVER_OUTPUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps({
            "mode": "pain_finder", "domain": args.domain,
            "pain_themes": themes, "results": ranked,
        }, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Saved → {out}")
    return 0


# ─────────────────────────────────────────────────────────────────────────────
# Modo 3 — Sharpen
# ─────────────────────────────────────────────────────────────────────────────

def _generate_hypotheses(
    client: Any, config: Any, vague_idea: str, context: str
) -> list[dict[str, Any]]:
    result = client.json_completion(
        model=config.reasoner_model,
        temperature=0.4,
        system_prompt=(
            "You are a startup advisor who turns vague concepts into specific testable ideas. "
            "Your job is to CLARIFY and SHARPEN — not validate. Return only valid JSON."
        ),
        user_prompt=f"""Turn this vague idea into 3 specific, testable startup hypotheses.

VAGUE IDEA: {vague_idea}

COUNTRY CONTEXT: Peru/LATAM — 70%+ informal economy, low B2C WTP, B2B stronger monetization.

For each hypothesis:
1. Name ONE specific customer segment (job title, industry, size, geography)
2. Name ONE specific pain (what, how often, what it costs them)
3. Name the narrowest possible MVP (one workflow, one output)
4. Name the riskiest assumption (what must be true for this to work)

Make 3 hypotheses with DIFFERENT customer/problem combinations — not the same framing.

YC CONTEXT:
{context[:2000]}

Return JSON:
{{
  "vague_idea": "{vague_idea}",
  "hypotheses": [
    {{
      "id": "H1",
      "name": "<startup name>",
      "customer": "<specific segment>",
      "pain": "<specific recurring problem: who, what, how often, cost>",
      "mvp": "<one workflow, one output — narrowest possible>",
      "riskiest_assumption": "<what must be true for this to work>",
      "idea": "<3-sentence description ready for Stage 0 validation>"
    }},
    {{"id": "H2", ...}},
    {{"id": "H3", ...}}
  ]
}}
""",
        fallback=lambda: {
            "vague_idea": vague_idea,
            "hypotheses": [
                {
                    "id": f"H{i}",
                    "name": f"Hypothesis {i}",
                    "customer": "Unknown — run with LLM enabled.",
                    "pain": "Unknown.",
                    "mvp": "Unknown.",
                    "riskiest_assumption": "Unknown.",
                    "idea": f"Hypothesis {i} for: {vague_idea}",
                }
                for i in range(1, 4)
            ],
        },
    )
    return result.get("hypotheses", [])


def run_sharpen(args: argparse.Namespace) -> int:
    client, config, context = _load_client_and_context(args)

    print(f"\nSHARPEN MODE — vague idea: {args.idea[:70]}")
    print("=" * 60)
    print("  Generating 3 problem hypotheses...")

    hypotheses = _generate_hypotheses(client, config, args.idea, context)
    if not hypotheses:
        print("No hypotheses generated.")
        return 1

    print(f"\n--- 3 Sharpened Hypotheses for: {args.idea[:50]} ---")
    for h in hypotheses:
        print(f"\n  {h.get('id', '?')} — {h.get('name', '?')}")
        print(f"     Customer:  {h.get('customer', '')}")
        print(f"     Pain:      {h.get('pain', '')[:90]}")
        print(f"     MVP:       {h.get('mvp', '')[:90]}")
        print(f"     Riskiest:  {h.get('riskiest_assumption', '')[:90]}")

    if args.validate:
        print("\n  Running Stage 0 on all 3 hypotheses...")
        ideas = [
            {"name": f"{h.get('id', '?')} {h.get('name', '?')}", "idea": h.get("idea", "")}
            for h in hypotheses
        ]
        ranked = _run_stage0_on_ideas(ideas, client, config, context)
        _print_stage0_table(ranked, f"SHARPEN STAGE 0 — {args.idea[:40]}")
    else:
        ranked = []
        print("\n  (Add --validate to run Stage 0 on all 3 hypotheses)")

    out = Path(args.output) if args.output else DISCOVER_OUTPUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps({
            "mode": "sharpen", "vague_idea": args.idea,
            "hypotheses": hypotheses,
            **({"stage0_results": ranked} if ranked else {}),
        }, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Saved → {out}")
    return 0


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Discover, Pain-Finder, and Sharpen modes for startup idea generation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--discover", action="store_true",
        help="Mode 1: domain -> N generated ideas -> Stage 0 ranking",
    )
    mode.add_argument(
        "--pain-finder", action="store_true",
        help="Mode 2: domain -> pain themes (web or LLM) -> ideas -> Stage 0",
    )
    mode.add_argument(
        "--sharpen", action="store_true",
        help="Mode 3: vague idea -> 3 problem hypotheses -> sharpened ideas",
    )
    parser.add_argument("--domain", help="Problem domain for --discover / --pain-finder")
    parser.add_argument("--idea", help="Vague idea for --sharpen")
    parser.add_argument("--n", type=int, default=5, help="Ideas to generate in --discover (default 5)")
    parser.add_argument(
        "--web", action="store_true",
        help="Use Firecrawl CLI for real web search in --pain-finder (falls back to LLM if unavailable)",
    )
    parser.add_argument(
        "--validate", action="store_true",
        help="Run Stage 0 on all sharpened hypotheses in --sharpen",
    )
    parser.add_argument("--output", help="Output JSON path (default: docs/discover_results.json)")
    parser.add_argument("--no-llm", action="store_true", help="Use deterministic fallbacks (no API calls)")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.discover:
        if not args.domain:
            print("Error: --domain required for --discover")
            return 1
        return run_discover(args)
    if args.pain_finder:
        if not args.domain:
            print("Error: --domain required for --pain-finder")
            return 1
        return run_pain_finder(args)
    if args.sharpen:
        if not args.idea:
            print("Error: --idea required for --sharpen")
            return 1
        return run_sharpen(args)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
