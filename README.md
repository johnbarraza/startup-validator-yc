# hw7_ds — Pipeline de Validación de Ideas de Startup (estilo YC)

Workflow de agentes de IA para evaluar, puntuar y seleccionar ideas de startup usando la metodología de Y Combinator. Desarrollado como proyecto final de Data Science con Python — Universidad del Pacífico, 2026.

> **Proyecto derivado destacado:** [SaludApp Peru](https://github.com/JohnxBar/saludapp-peru) — la idea ganadora del torneo (score 80/100), hoy un producto real con bot de WhatsApp, OCR de recetas médicas y deploy Docker.

---

## ¿Qué hace este repo?

Dado una idea de startup en texto libre, el pipeline:

1. **Investiga** alternativas existentes en el mercado
2. **Identifica gaps** reales sin cubrir
3. **Valida** contra criterios YC (problema, mercado, moat, timing)
4. **Simula** reacciones de stakeholders reales (MiroFish — 10 personas paralelas)
5. **Genera** un dossier YC con score /100 y decisión Go/No-Go
6. **Produce** un reporte Markdown final

---

## 🧭 Framework de Validación YC

El workflow usa:

- Reglas YC y preguntas de Jared Friedman → `docs/ycombinator/rules_summary.md`
- YC RFS Spring/Summer 2026 → `docs/ycombinator/`
- Análisis de 400 startups YC 2025 → `docs/ycombinator/Analyzing Latest 400...`
- Ideas consolidadas listas para probar → `docs/ideas_consolidadas_para_validacion.md`
- Ideas en borrador → `docs/ideas_borradores/`

### Flujo de Agentes

```
Stage 0:  Clasificación de idea
Stage 1:  Research de alternativas actuales
Stage 2:  Análisis de gaps de mercado
          └── Checkpoint 1: elección humana del gap
Stage 3:  Validación YC (criterios fundacionales)
Stage 3B: Simulación MiroFish (10 personas paralelas)
Stage 3C: Dossier YC + score /100
          └── Checkpoint 2: aprobación humana
Stage 4:  Reporte Markdown final
```

---

## ⚡ Uso Rápido

```powershell
cd E:\github\hw7_ds

# Correr con DeepSeek (recomendado)
python -m ai.validation_agents.run_pipeline --auto --force --idea "Tu idea aquí"

# Sin API key (fallbacks deterministas)
python -m ai.validation_agents.run_pipeline --no-llm --auto --force --idea "Tu idea aquí"

# Con análisis de mercado regional
python -m ai.validation_agents.run_pipeline --auto --force --regions "Peru,LATAM,USA" --idea "Tu idea aquí"
```

### Human-in-the-Loop

```powershell
# Sin --auto: se detiene para que el founder elija gap y apruebe estrategia
python -m ai.validation_agents.run_pipeline --idea "Tu idea aquí"
python -m ai.validation_agents.run_pipeline --idea "Tu idea aquí" --gap-id G1
python -m ai.validation_agents.run_pipeline --idea "Tu idea aquí" --gap-id G1 --approve
```

### Torneo de Ideas (bracket eliminatorio)

```powershell
python -m ai.validation_agents.run_batch \
  --ideas-file docs/ideas_consolidadas_para_validacion.md --tournament --verbose
```

Ver resultados: `docs/tournament.md` y `docs/leaderboard.md`

---

## 📦 Outputs por Idea

```
ai/validation_agents/outputs/<idea-key>/
├── state.json
├── report.md
├── stage0_classify.json
├── stage1_research.json
├── stage2_gaps.json
├── stage3_yc_validation.json
├── stage3b_simulation.json
├── stage3c_dossier.json
└── stage4_report.json
```

---

## 🏆 Torneo 2026 — Top Ideas

| Idea | Score | Decisión |
|---|---|---|
| **SaludApp Peru** ← [repo](https://github.com/JohnxBar/saludapp-peru) | 80/100 | ✅ Conditional Go |
| VocacionData AI | 72/100 | ✅ Conditional Go |
| ClimaAgro | 56/100 | ✅ Conditional Go |
| OCR-Receta Peru | 54/100 | ✅ Conditional Go |
| ContaBot | 54/100 | ⚠️ GO caution |

---

## 🚀 Proyecto Derivado: SaludApp Peru

**[github.com/JohnxBar/saludapp-peru](https://github.com/JohnxBar/saludapp-peru)**

La idea ganadora del torneo fue desarrollada como producto real en `E:\github\saludapp-peru`. Stack:
- Bot WhatsApp con Baileys (Node.js) — whitelist, freemium, onboarding
- OCR recetas médicas con Gemini Vision
- Clasificador híbrido determinista + DeepSeek para intents
- Audio → transcripción Gemini → intent
- FastAPI backend + Streamlit frontend
- Deploy Docker multi-servicio

---

## 📁 Estructura

```
ai/
  validation_agents/     ← pipeline principal
    stages/              ← stage0 al stage4
    outputs/             ← resultados por idea
backend/                 ← FastAPI (demo MineAssist legacy)
frontend/                ← Streamlit (demo MineAssist legacy)
data/                    ← datasets CWRU, farmacias
docs/
  ideas_consolidadas_para_validacion.md
  ideas_borradores/      ← pitches en borrador (MineAssist, etc.)
  ycombinator/           ← reglas YC, RFS, análisis
  tournament.md
  leaderboard.md
```

---

## 🙏 Agradecimientos

- **[WhiskeySockets/Baileys](https://github.com/WhiskeySockets/Baileys)** — gateway WhatsApp Web para el bot de SaludApp
- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** — framework de agentes que inspiró la arquitectura
- **[Claude Code / Anthropic](https://github.com/anthropics/claude-code)** — copiloto de ingeniería, skills GSD y debugging
- **Y Combinator** — metodología de validación, videos y RFS que guiaron el pipeline
- **DeepSeek / Google Gemini** — LLMs para razonamiento, OCR y clasificación de intents

---

## 🤖 Asistencia de IA

Pipeline de agentes, backend FastAPI, frontend Streamlit y bot WhatsApp desarrollados con **Claude Code (Anthropic)** como copiloto de ingeniería. Dirección estratégica, selección de ideas y decisiones de producto son del founder.
