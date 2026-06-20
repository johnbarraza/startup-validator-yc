from datetime import datetime, timezone
from pathlib import Path
from typing import Any


# ── Rendering helpers ────────────────────────────────────────────────────────

def _table(rows: Any) -> str:
    lines = ["| Criterion | Score | Note |", "|---|---:|---|"]
    if isinstance(rows, dict):
        for key, val in rows.items():
            criterion = str(key).replace("_", " ").title().replace("|", "/")
            score = val if not isinstance(val, dict) else val.get("score", "")
            note = val.get("note", "") if isinstance(val, dict) else ""
            lines.append(f"| {criterion} | {score} | {note} |")
    elif isinstance(rows, list):
        for row in rows:
            if isinstance(row, dict):
                criterion = str(
                    row.get("criterion", row.get("name", row.get("dimension", "")))
                ).replace("|", "/")
                score = row.get("score", row.get("points", ""))
                note = str(row.get("note", "")).replace("|", "/")
            else:
                criterion = str(row).replace("|", "/")
                score = note = ""
            lines.append(f"| {criterion} | {score} | {note} |")
    return "\n".join(lines)


def _score_table(rows: Any) -> str:
    lines = ["| Dimension | Points | Max | Note |", "|---|---:|---:|---|"]
    if isinstance(rows, dict):
        for key, val in rows.items():
            if key in ("total_score", "total_subscore_weighted"):
                continue
            dimension = str(key).replace("_", " ").title().replace("|", "/")
            points = val if not isinstance(val, dict) else val.get("points", val)
            max_points = val.get("max_points", "-") if isinstance(val, dict) else "-"
            note = val.get("note", "") if isinstance(val, dict) else ""
            lines.append(f"| {dimension} | {points} | {max_points} | {note} |")
    elif isinstance(rows, list):
        for row in rows:
            if isinstance(row, dict):
                dimension = str(row.get("dimension", "")).replace("|", "/")
                points = row.get("points", "")
                max_points = row.get("max_points", "")
                note = str(row.get("note", "")).replace("|", "/")
            else:
                dimension = str(row).replace("|", "/")
                points = max_points = note = ""
            lines.append(f"| {dimension} | {points} | {max_points} | {note} |")
    return "\n".join(lines)


def _dict_lines(data: Any) -> str:
    if isinstance(data, str):
        return data
    if isinstance(data, list):
        return _list_lines(data)
    if not isinstance(data, dict):
        return str(data) if data is not None else ""
    lines = []
    for key, value in data.items():
        label = str(key).replace("_", " ").title()
        rendered = "; ".join(str(i) for i in value) if isinstance(value, list) else str(value)
        lines.append(f"- {label}: {rendered}")
    return "\n".join(lines)


def _list_lines(items: Any) -> str:
    if isinstance(items, str):
        return f"- {items}"
    if isinstance(items, dict):
        return _dict_lines(items)
    if not isinstance(items, list):
        return f"- {items}" if items is not None else ""
    lines = []
    for item in items:
        if isinstance(item, dict):
            parts = [f"{str(k).replace('_',' ').title()}: {v}" for k, v in item.items()]
            lines.append(f"- {'; '.join(parts)}")
        else:
            lines.append(f"- {item}")
    return "\n".join(lines)


# ── Section builders ─────────────────────────────────────────────────────────

def _render_classification(classification: dict[str, Any]) -> str:
    problem_type = classification.get("problem_type", "UNKNOWN")
    proceed = classification.get("proceed_recommendation", "?")
    badge = {"PROCEED": "✓ PROCEED", "WARN": "⚠ WARN", "ABORT": "✗ ABORT"}.get(proceed, proceed)
    pit_sigs = classification.get("pit_signals_detected", [])
    pain_sigs = classification.get("painkiller_signals_detected", [])
    pit_lines = "\n".join(f"  - {s}" for s in pit_sigs) or "  (none)"
    pain_lines = "\n".join(f"  - {s}" for s in pain_sigs) or "  (none)"
    return f"""\
**Type:** {problem_type} | **Vertical:** {classification.get('vertical')} | **Customer:** {classification.get('customer_type')} | **Severity:** {classification.get('problem_severity')}

**Verdict:** {badge}

{classification.get('classification_rationale', '')}

**Red flags (pit signals):**
{pit_lines}

**Green flags (painkiller signals):**
{pain_lines}

**Suggested pivot:** {classification.get('suggested_pivot', 'N/A')}"""


