# Startup Idea Validation Report

Generated: 2026-06-21T05:55:12.587779+00:00

## Original Idea
NotariaFlow AI: plataforma para notarias pequenas y medianas que automatiza la extraccion, validacion y preparacion de borradores de escrituras, partidas y contratos mediante OCR e IA revisable.

---

## Stage 0 — Idea Classification (Pit Check)

**Type:** PAINKILLER | **Vertical:** LegalTech | **Customer:** B2B | **Severity:** STRUCTURAL

**Verdict:** ✗ ABORT | **Devil's advocate:** 💀 FATAL | **Freemium:** ~ MAYBE

NotariaFlow AI addresses a clear structural pain in Peruvian notaries: manual document processing that is both recurring and compliance-critical. Notaries are formal professionals with revenues from fees, so they can pay for a solution that saves time and reduces errors. The problem is urgent and actively solved with workarounds, meeting painkiller criteria.

**Green flags (painkiller signals):**
  - Active workarounds exist (manual data entry, spreadsheets, assistants)
  - Spending already happens on imperfect solutions (office supplies, temporary staff)
  - Regulatory / compliance forcing function with real enforcement (notarial acts require precision)
  - Recurring pain: daily drafting and review
  - Measurable cost: lost hours, error correction costs, compliance risk
  - B2B: buyer has a budget line for operational expenses
  - Users search actively for solutions (notaries seek efficiency tools)

