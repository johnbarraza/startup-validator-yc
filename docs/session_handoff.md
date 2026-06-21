# Session Handoff — 2026-06-21

## Branch: main | DeepSeek: $2.97 crédito | Gemini set | Anthropic NOT set

---

## Pipeline updates

- `ai/validation_agents/run_pipeline.py` — fix encoding: `→` → `->` (Windows CP1252 crash)
- Correr con `PYTHONIOENCODING=utf-8` en PowerShell

## Torneo completo (16 ideas)

```bash
cd E:\github\hw7_ds
PYTHONIOENCODING=utf-8 python -m ai.validation_agents.run_batch \
  --ideas-file docs/ideas_consolidadas_para_validacion.md --tournament --verbose
```

16 ideas en `docs/ideas_consolidadas_para_validacion.md`. Top scores:

| Idea | Score | Sim | Decision |
|---|---|---|---|
| SaludApp Peru | 80/100 | 0.30 | 8.0/10 Conditional Go |
| VocacionData AI | 72/100 | 0.42 | Conditional Go |
| ClimaAgro | 56/100 | 0.37 | Conditional Go |
| OCR-Receta Peru | 54/100 | 0.34 | Conditional Go |
| ContaBot | 54/100 | 0.37 | GO caution |
| EPS Admin AI | 54/80 | 0.41 | Conditional Go |
| PescaIA | 30/50 | 0.47 | Conditional Go |

Ninguna supera sim gate 0.60.

---

## 💊 SaludApp Peru — PROYECTO SEPARADO

```
E:\github\saludapp-peru\   ← limpio, sin pipeline

frontend/app.py              ← Streamlit 5 tabs
backend/app/main.py          ← FastAPI (10 endpoints)
backend/app/health_models.py ← FINDRISC + roadmap BEHRT→CLMBR→MOTOR→Delphi
ai/health_agents.py          ← OCR: PaddleOCR→Gemini→DeepSeek→mock
data/farmacias_lima.json     ← 15 farmacias Lima
data/medicamentos.json       ← 20 medicamentos DIGEMID
docs/PLANNING.md             ← Arquitectura completa
Dockerfile + docker-compose  ← Listo para VPS
```

### Para correr

```bash
cd E:\github\saludapp-peru
pip install -r frontend/requirements.txt
streamlit run frontend/app.py
```

### Deploy VPS

```bash
cp .env.example .env && nano .env
docker compose up -d --build
# → http://localhost:8501
```

### Keys disponibles

- GEMINI_API_KEY: ✅ SET (Gemini Vision OCR)
- DEEPSEEK_API_KEY: ✅ SET (razonamiento texto)
- ANTHROPIC_API_KEY: ❌ NOT SET

---

## Presentación UP — Martes 23 Jun 2026 09:05 AM

Pendiente:
- Pitch deck
- Video demo
- Probar OCR con boleta real (con Gemini, ya que key está set)
- Deploy Streamlit Cloud (URL pública gratis)

---

## YC RFS analizados

- `docs/ycombinator/spring_2026_requests for Startups Y Combinator.md`
- `docs/ycombinator/summer_2026_Requests for Startups Y Combinator(4).md`

Mejores fits YC: SaludApp (personalized care), EPS Admin AI (healthcare admin service)
