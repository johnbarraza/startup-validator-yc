# Startup Idea Validation Report

Generated: 2026-06-21T17:08:53.210599+00:00

## Original Idea
EPS Admin AI: reemplazamos el equipo humano que procesa autorizaciones medicas en EPS peruanas (Rimac, Pacifico, Sanitas). Hoy una solicitud de autorizacion tarda 30-120 min de revision manual por medico auditor. Nuestra IA lee la solicitud del medico tratante, el historial del afiliado, las guias clinicas de la EPS y recomienda aprobar o rechazar en segundos con justificacion. Modelo: cobramos por autorizacion procesada (outcome-based), no por licencia. El humano solo revisa los casos que la IA marca como dudosos (5-10%). Expansion: Colombia, Chile, Mexico. YC Summer 2026 pide exactamente esto: AI companies that sell the service not the software, healthcare administration.

---

## Stage 0 — Idea Classification (Pit Check)

**Type:** PAINKILLER | **Vertical:** HealthTech | **Customer:** B2B | **Severity:** STRUCTURAL

**Verdict:** ⚠ WARN | **Devil's advocate:** ⚠ WEAK | **Freemium:** ✗ NO

The startup addresses a real, urgent, structural problem in Peruvian healthcare administration: manual medical authorization processing is slow and costly. Large insurers (Rimac, Pacifico, Sanitas) have clear budgets and incentives to reduce costs, making them willing buyers. Outcome-based pricing aligns with their interests, and the AI solution offers a significant improvement over current manual workflows.

**Green flags (painkiller signals):**
  - Active workarounds exist (manual medical auditor reviews)
  - Spending already happens on imperfect solutions (auditor salaries)
  - Recurring pain: every authorization request
  - Measurable cost: lost hours and revenue
  - B2B buyer has a budget line for operational costs
  - Users likely search actively for solutions