def _render_iterations(iterations_result: dict[str, Any], winning_id: str) -> str:
    lines = [
        "| ID | Angle | One-Liner | Acuity | Market | Feasibility | Total |",
        "|---|---|---|---:|---:|---:|---:|",
    ]
    for it in iterations_result.get("iterations", []):
        sc = it.get("quick_score", {})
        winner_mark = " ★" if it.get("id") == winning_id else ""
        one_liner = str(it.get("one_liner", "")).replace("|", "/")[:70]
        lines.append(
            f"| {it.get('id')}{winner_mark} | {it.get('angle')} | {one_liner} "
            f"| {sc.get('problem_acuity','?')} | {sc.get('market_size','?')} "
            f"| {sc.get('founder_feasibility','?')} | {sc.get('total','?')} |"
        )
    detail_lines: list[str] = []
    for it in iterations_result.get("iterations", []):
        winner_mark = " ★ WINNER" if it.get("id") == winning_id else ""
        detail_lines.append(f"\n### {it.get('id')} — {it.get('angle')}{winner_mark}")
        detail_lines.append(f"**Target:** {it.get('target_customer', '')}")
        detail_lines.append(f"**Problem:** {it.get('core_problem', '')}")
        detail_lines.append(f"**Hook:** {it.get('solution_hook', '')}")
        detail_lines.append(f"**Why this angle:** {it.get('why_this_angle', '')}")
    return "\n".join(lines) + "\n" + "\n".join(detail_lines)


def _render_validations_comparison(validations: list[dict[str, Any]]) -> str:
    lines = ["| Iteration | Angle | Decision |", "|---|---|---|"]
    for v in validations:
        lines.append(
            f"| {v.get('_iteration_id','?')} | {v.get('_iteration_angle','?')} "
            f"| {v.get('go_no_go','?')} |"
        )
    return "\n".join(lines)


# ── Main report builder ──────────────────────────────────────────────────────

