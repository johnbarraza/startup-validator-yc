# Startup Idea Validation Report

Generated: 2026-06-21T17:19:14.673322+00:00

## Original Idea
ContaBot: servicio de contabilidad automatica para microempresas y PYMES peruanas que deben cumplir con SUNAT (factura electronica, declaraciones mensuales PDT, impuesto a la renta). Hoy pagan S/200-500/mes a un contador o lo hacen mal y reciben multas. ContaBot lee sus facturas electronicas de SUNAT directamente via API, categoriza gastos, genera el PDT automaticamente y lo presenta ante SUNAT. Modelo: cobramos S/80/mes por empresa, hacemos el trabajo completo como servicio no como software. YC Spring 2026 pide AI-powered agencies que reemplacen servicios con margenes de software.

---

## Stage 0 — Idea Classification (Pit Check)

**Type:** PAINKILLER | **Vertical:** FinTech | **Customer:** B2B | **Severity:** STRUCTURAL

**Verdict:** ⚠ WARN | **Devil's advocate:** ⚠ WEAK | **Freemium:** ✗ NO

ContaBot addresses a structural, recurring compliance pain for Peruvian SMEs. They currently pay higher fees for manual accounting or risk fines. The AI-powered service offers a cheaper, automated alternative with direct SUNAT integration. Strong painkiller signals and clear willingness to pay given existing budget. Not crowded by incumbents with same model; regulatory mandate ensures urgency.

**Green flags (painkiller signals):**
  - Active workarounds exist (manual contador)
  - Spending already happens (S/200-500/month)
  - Regulatory forcing function (SUNAT, fines)
  - Recurring pain (monthly declarations)
  - Measurable cost (fines, hours)
  - B2B buyer has budget (already paying for accounting)
  - Users search actively for solutions