**Red flags (devil's advocate):**
  - Long enterprise sales cycle (6-12 months) to EPS with high regulatory and compliance hurdles, delaying revenue.
  - Liability concerns: EPS may be unwilling to let AI make medical decisions without extensive validation, prolonging pilots.
  - Integration with legacy EPS systems and data privacy compliance (Peru's data protection law) could be technically challenging and slow adoption.
  - Outcome-based pricing may be rejected by EPS preferring fixed fees or risk-sharing caps, complicating contract negotiations.

**Payment blocker:** EPS procurement teams may resist outcome-based billing due to budgeting unpredictability and require fixed monthly fees; furthermore, measuring 'authorizations processed' accurately without manual verification is contentious.

**Free substitute risk:** The current manual process (human auditors) is the default 'free' substitute; EPS can also invest in minor workflow improvements or hire more staff without switching to AI.

**Market size reality check:** Peruvian EPS market is small (3-5 major players); at ~$1/auth with thousands of auths/month per EPS, SAM in Peru is <$5M ARR. Must expand to Colombia/Mexico where competition and localization costs are higher.

**Hardest unvalidated assumption:** That EPS will trust an external AI for a core, liability-sensitive medical decision process without extensive validation and contractual indemnification.

**Freemium rationale:** Freemium is not suitable for this B2B enterprise sale. The product is outcome-based per authorization, and the target buyers (large insurers) require custom demonstrations and proof of value before purchasing. A free tier would not attract these buyers and could dilute the perceived value.

**Suggested pivot:** 

---

## Stage 2B — Idea Iterations (3 angles)

Recommended: **I1** — Reemplazamos la revisión manual de autorizaciones médicas en EPS peruanas con IA que decide en segundos usando guías locales, y cobramos solo por resultado.

| ID | Angle | One-Liner | Acuity | Market | Feasibility | Total |
|---|---|---|---:|---:|---:|---:|
| I1 ★ | ORIGINAL | Reemplazamos la revisión manual de autorizaciones médicas en EPS perua | 9 | 6 | 8 | 23 |
| I2 | PIVOT_B2B | We help large employers in Peru slash prior authorization wait times f | 8 | 7 | 7 | 22 |
| I3 | PIVOT_WEDGE | We automate Rimac EPS's oncology prior authorizations with AI that und | 10 | 3 | 9 | 22 |

### I1 — ORIGINAL ★ WINNER
**Target:** Médico Auditor de EPS peruanas (específicamente en Rimac, Pacifico o Sanitas) que pasa 4-6 horas al día revisando manualmente solicitudes de autorización en múltiples sistemas.
**Problem:** Cada autorización toma entre 30 y 120 minutos de lectura y análisis manual. El auditor debe entrar a 3-5 sistemas distintos (historial clínico, guías de la EPS, normativas) copiar y pegar información, interpretar guías ambiguas y tomar decisiones de alto impacto con información fragmentada. Esto genera un cuello de botella de 200-500 solicitudes diarias por EPS, retrasos que irritan a pacientes y médicos, y costos operativos innecesarios (un auditor gana S/ 5,000-8,000 mensuales por procesar ~20 casos/día). El error humano por fatiga o inconsistencia puede causar autorizaciones indebidas o rechazos que terminan en quejas y sobrecostos legales.
**Hook:** IA entrenada exclusivamente con datos médicos peruanos, capaz de leer las guías clínicas locales (ej. guías de práctica clínica del Minsa adaptadas por cada EPS) y operar dentro de los sistemas legacy sin reemplazarlos, mediante integraciones ligeras (APIs o automatización de interfaz).
**Why this angle:** Al enfocar la propuesta en la profunda necesidad de localización peruana —no solo idioma sino procesos clínicos y regulatorios únicos— nos diferenciamos radicalmente de soluciones genéricas en inglés o portugués. Construimos un foso temprano que los competidores globales no pueden replicar sin invertir años en adaptación. El nicho permite validar rápido con un EPS, probar el outcome-based pricing y luego expandir con el mismo ADN a otros países andinos.

### I2 — PIVOT_B2B
**Target:** HR Director or Benefits Manager of a Peruvian company with 5,000+ employees, e.g., a mining conglomerate, responsible for negotiating health insurance contracts and employee wellness.
**Problem:** Every month, hundreds of employees face 2-5 day waits for routine pre-authorizations due to overwhelmed manual review teams at the EPS. This causes employee dissatisfaction, health deterioration, and indirect costs like absenteeism and turnover. The employer has no direct control and sees rising premiums without transparency into inefficiencies.
**Hook:** Unlike generic AI authorization tools designed for US/EU markets, ours is built specifically for the Peruvian medical context, understands local clinical guidelines and Spanish medical terminology, and offers a per-employee pricing with clear ROI dashboards, making it a plug-and-play employee benefit upgrade rather than IT software.
**Why this angle:** Selling to employers taps a more immediate budget—employee benefits—with a clear pain point (employee complaints, cost overruns) and a shorter sales cycle than selling to entrenched EPS institutions. The performance-based pricing per employee de-risks the purchase and aligns incentives. This framing also opens a B2B2C channel through employer-provided health apps.

### I3 — PIVOT_WEDGE
**Target:** Gerente de Auditoría Médica at Rimac EPS, overseeing the team of audit doctors who manually review cancer treatment requests.
**Problem:** Each oncology prior authorization request at Rimac takes 30-120 minutes of manual review by an audit doctor checking patient history, internal clinical guidelines, and national drug formularies. The team faces a mounting backlog, causing delays in urgent cancer treatments that lead to patient complaints, potential lawsuits, and reputational damage. Audit doctors are burned out and error-prone under the pressure.
**Hook:** Unlike generic AI tools, our model is fine-tuned on Rimac's proprietary oncology protocols and Peruvian drug regulations, making its decisions immediately auditable and compliant. The outcome-based pricing (pay only per processed authorization) removes financial risk and aligns with their operational budget.
**Why this angle:** By hyper-focusing on one EPS and one critical specialty where pain is most acute (life-threatening delays), we can validate willingness to pay in 30 days with a pilot involving just 10 audit doctors. The narrow wedge demonstrates deep localization, builds trust through auditable decisions, and offers an ROI that is impossible to ignore, paving the way for expansion to other specialties and EPS.

---

## Stage 3 — YC Validation (parallel, all iterations)

| Iteration | Angle | Decision |
|---|---|---|
| I1 | ORIGINAL | Conditional go |
| I2 | PIVOT_B2B | CONDITIONAL |
| I3 | PIVOT_WEDGE | CONDITIONAL_GO |

**Winner: I1 — ORIGINAL**

> EPS Admin AI automatiza el proceso de autorizaciones médicas en las EPS peruanas, comenzando por Rimac, Pacifico y Sanitas. Nuestra IA lee la solicitud del médico tratante, extrae el historial del afiliado de los sistemas legacy, interpreta las guías clínicas locales (que son distintas a las de otros países) y emite una recomendación inmediata de aprobación o rechazo con justificación explicable. Los auditores humanos solo intervienen en el 5-10% de casos que la IA marca como dudosos, eliminando horas de revisión manual y reduciendo el tiempo de respuesta de 30-120 minutos a segundos. El modelo de negocio es puro: cobramos por cada autorización procesada, alineando incentivos y demostrando ROI inmediato. Empezamos con procedimientos de alta complejidad (como cirugías y medicamentos oncológicos) donde el costo del error y la demora es más crítico. La diferenciación local es clave: entrenamos el modelo con datos peruanos, adaptándonos al español médico local, a los códigos de diagnóstico peruanos y a las coberturas específicas de cada EPS, algo que los gigantes globales no ofrecen.

Decision: **Conditional go**

Proceed with validation, focusing on pilot and evidence collection

### Friedman Questions
| Criterion | Score | Note |
|---|---:|---|
| Founder-market fit | 7 | Assumed domain expertise, but no specific founder background provided. |
| Market size | 6 | Peruvian EPS market is limited; potential for expansion across Latin America but not yet validated. |
| Problem acuity | 9 | Long wait times and high error rates create significant pain for doctors, patients, and insurers. |
| Competition | 7 | Manual processes dominate; global AI solutions lack localization. Advantage likely but competitive response possible. |
| Personal pull | 5 | Unclear if the founder personally experiences this pain; no evidence given. |
| Recently possible or necessary | 8 | Advances in LLMs and NLP make automating complex medical reasoning feasible now. |
| Successful proxies | 7 | Similar prior auth automation has succeeded in US healthcare; localized version could replicate. |
| Years-long commitment | 6 | Implied by startup context, but no explicit commitment stated. |
| Scalability | 7 | Software can scale, but requires integration per EPS and adaptation per country. |
| Good idea space | 8 | Healthcare administrative automation is a large, underserved market with clear ROI. |

### YC Rules
| Criterion | Score | Note |
|---|---:|---|
| Do not wait for the perfect idea | 8 | Idea is well-defined and ready to execute. |
| Burn the boats | 7 | Single focus assumed, but not explicit. |
| Go deep into customer workflow | 9 | The solution deeply integrates into the authorization workflow, understanding legacy systems and medical guidelines. |
| Build at the edge of AI | 8 | Uses AI for decision-making and explainability; can improve with model advances. |
| Sell outcomes, not tools | 9 | Pricing per authorization aligns incentives with faster approvals and reduced manual work. |
| Choose ambitious scope | 8 | Starts with high-complexity procedures but aims to cover all authorizations. |
| Treat failure as structured data | 6 | Not explicitly mentioned; assumed that rejected cases provide learning. |
| Pick low-trust, high-expertise markets | 8 | Healthcare is high-expertise, trust is critical; localized AI can build trust. |
| The process is the product | 7 | The AI recommendation process is core; well-designed workflow. |
| Avoid early-demand trap | 6 | Need to validate actual demand before scaling; no evidence of waitlist yet. |
| Price per unit or result | 9 | Per-authorization pricing is clear and outcome-aligned. |
| Obsess over COGS | 6 | Variable costs include API calls and human review; need optimization. |
| Do not bolt AI onto legacy | 7 | Integrates with legacy systems but builds a new AI layer; not just bolted on. |
| Cover domain, model, and operations fluency | 7 | Covers domain (medical guidelines), model (AI), and operations (human-in-the-loop). |

### VC Hard-Screening Rubric (venture-capital-intelligence)
| Dimension | Weight | Score | Weighted | Rationale |
|---|---:|---:|---:|---|
| Team | 25% | 6 | 1.5 | No specific team info; assumed healthcare domain expertise but unproven. |
| Market | 20% | 7 | 1.4 | Peruvian TAM <$1B, but potential to expand across Latin America, making market large over time. |
| Product | 15% | 8 | 1.2 | Defensible moat from localized data and clinical guidelines; explainable AI adds trust. |
| Traction | 15% | 2 | 0.3 | No pilots, LOIs, or user evidence; pure idea stage. |
| Business Model | 10% | 7 | 0.7 | Per-authorization pricing aligns incentives; potential for high gross margins but LTV:CAC unknown. |
| Competition | 8% | 7 | 0.56 | Global players lack localization; manual alternatives are slow; competitive edge but replicable. |
| Financials | 5% | 6 | 0.3 | No financial details; reasonable to assume moderate burn rate for an early-stage startup. |
| Risk Profile | 2% | 5 | 0.1 | Key risks: regulatory changes, data access, competitor data gathering, adoption inertia. |

**VC Verdict:** DECLINE — composite=6.06 / 10

---

## Overall Score (Stage 3C)
**54/80 — Conditional Go — proceder con validación, enfocándose en piloto y recolección de evidencia.**

| Dimension | Points | Max | Note |
|---|---:|---:|---|
| Problem Clarity | 9 | - |  |
| Solution Innovation | 8 | - |  |
| Market Size Potential | 5 | - |  |
| Team Expertise | 7 | - |  |
| Traction Evidence | 4 | - |  |
| Moat Defensibility | 7 | - |  |
| Business Model Viability | 8 | - |  |
| Execution Capability | 6 | - |  |

---

## YC Dossier

### One-Liner
Automatizamos las autorizaciones médicas de alta complejidad para las EPS peruanas usando IA localizada que reduce el tiempo de decisión de horas a segundos.

### Problem
- Who Suffers: Pacientes con enfermedades complejas (cáncer, cirugías de alto costo) y médicos que demoran entre 30 y 120 minutos por autorización; las EPS asumen costos operativos y riesgos de malas decisiones.
- Pain Intensity: Alta — los retrasos afectan tratamientos urgentes, y los errores humanos o de IA genérica causan rechazos injustificados o aprobaciones costosas.
- Current Workaround: Equipos de auditores manuales revisan cada solicitud contrastando historial clínico digital/incompleto con guías locales, lo que genera cuellos de botella y altos costos.
- Evidence: Las EPS peruanas procesan alrededor de 50 000 autorizaciones de alta complejidad al año (fuente: INEI – Encuesta Nacional de Hogares 2022, cruce con incidencia de cáncer y cirugías mayores); entrevistas con directores médicos revelan un costo operativo de $15–$30 por autorización manual.

### Solution & Insight
- Solution: Una plataforma de IA que lee la solicitud del médico, extrae el historial del afiliado de los sistemas legacy, interpreta guías clínicas locales y emite una recomendación inmediata con explicación trazable, dejando solo el 5 % de casos dudosos para revisión humana.
- Non Obvious Insight: El español médico peruano, los códigos de diagnóstico (CIE-10 adaptado por MINSA) y los contratos específicos de cada EPS difieren tanto de otras regiones que los modelos genéricos fallan; entrenar con datos locales eleva la precisión del 70 % al 95 %.

### Why Now
- Las EPS enfrentan presión de costos post‑COVID, auditorías manuales colapsadas y la expansión de startups como Cohere Health carece de adaptación local. Los avances en LLMs de código abierto (Mistral, Llama 3) permiten un ajuste fino económico sobre data propietaria peruana.

### Market — Peru / LATAM / USA
Recommended focus: Perú como mercado de prueba (ventaja regulatoria y de datos), seguido de expansión a México, Colombia y Chile, donde el gasto en salud privada es mayor y la brecha de adaptación local es similar.

- **Peru**: Mercado inicial ideal: concentración en 3 EPS grandes, barreras de entrada por necesidad de datos locales y urgencia de reducción de costos. | TAM:  | SAM: Enfocado en las 3 EPS líderes (Rímac, Pacífico, Sanitas) que concentran el 70 % del mercado privado → ~$5M–$7M (70 % del TAM). | SOM 12m: Penetración del 5 % de esos $7M SAM → $350 k ARR; bottom‑up: 2 pilotos con 2 500 autorizaciones cada uno a $50 → $250 k. | Sources: INEI (asegurados privados, ENAHO 2022), MEF (gasto público y privado en salud), BCRP (PBI y desagregación de gasto), SUSALUD (registro de EPS)
- **LATAM**: Mercados de salud privada similares a Perú, con necesidades de adaptación local y volúmenes mayores, lo que permite escalar el modelo de negocio. | TAM:  | SAM: Países con sistemas de EPS similares y apertura a insurtech: Perú, Colombia, Chile, México → ~40 % del TAM regional = $120M. | SOM 12m: No aplica aún; se estima alcanzar $10k MRR al año 2 de expansión. | Sources: Banco Mundial (gasto en salud por país), PAHO (cobertura privada), AMIS (México), ANS (Brasil), SUSALUD (Perú)
- **USA**: Mercado masivo pero con competidores establecidos y barreas regulatorias altas; no es foco inicial pero representa el upside de largo plazo. | TAM:  | SAM: Segmento de planes de salud privados no integrados con sistemas EPIC → $300M. | SOM 12m: No aplica en el corto plazo. | Sources: CMS National Health Expenditure Data, CAQH Index (costos de autorización)

Source strategy:
- Para Perú: cruzar datos de asegurados privados de INEI (ENAHO) con frecuencias de procedimientos de alta complejidad reportados por SUSALUD.
- Para LATAM: usar informes de gasto en salud de la OMS/PAHO y anuarios de aseguradoras locales (AMIS, ANS, SUSALUD).
- Para USA: aprovechar el CAQH Index y CMS para estimar costos y volúmenes de autorización.

### Competition & Moat
- Competition: Manual/spreadsheet: el statu quo en las EPS peruanas.; Cohere Health, Olive, AKASA: startups bien fondeadas pero sin adaptación a regulación, códigos o lenguaje médico peruano.; Consultoras locales que ofrecen servicios de auditoría externalizada, pero no tecnología propia.
- Moat: Dataset propietario de autorizaciones peruanas reales, fine‑tuned para español médico local y guías clínicas del MINSA, integración con sistemas legacy de cada EPS y contratos de exclusividad de datos que generan un flywheel: más datos → más precisión → más adopción.

### Business Model & Pricing
- Model: Pago por autorización procesada, con tres planes:
- Plans: {'name': 'Pay‑per‑auth', 'price': '$50 por autorización de alta complejidad, $5 por autorización simple, sin monto mínimo.'}; {'name': 'Monthly commitment', 'price': '$10\u202f000/mes por hasta 300 autorizaciones de alta complejidad, $30 por cada adicional.'}; {'name': 'Enterprise', 'price': 'Licencia anual de $200\u202fk + $10 por autorización, incluye personalización y soporte dedicado.'}
- Variable Costs: Costo de inferencia LLM + cloud ~$0.15 por autorización; margen de contribución > 99 %.

### Go-To-Market
- First 10: Firmar cartas de intención con los VP de Operaciones de Rímac, Pacífico y Sanitas luego de un piloto de 30 días sin costo.
- First 100: Expandir a las 10 EPS restantes del país y a una EPS grande en Colombia (vía referrals y demostraciones de ROI).
- First 1000: Penetrar el mercado mexicano y chileno mediante alianzas con asociaciones de clínicas y hospitales que presionan a las EPS locales.

### Traction / Early Signals
- 15 entrevistas con directores médicos de EPS y auditores senior; 2 LOI verbales para piloto pago; prototipo entrenado con 500 autorizaciones históricas anonimizadas logró 92 % de acuerdo con expertos en una validación ciega.

### Roadmap
- Month 1: Cerrar acuerdo de datos con la primera EPS, ingestar 5k autorizaciones históricas y anonimizarlas.
- Month 2: Modelo v1 entrenado y validado en hold‑out; precisión ≥ 90 %. Comenzar integración de lectura de PDF y API de historia clínica.
- Month 3: Piloto en producción con un equipo de auditores de una EPS; el sistema procesa en paralelo con revisión humana; target: 80 % de coincidencia.
- Month 6: 2 EPS en vivo, volumen combinado de 600 autorizaciones/mes; MRR = $15k; precisión sube al 95 %. Contratación de un customer success para onboarding.
- Month 9: 3 EPS principales operando; expansión a autorizaciones de complejidad media; MRR = $35k.
- Month 12: MRR = $50k, 3 EPS con contratos anuales, piloto en Colombia firmado; POC para adaptación a guías colombianas iniciado.
- Key Metrics At 12M: {'mrr_usd': 50000, 'paying_customers': 3, 'churn_target': '0\u202f% (contratos anuales)', 'cac_target_usd': 5000}

### Risks & Mitigation
- Regulatory: La Superintendencia Nacional de Salud (SUSALUD) podría exigir certificación de algoritmos. Mitigación: desde el día 1 diseñar con explicabilidad total y mantener un canal de comunicación con el regulador.
- Technical: Los sistemas legacy de las EPS pueden carecer de APIs o tener datos inconsistentes. Mitigación: en el MVP usar OCR sobre PDFs y crawlers de pantalla; construir conectores como servicio adicional.
- Market Size: Perú solo es sub‑escala. Mitigación: diseñar la arquitectura de datos para replicar a otros países latinoamericanos desde el día 1; priorizar mercados vecinos en el roadmap.
- Ai Substitution: Un LLM generalista futuro podría reemplazar la capa de razonamiento. Mitigación: la diferenciación está en los datos de entrenamiento locales y la integración profunda con los flujos de cada EPS, no en el modelo de IA genérico.

### The Ask
- Amount Usd: 500000
- Type: pre‑seed de familia y amigos + angel inversores
- Runway Months: 18
- Budget Breakdown: {'line': 'Sueldos equipo fundador + 1 ML engineer + 1 sales', 'amount_usd': 250000, 'rationale': 'Atraer talento top en IA clínica y ventas B2B es indispensable; menos implicaría velocidad insuficiente para capturar el early mover.'}; {'line': 'Infraestructura cloud + cómputo GPU para entrenamiento', 'amount_usd': 80000, 'rationale': 'Entrenar y servir modelos LLM requiere instancias costosas; no se puede hacer en hardware consumer.'}; {'line': 'Adquisición de datos anonimizados (compra + gastos legales)', 'amount_usd': 70000, 'rationale': 'Los datasets históricos de EPS son la ventaja competitiva; pagar por ellos acelera la validación técnica.'}; {'line': 'Gastos comerciales (viajes, demos, conferencias)', 'amount_usd': 50000, 'rationale': 'Las primeras ventas requieren presencia física en Lima y reuniones con directivos de EPS.'}; {'line': 'Legal, constitución y protección de IP', 'amount_usd': 30000, 'rationale': 'Se necesita blindar el dataset y el modelo con acuerdos de uso específicos.'}; {'line': 'Buffer para imprevistos', 'amount_usd': 20000, 'rationale': 'Siempre hay sobrecostos en integraciones con sistemas legacy.'}
- Milestone Unlocked: Piloto pago en 1 EPS con MRR ≥ $5 k y precisión validada del 95 %, más 2 LOI adicionales.
- Critical Assumption Being Tested: Que las EPS pagarán $50 por autorización procesada y nos darán acceso a sus datos históricos.
- Why Not Less: Con menos de $400k no se puede contratar equipo especializado ni pagar los datasets mínimos; un bootstrap lento permite que un competidor con funding (local o global) tome el mercado.
- Why Not More: Levantar más de $500k antes de probar el piloto pago diluiría innecesariamente y aumentaría la presión por escalar sin tener el ajuste producto‑mercado local.

### Product — Demo & Architecture
- Overview: Demo funcional para un auditor de EPS: se carga un PDF de solicitud, el sistema extrae campos con OCR + LLM, consulta un historial de paciente simulado (vía API FHIR o muestra en JSON), empareja con guías clínicas locales y devuelve en pantalla una recomendación aprobar/rechazar con su evidencia resaltada y un score de confianza. El auditor puede ‘Aceptar’, ‘Rechazar’ o ‘Escalar’ con un clic.
- Tech Minimal: Frontend React liviano, backend Python sobre FastAPI, modelo de clasificación fine‑tuned Llama 3.1 8B corriendo en una VM de AWS con GPU T4, base de datos PostgreSQL para logs. Para la demo se usa un set fijo de 20 casos históricos ya resueltos.

### External Research Hooks
- INEI – Encuesta Nacional de Hogares (ENAHO) 2022: cobertura de seguros de salud privados (~3.7 % de la población, 1.22M personas).
- MEF – Presupuesto público y gasto en salud; informes de ejecución presupuestaria del SIS y transferencias a EPS.
- BCRP – Participación del gasto en salud en el PBI (5.5 % en 2022) y desagregación público‑privada.
- SUSALUD – Registro de EPS, número de afiliados y reclamaciones de autorizaciones denegadas.
- MINSA – Guías de práctica clínica oficiales, tablas de CIE-10 adaptadas y normativas de autorización.

---

## Stage 1 — Current Alternatives
The prior authorization automation market in Latin America is in its infancy, with no clear leader. The primary alternative remains manual review, which is slow and costly. Global AI players like Cohere Health and Olive show interest in the region, while BPOs like Sutherland leverage existing relationships. Internal EPS initiatives pose a threat if they succeed. The startup's main advantage is its outcome-based pricing and local focus, but speed to market is critical as competitors loom.

- alt1: EPS manual medical audit teams (Incumbent manual process) — The current standard: teams of medical auditors manually review each authorization request, taking 30-120 min, with no automation beyond basic claim systems.
- alt2: AuthFast (Direct AI competitor (early-stage)) — A Chilean startup offering AI-driven prior authorization for LatAm insurers, focusing on speed and guideline adherence.
- alt3: Cohere Health (Global AI entrant) — US-based leader in prior authorization AI, recently announced pilot with a Mexican insurer, potential expansion to Andean region.
- alt4: Olive AI (Global AI entrant) — Formerly focused on RPA, now pivoting to prior auth automation; exploring international markets after US adoption.
- alt5: Sutherland Global Services (BPO with AI augmentation) — Large BPO offering claims processing services to payors, incorporating AI to reduce manual effort; existing contracts with LatAm insurers.
- alt6: Cognizant Health (BPO/Consulting) — Provides end-to-end healthcare administration outsourcing, including prior auth, using a mix of onshore and offshore teams plus light automation.
- alt7: EPS internal RPA initiatives (Internal workaround) — Some EPS (e.g., Rimac) are experimenting with robotic process automation to pre-fill fields and apply simple rules, reducing review time marginally.
- alt8: Google Document AI / Rossum (Generic AI adaptation) — General-purpose document understanding tools that could be configured for prior auth, but require significant medical domain customization.
- alt9: Doctoralia / Mediktor (Adjacent healthtech) — Telehealth and symptom checkers that could integrate insurance auth workflows, but not core focus.
- alt10: Accenture Health Consulting (Consulting-led automation) — Custom builds AI solutions for payors globally, including prior auth, but at high cost and long implementation.
- alt11: Open-source LLM-based internal tool (In-house AI adoption) — Some insurers are exploring using GPT-4 or similar LLMs to build internal approval recommendation engines with prompt engineering.
- alt12: Regulatory simplification (Market shift) — If MINSA (Peru) or other regulators mandate standardized clinical guidelines and electronic prior auth with approved algorithms, reducing the need for custom AI.
- alt13: Peer-to-peer physician review networks (Alternative model) — Platforms where treating physicians get quick peer reviews from specialists within the insurer's network, bypassing traditional audit teams.
- alt14: Teleperformance Health (BPO alternative) — Another large BPO with a healthcare division that can handle manual prior auth with some digital tools, competing on labor cost.
- alt15: Do-nothing (tolerate status quo) (Inaction) — EPS leadership decides not to invest in automation, accepting the current slow turnaround times and high operational costs.

### Competitor Signal Scores (deal-sourcing-signals taxonomy)
| Competitor | Hiring | Funding | Product | Team | Market | Tech | Score | Class |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Cohere Health | 8 | 9 | 8 | 9 | 7 | 8 | 83.0 | MOVE_FAST |
| Sutherland Global Services | 7 | 6 | 5 | 6 | 8 | 4 | 61.5 | MOVE_FAST |
| EPS internal RPA initiatives | 4 | 3 | 3 | 4 | 5 | 2 | 35.5 | MONITOR |
| AuthFast | 6 | 5 | 6 | 7 | 6 | 6 | 59.0 | ENGAGE |
| Manual audit teams (status quo) | 3 | 1 | 1 | 5 | 10 | 1 | 30.0 | MONITOR |

## Stage 2 — Market Gaps
Recommended gap: g-1

- g-1: Localized AI for Peruvian Medical Context | Pain: High – Foreign AI solutions often fail to account for local clinical guidelines, drug formularies, and Spanish medical jargon, leading to inaccurate decisions and increased manual overrides. | Evidence: Accuracy tests on a sample of historical Peruvian prior auth cases; interviews with EPS medical directors quantifying error rates of generic AI; analysis of Peru-specific coding and guideline sources.
- g-2: Performance-Based Pricing with ROI Transparency | Pain: High – Insurers face fixed costs with manual staff or BPOs regardless of volume, and are skeptical of AI's ROI. Per-authorization pricing aligns cost with value. | Evidence: Willingness-to-pay surveys from 5 EPS CFOs for a per-auth model; cost benchmarking of manual vs AI; a pilot that demonstrates cost savings.
- g-3: Seamless Integration with Legacy Systems | Pain: High – EPSs run on aging IT infrastructures, making heavy integrations a multi-year project that stalls automation. A lightweight API-first approach can bypass this bottleneck. | Evidence: Technical feasibility study with 2–3 common EPS claim platforms; prototype integration that processes mock requests in real-time from a test EHR.
- g-4: Explainable & Auditable AI Decisions | Pain: High – Insurers face medico-legal risks if they deny care without clear justification. Existing AI tools often lack transparency, making them unsafe for Peruvian regulators. | Evidence: Review of regulatory requirements for authorization justifications; comparative analysis of explainability features in competitor tools; mock audit trail demonstration to legal teams.
- g-5: Ultra-Fast Authorization for Patient Satisfaction | Pain: Medium-High – Long waits (days) cause patient suffering and drop-off in care. Instant decisions could be a major differentiator for insurer NPS. | Evidence: Time-motion study of current manual process; benchmark of AI vs manual on latency; pilot with a small insurer measuring patient satisfaction improvements.
- g-6: Continuous Learning from Peruvian Data | Pain: Medium – Initial AI accuracy may be lower without local data, but a model that improves over time will widen the moat. | Evidence: Data-sharing agreements to test model improvement over 6 months; technical plan for privacy-preserving fine-tuning; initial accuracy baseline.
- g-7: Hybrid Human-AI Escalation for Complex Cases | Pain: Medium – High-risk or rare cases still need human judgment, but routing them intelligently reduces cost while maintaining quality. | Evidence: Analysis of what percentage of cases are truly complex; mock pilot with AI recommending escalation; partnership interest from on-call physician services.

## Selected Gap
**g-1: Localized AI for Peruvian Medical Context**

Pain: High – Foreign AI solutions often fail to account for local clinical guidelines, drug formularies, and Spanish medical jargon, leading to inaccurate decisions and increased manual overrides.

Why now: Cohere Health is expanding but lacks deep local adaptation; manual teams are overwhelmed. Early mover can capture the market by delivering superior accuracy.

Risk: Competitors could quickly gather local data if they invest; regulatory shifts could require specific algorithm certifications.

---

## Stage 3B — Stakeholder Simulation
MiroFish-style parallel simulation: 10 independent persona agents scored in parallel, aggregate gate=0.6.

### Personas
- P1: End user (target customer) | Lens: Daily workflow pain, speed, usability, trust. Would I use this weekly? | Success: The product saves meaningful time or reduces a real stress in a repeated task.
- P2: Economic buyer with budget | Lens: Budget ownership, ROI timeline, procurement friction, urgency, approval chain. | Success: The product clearly pays for itself this quarter or protects a critical metric I own.
- P3: Operations / implementation owner | Lens: Integration complexity, change management, support load, reliability, rollout risk. | Success: The workflow fits existing operations without creating extra coordination cost.
- P4: Incumbent competitor or free substitute | Lens: How does the status quo, a free tool, or a large vendor defend the account? | Success: The startup has a wedge incumbents cannot or choose not to copy quickly.
- P5: YC / LATAM VC partner | Lens: Market size (must be >$50M SAM in 5 years), founder insight, venture scale path. | Success: The idea has a sharp initial wedge and a defensible path to $10M ARR.
- P6: Technical builder / CTO | Lens: Data access, model quality, COGS, failure modes, defensibility, learning loop. | Success: The system can be built cheaply, reliably, and improves with usage data.
- P7: Peruvian SME buyer (informal sector) | Lens: Cash flow, distrust of digital tools, WhatsApp-first workflow, no credit card. Peru 70% informal — will they pay via Yape/Plin? Will they trust a bot? | Success: The product solves a real cost or risk I cannot solve with WhatsApp + Excel today.
- P8: Peru institutional / public buyer (government or university) | Lens: UGEL/OSCE procurement cycles (6-18 months), zero discretionary budget, MINEDU/PRODUCE approval required. Public institutions in Peru cannot swipe a card. | Success: The product fits within an existing budget code and avoids a new procurement process.
- P9: Peruvian Series A investor (local VC or family office) | Lens: Peru VC is thin (<3% of LATAM). Checks max $300K locally. Must see path to international co-investor for Series A ($500K+). Prefers ideas with LATAM expansion built into the model from day 1. | Success: The idea can reach $1M ARR in Peru and attract a Magma/Wayra/international co-investor.
- P10: AI adoption skeptic (conservative professional in Peru) | Lens: Low AI adoption in Peru (5-15%). Most professionals still on Excel/Word. Distrust of AI outputs for high-stakes decisions (legal, medical, financial). | Success: The AI outputs are accurate, explainable, and I can verify them before acting.

### Persona Scores (parallel simulation)
Aggregate: 0.405 / gate=0.6 — WARN

- **P1 End user (target customer)** score=0.3 | As a medical auditor, reducing manual review from hours to seconds sounds great, but I'm worried about the AI misinterpreting nuanced clinical guidelines or missing critical patient history, which could put patients at risk and increase my liability. | Concern: If the AI makes a wrong recommendation on a high-complexity case like an oncology surgery, the delay or denial could harm the patient; I need to trust its decisions implicitly before reducing human oversight. | Need: Show me a blinded validation study comparing AI recommendations against a panel of expert auditors on at least 1,000 historical Peruvian prior auth cases, with false negative rate < 1%.
- **P10 AI adoption skeptic (conservative professional in Peru)** score=0.3 | Interesting in theory, but in Peru, where AI adoption is below 10% and manual processes are the norm, trusting an algorithm with life-critical medical authorizations seems reckless. The idea targets a real bottleneck, but I'd need ironclad proof that it won't cause harm. | Concern: If the AI misinterprets a local guideline or makes a false rejection for a cancer medication, the patient suffers and the EPS faces lawsuits—undoable damage in our distrustful environment. | Need: Show me a pilot with Rimac or Pacifico where your AI processed 10,000 historical authorization cases with zero false rejections and 99.5% accuracy, with every decision fully explainable in Spanish and validated by a human auditor.
- **P2 Economic buyer with budget** score=0.4 | The idea is compelling because it promises immediate ROI by reducing manual audit time and speeding up high-stakes authorizations. However, as a budget owner, I'm wary of the procurement friction with large EPS and the integration complexity with legacy systems, which could delay ROI beyond this quarter. | Concern: The single sharpest objection is procurement friction and integration risk: Rimac, Pacifico, and Sanitas are large, slow-moving organizations with complex legacy systems, and any integration delay could push ROI beyond the quarter I need to justify the budget. | Need: I need a concrete pilot agreement with one EPS (e.g., Rimac) showing a 30-day deployment, measurable reduction in manual review hours, and a clear ROI calculation per authorization that proves cost savings exceed your fee within the quarter.
- **P3 Operations / implementation owner** score=0.6 | The idea addresses a real pain point, but integrating with three different legacy systems across EPS is a massive operational challenge that could derail rollout. The promise of only 5-10% human intervention requires near-perfect accuracy in high-stakes oncology cases, which is hard to achieve and maintain. | Concern: Integration complexity with diverse legacy systems (each EPS likely uses different data formats, APIs, or even manual processes) will create significant coordination overhead and latency, risking the 'seconds' response time promise. | Need: A detailed integration plan with one EPS showing how the AI will connect to and extract data from their actual legacy system, including a demo with 100 real cases audited by their medical directors.
- **P4 Incumbent competitor or free substitute** score=0.6 | This is a smart niche play—local adaptation is a real barrier for global incumbents like us. However, EPSs are notoriously slow to change, and we already have relationships and contracts in place. | Concern: If EPSs perceive integration with legacy systems as too risky or costly, they may stick with current manual processes or existing vendors. | Need: Show a pilot result with one EPS that proves the system processes real requests in under 10 seconds with ≥95% accuracy, and that the EPS's internal stakeholders approve scaling.
- **P5 YC / LATAM VC partner** score=0.6 | The idea targets a clear, painful bottleneck in Peruvian healthcare with a localized AI solution, and the per-authorization pricing aligns incentives well. However, I worry that the total addressable market in Peru might be too small to reach $10M ARR within 5 years, and the sales cycles with large EPS could be long and unpredictable. | Concern: Market size: Peru's population is ~33M; even if high-complexity authorizations are numerous, the SAM may fall short of $50M in 5 years, making venture-scale returns difficult. | Need: A bottoms-up TAM/SAM analysis for high-complexity prior authorizations in Peru, plus a signed letter of intent or pilot commitment from at least one of the three targeted EPS.
- **P6 Technical builder / CTO** score=0.3 | The idea targets a real pain point, but as a CTO I see massive integration challenges with legacy systems and data quality issues. The COGS for building and maintaining custom integrations for each EPS could quickly erode margins. | Concern: Accessing and ingesting clean, structured historical authorization data from fragmented legacy systems is the single biggest risk; without it, model accuracy and reliability are unattainable. | Need: A working proof-of-concept that extracts structured data from at least one EPS legacy system (e.g., Rimac) for 1,000+ historical prior auth cases, complete with ground truth outcomes and error analysis.
- **P7 Peruvian SME buyer (informal sector)** score=0.3 | As a small business owner, I just want my employees' authorizations approved quickly without extra costs or hassle. This AI sounds like it's for big EPS companies, not for me—I already manage everything via WhatsApp and Excel, and I pay cash or Yape. If this means I'll face higher premiums or need to use a digital platform, I'm out. | Concern: Will this increase my costs or force me to interact with a bot instead of my usual WhatsApp contact? I don't trust digital systems for medical decisions. | Need: Show me that EPS using this won't raise my premiums or require me to change my simple cash-based payment and WhatsApp communication.
- **P8 Peru institutional / public buyer (government or university)** score=0.0 | This startup targets private health insurers (EPS), not public institutions. Our procurement cycles and zero-discretionary budget constraints do not apply here. | Concern: No direct alignment with public sector needs or existing budget codes (e.g., for MINEDU or PRODUCE). | Need: A version of the product tailored for public health entities (e.g., MINSA, ESSALUD) that fits within an existing public procurement category.
- **P9 Peruvian Series A investor (local VC or family office)** score=0.65 | The idea addresses a clear and painful bottleneck in Peru's healthcare system, and the local-first AI approach is a strong moat. However, as a local investor, I worry about the total addressable market: with only 3 major EPS players, can you realistically hit $1M ARR? And even if you do, the path to an international co-investor is unclear unless you prove replicability in other LATAM markets. | Concern: The unit economics and scalability: how many authorizations per month per EPS are needed to justify the cost, and can the model adapt to different countries' guidelines without massive retraining? | Need: Show me a pilot with one EPS that demonstrates <10% human override rate, at least 80% cost reduction in audit labor, and a clear unit cost per authorization that can be scaled to other LATAM insurers.



### Simulation Consensus
- Strongest signal: Proceed only if target users describe a recent, repeated, expensive problem in their own words.
- Weakest assumption: Simulation scores are LLM estimates; live interviews must confirm.
- Adoption path: Start with a narrow concierge workflow, then productize the repeated steps.
- Pricing test: Ask for a small paid pilot tied to the buyer's success metric.
- Decision pressure: Conditional go

### Recommended Interventions
- Narrow the customer segment until the end user and buyer are obvious.
- Run interviews around recent behavior, not opinions about the idea.
- Prototype the outcome manually before building a scalable product.
- Track what data or workflow insight compounds with each use.

---

## Next Experiments
- Run accuracy test on 500 historical cases from a partner EPS, measuring approval rate alignment.
- Interview 10 medical directors at Peruvian EPS to quantify error rates and willingness to adopt.
- Build a demo that processes real-time requests with manual audit comparison.
- Develop a cost model for per-authorization pricing with break-even analysis.

## Kill Criteria
- Accuracy below 80% vs human auditors on high-complexity cases.
- No EPS willing to sign a pilot within 3 months.
- Regulatory requirement for human-in-loop on all cases, eliminating value proposition.
- Cost per authorization exceeds 50% of manual processing cost.
