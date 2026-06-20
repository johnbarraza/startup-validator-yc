"""Deterministic VC calculation functions.

Adapted from github.com/isanthoshgandhi/venture-capital-intelligence
(MIT License, isanthoshgandhi)

These functions POST-PROCESS LLM outputs to compute deterministic scores,
replacing or validating the LLM's own verdict guesses.

Modules:
  apply_vc_verdict(validation)   — weighted composite + PASS/CONDITIONAL/DECLINE
  apply_signal_scores(research)  — exponential signal scoring per competitor
  apply_market_calcs(dossier)    — dual-method TAM + VC threshold flags
"""
import math
from typing import Any

# ── Hard-screening rubric ─────────────────────────────────────────────────────

WEIGHTS = {
    "team":           0.25,
    "market":         0.20,
    "product":        0.15,
    "traction":       0.15,
    "business_model": 0.10,
    "competition":    0.08,
    "financials":     0.05,
    "risk_profile":   0.02,
}

SEQUOIA_DIMS = ["market", "team", "product"]
YC_DIMS      = ["team", "traction"]
TIGER_DIMS   = ["traction", "business_model", "financials"]


def _normalize_dim(name: str) -> str:
    aliases = {
        "business model": "business_model",
        "risk profile":   "risk_profile",
        "risk":           "risk_profile",
    }
    return aliases.get(name.lower().strip(), name.lower().replace(" ", "_"))


def compute_weighted_score(vc_rows: list[dict[str, Any]]) -> float:
    total = 0.0
    for row in vc_rows:
        dim = _normalize_dim(str(row.get("dimension", "")))
        w = WEIGHTS.get(dim, 0.0)
        s = float(row.get("score", 0) or 0)
        total += s * w
    return round(total, 2)


def determine_verdict(weighted: float, vc_rows: list[dict[str, Any]]) -> dict[str, Any]:
    dim_scores = {}
    for row in vc_rows:
        dim = _normalize_dim(str(row.get("dimension", "")))
        dim_scores[dim] = float(row.get("score", 0) or 0)

    disqualifying = [d for d, s in dim_scores.items() if s <= 2]
    weak = [d for d, s in dim_scores.items() if s <= 3]
    min_score = min(dim_scores.values()) if dim_scores else 0

    if disqualifying:
        verdict = "DECLINE"
        reason = f"Disqualifying score on: {', '.join(disqualifying)}"
    elif weighted >= 7.5 and min_score >= 4:
        verdict = "PASS"
        reason = "Strong across all dimensions"
    elif weighted >= 6.0 and min_score >= 3:
        verdict = "CONDITIONAL_PASS"
        reason = f"Needs improvement on: {', '.join(weak) or 'minor gaps'}"
    else:
        verdict = "DECLINE"
        reason = f"Weighted score {weighted} below threshold; weak: {', '.join(weak)}"

    def _lens(dims: list[str], threshold: float = 6.5) -> str:
        vals = [dim_scores.get(d, 0) for d in dims]
        avg = sum(vals) / len(vals) if vals else 0
        return "PASS" if avg >= threshold else ("WATCH" if avg >= 5.0 else "FAIL")

    risk_avg = (dim_scores.get("risk_profile", 5) + dim_scores.get("competition", 5)) / 2
    risk_label = "MANAGEABLE" if risk_avg >= 7 else ("ELEVATED" if risk_avg >= 5 else "CRITICAL")

    return {
        "composite_score": weighted,
        "verdict": verdict,
        "reason": reason,
        "weak_dims": weak,
        "disqualifying_dims": disqualifying,
        "investor_lenses": {
            "sequoia":      _lens(SEQUOIA_DIMS),
            "yc":           _lens(YC_DIMS),
            "tiger_global": _lens(TIGER_DIMS),
            "risk_mgmt":    risk_label,
        },
        "source": "deterministic_vc_calcs",
    }


def apply_vc_verdict(validation: dict[str, Any]) -> dict[str, Any]:
    """Recompute vc_verdict deterministically from vc_rubric_scores."""
    rows = validation.get("vc_rubric_scores", [])
    if not rows:
        return validation
    weighted = compute_weighted_score(rows)
    verdict = determine_verdict(weighted, rows)
    # Augment each row with deterministic weighted value
    for row in rows:
        dim = _normalize_dim(str(row.get("dimension", "")))
        w = WEIGHTS.get(dim, 0.0)
        s = float(row.get("score", 0) or 0)
        row["weighted"] = round(s * w, 2)
        row["weight"] = w
    validation["vc_rubric_scores"] = rows
    validation["vc_verdict"] = verdict
    return validation


# ── Signal scorer ─────────────────────────────────────────────────────────────

SIGNAL_TYPES = ["HIRING", "FUNDING", "PRODUCT", "TEAM", "MARKET", "TECH"]

SIGNAL_WEIGHTS = {
    "HIRING":  0.25,
    "FUNDING": 0.25,
    "PRODUCT": 0.20,
    "TEAM":    0.15,
    "MARKET":  0.10,
    "TECH":    0.05,
}

