# MineAssist-PdM: Copiloto de Mantenimiento Predictivo para Activos Críticos Mineros

MineAssist-PdM es una plataforma AI-native de mantenimiento predictivo (PdM) diseñada para prevenir paradas no programadas en equipos de alta criticidad en la gran y mediana minería en el Perú y Latinoamérica, combinando modelos clásicos de Machine Learning sobre señales de vibración con copilotos inteligentes explicables.

---

## 🚀 Pitch Y Combinator Format

### 1. One-liner (1 frase)
**Hacemos** monitoreo y diagnóstico automatizado de fallas en maquinaria pesada **para** empresas mineras **mediante** el análisis de vibraciones mecánicas interpretado por asistentes inteligentes de IA explicable.

### 2. Founder (tú) & Founder-Market Fit
* **Founder:** John Barraza
* **¿Por qué yo?:** Estudiante de Data Science con Python en la Universidad del Pacífico, especializado en análisis de series de tiempo y optimización operativa. Como economista en formación, entiendo que el impacto de una parada mecánica no planificada en minería no es solo un reto de ingeniería, sino una pérdida económica masiva que afecta los flujos de caja y la balanza comercial de la región. Mi rol como solo founder es cubierto y apalancado mediante el uso de agentes de código avanzados (`Claude Code` como CTO de backend, `Codex` como diseñador de frontend, y `crewAI` para automatización de alertas).

### 3. El Problema
* **Quién lo sufre:** Gerentes de mantenimiento mecánico y superintendentes de confiabilidad en las más de 60 unidades mineras activas en el Perú (como Minera Las Bambas, Antamina, Cerro Verde).
* **Qué tan doloroso es:** Una chancadora primaria o un molino de bolas detenido de forma imprevista cuesta entre **$50,000 y $150,000 USD por hora** de inactividad de producción. Además, las fallas mecánicas de rodamientos no detectadas a tiempo pueden resultar en accidentes laborales graves o destrucción total de componentes de transmisión.
* **Cómo lo resuelven hoy:**
  1. *Reactivo:* Reparar cuando la máquina se rompe (pérdidas masivas).
  2. *Rutinas manuales en Excel:* Técnicos de vibraciones toman datos una vez al mes y redactan informes que tardan semanas en procesarse.
