# Startup Idea Validation Pipeline

Multi-agent YC-style validation pipeline inspired by
[MiroFish](https://github.com/666ghj/MiroFish) (parallel persona simulation)
and [Top_papers_creator](https://github.com/jnichor/Top_papers_creator)
(iteration loop + gate pattern).

---

## Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│  INPUT: startup idea (free text)                                    │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │   STAGE 0           │  classifier_model (fast)
                    │   Pit Check         │  PAINKILLER / VITAMIN /
                    │   + Categorize      │  PIT / CROWDED_COPYCAT
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐  ABORT if PIT
                    │  proceed? ──────────┼──────────────────────────►
                    │  WARN continues     │  (use --force-pit to skip)
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   STAGE 1           │  chat_model
                    │   Research          │  current alternatives,
                    │   alternatives      │  competitor positioning
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   STAGE 2           │  chat_model
                    │   Market gaps       │  8 gaps ranked by priority
                    └──────────┬──────────┘
                               │
              ┌────────────────▼─────────────────┐
              │  CHECKPOINT 1 (human / --auto)   │
              │  Select gap to pursue            │
              └────────────────┬─────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │   STAGE 2B          │  iteration_model (creative)
                    │   3 idea framings   │  Parallel: I1/I2/I3
                    │   in parallel       │  ORIGINAL / B2B / WEDGE
                    └──────────┬──────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
    ┌────▼─────┐         ┌─────▼────┐         ┌─────▼────┐
    │ Stage 3  │         │ Stage 3  │         │ Stage 3  │
    │  YC Val  │         │  YC Val  │         │  YC Val  │
    │   I1     │         │   I2     │         │   I3     │
    └────┬─────┘         └─────┬────┘         └─────┬────┘
         └─────────────────────┼─────────────────────┘
                               │ pick winner (highest score)
                    ┌──────────▼──────────┐
                    │   STAGE 3B          │  chat_model × 6 (parallel)
                    │   MiroFish          │  6 personas scored
                    │   Stakeholder Sim   │  independently
                    │   on WINNER only    │  gate = 0.60
                    └──────────┬──────────┘
                               │
              ┌────────────────▼─────────────────┐
              │  SIMULATION GATE (0.60)          │
              │  WARN if aggregate score < 0.60  │
              │  (pipeline continues either way) │
              └────────────────┬─────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │   STAGE 3C          │  reasoner_model (deep)
                    │   Full YC Dossier   │  100-pt scorecard,
                    │   + Demo & Arch     │  Demo URL, architecture,
                    │   on WINNER only    │  AI models rationale
                    └──────────┬──────────┘
                               │
              ┌────────────────▼─────────────────┐
              │  CHECKPOINT 2 (human / --auto)   │
              │  Approve strategy                │
              └────────────────┬─────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │   STAGE 4           │
                    │   Markdown report   │  report.md
                    └─────────────────────┘
```

---

## Usage

```bash
# Full run, auto mode, verbose
python -m ai.validation_agents.run_pipeline \
  --idea "Your startup idea here" \
  --auto --verbose

# Force recompute all stages
  --force

# Skip pit detector (testing only)
  --force-pit

# Resume from existing state (skips completed stages)
  --state ai/validation_agents/outputs/<run-folder>/state.json

# No API calls (deterministic fallbacks)
  --no-llm

# Print all artifacts as JSON
  --json
```

---

## Providers & Models

| Purpose | Env var | Default |
|---|---|---|
| Primary API key | `DEEPSEEK_API_KEY` | — |
| Chat model (most stages) | `DEEPSEEK_CHAT_MODEL` | `deepseek-chat` |
| Reasoner model (Stage 3C) | `DEEPSEEK_REASONER_MODEL` | `deepseek-reasoner` |
| Classifier (Stage 0) | `CLASSIFIER_MODEL` | `deepseek-chat` |
| Iteration generator (2B) | `ITERATION_MODEL` | `deepseek-chat` |
| OpenRouter gateway | `OPENROUTER_API_KEY` | — |
| Qwen / DashScope | `DASHSCOPE_API_KEY` | — |

**Model prefix routing:**
```
openrouter/anthropic/claude-3-haiku   → Claude via OpenRouter
openrouter/qwen/qwen-plus             → Qwen via OpenRouter
qwen/qwen-plus                        → Qwen direct (DashScope)
deepseek-chat                         → DeepSeek (default)
```

---

## Stages Reference

| Stage | File | Model | Output |
|---|---|---|---|
| 0 | `stage0_classify.py` | classifier | problem_type, proceed_recommendation |
| 1 | `stage1_research.py` | chat | alternatives, research_summary |
| 2 | `stage2_gaps.py` | chat | 8 gaps ranked, recommended_gap_id |
| 2B | `stage2b_iterations.py` | iteration | 3 framings × quick_score |
| 3 | `stage3_validation.py` | chat × N parallel | go_no_go, friedman_scores, yc_rule_scores |
| 3B | `stage3b_simulation.py` | chat × 6 parallel | aggregate_score, gate_passed, persona_results |
| 3C | `stage3c_dossier.py` | reasoner | 100-pt scorecard, full dossier |
| 4 | `stage4_report.py` | — | report.md |

---

## Pit Idea Detector (Stage 0)

Classifies along two axes:

**Problem type**
- `PAINKILLER` — urgent, structural, users pay today → PROCEED
- `VITAMIN` — nice-to-have, low urgency → WARN
- `PIT` — non-problem or founder-only pain → ABORT
- `CROWDED_COPYCAT` — real problem, no wedge → WARN/ABORT

**Red flags that trigger ABORT (2+ = PIT)**
- Problem described abstractly ("people waste time"), not behaviorally
- No evidence of active workarounds or search behavior
- Only the founder is the customer
- Free tool already solves this (Notion template, ChatGPT prompt)
- Market too small for venture scale even at 100% penetration

---

## Iteration Angles (Stage 2B)

| ID | Angle | Focus |
|---|---|---|
| I1 | ORIGINAL | Refine founder's idea — sharper pain, narrower wedge |
| I2 | PIVOT_B2B | Same pain, institutional buyer with budget (university/employer/gov) |
| I3 | PIVOT_WEDGE | Narrowest slice, fastest evidence of willingness to pay in 30 days |

All 3 run Stage 3 YC validation in parallel. Highest score wins.

---

## Why not use VettIQ or similar?

VettIQ (LangGraph) does market research and competitor analysis but has no:
- Pit idea classifier with structural problem detection
- Parallel persona simulation with independent scoring + gate
- Idea iteration loop with multiple angles
- Integrated YC doctrine scoring
- Provider-agnostic multi-model routing

This pipeline is self-contained, runs locally, and costs ~$0.05–0.15 per full run with DeepSeek.