**Red flags (devil's advocate):**
  - Informal economy: 70-75% of businesses are informal and don't file taxes or can evade for years. The addressable market is only formal micro/SMEs, estimated at ~200K out of 3M+ businesses.
  - Low willingness to pay: Peruvian SMEs typically pay S/200-500/month for a full accountant. At S/80/month, the value prop may not be compelling enough to overcome inertia and trust issues, especially when a cheap local accountant provides personalized service.
  - Trust + security risk: SMEs must share SUNAT credentials (or API access) with ContaBot. Any error or data breach could result in fines or audits, making adoption slow for risk-averse owners.
  - SUNAT API fragility: The API for electronic invoices may change, have downtime, or not cover all edge cases (e.g., manual receipts). ContaBot becomes a single point of failure for compliance.
  - Sales cycle via WhatsApp: B2B sales in Peru require multiple face-to-face demos and personal relationships. Scaling via WhatsApp alone is difficult; unit economics may break if high-touch sales needed.

**Payment blocker:** B2B payment is via CCI bank transfer (not credit card or instant payment), adding friction for monthly recurring billing. Many SMEs pay quarterly or annually, causing cash flow gaps.

**Free substitute risk:** SUNAT's free portal allows manual PDF upload and PDT generation. Combined with a spreadsheet and WhatsApp accountant guidance, many businesses will stick with the free, familiar workaround.

**Market size reality check:** Realistic SAM: formal micro and SMEs in Peru that need automated filing and can pay S/80/month ≈ 100,000-200,000 businesses. At S/960/year per business, max TAM ~$50M/year; but actual penetration will be <5% in 3 years, giving <$2.5M ARR — too small for YC-scale venture.

**Hardest unvalidated assumption:** That Peruvian SMEs value automation enough to pay S/80/month and trust an AI service over a human accountant, despite cultural preference for personal relationships and low digital trust.

**Freemium rationale:** The service is full-service (filing tax returns), not a self-serve software. A free tier would require limiting core filing, reducing value, and increasing costs. Given low price point (S/80/month), converting free users to paid is uncertain; better to monetize directly. A free trial (e.g., first month free) could work but is not a permanent freemium tier.

**Suggested pivot:** 

---

## Stage 2B — Idea Iterations (3 angles)

Recommended: **I1** — ContaBot automatiza todo el proceso de declaración mensual ante SUNAT para dueños de microempresas, tomando las facturas desde la API oficial y presentando el PDT sin que toquen un papel.

| ID | Angle | One-Liner | Acuity | Market | Feasibility | Total |
|---|---|---|---:|---:|---:|---:|
| I1 | ORIGINAL | ContaBot automatiza todo el proceso de declaración mensual ante SUNAT  | 9 | 8 | 10 | 27 |
| I2 | PIVOT_B2B | We provide an AI-driven tax compliance platform for Peruvian instituti | 9 | 9 | 6 | 24 |
| I3 ★ | PIVOT_WEDGE | Servicio contable 100% automático para bodegas que necesitan cumplir c | 9 | 5 | 10 | 24 |

### I1 — ORIGINAL
**Target:** Dueño de una bodega o peluquería en Lima que factura electrónicamente por obligación pero que odia lidiar con trámites tributarios.
**Problem:** Cada mes, antes del vencimiento del PDT, vive con ansiedad: no sabe cómo llenar el formulario, intenta seguir tutoriales confusos o paga a un contador que a veces olvida el plazo. Si no declara a tiempo, arriesga multas de hasta S/1,500 y posible cierre fiscal de su negocio. El tiempo perdido y el miedo constante afectan su operación diaria.
**Hook:** El único servicio que no solo lee las facturas, sino que genera y presenta el PDT automáticamente conectándose a SUNAT, sin requerir que el dueño entienda contabilidad ni mueva un dedo cada mes.
**Why this angle:** Al concentrarse en el acto concreto de presentar el PDT (el peak del dolor mensual) y automatizarlo al 100%, la propuesta se vuelve ultra-específica, tangible y fácil de vender: 'olvídate de la SUNAT'. Se diferencia de los software que dejan la presentación como último paso manual.

### I2 — PIVOT_B2B
**Target:** Director de Formalización Empresarial at the Ministry of Production of Peru, or Gerente de Servicios at the Lima Chamber of Commerce.
**Problem:** Millions of microenterprises in Peru operate informally or face constant fines and accountant fees, while government and trade groups lack a scalable, low-cost tool to enforce compliance and bring businesses into the formal economy. This leads to lost tax revenue, stunted economic growth, and political pressure on institutions to act.
**Hook:** ContaBot integrates directly with SUNAT’s e-invoicing ecosystem to fully automate categorization, return generation, and filing with zero manual intervention, enabling institutional buyers to offer a turnkey, proactive compliance service at an order-of-magnitude lower cost than human accountants or legacy software.
**Why this angle:** Institutional buyers have budget, urgency, and a mandate to solve informality, enabling multi-year contracts and mass adoption without the high CAC of direct-to-microenterprise sales. A single deal can onboard thousands of users, driving revenue while fulfilling a national policy need, with software-like margins on the service.

### I3 — PIVOT_WEDGE ★ WINNER
**Target:** Dueño de bodega en Lima (p.ej., María de San Juan de Lurigancho) que factura electrónicamente más de 50 comprobantes al mes, con ventas anuales entre S/50k y S/100k, y ya ha recibido al menos una multa tributaria.
**Problem:** Cada mes, el bodeguero debe recopilar facturas de compra y venta, calcular IGV y renta, y presentar el PDT 621. Su contador actual cobra S/250 pero a menudo incumple plazos o comete errores, generando multas de S/300-500 que afectan su flujo de caja. El dueño no tiene tiempo de aprender contabilidad ni dinero para un mejor servicio; el incumplimiento le causa estrés y riesgo de fiscalización.
**Hook:** Lectura automática de facturas desde SUNAT, categorización inteligente con reglas fiscales peruanas, y envío directo del PDT sin que el cliente tenga que mover un dedo — un servicio cerrado, no un software que requiera habilidad contable.
**Why this angle:** Al aterrizar en bodegas con facturación electrónica y multas recientes, se ataca el dolor más agudo con un segmento homogéneo fácil de reclutar y referenciar. Esto permite validar velocidad de pago en 30 días y ajustar la propuesta antes de expandir a otros giros.

---

## Stage 3 — YC Validation (parallel, all iterations)

| Iteration | Angle | Decision |
|---|---|---|
| I1 | ORIGINAL | Conditional - proceed with validation |
| I2 | PIVOT_B2B | NO_GO |
| I3 | PIVOT_WEDGE | {'decision': 'GO with caution', 'reasoning': 'El composite de 5.05 indica potencial pero con riesgos significativos. La tracción inicial y el dolor alto justifican continuar, pero se requieren milestones claros para avanzar.'} |

**Winner: I3 — PIVOT_WEDGE**

> ContaBot se enfoca en bodegas limeñas que emiten más de 50 facturas electrónicas al mes. Estos negocios facturan montos pequeños (S/50k-100k/año), pero el propietario no tiene tiempo ni conocimiento contable. Actualmente pagan S/200-300 a un contador freelance que suele fallar en las presentaciones, resultando en multas de S/300-500. ContaBot automatiza completamente el proceso: extrae facturas del portal SUNAT, categoriza con IA entrenada en reglas tributarias peruanas, genera el PDT 621 y lo envía, sin intervención del usuario. El dueño solo paga S/79/mes y recibe confirmación de todo en regla. Validamos en 30 días ofreciendo a 10 bodegas una prueba gratuita y midiendo su disposición a pagar al final del mes.

Decision: **{'decision': 'GO with caution', 'reasoning': 'El composite de 5.05 indica potencial pero con riesgos significativos. La tracción inicial y el dolor alto justifican continuar, pero se requieren milestones claros para avanzar.'}**



### Friedman Questions
| Criterion | Score | Note |
|---|---:|---|
| Founder-market fit | 5 | No se detalla experiencia del founder, pero la validación con 10 bodegas sugiere conocimiento tácito. |
| Market size | 6 | Mercado de bodegas en Lima es grande (~50k+), pero ARPU bajo (S/79/mes). TAM estimado <$50M. |
| Problem acuity | 9 | Multas de S/300-500 vs. precio del servicio S/79; dolor alto y recurrente. |
| Competition | 7 | Existen contadores humanos y software tipo Alegra, pero no un servicio totalmente automatizado y gestionado para microempresas. |
| Personal pull | 7 | El founder parece motivado, invirtió tiempo en construir la solución y validar. |
| Recently possible or necessary | 8 | Obligación SUNAT de facturación electrónica y PDT + madurez de APIs e IA hacen posible la automatización. |
| Successful proxies | 6 | Existen SaaS contables exitosos, pero enfocados en PYMES más grandes; el nicho micro no tiene un líder claro. |
| Years-long commitment | 8 | El mercado requiere persistencia; se asume compromiso del founder. |
| Scalability | 7 | Producto de software escalable, pero la adquisición de muchos clientes de bajo ticket requiere canales eficientes. |
| Good idea space | 8 | Automatización de contabilidad para microempresas es una oportunidad clara y poco explotada. |

### YC Rules
| Criterion | Score | Note |
|---|---:|---|
| Do not wait for the perfect idea | 9 | Ya iniciaron con 10 bodegas en prueba gratuita. |
| Burn the boats | 8 | Enfoque en una sola idea; no hay evidencia de dispersión. |
| Go deep into customer workflow | 9 | Integración con SUNAT y automatización completa del proceso contable. |
| Build at the edge of AI | 7 | Usa IA para categorizar gastos, pero la diferenciación principal es la automatización del flujo. |
| Sell outcomes, not tools | 8 | Venden tranquilidad y cumplimiento sin multas, no solo un software. |
| Choose ambitious scope | 6 | Se limitan a bodegas limeñas; podrían expandirse a otros microempresas. |
| Treat failure as structured data | 7 | El piloto de 30 días generará datos sobre disposición a pagar y fricciones. |
| Pick low-trust, high-expertise markets | 7 | Contabilidad para microempresas requiere confianza y conocimiento tributario; la automatización lo reemplaza. |
| The process is the product | 9 | El proceso automatizado de principio a fin es el producto mismo. |
| Avoid early-demand trap | 6 | Prueba gratuita puede generar señales falsas; falta medir pago real. |
| Price per unit or result | 5 | Precio fijo mensual, no atado al resultado o volumen de facturas. |
| Obsess over COGS | 8 | Bajo costo marginal por cliente al ser software; las APIs SUNAT son gratuitas. |
| Do not bolt AI onto legacy | 8 | Construido desde cero para automatización, no añadido a un proceso manual. |
| Cover domain, model, and operations fluency | 8 | Conocimiento de normativa peruana, modelo de IA y operaciones de extracción de datos. |

### VC Hard-Screening Rubric (venture-capital-intelligence)
| Dimension | Weight | Score | Weighted | Rationale |
|---|---:|---:|---:|---|
| Team | 25% | 5 | 1.25 | No se proporciona perfil del founder; la ejecución inicial sugiere capacidad pero es insuficiente para ser única. |
| Market | 20% | 4 | 0.8 | TAM limitado (<$50M); ARPU bajo; crecimiento moderado. |
| Product | 15% | 6 | 0.9 | Defensa inicial por integración SUNAT, pero replicable por competidores con recursos. |
| Traction | 15% | 4 | 0.6 | Solo prueba gratuita con 10 negocios; aún no hay ingresos ni conversión validada. |
| Business Model | 10% | 7 | 0.7 | S/79/mes con márgenes altos; LTV:CAC >3x posible si retención es buena. |
| Competition | 8% | 5 | 0.4 | Alegra/QuickBooks pueden bajar al nicho; contadores freelance compiten en precio. |
| Financials | 5% | 6 | 0.3 | No se detalla burn; se asume lean, pero riesgo de efectivo en etapa temprana. |
| Risk Profile | 2% | 5 | 0.1 | Alto riesgo regulatorio (cambios SUNAT) y de error automático con consecuencias fiscales. |

**VC Verdict:** DECLINE — composite=5.05 / 10

---

## Overall Score (Stage 3C)
**54/100 — Needs sharper validation**

| Dimension | Points | Max | Note |
|---|---:|---:|---|
| problem_validation | 8 | 15 | Promising only after 5 concrete user interviews prove recent painful behavior. |
| solution_insight | 6 | 10 | Insight needs sharper wording around what existing alternatives miss. |
| market_quality | 7 | 15 | Market sizing is not yet evidenced; compare Peru, LATAM, and USA before choosing focus. |
| competition_moat | 5 | 10 | Moat is weak until workflow data, distribution, or community compounds. |
| business_model_pricing | 6 | 10 | Pricing needs a concrete buyer metric and contribution margin assumptions. |
| go_to_market | 6 | 10 | First 10 users can be founder-led; first 100 and 1,000 need a repeatable channel. |
| traction_or_evidence | 3 | 10 | No traction provided in the input; require interviews, waitlist, pilots, or usage. |
| execution_roadmap | 7 | 10 | A 3/6/12 month roadmap is feasible if the first wedge is narrow. |
| risk_control | 6 | 10 | AI-platform substitution and weak demand are the main risks to control. |

---

## YC Dossier

### One-Liner
We help a specific customer segment solve 'Manejo contable 100% automático para microempresas' through a focused software/AI workflow.

### Problem
- Who Suffers: Define one specific user and one economic buyer. Avoid broad labels like 'everyone' or 'companies'.
- Pain Level: Quantify hours lost, money lost, risk, errors, or missed revenue per month.
- Current Workaround: Identify the real competitor: spreadsheet, WhatsApp, email, manual labor, incumbent, or doing nothing.
- Evidence Needed: At least 5 interviews, screenshots, public data, or workflow artifacts.

### Solution & Insight
- Solution: A narrow workflow that produces an outcome the buyer already values.
- Insight: The likely insight is not 'AI can do it'; it is that a repeated expert workflow can be compressed and standardized.
- Non Stack Note: This dossier intentionally avoids frontend/backend stack because the correct stack changes by idea.

### Why Now
- LLMs and agents can now execute and explain multi-step workflows cheaply.
- Distribution through communities, outbound, and self-serve demos is faster for solo founders.
- Users are more willing to try AI-native tools when the workflow is narrow and auditable.

### Market — Peru / LATAM / USA
Recommended focus: Start where the founder has fastest access to users and evidence; compare Peru, LATAM, and USA before committing.

- **Peru**: Potentially strong for problems with local regulation, Spanish workflows, public data, or underserved SMEs. | TAM: Estimate from national population, firms, households, sector output, or public expenditure. | SAM: Start with reachable cities, industries, institutions, or customer segments where the founder can sell. | SOM 12m: Use a bottom-up estimate: reachable leads x conversion rate x annual contract value. | Sources: INEI microdata and surveys, MEF budget data, BCRP statistics, sector associations, local interviews
- **LATAM**: Attractive if the problem repeats across Spanish-speaking markets and does not require heavy country-by-country integration. | TAM: Estimate from regional sector size, number of firms, workers, students, patients, transactions, or institutions. | SAM: Prioritize countries with similar language, regulation, distribution, and payment behavior. | SOM 12m: Estimate expansion only after proving one repeatable channel in the first country. | Sources: World Bank, IDB, ECLAC/CEPAL, national statistics offices, industry reports
- **USA**: Useful benchmark for market size and competitor density; attractive if willingness to pay is higher and distribution is reachable. | TAM: Estimate from US sector spend, number of businesses, paid seats, transactions, or workflow volume. | SAM: Narrow to a buyer segment the founder can actually reach through outbound, communities, or integrations. | SOM 12m: Use a conservative founder-led sales or self-serve acquisition model. | Sources: US Census, BLS, World Bank, Statista or industry reports, academic papers

Source strategy:
- Use INEI microdata for Peru when the market depends on households, employment, education, health, agriculture, firms, or municipalities.
- Use MEF/BCRP for public budgets, macro indicators, credit, sector output, and Peru-specific economic framing.
- Use World Bank/CEPAL/IDB for LATAM comparables.
- Use papers and industry reports when the market is technical, clinical, educational, or scientific.
- Use bottom-up SOM for the first 12 months; do not rely only on top-down TAM.

### Competition & Moat
- Alternatives To Compare: doing nothing; spreadsheet/manual workflow; horizontal SaaS; incumbent platform; AI assistant
- Moat Candidates: proprietary workflow data; distribution/community; integrations; trust/brand; regulatory or local-domain expertise
- Weak Moat Warning: If Claude/OpenAI can solve the job with a prompt, the startup needs a workflow, data, distribution, or compliance layer.

### Business Model & Pricing
- Model Options: monthly SaaS; usage-based; transaction fee; marketplace take rate; paid pilot; enterprise license
- Pricing Rule: Use no more than 3 plans and tie price to a buyer-visible outcome.
- Contribution Margin: Estimate tokens/API calls, storage, human review, support, and acquisition cost per customer.

### Go-To-Market
- First 10: Founder-led outreach to people with the exact painful workflow.
- First 100: Repeat the channel that produced the first paid or high-intent users.
- First 1000: Add scalable distribution: partnerships, integrations, content, community, marketplace, or PLG.

### Traction / Early Signals
- 5+ interviews with recent pain stories
- waitlist with qualified users
- letters of intent or paid pilots
- prototype usage by real users
- before/after workflow evidence

### Roadmap
- 3 Months: Validate the wedge, ship concierge/prototype workflow, close first paying or high-intent users.
- 6 Months: Productize repeated steps, measure retention, build first repeatable acquisition channel.
- 12 Months: Expand to adjacent workflow or geography after proving retention and willingness to pay.

### Risks & Mitigation
- Risk: Market risk: users like the idea but do not have urgent pain.; Mitigation: Interview around recent behavior and require evidence of money/time/risk.
- Risk: AI substitution risk: Claude, OpenAI, or another foundation-model tool absorbs the feature.; Mitigation: Own workflow data, distribution, integrations, evaluation harnesses, and domain trust beyond the prompt.
- Risk: Execution risk: solo founder overbuilds before validation.; Mitigation: Run concierge tests and kill criteria before building broad product surface area.

### The Ask
- Amount: Define a specific amount or resource ask only after the first validation sprint.
- Use Of Funds: customer discovery; prototype; data acquisition; distribution experiments
- Milestone: Unlock proof that one segment has repeated pain and will pay for the outcome.

### Product — Demo & Architecture
- Demo Url: TODO: deploy a public demo (Streamlit, Vercel, Railway, or Hugging Face Spaces)
- Demo Credentials: TODO: add test user credentials once demo is live
- Main Flow Screenshots: 1. Landing / onboarding screen; 2. Core input form or conversation entry; 3. AI processing / loading state; 4. Result / output screen; 5. Export or share action; 6. Settings or profile (optional)
- Architecture Diagram: Frontend (web/mobile) → API layer (FastAPI / Flask) → Orchestration (agent loop) → LLM API + domain data sources → Database (Postgres / SQLite) → Output / report
- Repo Structure: frontend/  — UI (React / Streamlit / Vue); backend/   — API + agent logic; ai/        — prompts, agents, pipelines; data/      — seed data, validation sets; notebooks/ — exploration and analysis; docs/      — architecture diagram, pitch assets
- Ai Models Used: deepseek-chat — fast, cheap inference for classification and structured extraction; deepseek-reasoner — multi-step reasoning for validation and scoring

### External Research Hooks
- Inei Microdatos: Useful for Peru-specific TAM/SAM evidence from INEI surveys and variable search.
- Paperdl: Useful for finding academic papers when the idea needs scientific, health, education, or technical evidence.

---

## Stage 1 — Current Alternatives
El mercado peruano de microempresas está dominado por contadores humanos (frágiles, caros) y software local que requiere conocimientos contables. La facturación electrónica obligatoria abre oportunidades de automatización, pero ningún competidor ofrece un servicio gestionado de punta a punta a precio ultra bajo. Los sustitutos incluyen incumplimiento (alto riesgo) y BPOs tradicionales (aún más caras). ContaBot apunta al segmento insatisfecho de 200-500 S/ mes que busca cumplimiento sin esfuerzo.

- s1: Contador humano independiente (External Accountant) — Servicio personalizado a S/200-500/mes; confianza y experiencia, pero variable en calidad y sin automatización. Opción dominante en microempresas.
- s2: No hacer nada / incumplimiento (Do-Nothing / Non-Compliance) — Muchos microempresarios ignoran obligaciones o declaran con errores; alto riesgo de multas SUNAT (>S/1,500). Alternativa común por desconocimiento o costo.
- s3: Autogestión con Excel (Manual Spreadsheets) — Uso de plantillas propias o formatos bajados de SUNAT; requiere conocimiento contable y tiempo, propenso a errores.
- s4: Alegra (Cloud Accounting Software) — Plataforma SaaS con facturación electrónica, contabilidad básica y reportes; penetración en Perú. Plan desde ~S/39/mes pero requiere que el usuario categorice y entienda contabilidad.
- s5: Siigo (Cloud Accounting Software) — ERP contable con módulo de facturación, inventario y nómina; presencia en Perú vía alianzas. Enfocado a PYMEs con contador interno o externo.
- s6: ContaPyme (Cloud Accounting Software) — Software 100% peruano, especializado en PYMES; incluye PDT, libros electrónicos y facturación. Requiere aprendizaje y cierta dedicación de la empresa.
- s7: Nubox (Cloud Accounting Software) — Contabilidad simplificada chilena adaptada a Perú; plan PYME ~S/79/mes con facturación ilimitada. Buena UX pero aún requiere intervención humana para conciliaciones complejas.
- s8: QuickBooks + conector SUNAT (Cloud Accounting Software) — Marca global con partner local para integrar facturación electrónica; no cubre PDT automático ni presenta declaraciones sin pasos adicionales. Plan desde ~US$15/mes.
- s9: SAP Business One (Enterprise ERP) — ERP robusto con localización SUNAT; costoso (implementación >US$5,000) y orientado a medianas-grandes, no microempresas.
- s10: Odoo con módulo Perú (Enterprise ERP) — ERP open-source con partner local que adapta contabilidad; flexible pero requiere personalización y mantenimiento técnico, no apto para microempresas sin TI.
- s11: Zoho Books + integración SUNAT (Cloud Accounting Software) — Suite global con API abierta; terceros han creado puentes para facturación peruana. Poco conocido en Perú y sin PDT integrado de fábrica.
- s12: SmartConexa (Peruvian Fintech) — Plataforma peruana de facturación electrónica y gestión de comprobantes; integración con SUNAT pero no reemplaza al contador. Plan desde S/19/mes solo facturación.
- s13: Portal SUNAT (facturador gratuito) (Free Government Tool) — Emisión de facturas electrónicas sin costo; no ofrece contabilidad, categorización ni generación de PDT. Solución complementaria, siempre necesitará un contador.
- s14: BPO contable local (outsourcing) (BPO Accounting Services) — Empresas de servicios contables que asignan un contador al negocio; precios desde S/150/mes, proceso manual con algo de software. Suelen atender varias PYMES con un contador.
- s15: Contabilium (Latam) (Cloud Accounting Software) — Startup argentina con expansión a Perú; promete contabilidad automática pero aún necesita categorización manual del usuario. Plan desde ~US$20/mes.

### Competitor Signal Scores (deal-sourcing-signals taxonomy)
| Competitor | Hiring | Funding | Product | Team | Market | Tech | Score | Class |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Alegra | 7 | 8 | 8 | 7 | 8 | 6 | 75.0 | MOVE_FAST |
| Siigo | 6 | 9 | 7 | 7 | 7 | 5 | 71.5 | MOVE_FAST |
| ContaPyme | 4 | 3 | 6 | 5 | 6 | 4 | 45.0 | ENGAGE |
| Nubox | 5 | 6 | 7 | 6 | 5 | 5 | 58.0 | MOVE_FAST |
| QuickBooks | 8 | 10 | 6 | 8 | 5 | 8 | 78.0 | MOVE_FAST |

## Stage 2 — Market Gaps
Recommended gap: g1

- g1: Manejo contable 100% automático para microempresas | Pain: 9 | Evidence: Disposición a pagar S/80/mes, viabilidad de integración con APIs SUNAT en producción, precisión del sistema en un piloto con 30 empresas.
- g2: Solución ultrabarata para nanonegocios (ventas < S/100k/año) | Pain: 8 | Evidence: Tamaño real del segmento (número de microempresas con ventas menores a S/100k), sensibilidad al precio (S/50-80 vs S/80-120), canales de adquisición eficientes (ej. asociaciones de bodegueros, ferias).
- g3: Categorización automática de gastos con reglas tributarias peruanas | Pain: 7 | Evidence: Precisión de categorización comparada con un contador senior; disponibilidad de un dataset anonimizado de comprobantes con categorías validadas; contexto legal para hacer reclasificaciones automáticas sin riesgo de revisión.
- g4: Generación y presentación automática del PDT sin intervención manual | Pain: 8 | Evidence: Viabilidad técnica de replicar la lógica del PDT en un sistema automatizado; homologación con SUNAT (consultas vinculantes); pruebas de extremo a extremo con declaraciones pasadas validadas por contadores.
- g5: Blindaje proactivo contra fiscalizaciones SUNAT para microempresas | Pain: 9 | Evidence: Viabilidad legal de ofrecer representación masiva mediante alianzas con estudios boutique; disposición a pagar un adicional (ej. S/20-30/mes) por un seguro de auditoría; procesos para automatizar alertas de riesgo fiscal.
- g6: Onboarding sin fricción para empresarios no contables con interfaz conversacional | Pain: 8 | Evidence: Test de usabilidad con al menos 20 dueños de microempresas (tienda, restaurante, oficio) midiendo tiempo hasta primera declaración correcta, satisfacción y errores comparados con un contador humano; contraste de interfaz conversacional vs formularios tradicionales.

## Selected Gap
**g1: Manejo contable 100% automático para microempresas**

Pain: 9

Why now: SUNAT obliga a facturación electrónica y PDT, y el segmento microempresarial paga entre S/200-500/mes a contadores humanos o incurre en multas. No existe un servicio gestionado de extremo a extremo a bajo costo.

Risk: Competidores SaaS con recursos (Alegra, QuickBooks) podrían replicar el modelo gestionado; cambios normativos repentinos; errores automáticos con impacto fiscal si la tasa de fallo no es cercana a cero.

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
Aggregate: 0.37 / gate=0.6 — WARN

- **P1 End user (target customer)** score=0.4 | Esto suena bien, pero me da miedo que un error automático me genere una multa más grande. Si realmente funciona sin que yo haga nada, me ahorraría tiempo y sustos. | Concern: Mi mayor preocupación es que la IA cometa un error en la categorización o en el envío del PDT, y yo termine con una multa que no pueda reclamar automáticamente. | Need: Necesito ver resultados de un piloto con al menos 10 bodegas similares a la mía, donde hayan tenido cero errores en todo un mes, incluyendo la presentación exitosa del PDT.
- **P10 AI adoption skeptic (conservative professional in Peru)** score=0.3 | La idea parece interesante, pero como profesional conservador en Perú, desconfío profundamente de que una IA pueda reemplazar a un contador para trámites fiscales con tantas multas en juego. Los bodegueros no tienen el conocimiento para verificar los resultados, y un error automático podría ser más costoso que el ahorro mensual. | Concern: El mayor riesgo es que la IA cometa errores en la categorización o en el PDT que el dueño no pueda detectar, resultando en multas mayores a las actuales y una pérdida de confianza total. | Need: Necesito ver un piloto con al menos 30 bodegas durante 3 meses completos donde cada declaración sea auditada de forma independiente por un contador humano y se demuestre una tasa de error cero en las presentaciones.
- **P2 Economic buyer with budget** score=0.6 | The value proposition is compelling: S/79/mo replaces a S/200-300 expense and eliminates fine risk. However, as an economic buyer, I need to be certain the automation is flawless—any error could result in fines that erase savings. | Concern: The accuracy of automated tax filing is critical; a single mistake could cost more than the savings and damage my compliance record. | Need: I need to see results from a pilot of at least 100 bodegas over 3 months with zero filing errors and validated tax payments.
- **P3 Operations / implementation owner** score=0.25 | The concept is appealing for its automation potential, but I'm worried about the dependency on SUNAT's portal and the complexity of reliably extracting and categorizing invoices without manual oversight. Any failure could lead to fines, creating a high support burden. | Concern: The risk of unrecoverable errors in automated PDT submission due to SUNAT API changes or AI misclassification could cause severe compliance penalties, and the support load for debugging such issues is untenable for a small team. | Need: A successful live demo processing invoices from 10 different bodegas over a full month with zero errors or manual interventions, including proof of correct PDT generation and submission confirmation from SUNAT.
- **P4 Incumbent competitor or free substitute** score=0.4 | Automation of tax filings for microenterprises is a clever wedge, but I'm skeptical that a tiny player can achieve the near-zero error rate required for fiscal compliance without massive investment; incumbents like us have the resources to replicate this if it gains traction, but we're not incentivized to cannibalize our existing profitable segments. | Concern: The single mistake in PDT submission could incur fines for the customer, destroying trust and leading to churn; the startup's liability and error handling are unclear. | Need: Show me pilot results with 10 bodegas over 3 months, proving zero errors in PDT submissions and successful handling of edge cases like invoice corrections or SUNAT outages.
- **P5 YC / LATAM VC partner** score=0.35 | ContaBot clearly solves a painful, manual process for micro-businesses in Peru, and your early validation shows some traction. However, the unit economics—$20/month per customer—require a massive customer base to reach $10M ARR, and the market of bodegas in Lima alone may be insufficient without a clear path to broader acquisition. | Concern: The low price point forces you to acquire tens of thousands of customers, but the current validation with 10 bodegas doesn't prove you can scale customer acquisition cost-effectively or that the total addressable market exceeds 100,000 businesses. | Need: Show that you can acquire customers at less than $10 each, ideally through organic or referral channels, and that there are over 100,000 qualifying micro-businesses in Peru with similar needs.
- **P6 Technical builder / CTO** score=0.4 | The automation of SUNAT PDT submissions is technically feasible but high-risk: any parsing or categorization error could lead to fines, eroding trust. COGS for reliable API integration and validation must be far below S/79/mo, which is aggressive. The learning loop is weak because each micro-business has unique, infrequent transactions, limiting model improvement. | Concern: Reliability near 100% is required for tax filings, but the system cannot recover from errors like a human accountant—one mistake could cause legal liability and customer churn. | Need: Demo of the full pipeline processing 10 real bodegas' historical data for an entire month with zero submission errors and validation against SUNAT receipts.
- **P7 Peruvian SME buyer (informal sector)** score=0.3 | La idea suena bien porque sí pierdo plata con las multas y el contador que me falla. Pero no confío en un bot para algo tan crítico como la SUNAT—si se equivoca, pierdo más. Además, pago solo con Yape o Plin, no tengo tarjeta ni quiero más apps complicadas. | Concern: Si el bot se equivoca, la multa me la pongo yo, y eso es peor que lo que tengo ahora. | Need: Muéstrame un video de 3 meses de uso en una bodega real como la mía, sin errores, y déjame probarlo gratis 2 meses antes de pagar un sol.
- **P8 Peru institutional / public buyer (government or university)** score=0.1 | ContaBot targets micro-business owners, not government institutions. Our procurement cycles and budget codes are designed for education, infrastructure, or public services—not individual business accounting tools. Even if the product were useful for a public program, it would require a new procurement process and MINEDU/PRODUCE approval, which takes 6-18 months. | Concern: The product has no place in any existing budget code used by UGELs or universities; it would require creating a new line item, which is nearly impossible given zero discretionary budget. | Need: Show me a documented case where a public institution in Peru has procured a similar micro-business accounting tool within an existing budget category, or demonstrate that ContaBot can be bundled into a larger existing public program (e.g., 'Fondo MYPE' or 'Impulsa Perú').
- **P9 Peruvian Series A investor (local VC or family office)** score=0.6 | I see a clear pain point and initial validation, but the US$20/month price point and the need for thousands of customers to reach $1M ARR raise red flags about scalability and unit economics. The path to an international co-investor is unclear without a clear expansion model beyond Peru. | Concern: The low price point (S/79/mo) combined with high customer acquisition costs and potential support overhead makes it difficult to achieve sustainable unit economics needed for a VC-backable business. | Need: Show a paid pilot of at least 100 customers over 3 months with a churn rate below 5% and customer acquisition cost below S/100 (1.3 months of revenue).



### Simulation Consensus
- Strongest signal: Proceed only if target users describe a recent, repeated, expensive problem in their own words.
- Weakest assumption: Simulation scores are LLM estimates; live interviews must confirm.
- Adoption path: Start with a narrow concierge workflow, then productize the repeated steps.
- Pricing test: Ask for a small paid pilot tied to the buyer's success metric.
- Decision pressure: {'decision': 'GO with caution', 'reasoning': 'El composite de 5.05 indica potencial pero con riesgos significativos. La tracción inicial y el dolor alto justifican continuar, pero se requieren milestones claros para avanzar.'}

### Recommended Interventions
- Narrow the customer segment until the end user and buyer are obvious.
- Run interviews around recent behavior, not opinions about the idea.
- Prototype the outcome manually before building a scalable product.
- Track what data or workflow insight compounds with each use.

---

## Next Experiments
- Finalizar el piloto de 30 días con las 10 bodegas y medir cuántas están dispuestas a pagar S/79/mes.
- Si <5 pagan, entrevistar a los que no para entender barreras (precio, confianza, funcionalidad).
- Ampliar piloto a 30 bodegas, midiendo precisión del sistema y satisfacción.
- Probar un esquema de precios basado en resultados (ej. % de multas evitadas) vs. tarifa fija.

## Kill Criteria
- Menos del 30% de los pilotos dispuestos a pagar después de la prueba gratuita.
- Tasa de error del sistema >5% en la clasificación de facturas o generación de PDT.
- Imposibilidad de escalar la extracción de datos de SUNAT por limitaciones técnicas o legales.
- Aparición de un competidor directo con financiamiento que ofrezca servicio gratuito o más barato.