def build_markdown_report(
    *,
    idea: str,
    classification: dict[str, Any],
    research: dict[str, Any],
    gaps: dict[str, Any],
    iterations_result: dict[str, Any],
    winning_iteration: dict[str, Any],
    validations: list[dict[str, Any]],
    validation: dict[str, Any],
    simulation: dict[str, Any],
    dossier: dict[str, Any],
) -> str:
    winning_id = winning_iteration.get("id", "I1")
    selected_gap = validation.get("selected_gap", {})
    solutions = research.get("solutions", [])
    gap_rows = gaps.get("gaps", [])

    solution_lines = [
        f"- {item.get('id')}: {item.get('name')} ({item.get('category')}) — {item.get('observed_positioning')}"
        for item in solutions
    ]
    gap_lines = [
        f"- {item.get('id')}: {item.get('title')} | Pain: {item.get('pain')} | Evidence: {item.get('evidence_needed')}"
        for item in gap_rows
    ]
    experiment_lines = [f"- {item}" for item in validation.get("next_experiments", [])]
    kill_lines = [f"- {item}" for item in validation.get("kill_criteria", [])]

    persona_lines = [
        f"- {p.get('id')}: {p.get('role')} | Lens: {p.get('lens')} | Success: {p.get('success_metric')}"
        for p in simulation.get("personas", [])
    ]
    persona_result_lines: list[str] = []
    for r in simulation.get("persona_results", []):
        persona_result_lines.append(
            f"- **{r.get('persona_id')} {r.get('role')}** score={r.get('score','?')} | "
            f"{r.get('reaction', '')} | "
            f"Concern: {r.get('concern', '')} | "
            f"Need: {r.get('evidence_request', '')}"
        )
    round_lines: list[str] = []
    for round_item in simulation.get("rounds", []):
        round_lines.append(f"### Round {round_item.get('round')} — {round_item.get('focus')}")
        for stmt in round_item.get("statements", []):
            round_lines.append(
                f"- {stmt.get('persona_id')}: {stmt.get('claim')} "
                f"Concern: {stmt.get('concern')} Evidence: {stmt.get('evidence_request')}"
            )
    consensus = simulation.get("consensus", {})
    consensus_lines = [
        f"- Strongest signal: {consensus.get('strongest_signal')}",
        f"- Weakest assumption: {consensus.get('weakest_assumption')}",
        f"- Adoption path: {consensus.get('adoption_path')}",
        f"- Pricing test: {consensus.get('pricing_test')}",
        f"- Decision pressure: {consensus.get('decision_pressure')}",
    ]
    intervention_lines = [f"- {item}" for item in simulation.get("recommended_interventions", [])]

    raw_scorecard = dossier.get("scorecard", [])
    if isinstance(raw_scorecard, dict):
        scorecard_rows = [
            {"dimension": k.replace("_", " ").title(), "points": v, "max_points": "-", "note": ""}
            for k, v in raw_scorecard.items()
            if k not in ("total_score", "total_subscore_weighted")
        ]
    else:
        scorecard_rows = raw_scorecard

    market_regions = dossier.get("market", {}).get("regions", []) if isinstance(dossier.get("market"), dict) else []
    market_region_lines = []
    for region in market_regions:
        if isinstance(region, dict):
            market_region_lines.append(
                f"- **{region.get('region')}**: {region.get('validity')} "
                f"TAM: {region.get('tam')} | SAM: {region.get('sam')} "
                f"| SOM 12m: {region.get('som_12_months')} "
                f"| Sources: {', '.join(region.get('recommended_sources', []))}"
            )
    source_strategy_lines = [
        f"- {item}" for item in
        (dossier.get("market", {}).get("source_strategy", []) if isinstance(dossier.get("market"), dict) else [])
    ]
    score = dossier.get("total_score", "")
    max_score = dossier.get("max_score", "")

    return f"""# Startup Idea Validation Report

Generated: {datetime.now(timezone.utc).isoformat()}

## Original Idea
{idea}

---

## Stage 0 — Idea Classification (Pit Check)

{_render_classification(classification)}

---

## Stage 2B — Idea Iterations (3 angles)

Recommended: **{iterations_result.get('recommended_iteration_id', winning_id)}** — {iterations_result.get('recommended_one_liner', '')}

{_render_iterations(iterations_result, winning_id)}

---

## Stage 3 — YC Validation (parallel, all iterations)

{_render_validations_comparison(validations)}

**Winner: {winning_id} — {winning_iteration.get('angle')}**

> {winning_iteration.get('idea_refined', '')}

Decision: **{validation.get('go_no_go')}**

{validation.get('decision', '')}

### Friedman Questions
{_table(validation.get("friedman_scores", []))}

### YC Rules
{_table(validation.get("yc_rule_scores", []))}

---

## Overall Score (Stage 3C)
**{score}/{max_score} — {dossier.get("rating", "")}**

{_score_table(scorecard_rows)}

---

## YC Dossier

### One-Liner
{dossier.get("one_liner", "")}

### Problem
{_dict_lines(dossier.get("problem", {}))}

### Solution & Insight
{_dict_lines(dossier.get("solution_insight", {}))}

### Why Now
{_list_lines(dossier.get("why_now", []))}

### Market — {" / ".join(r.get("region","") for r in market_regions) if market_regions else "Peru / LATAM / USA"}
Recommended focus: {dossier.get("market", {}).get("recommended_focus", "") if isinstance(dossier.get("market"), dict) else ""}

{chr(10).join(market_region_lines)}

Source strategy:
{chr(10).join(source_strategy_lines)}

### Competition & Moat
{_dict_lines(dossier.get("competition_moat", {}))}

### Business Model & Pricing
{_dict_lines(dossier.get("business_model_pricing", {}))}

### Go-To-Market
{_dict_lines(dossier.get("go_to_market", {}))}

### Traction / Early Signals
{_list_lines(dossier.get("traction_signals", []))}

### Roadmap
{_dict_lines(dossier.get("roadmap", {}))}

### Risks & Mitigation
{_list_lines(dossier.get("risks_mitigations", []))}

### The Ask
{_dict_lines(dossier.get("the_ask", {}))}

### Product — Demo & Architecture
{_dict_lines(dossier.get("product_demo_architecture", {}))}

### External Research Hooks
{_list_lines(dossier.get("external_research_hooks", []))}

---

## Stage 1 — Current Alternatives
{research.get("research_summary", "")}

{chr(10).join(solution_lines)}

## Stage 2 — Market Gaps
Recommended gap: {gaps.get("recommended_gap_id")}

{chr(10).join(gap_lines)}

## Selected Gap
**{selected_gap.get("id") if isinstance(selected_gap, dict) else ""}: {selected_gap.get("title") if isinstance(selected_gap, dict) else ""}**

Pain: {selected_gap.get("pain") if isinstance(selected_gap, dict) else ""}

Why now: {selected_gap.get("why_now") if isinstance(selected_gap, dict) else ""}

Risk: {selected_gap.get("risk") if isinstance(selected_gap, dict) else ""}

---

## Stage 3B — Stakeholder Simulation
{simulation.get("inspiration", "")}

### Personas
{chr(10).join(persona_lines)}

### Persona Scores (parallel simulation)
Aggregate: {simulation.get("aggregate_score", "n/a")} / gate={simulation.get("gate_threshold", 0.60)} — {"PASS" if simulation.get("gate_passed") else "WARN"}

{chr(10).join(persona_result_lines)}

{chr(10).join(round_lines)}

### Simulation Consensus
{chr(10).join(consensus_lines)}

### Recommended Interventions
{chr(10).join(intervention_lines)}

---

## Next Experiments
{chr(10).join(experiment_lines)}

## Kill Criteria
{chr(10).join(kill_lines)}
"""


def write_report(output_dir: Path, report: str, filename: str = "validation_report.md") -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / filename
    path.write_text(report, encoding="utf-8")
    return path