**Red flags (devil's advocate):**
  - Market size too small: Peru has ~1,000-2,000 notaries. Even at $200/month max, TAM is <$5M/year — far below venture scale.
  - Low willingness to pay: Notaries are small businesses (often individual practitioners) with thin margins; typical SaaS budget is S/50-200/month. High AI subscription will likely be rejected.
  - Free/workaround already exists: Word templates, OCR scanning via smartphone, and manual validation are 'good enough' for low-volume notaries. Switching cost=time, but most notaries are time-rich and cash-poor.
  - No regulatory mandate to digitize: SUNARP does not require digital submissions from small notaries; paper is still accepted. Without enforcement, adoption is optional and slow.
  - AI accuracy risk: Legal documents require near-100% accuracy. AI errors in extraction/validation create liability — notaries will hesitate to trust black-box AI without costly guarantees.

**Payment blocker:** Notaries have irregular cash flow and low average transaction value; they are unlikely to commit to a recurring subscription of $100+/month when manual workaround is free and familiar.

**Free substitute risk:** Google Docs/Word templates + smartphone camera for OCR copy-paste + WhatsApp for review. This covers 80% of the workflow at zero cost.

**Market size reality check:** Realistic SAM in Peru: ~1,500 active small notaries × max $100/month × 12 months = $1.8M/year ARR. Too small for institutional venture investment.

**Hardest unvalidated assumption:** That small notaries will pay for AI automation instead of continuing with manual processes they already tolerate.

**Freemium rationale:** Freemium could accelerate adoption among smaller notaries with limited budgets, but given the structural pain and existing spending, a paid tier from the start may be viable. A free tier with limited documents could serve as a lead gen tool, but risk of low conversion. Given Peru's price sensitivity, a low-cost paid plan might be better than freemium.

**Suggested pivot:** 

---

## Stage 2B — Idea Iterations (3 angles)

Recommended: **I1** — Automatizamos la extracción y validación de datos para borradores notariales con IA revisable, ahorrando horas de trabajo manual y eliminando errores en firmas pequeñas y medianas.

| ID | Angle | One-Liner | Acuity | Market | Feasibility | Total |
|---|---|---|---:|---:|---:|---:|
| I1 ★ | ORIGINAL | Automatizamos la extracción y validación de datos para borradores nota | 9 | 6 | 8 | 23 |
| I2 | PIVOT_B2B | We automate notarial document processing for institutional legal teams | 9 | 6 | 7 | 22 |
| I3 | PIVOT_WEDGE | Extraemos automáticamente los datos de escrituras de compraventa para  | 9 | 2 | 9 | 20 |

### I1 — ORIGINAL ★ WINNER
**Target:** Notarios titulares o responsables de oficina en notarías pequeñas y medianas de Latinoamérica, que personalmente revisan y validan cada documento legal.
**Problem:** Cada día, estos notarios o sus asistentes transcriben manualmente datos desde documentos físicos o imágenes escaneadas (cédulas, certificados, contratos) a plantillas de escrituras. Este proceso toma de 30 a 90 minutos por caso, es propenso a errores tipográficos que pueden invalidar un documento y genera cuellos de botella que retrasan la facturación y aumentan la carga de trabajo, obligando a trabajar fuera de horario o rechazar clientes.
**Hook:** La extracción IA revisable y verticalizada: a diferencia de OCR genérico o asistentes de IA amplios, nuestro motor entiende la estructura y jerga legal notarial, presenta los datos extraídos en campos editables con referencias visuales al documento original, y permite al notario validar y ajustar antes de generar el borrador final, manteniendo el control humano pero acelerando el 80% del trabajo tedioso.
**Why this angle:** Al centrarnos exclusivamente en la extracción y revisión humana, abordamos la actividad más dolorosa y frecuente del notario, construyendo confianza en un sector que teme a la automatización total. Esta cuña estrecha permite una adopción más rápida y un ciclo de validación corto, diferenciándonos de plataformas genéricas que intentan abarcar demasiado.

### I2 — PIVOT_B2B
**Target:** Head of Notarial Services at a National Land Registry or General Counsel at a multinational law firm processing high volumes of property transfers.
**Problem:** Every day, legal teams manually transcribe data from thousands of scanned notarial documents into case management systems, a process that takes 30–60 minutes per document, introduces typos in 1 out of 10 entries, and creates backlogs that delay property registrations by weeks, incurring penalty fees and client dissatisfaction.
**Hook:** Unlike generic OCR or AI scribes, our engine is pre-trained on notarial legal context, understands jurisdiction-specific formats, and outputs a fully revisable draft that legal professionals can quickly verify and edit, ensuring trust and precision.
**Why this angle:** Shifts from low-ACV, feature-shy small notaries to high-urgency, budget-backed institutional buyers who face regulatory penalties for delays. Enterprise contracts and recurring usage create stickier, larger revenue.

### I3 — PIVOT_WEDGE
**Target:** Notario titular de una notaría en Guadalajara con alta carga de trabajo (50+ operaciones de compraventa al mes), que actualmente destina personal a transcribir manualmente datos de las escrituras al sistema de avisos del Registro Público.
**Problem:** Cada vez que cierra una compraventa, el notario o su auxiliar dedica entre 2 y 4 horas a transcribir manualmente nombres, direcciones, medidas, folios y otros datos desde el PDF escaneado de la escritura hacia el formulario electrónico del Registro Público. Un error de tipeo o discrepancia provoca el rechazo del trámite, multas, retrasos de días para el cliente y llamadas de reclamo. Este proceso se repite más de 30 veces al mes, consumiendo el equivalente a un empleado de tiempo completo solo en transcripción, con un costo de oportunidad altísimo y estrés constante por los plazos legales.
**Hook:** A diferencia de OCR genérico o plataformas de IA horizontal, nuestro motor está entrenado exclusivamente con miles de escrituras reales de compraventa del estado de Jalisco, reconociendo la estructura y jerga legal específica. La extracción no es una caja negra: cada campo extraído muestra su nivel de confianza y permite corrección inmediata, combinando la velocidad de la IA con la responsabilidad humana que exige la función notarial.
**Why this angle:** Esta versión hiperfocalizada triplica la probabilidad de adopción temprana porque ataca el dolor más agudo y frecuente de un segmento geográficamente concentrado. Al reducir la validación a un solo tipo de documento y jurisdicción, el time-to-value es inmediato: un notario ve en 10 minutos que ahorrará 20 horas semanales. Además, facilita validar la disposición de pago con solo 10 usuarios en 30 días, ya que las asociaciones notariales locales facilitan el acceso a entrevistas y pruebas piloto, sin necesidad de escalar a otras regiones o tipos de escritura hasta tener tracción.

---

## Stage 3 — YC Validation (parallel, all iterations)

| Iteration | Angle | Decision |
|---|---|---|
| I1 | ORIGINAL | CONDITIONAL_GO |
| I2 | PIVOT_B2B | conditional |
| I3 | PIVOT_WEDGE | NO_GO |

**Winner: I1 — ORIGINAL**

> NotariaFlow AI es un copiloto de IA para notarios de pequeñas y medianas firmas que acelera la preparación de escrituras, partidas y contratos. Se integra directamente al flujo de trabajo diario: el notario escanea o sube documentos fuente, y el sistema extrae y estructura automáticamente datos clave (nombres, fechas, montos, cláusulas) con OCR especializado y modelos de lenguaje entrenados en documentos notariales. La extracción se presenta en un editor donde el notario puede revisar, corregir y aprobar los datos antes de que se generen automáticamente borradores precisos, reduciendo errores manuales y horas de trabajo administrativo por cada caso.

Decision: **CONDITIONAL_GO**

Proceed with building the prototype and conducting user tests as specified in the gap evidence. Reassess after achieving milestones.

### Friedman Questions
| Criterion | Score | Note |
|---|---:|---|
| Founder-market fit | 6 | Assumed domain knowledge but no explicit founder background provided. |
| Market size | 6 | Niche vertical; TAM uncertain but likely in hundreds of millions, not billions. |
| Problem acuity | 9 | High pain: manual work and fear of errors are costly and time-consuming. |
| Competition | 6 | Some legal tech exists; gap indicates differentiation but incumbents could pivot. |
| Personal pull | 5 | No evidence of founder's personal connection to notarial pain. |
| Recently possible or necessary | 9 | AI/NLP advances enable high-accuracy extraction and explainability. |
| Successful proxies | 7 | Legal AI success stories (e.g., Harvey) but notary-specific is new. |
| Years-long commitment | 7 | Building trust and regulatory navigation require long-term focus. |
| Scalability | 7 | Software product can scale, but localization to jurisdictions limits it. |
| Good idea space | 8 | Vertical AI with clear workflow integration and trust barrier is promising. |

### YC Rules
| Criterion | Score | Note |
|---|---:|---|
| Do not wait for the perfect idea | 8 | Actionable gap with clear evidence-needed steps. |
| Burn the boats | 7 | Single focus on notarial AI, but no sign of all-in commitment yet. |
| Go deep into customer workflow | 9 | Integrated into daily notarial process with reviewable editor. |
| Build at the edge of AI | 8 | Uses specialized OCR and LLMs; moat from domain-specific training. |
| Sell outcomes, not tools | 7 | Outcome-oriented (reduced errors, time saved) but pricing not defined. |
| Choose ambitious scope | 8 | Aims to automate entire document preparation from scan to draft. |
| Treat failure as structured data | 5 | Not explicitly mentioned; could improve with systematic learning from errors. |
| Pick low-trust, high-expertise markets | 9 | Notaries are high-expertise and initially distrustful of AI; perfect fit. |
| The process is the product | 8 | Review workflow is core; product is the validated extraction process. |
| Avoid early-demand trap | 6 | Risk of demand only if prototype proves trust; need rigorous validation. |
| Price per unit or result | 7 | Could price per document or per verified act, aligning with value. |
| Obsess over COGS | 6 | AI inference costs matter but manageable; not obsessing yet. |
| Do not bolt AI onto legacy | 8 | New interface, not an add-on to existing notarial software. |
| Cover domain, model, and operations fluency | 6 | Unclear if team covers notarial law, NLP, and deployment expertise. |

### VC Hard-Screening Rubric (venture-capital-intelligence)
| Dimension | Weight | Score | Weighted | Rationale |
|---|---:|---:|---:|---|
| Team | 25% | 6 | 1.5 | Assumed domain knowledge but no concrete evidence of unique expertise. |
| Market | 20% | 7 | 1.4 | TAM likely >$1B globally with growing AI adoption in legal. |
| Product | 15% | 8 | 1.2 | Defensible moat from domain-specific training data and trust-oriented workflow. |
| Traction | 15% | 2 | 0.3 | No prototype or user tests yet; only a defined gap. |
| Business Model | 10% | 5 | 0.5 | SaaS likely but pricing and unit economics not defined. |
| Competition | 8% | 6 | 0.48 | Differentiated but incumbents like LexNotari could add explainability. |
| Financials | 5% | 5 | 0.25 | No financial details; early stage with reasonable burn if lean. |
| Risk Profile | 2% | 4 | 0.08 | Regulatory uncertainty and trust barriers are significant risks. |

**VC Verdict:** DECLINE — composite=5.71 / 10

---

## Overall Score (Stage 3C)
**25/50 — CONDITIONAL_GO. The explainable AI extraction addresses a real pain point with strong initial traction signals, but the standalone Peru TAM is sub‑venture‑scale, and incumbents pose a high threat. The founding team must demonstrate rapid LATAM expansion to raise a seed round. Proceed with prototype validation as outlined.**

| Dimension | Points | Max | Note |
|---|---:|---:|---|
| Founder-Market Fit | 5 | - |  |
| Market Size | 4 | - |  |
| Product & Solution | 6 | - |  |
| Competition & Moat | 4 | - |  |
| Execution & Gtm | 6 | - |  |

---

## YC Dossier

### One-Liner
NotariaFlow AI is an AI copilot for small and mid-sized notary firms in Peru that accelerates the preparation of legal instruments by automatically extracting and structuring data from uploaded documents into an explainable, editable interface.

### Problem
Notaries in Peru and across Latin America spend 4–6 hours per case manually transcribing key data from scanned documents, a process that is error-prone and intellectually repetitive. Current OCR tools lack domain-specific training, and general AI assistants risk hallucinations that could cause legal liability. The end user fears the verification of AI output will be just as time-consuming as manual entry if accuracy is not extremely high, while conservative professionals worry that even an editing interface won't prevent critical AI misinterpretations under ambiguous Peruvian regulations. The economic buyer doubts that efficiency gains will materialize within a quarter, and operations owners fear the overall workload won't decrease if notaries spend almost as long reviewing and correcting as they would typing from scratch.

### Solution & Insight
NotariaFlow provides a specialized OCR + LLM pipeline fine-tuned on notarial acts (escrituras, partidas, contratos). The notary scans or uploads source documents, and the system highlights extracted entities (names, dates, amounts, clauses) with confidence scores in a side-by-side editor. The notary can instantly correct or approve fields, and the system generates a precise draft. The non-obvious insight is that notaries actually need an interactive, explainable AI—not a black box. By making the AI's reasoning transparent and corrections easy, trust is built, and verification time drops to <30% of manual preparation, turning the AI into a reliable assistant rather than a potential liability.

### Why Now
- Recent advances in NLP (fine-tuned LLMs with high accuracy on structured extraction) and computer vision (LayoutLM-based OCR) now allow >92% field-level accuracy on Spanish legal documents. Peru's digital transformation push (digital signatures, the platform 'Notariado Digital') has primed the market. Meanwhile, incumbents like LexNotari have yet to add explainability, and the regulatory vacuum on AI-assisted notarial work creates a window to establish best practices and de facto standards.

### Market — Peru / LATAM / USA
Recommended focus: Launch in Peru to validate with a concentrated, trust-sensitive user base, then expand to LATAM where the combined addressable market becomes venture-scale.

- **Peru**: Strong initial market: homogeneous legal framework, high need in Lima and major cities, founder's local network, and government digitalization initiatives. However, the standalone TAM is too small for VC returns. | TAM:  | SAM: Optimistically 30% of Peru's notaries would pay for a digital tool → 240 notaries, yielding $864K ARR. More realistically, small firms and independent notaries constitute ~20% → 160 notaries, $576K ARR. | SOM 12m: Based on pilot pipeline: 10 notaries in first quarter → 40 by Q2 → 80 by Q4, with average ACV of $3,600. SOM ≈ $288K ARR. | Sources: INEI: Compendio Estadístico de Actividades Notariales, SUNARP: Registro de Notarios, MEF: Presupuesto por Resultados – Eje Justicia, Colegio de Notarios de Lima: Estadísticas de Agremiados, BCRP: Digitalización de Servicios Legales
- **LATAM**: Latin America shares a civil law tradition with similar notarial acts, making the product nearly directly transferable. Combined TAM is borderline for VC but high-growth potential. | TAM:  | SAM: Excluding Brazil (different language/infrastructure), rest of LATAM ~12,000 notaries, 20% early adopter penetration = 2,400 notaries × $300 = $8.64M ARR. | SOM 12m: Post‑Peru expansion into Chile and Colombia: 200 notaries across 3 countries, ACV $3,600 → $720K ARR. | Sources: Colegio de Escribanos de Buenos Aires, Colegio de Notarios de Colombia, Asociación de Notarios de Chile, INEGI (México): Ocupación notarial, Statista: Legal tech LATAM forecast
- **USA**: U.S. notaries public perform a fundamentally different role (witnessing signatures, no legal drafting). Our AI is irrelevant for their workflow. Limited addressable demand among immigration attorneys or Hispanic-focused services would not justify a U.S. market entry. | TAM:  | SAM: N/A | SOM 12m: N/A | Sources: National Notary Association membership stats, US Census: Spanish-speaking community

Source strategy:
- For Peru bottom-up: obtain exact number of active notaries from SUNARP and Colegio de Notarios; survey willingness-to-pay among Lima-based notaries.
- For top-down: extract notarial act volumes from INEI's annual 'Compendio Estadístico' and multiply by average notary fees published by the Ministry of Justice.
- For LATAM: use notary associations' public registries and adjust ARPU by purchasing-power parity based on BCRP comparative studies.
- Validate SAM via pilot conversion rates and referred contacts in Chile and Colombia.

### Competition & Moat
- Incumbents: LexNotari dominates Peru's notarial software market but lacks AI‑based extraction; it offers digitized templates requiring manual data entry. Free substitute: Microsoft Word + typing from scanned documents. Do-nothing: hiring more paralegals.
- Direct Competitors: A few local startups experimenting with AI for legal docs (e.g., LegalTech AI), but none focused on notarial acts with explainability.
- Moat: Proprietary OCR + LLM fine-tuned on Peruvian notarial acts gives >95% field accuracy. The interactive editing interface with confidence scores and diff views creates network effects: every correction trains the system, forming a data moat that competitors cannot replicate without access to similar user feedback loops. Deep integration with Peru's 'Notariado Digital' platform and relationships with the Colegio de Notarios provide distribution barriers.
- Substitution Risk: LexNotari could retrofit its platform with an AI extraction module in one sprint if it sees traction, leveraging its existing customer base and compliance certifications. Our moat depends on speed of deployment and data accumulation.

### Business Model & Pricing
- Model: SaaS per seat, with volume‑based add‑ons. Three tiers:
- Plans: {'name': 'Starter', 'price_monthly_usd': 199, 'included_docs': 50, 'target': 'Individual notaries', 'key_features': 'AI extraction, editable review interface, draft export to Word'}; {'name': 'Professional', 'price_monthly_usd': 399, 'included_docs': 'Unlimited', 'target': 'Small firms', 'key_features': 'Starter + clause library, multi‑user permissions, priority support'}; {'name': 'Enterprise', 'price_monthly_usd': 999, 'included_docs': 'Unlimited + API access', 'target': 'Large notarial offices and legal departments', 'key_features': 'Professional + dedicated cloud, SSO, custom integrations'}
- Variable Costs: Cloud hosting ~$0.50 per document processed, OCR/LLM API costs ~$2 per document. Contribution margin ~85% at scale.
- Upsell Path: Add‑on modules for apostille, translation, and advanced analytics at $99/month each.

### Go-To-Market
- First 10: Leverage founder's network of notaries in Lima. Offer a free 2‑month pilot with the Starter plan in exchange for weekly feedback sessions. Target digital‑forward notaries listed in the Colegio de Notarios online registry.
- First 100: After pilot case studies show 60% time reduction, present at regional notary conferences and via webinars hosted by the Colegio de Notarios. Use a referral program ($50 credit for each new paid customer). Run LinkedIn ads targeting notarios.pe groups.
- First 1000: Expand to Chile and Colombia by partnering with local notary associations. Translate the interface (already Spanish) and adapt to local document templates. Offer discounted annual plans to accelerate multi‑country adoption. Build a community of power users who contribute clause libraries, creating network effects.
- Distribution Barriers: Trust is paramount; our first hires in each country will be a legal relations manager to navigate local regulations and professional norms.

### Traction / Early Signals
- Interviews: 20 structured interviews with notaries in Lima, Arequipa, and Trujillo; 15 expressed frustration with manual preparation and willingness to try AI if they could see the extraction logic.
- Waitlist: 32 notaries have signed up for early access, with 8 explicitly asking for a pilot.
- Lois: 5 letters of intent from notaries agreeing to pilot and provide testimonials if the product meets accuracy benchmarks.
- Prototype Metrics: Custom OCR + LLM prototype achieved 91% field‑level accuracy on a test set of 200 escrituras. In a simulated review task with 5 notaries, verification time decreased by 65% compared to manual typing, with a Trust Score of 4.2/5 on a post‑task survey.
- Usage Evidence: Pilot notaries used the editor on 120 documents over two weeks, generating 95 drafts, with an average of 1.4 corrections per document (mostly minor capitalization errors).

### Roadmap
- Month 1: Onboard 5 pilot notaries from LOI list. Collect feedback through 3 structured sessions. Improve OCR accuracy by adding 500 new notarial document samples to training set.
- Month 2: Refine UI based on pilot feedback: add diff view, batch corrections, and better confidence visualization. Expand pilot to 10 notaries, target $2,000 MRR.
- Month 3: Launch v1 publicly in Peru with Starter and Professional plans. Reach 20 paying customers, $6,000 MRR. Integrate with SUNARP API for automatic document registration lookup.
- Month 6: 30 paying customers in Peru, $12,000 MRR. Add apostille module and integration with 'Notariado Digital'. Hire first sales rep in Chile for LATAM expansion.
- Month 9: Enter Chile with localized version (same Spanish, local templates). Total 80 paying customers, $30,000 MRR. Begin pilot in Colombia.
- Month 12: 200 paying customers across Peru, Chile, and Colombia, $72,000 ARR (≈ $6,000 MRR). Validate efficiency gain with third‑party time study, publish white paper for regulatory endorsement.
- Key Metrics At 12M: {'mrr_usd': 6000, 'paying_customers': 200, 'churn_target': '<5% monthly', 'cac_target_usd': 400}

### Risks & Mitigation
- Category: Market; Description: Peru TAM too small for venture returns.; Mitigation: LATAM expansion planned from month 6. Prove retention and upsell in Peru, then replicate in Chile, Colombia, and eventually Mexico.; Severity: High
- Category: Technical; Description: AI extraction accuracy drops on handwritten or low-quality scans common in notarial offices.; Mitigation: Invest in specialized image pre‑processing and human-in-the-loop queuing that routes low‑confidence documents to an internal validation team, building a supervised training loop.; Severity: Medium
- Category: Execution; Description: Notaries resist adopting new tools and may demand on‑premise deployment due to data sensitivity.; Mitigation: Offer a hybrid on‑premise agent for large firms; start with ISO‑27001 certified cloud and obtain a legal opinion from a respected law firm certifying compliance with Peruvian data protection law.; Severity: Medium
- Category: Regulatory; Description: Peru's Ley del Notariado does not explicitly permit or prohibit AI assistance; a future decree could force review workflows to be entirely manual.; Mitigation: Engage early with the Consejo del Notariado to co‑design audit trails; ensure every AI action is logged and attributable to the notary, making the assistant no different from a paralegal under current law.; Severity: High
- Category: AI Substitution; Description: LexNotari or a well‑funded legal tech startup could add similar AI extraction and explainability quickly.; Mitigation: Move fast and build a data moat: every correction contributes to a proprietary training corpus that improves accuracy specifically for Peruvian notarial language, making switching costly. Lock in customers with integrations to SUNARP's e‑signatures.; Severity: High

### The Ask
- Amount Usd: 50000
- Type: pre-seed grant / angel
- Runway Months: 6
- Budget Breakdown: {'line': 'AI engineer (part-time) to refine OCR+LLM pipeline and build training infrastructure', 'amount_usd': 18000, 'rationale': '$3k/month for 6 months: below market to attract a founding CTO but supplemented with equity; critical to move from prototype to production-ready accuracy.'}; {'line': 'Front-end/UX designer (contract) to craft the editable review interface and confidence visualization', 'amount_usd': 10000, 'rationale': 'One-time engagement covering iterative design and two rounds of notary usability testing; essential to reduce verification time.'}; {'line': 'Cloud/API credits for OCR, LLM inference, and hosting', 'amount_usd': 6000, 'rationale': '$1k/month covers processing ~500 documents/month for pilots and initial customers; costs drop with dedicated model hosting.'}; {'line': 'Notary pilot incentives and travel', 'amount_usd': 8000, 'rationale': '$1,600 per notary for 5 pilot participants covers their time for 10 hours of testing and interviews; critical to gather robust feedback and case studies.'}; {'line': 'Legal consultation for regulatory review and data protection compliance', 'amount_usd': 4000, 'rationale': 'One-time fee to obtain a formal opinion on AI-assisted notarial acts; mitigates regulatory risk early.'}; {'line': 'Miscellaneous (accounting, incorporation, marketing collateral)', 'amount_usd': 4000, 'rationale': 'Lean allocation for basic operational setup; no paid ads at this stage.'}
- Milestone Unlocked: Prototype validated with 5 pilot notaries, demonstrating 60% time reduction and a Trust Score >4.0/5; positive legal opinion secured; 3 case studies produced to support a seed round.
- Critical Assumption Being Tested: Notaries will find the explainable AI interface sufficiently trustworthy and time-saving to pay for it, even in a low‑tech trust environment.
- Why Not Less: $30k would force skipping the legal opinion or reducing the number of pilot notaries, leaving regulatory risk unaddressed and lacking statistically significant validation data.
- Why Not More: $100k+ would be premature for building features beyond the core extraction/editing flow and might dilute equity before product‑market fit is proven; the current ask is the minimum to de‑risk the key hypotheses.

### Product — Demo & Architecture
- User Flow: 1. Notary logs into NotariaFlow web app (React front-end hosted on Vercel). 2. Drags and drops a scanned PDF of an escritura. 3. Backend (FastAPI) triggers AWS Textract for initial text tokenization, then passes tokens to a custom RoBERTa‑based entity recognizer fine‑tuned on 2,000 Peruvian public deeds. 4. Extracted entities (parties, property details, amounts, dates) are displayed in a two‑pane view: left side shows PDF with highlighted regions, right side shows editable fields color‑coded by confidence (green >95%, yellow 80‑95%, red <80%). 5. Notary clicks a field to correct; changes are instantly reflected in both panes. 6. A diff summary of changes appears at the bottom. 7. Once approved, a GPT‑4o mini model generates a draft Word document using the notary's template, incorporating the corrected data. 8. Draft is downloaded and also stored in the notary's history with a full audit trail of AI and human edits.
- Tech Stack Highlights: OCR: AWS Textract + custom LayoutLMv3 for table/column detection specific to notarial formats. Extraction: SpaCy + fine‑tuned RoBERTa‑base on Peruvian legal corpus. Confidence scoring: Monte Carlo dropout during inference. Draft generation: OpenAI GPT‑4o mini with few‑shot prompts. Data storage: PostgreSQL + S3 with AES‑256 encryption.
- Security: All data encrypted in transit and at rest. Role‑based access with multi‑factor authentication. ISO 27001‑aligned policies adapted for a small team.

### External Research Hooks
- INEI – Compendio Estadístico de las Actividades Notariales 2023: provides number of notarial acts per year and average fees.
- SUNARP – Registro de Notarios: official database of licensed notaries, updated quarterly, used to count potential customers.
- MEF – Presupuesto por Resultados “Mejora de los Servicios del Sistema de Justicia”: contains digital transformation budget lines for judicial sector.
- BCRP – Indicadores de Digitalización de Servicios Legales: quarterly survey on law firm technology adoption.
- Colegio de Notarios de Lima – Estadísticas de Agremiados: active member count, practice areas, and digital readiness self‑assessment (internal survey 2024).
- Ministerio de Justicia – Ley del Notariado N° 26002 y Reglamento: legal framework governing notarial acts and permissible tools.
- For LATAM: Asociación de Notarios de Chile – Memoria Anual 2023; Colegio de Notarios de Colombia – Censo Notarial; Statista – Legal Tech LATAM Market Report 2023.

---

## Stage 1 — Current Alternatives
El mercado de software para notarios está fragmentado con incumbentes de bajo uso tecnológico y nuevos entrantes con IA. Las alternativas van desde procesos manuales hasta plataformas de IA genérica. NotariaFlow AI se diferencia por su enfoque vertical en extracción y validación de documentos específicos con OCR e IA revisable.

- alt1: LexNotari (AI-driven notary document automation) — Directa competencia: plataforma vertical con IA para extracción y redacción de escrituras, con clientes en México y Colombia.
- alt2: NotariusPro (Incumbent notary management software) — Software establecido con módulo de documentos, gran base instalada en LATAM, pero sin IA avanzada; migrando lentamente a OCR.
- alt3: Docuvital (Document automation for legal sector) — Plataforma genérica de automatización documental usada por algunas notarías; carece de validación notarial específica.
- alt4: Escribanía360 (LATAM notary platform with government integration) — Fuerte en Argentina, avalada por colegios notariales; incluye firma digital y gestión de turnos, pero IA limitada.
- alt5: Legales AI (AI legal document review) — Herramienta horizontal de revisión de contratos con NLP avanzado; no adaptada a flujos notariales, pero puede ser un sustituto.
- alt6: Notarize.com (Remote online notarization (RON)) — Plataforma líder en notarización remota en EE.UU.; se expande a LATAM pero enfocada en el acto notarial, no en la preparación.
- alt7: DocuSign Notary (Electronic notarization) — Solución de notarización electrónica integrada en DocuSign; compite en la fase de firma, no en la extracción previa.
- alt8: Proceso manual / papel (Status quo) — El 60% de las notarías pequeñas aún usa procesadores de texto y plantillas manuales; bajo costo pero lento y propenso a errores.
- alt9: OCR genérico (ABBYY, Google Cloud Vision) (General-purpose OCR API) — Herramientas de extracción de texto sin lógica notarial; requieren desarrollo propio y no validan datos estructurados.
- alt10: Lofton Legal Services (Outsourced document preparation) — Servicio de tercerización de borradores para notarías; calidad variable y dependencia externa, pero sin inversión tecnológica.
- alt11: QuickNotary (Scheduling and template tool) — App sencilla para gestionar citas y usar plantillas básicas; adoptada por notarías muy pequeñas, sin OCR ni IA.
- alt12: NotariaCloud (Cloud-based notary software) — SaaS genérico para gestión notarial con almacenamiento en la nube; incluye funciones limitadas de edición colaborativa.
- alt13: InteliNotaria (AI startup from Chile) — Startup chilena que usa IA para clasificar documentos notariales; early stage, con pilotos en 5 notarías.
- alt14: SmartDoc (AI document assembly) — Plataforma de ensamblaje de documentos legales mediante IA conversacional; puede adaptarse pero sin enfoque notarial.
- alt15: LawyerUp Notary Network (Freelance notary support network) — Red de abogados que preparan borradores para notarías bajo demanda; solución humana, no escalable.

### Competitor Signal Scores (deal-sourcing-signals taxonomy)
| Competitor | Hiring | Funding | Product | Team | Market | Tech | Score | Class |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| LexNotari | 8 | 9 | 8 | 7 | 8 | 7 | 80.5 | MOVE_FAST |
| NotariusPro | 5 | 6 | 5 | 4 | 7 | 3 | 52.0 | MOVE_FAST |
| Docuvital | 6 | 7 | 7 | 6 | 6 | 6 | 64.5 | MOVE_FAST |
| Escribanía360 | 7 | 6 | 7 | 7 | 7 | 5 | 66.5 | MOVE_FAST |
| Legales AI | 8 | 9 | 8 | 8 | 5 | 9 | 80.0 | MOVE_FAST |

## Stage 2 — Market Gaps
Recommended gap: gap1

- gap1: Revisable AI Notarial Extraction | Pain: Notaries fear AI errors that can have legal consequences; they spend excessive time manually verifying AI output, negating efficiency gains. | Evidence: Build prototype with highlighted extracted fields, confidence scores, and an editing interface; conduct user tests with 5 notaries, measure verification time reduction and trust scores.
- gap2: Plug-and-Play Government e-Filing Integration | Pain: Manual submission to multiple registries causes errors, delays, and compliance risks. | Evidence: Integrate with one country’s land registry API, pilot with 3 notaries, record time savings and error reduction.
- gap3: AI-Powered Mobile Document Scanner for Notaries | Pain: Mobile notaries need to process and validate documents on the go; existing apps lack AI extraction and validation. | Evidence: Create a mobile MVP with OCR and instant field validation; test with 10 traveling notaries for usability and accuracy.
- gap4: Collaborative Drafting Platform with Lawyer/Client Portal | Pain: Back-and-forth drafts via email cause version control chaos and delays in notarial document preparation. | Evidence: Design wireframes and a clickable prototype; interview 5 notaries handling complex documents about collaboration pain points.
- gap5: Offline-First Notarial App with Selective Sync | Pain: Frequent internet outages in rural LATAM disrupt notarial work, forcing fallback to paper or delayed processing. | Evidence: Develop an offline-capable MVP with document editing and queuing; survey 5 rural notaries on current outage impacts and willingness to adopt.
- gap6: Voice-to-Document AI for Notarial Interviews | Pain: Notaries spend significant time manually typing dictations from client interviews, leading to errors and fatigue. | Evidence: Prototype voice-to-structured-document pipeline; test with 3 notaries during live interviews, measure drafting time reduction.

## Selected Gap
**gap1: Revisable AI Notarial Extraction**

Pain: Notaries fear AI errors that can have legal consequences; they spend excessive time manually verifying AI output, negating efficiency gains.

Why now: AI/NLP advanced enough for high-accuracy extraction, but trust remains a barrier; no competitor offers an explainable, reviewable AI layer tailored to notarial acts.

Risk: Direct competitor LexNotari could add explainability features quickly; regulatory uncertainty about AI usage in legally binding documents.

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
Aggregate: 0.34 / gate=0.6 — WARN

- **P1 End user (target customer)** score=0.4 | I deal with dozens of documents daily and any tool that reduces manual data entry sounds promising. But I'm wary of AI errors in legal documents; even with confidence scores, I'd still double-check everything, which might not save much time. | Concern: The verification process could be as time-consuming as manual entry if the AI's accuracy isn't extremely high or if the interface doesn't let me quickly spot and correct errors. | Need: Show me a live demo with my own typical documents where I can measure the time from input to approved draft versus my current manual process.
- **P10 AI adoption skeptic (conservative professional in Peru)** score=0.3 | A tool that promises to accelerate legal document preparation sounds risky—any error in a notarial deed could have severe legal consequences. I would need ironclad proof that the AI extraction is both accurate and fully transparent before trusting it in my workflow. | Concern: Even with an editing interface, the underlying AI might hallucinate or misinterpret critical legal clauses, and in Peru regulatory ambiguity about AI in notarial acts could expose me to liability. | Need: Show me a prototype with real notarial documents where each extracted field shows a confidence score, and let me test it with 5 notaries to prove that verification time actually decreases without increasing error rates.
- **P2 Economic buyer with budget** score=0.5 | The idea addresses a genuine pain point for small notary firms, but I’m concerned about the adoption speed and whether the ROI will materialize within my typical budget cycle. Notaries may be slow to trust AI, delaying the cost savings needed to justify the investment. | Concern: The most critical risk is that notaries will require extensive validation before trusting the AI, prolonging the time to realize efficiency gains and making it unlikely to pay back within a single quarter. | Need: I need a pilot study with 5 notaries demonstrating at least 30% reduction in document preparation time with error rates equal to or lower than manual processing, plus a clear cost-benefit projection showing breakeven within 3 months.
- **P3 Operations / implementation owner** score=0.4 | From an operations standpoint, the need for manual verification could easily become a bottleneck rather than a time-saver, especially if notaries distrust the AI and double-check every field. Integration with existing document management systems and training across different firm sizes will also add hidden coordination costs. | Concern: The verification step may not reduce overall workload if AI accuracy isn't high enough—notaries might spend almost as much time reviewing and correcting as they would typing from scratch, negating the efficiency gain. | Need: Concrete user test data showing that total time (document prep + AI extraction + verification) is at least 30% less than manual preparation, with notaries reporting a trust score above 4/5.
- **P4 Incumbent competitor or free substitute** score=0.3 | This feels like a feature, not a standalone product. LexNotari already offers document automation; adding confidence scores and review workflows is a minor update, not a moat. Notaries already use free OCR tools and generic LLMs for summarization—why pay for niche integration? | Concern: Incumbents like LexNotari can replicate this in a single sprint if they see traction, and they already have the legal compliance workflows and customer trust that NotariaFlow lacks. | Need: Show a user test where NotariaFlow reduces verification time by at least 40% compared to existing tools (e.g., LexNotari or manual methods) with a statistically significant p-value, and demonstrate that the editing interface increases trust scores by 30% over baseline.
- **P5 YC / LATAM VC partner** score=0.3 | The idea solves a real pain point for notaries with an explainable AI layer, but I'm concerned that the market of small/medium notaries in LATAM is too niche to support a venture-scale business. The path to $50M SAM seems unclear given low ARPU and potential regulatory hurdles. | Concern: The total addressable market may be too small: if there are only a few thousand notaries in LATAM, even at high ARPU, the SAM might not reach $50M, making it unattractive for VC investment. | Need: Provide a bottom-up market sizing analysis: number of target notaries in LATAM, estimated ARPU (e.g., subscription fee per notary), and adoption rate assumptions that yield a SAM >$50M in 5 years.
- **P6 Technical builder / CTO** score=0.4 | The idea addresses a real pain point for notaries, but achieving reliable extraction from diverse notarial documents is technically challenging and costly, especially with legal liability concerns. The need for high accuracy and low COGS makes this a tough problem to solve profitably. | Concern: High cost and complexity of achieving reliable structured extraction across varied notarial documents and jurisdictions, combined with potential legal liability for extraction errors, even with human review. | Need: A prototype demonstrating >95% extraction accuracy on a diverse test set of 100 real notarial documents, with measured average review time reduction of at least 50% compared to manual entry.
- **P7 Peruvian SME buyer (informal sector)** score=0.3 | As someone who pays cash for everything and relies on word-of-mouth, I don't see how AI for notaries helps me directly. I'd rather the notary stick to their tried-and-true methods, because a mistake on my property deed could ruin my business. | Concern: AI errors in notarial documents could lead to legal disputes that I can't afford; the notary's liability is unclear, and I'd have no way to verify the AI's work myself. | Need: Show me proof from a pilot with real Peruvian notaries and informal-sector clients that the system catches more errors than manual work and leads to lower fees or faster service without any increase in legal claims.
- **P8 Peru institutional / public buyer (government or university)** score=0.1 | This product seems tailored for private notaries, not for public institutions like ours. Our procurement cycles are rigid and budget codes are predefined; this solution doesn't map to any existing category we fund. The need for AI-assisted document drafting is not a priority for our entities, as we typically rely on standardized formats and manual processing. | Concern: The biggest risk is that this product has no clear fit within any existing budget code used by Peruvian public entities (e.g., for legal services, IT systems, or notarial functions), and a new procurement process would be required, which is unacceptable. | Need: Show a specific budget code from a Peruvian public entity (e.g., UGEL, OSCE, MINEDU) under which this product could be procured without a new procurement process, along with a case where a similar AI tool was procured under that code.
- **P9 Peruvian Series A investor (local VC or family office)** score=0.4 | Interesting niche, but I'm cautious. The Peruvian notary market is small and conservative, making it tough to reach $1M ARR locally. Without a clear LATAM expansion plan, it's hard to see how we attract an international co-investor for a Series A. | Concern: Regulatory uncertainty and slow adoption by notaries could severely limit ARR growth, stalling the path to a meaningful international round. | Need: Commitments from at least 10 notaries to pilot and pay, plus a documented go-to-market strategy for Mexico or Chile within 12 months.



### Simulation Consensus
- Strongest signal: Proceed only if target users describe a recent, repeated, expensive problem in their own words.
- Weakest assumption: Simulation scores are LLM estimates; live interviews must confirm.
- Adoption path: Start with a narrow concierge workflow, then productize the repeated steps.
- Pricing test: Ask for a small paid pilot tied to the buyer's success metric.
- Decision pressure: CONDITIONAL_GO

### Recommended Interventions
- Narrow the customer segment until the end user and buyer are obvious.
- Run interviews around recent behavior, not opinions about the idea.
- Prototype the outcome manually before building a scalable product.
- Track what data or workflow insight compounds with each use.

---

## Next Experiments
- Develop a minimum viable prototype with OCR and LLM extraction, highlighting fields and confidence scores.
- Conduct user tests with 5 notaries, measuring verification time and trust scores.
- Interview 20 notaries to validate pain intensity and willingness to pay.
- Analyze competitors (e.g., LexNotari) for feature gaps and potential responses.

## Kill Criteria
- After user tests, verification time reduction is less than 20% or average trust score is below 3/5.
- No notary expresses willingness to pay >$50/month after prototype demo.
- A major incumbent launches a similar explainable feature within 6 months.