* **Evidencia:** Validación e ideas consolidadas en [ideas_consolidadas_para_validacion.md](file:///E:/github/hw7_ds/docs/ideas_consolidadas_para_validacion.md), más datos oficiales del sector cuando corresponda.

### 4. Solución & Insight
* **Qué construimos:** Un panel integrado que geolocaliza activos mediante GIS e ingiere telemetría de vibración (RMS, Curtosis, Crest Factor) y temperatura. Los datos son clasificados instantáneamente por un modelo de Machine Learning entrenado con el dataset de la **Case Western Reserve University (CWRU)** y procesados por un Agente Explicador de IA que traduce el diagnóstico crudo en un plan de acción de mantenimiento físico en español.
* **El Insight:** Las empresas mineras no necesitan más pantallas con gráficos difíciles de interpretar. El verdadero valor radica en la **explicabilidad conversacional**: dar al mecánico de planta una recomendación en lenguaje natural y clara sobre *qué hacer* ("Lubricar pista interna de inmediato, programar reemplazo en 48 horas") en lugar de un simple espectro de frecuencias.

### 5. Why now? (¿Por qué ahora?)
1. **Acceso a modelos de lenguaje económicos y rápidos:** Runtimes compactos como Gemini 1.5 Flash y GPT-4o-mini permiten inferencia conversacional en tiempo real a fracciones de centavo.
2. **Abaratamiento de sensores IoT:** Sensores de vibración inalámbricos industriales a bajo costo que reportan datos cada segundo.
3. **Avance en modelos fundacionales de series de tiempo:** Modelos como IBM Granite TSPulse abren paso a la detección no supervisada de anomalías de manera generalizable.

### 6. Tamaño del Mercado (TAM / SAM / SOM)
* **TAM (Total Addressable Market):** **$4.2B USD** (Mercado global de mantenimiento predictivo industrial).
* **SAM (Serviceable Available Market):** **$350M USD** (Gasto total en servicios de mantenimiento de activos críticos mineros en Latinoamérica).
* **SOM (Serviceable Obtainable Market):** **$12M USD** (Mercado objetivo en el Perú en los primeros 24 meses, equivalente a digitalizar 350 activos críticos en las 15 principales unidades mineras del país).
* **Fuentes:** Ministerio de Energía y Minas (MINEM), BCRP (Reportes de exportaciones e inversión de capital minero), informes de Statista 2025.

### 7. Competencia y Moat (Barrera de Entrada)
| Alternativa | Costo | Latencia / Tiempo | Moat (Nuestra Ventaja) |
| :--- | :--- | :--- | :--- |
| **Hacerlo en Excel** | Muy Bajo | Semanal / Mensual | Es puramente reactivo y propenso a errores humanos. |
| **Legacy SaaS (SAP PM)** | Muy Alto | Horas / Días | Estructura rígida, no analiza datos de sensores de vibración directamente y carece de explicabilidad IA. |
| **Servicios Externos de Confiabilidad**| Alto | Semanas | Informes estáticos en PDF que no son en tiempo real. |
| **MineAssist-PdM** | **Suscripción mensual media** | **Segundos** | **Moat:** Integración del modelo de ML de vibración con un copiloto de lenguaje natural para mecánicos en campo y digitalización de manuales técnicos mediante OCR. |

### 8. Modelo de Negocio y Pricing
* **Esquema:** B2B SaaS basado en volumen de activos monitoreados.
* **Planes de Suscripción:**
  * **Plan Piloto:** $1,500 USD/mes (Hasta 5 activos monitoreados, reportes estándar de IA).
  * **Plan Confiabilidad:** $5,000 USD/mes (Hasta 25 activos monitoreados, copiloto ilimitado, soporte 24/7).
  * **Plan Enterprise:** $15,000 USD/mes (Activos ilimitados, integración con SAP/Enterprise ERP, modelos personalizados fine-tuneados).
* **Costos Variables:** Inferencia de APIs de LLM (~$0.02 USD por explicación de falla generada). Margen de contribución estimado del **88%**.

### 9. Go-to-market (GTM)
* **Primeros 10 clientes:** Vender directamente a contratistas mecánicos autorizados que brindan servicios de tercerización de mantenimiento a Minera Las Bambas y Antamina.
* **Primeros 100 clientes:** Alianzas con distribuidores autorizados de rodamientos (ej. SKF Perú) para empaquetar nuestro software junto con la venta física de componentes de precisión.
* **Primeros 1,000 clientes:** Expansión corporativa a consorcios mineros multinacionales (Anglo American, BHP, Glencore) y eventos especializados del sector (Convención Minera Perumin, Innova TI).

---

## 🧭 Principios Fundacionales (Alineación Y Combinator)

El diseño estratégico de **MineAssist-PdM** se basa en las metodologías de validación del repositorio [yc-startups-analysis](file:///E:/github/hw7_ds/yc-startups-analysis/README.md) y en los mandamientos de YC para fundadores solistas:

1. **Evitar la trampa de la "Idea Perfecta":** No paramos la ejecución buscando el dataset perfecto de una mina real peruana. Validamos y prototipamos con el estándar de la industria ([CWRU Bearing Dataset](file:///E:/github/hw7_ds/data/cwru_bearing_small.csv)).
2. **Foco e Inferencia del Negocio (Go Deep):** Adoptamos métricas mecánicas reales (RMS, Curtosis, BPFI/BPFO) para que la IA actúe como un especialista de mantenimiento capaz de operar la faja o el molino.
3. **Selling Outcomes (Venta de Resultados):** No vendemos "gráficos de sensores" (SaaS clásico); vendemos la **prevención de la parada de planta** (Outcome) verticalizado al sector de minería peruana.
4. **Diseño "Safe" contra AI Wrappers:** El asistente IA es un feature de usabilidad conversacional, no el producto en sí. El producto reside en el dashboard, la geolocalización física y los modelos matemáticos propios entrenados localmente.

Para un análisis más profundo de estos principios y la mitigación de riesgos de muerte por plataformas de IA, consulta [rules_summary.md](file:///E:/github/hw7_ds/docs/ycombinator/rules_summary.md).

---

## 📐 Arquitectura del Sistema y Stack Tecnológico

El prototipo funcional está diseñado con una arquitectura desacoplada y orientada a eventos:

```
                  ┌───────────────────────────────┐
                  │      Streamlit Frontend       │
                  └───────────────┬───────────────┘
                                  │ (HTTP / JSON)
                                  ▼
                  ┌───────────────────────────────┐
                  │      FastAPI Backend API      │
                  └───────────────┬───────────────┘
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│  Random Forest  │      │   LLM Agent /   │      │   PaddleOCR /   │
│  Model (CWRU)   │      │   Gemini API    │      │   Document AI   │
└─────────────────┘      └─────────────────┘      └─────────────────┘
```

### Tecnologías Utilizadas:
1. **Frontend:** [Streamlit](file:///E:/github/hw7_ds/frontend/app.py) para una interfaz de usuario premium, interactiva y responsiva con gráficos dinámicos de [Plotly](file:///E:/github/hw7_ds/frontend/app.py#L228) y mapeo geoespacial en [Folium](file:///E:/github/hw7_ds/frontend/app.py#L182) de la planta concentradora Las Bambas.
2. **Backend:** [FastAPI](file:///E:/github/hw7_ds/backend/app/main.py) exponiendo endpoints para la predicción, reportes de IA y simulación de OCR/Whisper.
3. **Machine Learning:** [Scikit-learn](file:///E:/github/hw7_ds/backend/app/models.py) con un modelo `RandomForestClassifier` autoentrenable y serializado en disco.
4. **Agentes de IA:** [Agente Conversacional Gemini/OpenAI](file:///E:/github/hw7_ds/ai/agents.py) con fallback determinista basado en reglas para asegurar la robustez de la demo.

---

## 🛠️ Estructura del Directorio y Planificación

El repositorio está organizado para separar claramente la lógica del negocio, los datos, y los recursos del agente IA:

*   **.agents/**: Reglas de comportamiento del agente basadas en los principios de Y Combinator.
*   **.planning/**: Archivos de contexto continuo (ej. `context.md`) para reanudar el trabajo en las próximas sesiones sin perder el hilo.
*   **ai/**: Lógica de los agentes, flujos de validación (Fase 0) e integraciones con LLMs.
*   **backend/**: API REST construida con FastAPI (`main.py`, `models.py`).
*   **docs/**: Documentación, auditorías y metodologías de YC (`ycombinator/`).
*   **frontend/**: Interfaz de usuario construida con Streamlit (`app.py`).
*   **data/** & **notebooks/**: Datasets (ej. CWRU) y exploración de datos (EDA).

---

## 🛠️ Estructura del Código y Símbolos Documentados

### Backend Endpoint API: [main.py](file:///E:/github/hw7_ds/backend/app/main.py)
* **`read_root()`** (`GET /`): Health check y documentación interactiva de endpoints.
* **`get_assets()`** (`GET /assets`): Retorna los equipos mineros cargados del dataset [machine_telemetry.csv](file:///E:/github/hw7_ds/data/machine_telemetry.csv).
* **`predict(request: PredictRequest)`** (`POST /predict`): Ingiere métricas de sensores y llama a la inferencia del modelo.
* **`explain(request: ExplainRequest)`** (`POST /explain`): Genera la explicación de IA del fallo mecánico.
* **`parse_manual(...)`** (`POST /parse-manual`): Simulación de extracción estructurada de manuales mediante PaddleOCR/Document AI.
* **`voice_log(...)`** (`POST /voice-log`): Simulación de bitácora de incidencias acústicas mediante Whisper.

### Inferencia y Entrenamiento: [models.py](file:///E:/github/hw7_ds/backend/app/models.py)
* **`get_model_and_encoder()`**: Carga el clasificador y el decodificador de etiquetas. Si no existen en disco, entrena y serializa un nuevo clasificador Random Forest utilizando el dataset de vibración [cwru_bearing_small.csv](file:///E:/github/hw7_ds/data/cwru_bearing_small.csv).
* **`predict_bearing_fault(...)`**: Recibe features (`rms`, `kurtosis`, `crest_factor`, etc.) y calcula la predicción, criticidad y vector de probabilidades del rodamiento.

### Agentes Conversacionales: [agents.py](file:///E:/github/hw7_ds/ai/agents.py)
* **`explain_maintenance_fault(...)`**: Construye el prompt técnico contextualizado en la minería peruana y realiza la llamada a la API de OpenAI o Google Gemini. Posee un método `get_rule_based_explanation` de respaldo en caso no existan credenciales API de terceros en el entorno.

---

## 🤖 Declaración de Asistencia de IA

De acuerdo a las pautas de honestidad académica del curso:
* **Código Generado/Asistido:** Toda la arquitectura del backend en FastAPI, el frontend del dashboard en Streamlit con diseño CSS personalizado y el JSON del Jupyter Notebook de EDA fueron desarrollados con asistencia y copiloto del agente de inteligencia artificial **Antigravity**.
* **Código de Autoría Propia:** El diseño de la arquitectura conceptual del PdM minero, la selección de features estadísticas de vibración (CWRU) y la estructuración del pitch Y Combinator.

---

## 🧪 Framework de Validación de Ideas YC

Además del MVP de MineAssist-PdM, este repo incluye un pipeline general para evaluar ideas de startup estilo Y Combinator:

```text
ai/validation_agents/
```

El workflow usa:

* Reglas YC y preguntas de Jared Friedman en `docs/ycombinator/rules_summary.md`.
* Videos YC 2026 en `docs/ycombinator/video_*.md`.
* Análisis de 400 startups YC 2025 en `docs/ycombinator/Analyzing Latest 400 Business Ideas funded by YCombinator  by Harshit Tyagi  Medium.md`.
* Formato de pitch del proyecto final en `docs/Final_Project_Startup_principal.pdf`.
* Ideas consolidadas listas para probar en `docs/ideas_consolidadas_para_validacion.md`.

### Flujo de Agentes

```text
Stage 1: Research de alternativas actuales
Stage 2: Análisis de gaps de mercado
Checkpoint 1: elección humana del gap
Stage 3: Validación YC
Stage 3B: simulación de stakeholders estilo MiroFish
Stage 3C: dossier YC + score /100
Checkpoint 2: aprobación humana
Stage 4: reporte Markdown final
```

### Probar una Idea Rápido

Desde la raíz del repo:

```powershell
cd E:\github\hw7_ds
python -m ai.validation_agents.run_pipeline --no-llm --auto --force --idea "VocacionData AI: orientacion vocacional basada en datos laborales reales para postulantes y estudiantes peruanos, usando un agente conversacional que cruza intereses, salarios, empleabilidad, oferta universitaria y ubicacion para reducir malas decisiones de carrera."
```

Con comparación de mercado:

```powershell
python -m ai.validation_agents.run_pipeline --no-llm --auto --force --regions "Peru,LATAM,USA" --idea "StudyPet: companion gamificado de estudio para universitarios que convierte silabos y lecturas PDF en calendario, quizzes, flashcards y progreso visual tipo mascota o jardin para sostener habitos de estudio."
```

### Human-in-the-Loop

Sin `--auto`, el pipeline se detiene para que el founder elija el gap y apruebe la estrategia:

```powershell
python -m ai.validation_agents.run_pipeline --no-llm --idea "GovAuditor OSCE: herramienta para periodistas, veedores y auditores que detecta patrones sospechosos en contrataciones publicas peruanas usando scraping, OCR, comparacion semantica de propuestas y mapas de proveedores."
python -m ai.validation_agents.run_pipeline --no-llm --idea "GovAuditor OSCE: herramienta para periodistas, veedores y auditores que detecta patrones sospechosos en contrataciones publicas peruanas usando scraping, OCR, comparacion semantica de propuestas y mapas de proveedores." --gap-id G1
python -m ai.validation_agents.run_pipeline --no-llm --idea "GovAuditor OSCE: herramienta para periodistas, veedores y auditores que detecta patrones sospechosos en contrataciones publicas peruanas usando scraping, OCR, comparacion semantica de propuestas y mapas de proveedores." --gap-id G1 --approve
```

### Outputs

Cada idea genera una carpeta independiente:

```text
ai/validation_agents/outputs/<idea-key>/
├── state.json
├── report.md
├── stage1_research.json
├── stage2_gaps.json
├── stage3_yc_validation.json
├── stage3b_simulation.json
├── stage3c_dossier.json
└── stage4_report.json
```

### Usar DeepSeek

```powershell
$env:DEEPSEEK_API_KEY="tu_api_key"
python -m ai.validation_agents.run_pipeline --auto --force --idea "NotariaFlow AI: plataforma para notarias pequenas y medianas que automatiza la extraccion, validacion y preparacion de borradores de escrituras, partidas y contratos mediante OCR e IA revisable."
```

Si no tienes API key, usa `--no-llm`; el pipeline corre con fallbacks deterministas.

---

## 🚀 Instrucciones para Correr la Aplicación

1. **Instalar Dependencias:**
   ```bash
   pip install -r backend/requirements.txt
   pip install -r frontend/requirements.txt
   ```
2. **Ejecutar el Servidor Backend (FastAPI):**
   ```bash
   cd backend
   uvicorn app.main:app --reload --port 8000
   ```
3. **Ejecutar la Interfaz de Usuario (Streamlit):**
   ```bash
   cd frontend
   streamlit run app.py
   ```
   *Nota: Si prefieres no correr el backend, el frontend tiene un **modo embebido automático** que importará y ejecutará los modelos de manera local.*