SENTIMENT_MULT = {"POSITIVE": 1.0, "NEUTRAL": 0.6, "NEGATIVE": 0.0}


def _score_signal_type(raw_scores: list[dict[str, Any]]) -> float:
    """Exponential curve → 0-100."""
    if not raw_scores:
        return 0.0
    total = sum(
        s.get("strength", 5) * SENTIMENT_MULT.get(s.get("sentiment", "NEUTRAL"), 0.6)
        for s in raw_scores
    )
    n = len(raw_scores)
    return min(100.0, round((1.0 - math.exp(-total / (n * 7))) * 100, 1))


def _investment_readiness(overall: float, signal_scores: dict[str, float]) -> str:
    funding = signal_scores.get("FUNDING", 0)
    if overall >= 70 or funding >= 60:
        return "MOVE_FAST"
    if overall >= 45:
        return "ENGAGE"
    return "MONITOR"


def _score_competitor_from_llm(entry: dict[str, Any]) -> dict[str, Any]:
    """Convert LLM per-signal scores (1-10) to 0-100 using SIGNAL_WEIGHTS."""
    raw_scores: dict[str, float] = {}
    for sig in SIGNAL_TYPES:
        key = f"{sig.lower()}_score"
        raw_scores[sig] = float(entry.get(key, 5) or 5) * 10  # scale 1-10 → 0-100

    overall = sum(raw_scores[t] * SIGNAL_WEIGHTS[t] for t in SIGNAL_TYPES)
    overall = round(overall, 1)
    readiness = _investment_readiness(overall, raw_scores)
    return {**entry, "overall_score": overall, "classification": readiness}


def apply_signal_scores(research: dict[str, Any]) -> dict[str, Any]:
    """Recompute overall_score and classification deterministically for each competitor."""
    signals = research.get("competitor_signals", [])
    if not signals:
        return research
    research["competitor_signals"] = [
        _score_competitor_from_llm(s) if isinstance(s, dict) else s
        for s in signals
    ]
    return research


# ── TAM calculator ────────────────────────────────────────────────────────────

VENTURE_TAM_THRESHOLD = 1_000_000_000   # $1B
GOOD_CAGR_THRESHOLD   = 0.15            # 15%


def _parse_usd(val: Any) -> float:
    """Parse '$50M', '$1.2B', or numeric strings to float."""
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).replace(",", "").replace("$", "").strip().upper()
    mult = 1.0
    if s.endswith("B"):
        mult, s = 1e9, s[:-1]
    elif s.endswith("M"):
        mult, s = 1e6, s[:-1]
    elif s.endswith("K"):
        mult, s = 1e3, s[:-1]
    try:
        return float(s) * mult
    except ValueError:
        return 0.0


def _calc_region(region: dict[str, Any]) -> dict[str, Any]:
    tam_td = _parse_usd(region.get("tam_topdown", region.get("tam", 0)))
    tam_bu = _parse_usd(region.get("tam_bottomup", 0))
    sam_raw = _parse_usd(region.get("sam", 0))
    som_raw = _parse_usd(region.get("som_12_months", 0))

    # Derive missing values
    if tam_td == 0 and tam_bu > 0:
        tam_td = tam_bu
    if tam_bu == 0 and tam_td > 0:
        tam_bu = tam_td
    if sam_raw == 0 and tam_td > 0:
        sam_raw = tam_td * 0.20
    if som_raw == 0 and sam_raw > 0:
        som_raw = sam_raw * 0.05

    tam_low  = min(tam_td, tam_bu) if tam_bu > 0 else tam_td
    tam_high = max(tam_td, tam_bu) if tam_bu > 0 else tam_td

    # VC threshold check
    if tam_high >= VENTURE_TAM_THRESHOLD:
        threshold = "ABOVE_$1B"
    elif tam_high >= 500_000_000:
        threshold = "BORDERLINE_$500M-$1B"
    else:
        threshold = "BELOW_$500M"

    return {
        **region,
        "tam_topdown_usd":    round(tam_td, 0),
        "tam_bottomup_usd":   round(tam_bu, 0),
        "tam_consensus_low":  round(tam_low, 0),
        "tam_consensus_high": round(tam_high, 0),
        "sam_usd":            round(sam_raw, 0),
        "som_usd":            round(som_raw, 0),
        "venture_threshold":  threshold,
        "source": "deterministic_tam_calc",
    }


def apply_market_calcs(dossier: dict[str, Any]) -> dict[str, Any]:
    """Recompute TAM/SAM/SOM deterministically for each region."""
    market = dossier.get("market")
    if not isinstance(market, dict):
        return dossier
    regions = market.get("regions", [])
    if not regions:
        return dossier
    market["regions"] = [
        _calc_region(r) if isinstance(r, dict) else r
        for r in regions
    ]
    dossier["market"] = market
    return dossier
