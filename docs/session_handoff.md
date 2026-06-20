# Session Handoff — 2026-06-20

## Estado del pipeline

El pipeline `ai/validation_agents/run_pipeline.py` corre end-to-end:

```
Stage 1 → research de alternativas
Stage 2 → gaps de mercado + checkpoint (auto con --auto)
Stage 3 → validación YC (go/no-go)
Stage 3B → simulación MiroFish paralela (6 agentes, gate 0.60)
Stage 3C → dossier YC enriquecido + scorecard 100pts + Demo & Arquitectura
Stage 4 → report.md final
```

## Qué se hizo hoy

### 1. Bug fix: `gap_id` int crash
- `run_pipeline.py:187` — `str(selected_gap_id)` al llamar `find_gap()`

### 2. MiroFish Opción B — parallel simulation
- `ai/validation_agents/stages/stage3b_simulation.py` reescrito completo
- `SIMULATION_GATE = 0.60` como constante
- `_simulate_persona()` — cada persona hace su propia llamada LLM
- `ThreadPoolExecutor` — 6 agentes corren en paralelo
- Output incluye `aggregate_score`, `gate_passed`, `persona_results` con scores individuales
- `run_pipeline.py` — gate check entre Stage 3B y 3C con log + warning visible

### 3. Nueva sección: "Product – Demo & Architecture"
- `stage3c_dossier.py` — `product_demo_architecture` agregado a PITCH_SECTIONS, prompt LLM y fallback
- `stage4_report.py` — sección renderizada en el report final
- Contiene: demo_url, main_flow_screenshots, architecture_diagram, repo_structure, ai_models_used

### 4. Robustez de report helpers
- `_table()` — maneja dict / list-of-dicts / list-of-strings
- `_score_table()` — maneja dict (clave=dimension, valor=score) o list-of-dicts
- `_dict_lines()` — maneja str / list / dict / None
- `_list_lines()` — maneja str / dict / list / None
- `external_research_hooks` — usa `_list_lines` (viene como lista del LLM)

## Para correr mañana

```powershell
# Run limpio con la idea de VocacionData
python -m ai.validation_agents.run_pipeline `
  --auto --force --verbose `
  --idea 'VocacionData AI: orientacion vocacional basada en datos laborales reales para postulantes y estudiantes peruanos, usando un agente conversacional que cruza intereses, salarios, empleabilidad, oferta universitaria y ubicacion para reducir malas decisiones de carrera.'
```

## Pendientes

- [ ] `Stage 3C score: None/None` — el LLM a veces anida `total_score`/`max_score` dentro del scorecard en vez de top-level. Normalizar en `build_markdown_report`.
- [ ] Gate WARN (0.28-0.38 < 0.60) para VocacionData — las personas dan scores bajos por falta de traction. Normal para idea sin MVP. Revisar si el threshold es apropiado o bajarlo a 0.45.
- [ ] Agregar `--regions Peru,LATAM,USA` al comando por defecto
- [ ] MiroFish submodule real (Opción A) — pendiente para cuando se quiera simulación con memorias persistentes (Zep Cloud)
- [ ] `friedman_scores` y `yc_rule_scores` — el LLM no siempre incluye el campo `criterion`. Considerar prompt más estricto en stage3_validation.py.

## Estructura de archivos clave

```
ai/
  validation_agents/
    run_pipeline.py       # orquestador principal
    config.py             # ValidationConfig, load_config
    llm_client.py         # LLMClient, json_completion
    state.py              # PipelineState
    stages/
      stage1_research.py
      stage2_gaps.py
      stage3_validation.py
      stage3b_simulation.py   ← MiroFish parallel agents
      stage3c_dossier.py      ← dossier + demo/arch section
      stage4_report.py        ← markdown report builder
```

## Inspiración arquitectural

- `stage3b_simulation.py` inspirado en MiroFish (https://github.com/666ghj/MiroFish)
- Patrón de gates y agentes paralelos de Top_papers_creator (https://github.com/jnichor/Top_papers_creator)
- LLM: DeepSeek (chat + reasoner) via OpenAI-compatible API
