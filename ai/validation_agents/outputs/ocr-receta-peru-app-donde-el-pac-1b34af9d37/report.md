# Startup Idea Validation Report

Generated: 2026-06-21T16:23:22.156630+00:00

## Original Idea
OCR-Receta Peru: app donde el paciente fotografa su receta medica, el sistema extrae los medicamentos via OCR y muestra el generico equivalente mas barato en farmacia cercana por GPS, con modelo de negocio B2B donde farmacias pagan comision por cada cliente derivado.

---

## Stage 0 — Idea Classification (Pit Check)

**Type:** PAINKILLER | **Vertical:** HealthTech | **Customer:** B2B2C | **Severity:** RECURRING

**Verdict:** ⚠ WARN | **Devil's advocate:** ⚠ WEAK | **Freemium:** ✗ NO

Peruvian patients face a recurring financial and health burden from expensive branded medications, with manual workarounds. Pharmacies actively seek customer acquisition channels and are willing to pay per lead. The B2B commission model aligns incentives and fits local payment realities.

**Green flags (painkiller signals):**
  - Active workarounds exist (manual comparison or relying on pharmacy staff)
  - Spending already happens on imperfect solutions (paying more for branded drugs)
  - Recurring pain: every prescription fill
  - Measurable cost: potential savings on generic equivalents

**Red flags (devil's advocate):**
  - Patient behavior change is high: Most patients ask the pharmacist directly for the cheapest option, a free and instantaneous workaround. The app requires downloading, photographing a prescription, and trusting OCR to show prices — a multi-step process that adds friction over the habitual 'just ask' loop.
  - Pharmacy willingness to pay is dubious: In Peru, the pharmacy industry is dominated by large chains (Inkafarma, Mifarma) with thin margins and existing loyalty programs (e.g., Inkafarma's 'Puntos Beneficio'). They are unlikely to pay a commission per customer when they already attract foot traffic. Small bodega pharmacies operate on even tighter margins and see no value in paying for inbound traffic they already have.
  - OCR on handwritten Peruvian prescriptions is unreliable: Prescriptions are often handwritten with varying legibility, using brand names (not generics). The OCR would need to handle Spanish, drug name variations, and dosage errors. Any misread leads to mistrust and abandonment. The technical risk is high and the human-in-the-loop (verification) is costly.

**Payment blocker:** Pharmacies in Peru, especially the small and informal ones that would benefit most from price comparison traffic, rarely have digital payment infrastructure. They operate on cash and basic CCI transfers. Commission collection would require manual invoicing and follow-up, making the unit economics negative for low-value transactions.

**Free substitute risk:** The patient's existing behavior – asking the pharmacy clerk '¿Cuál es el genérico más barato?' – is free, instantaneous, and requires no app. For patients who are extremely price-sensitive, they already comparison-shop between two nearby pharmacies by walking, not using an app.

**Market size reality check:** The real paying market is constrained to formal pharmacy chains (Lima-based) and price-sensitive patients with smartphones. Assuming 5% of Lima's 10M population (500K) might use it, and each referral is worth S/2-5 ($0.5-1.3), the potential annual revenue is < $1M — too small for VC scale without broader LATAM expansion, which requires separate localization for each country's drug databases and pricing.

**Hardest unvalidated assumption:** That patients will adopt a new app to do something they already do for free with less friction (asking the pharmacist), and that pharmacies will pay for leads when they already have high walk-in traffic and thin margins.

**Freemium rationale:** The consumer app is already free; revenue comes from pharmacy commissions per referred customer, so no freemium tier is needed. A free trial for pharmacies (e.g., first leads free) could be part of sales, not a freemium product model.

**Suggested pivot:** 

---

## Stage 2B — Idea Iterations (3 angles)

Recommended: **I2** — We help Peruvian health insurers and self-insured employers slash prescription spending by up to 40% by instantly converting patient prescriptions into the cheapest available generic equivalent at a nearby pharmacy, via OCR and real-time price aggregation.

| ID | Angle | One-Liner | Acuity | Market | Feasibility | Total |
|---|---|---|---:|---:|---:|---:|
| I1 | ORIGINAL | We aggregate real-time generic drug prices and stock across independen | 8 | 7 | 7 | 22 |
| I2 ★ | PIVOT_B2B | We help Peruvian health insurers and self-insured employers slash pres | 9 | 8 | 7 | 24 |
| I3 | PIVOT_WEDGE | We help diabetic patients in Comas find the cheapest monthly diabetes  | 9 | 2 | 9 | 20 |

### I1 — ORIGINAL
**Target:** A 45-year-old diabetic in Lima who spends S/ 200 monthly on metformin and enalapril, and currently visits two or three pharmacies on foot every refill to save S/ 30–50.
**Problem:** Chronic patients in Peru overpay by 40–80% for branded medications because they have no way to compare real-time generic prices and availability without physically visiting multiple pharmacies—a 1–2 hour task they repeat every month, costing time, transport, and mental stress.
**Hook:** Unlike generic price-comparison websites that list outdated reference prices with no stock data, we show live inventory from independent pharmacies and let patients reserve the exact product at the displayed price for guaranteed pickup.
**Why this angle:** Focusing on real-time aggregation for independent pharmacies creates a defensible supply-side network effect and addresses the highest-urgency gap in the market, turning a fragmented pain into a sticky daily habit for patients and a must-have customer acquisition channel for small pharmacies.

### I2 — PIVOT_B2B ★ WINNER
**Target:** Pharmacy Benefits Manager at a Peruvian health insurance company (e.g., Pacífico, Rímac) or HR Director of a large employer with self-funded health benefits, tasked with controlling escalating drug costs but lacking real-time steering tools.
**Problem:** These institutions lose millions annually because patients fill branded prescriptions or don't know where generics are cheaper. Without dynamic, point-of-care guidance, 30–50% of drug claim costs are avoidable overspend—a daily structural drain that forces higher premiums and erodes trust.
**Hook:** The only platform merging real-time, cross-pharmacy generic price aggregation (including independent pharmacies) with instant OCR prescription reading, enabling institutions to automatically steer patients to the lowest-cost option at the moment of need.
**Why this angle:** Selling to institutional payers with budget and urgent cost pressure aligns incentives: they save money, patients save money, and adoption is faster than a commission-based B2B2C model. The recurring SaaS model scales with covered lives, directly tackling a top-priority pain point.

### I3 — PIVOT_WEDGE
**Target:** A 55-year-old diabetic patient in Comas spending S/150 monthly on metformin and insulin, who currently calls or visits 3–4 pharmacies each month to compare prices, losing time and overpaying.
**Problem:** Monthly medication shopping consumes 2–3 hours and S/10–15 in transport, with patients often overpaying by S/30–50 because real-time generic prices are opaque across pharmacies. The annual cost of this friction exceeds S/500, and skipped doses due to high prices pose health risks.
**Hook:** Real-time price and stock aggregation from a curated pharmacy network, delivered via a WhatsApp bot with OCR and integrated payment, reducing a 2-hour chore to a 30-second, money-saving action.
**Why this angle:** By tackling one segment with high-frequency, predictable need and manually onboarding a handful of pharmacies and patients, we can test direct payment willingness and gather undeniable evidence of demand in 30 days, before building scalable infrastructure.

---

## Stage 3 — YC Validation (parallel, all iterations)

| Iteration | Angle | Decision |
|---|---|---|
| I1 | ORIGINAL | NO_GO |
| I2 | PIVOT_B2B | CONDITIONAL_GO |
| I3 | PIVOT_WEDGE | No go |

**Winner: I2 — PIVOT_B2B**

> A B2B platform for Peruvian health insurers, self-insured employers, and government health programs that aggregates real-time generic drug prices and availability across all pharmacy types. When an insured member or employee scans a prescription via OCR, the system instantly identifies the cheapest generic equivalent at a nearby pharmacy, steering the patient there for pickup. The institution pays a per-covered-life or per-transaction fee, cutting prescription benefit costs by up to 40% through redirected adherence, while the end user enjoys lower prices without sacrificing convenience.

Decision: **CONDITIONAL_GO**

Proceed with validation experiments but require founder to prove partnership traction and domain knowledge before committing full resources.

### Friedman Questions
| Criterion | Score | Note |
|---|---:|---|
| Founder-market fit | 6 | No specific founder background provided; assumes healthcare/pharma domain knowledge needed. Without evidence of deep industry ties or prior experience, this is a moderate risk. |
| Market size | 8 | Peru's healthcare spending is significant; generic drug market is large and growing. TAM likely >$1B, but need precise figures. |
| Problem acuity | 9 | Patients actively suffer from high drug costs and inconvenience; insurers want cost reduction. Pain is clear and urgent. |
| Competition | 5 | Local attempts (RecetaFácil) exist but lack scale; GoodRx is US-only. However, pharmacy chains may resist, and independent pharmacies may lack tech capabilities. |
| Personal pull | 7 | Founder likely has personal experience or strong interest; B2B model aligns with institutional buyers. But more evidence needed. |
| Recently possible or necessary | 8 | High smartphone penetration, OCR technology, and real-time API capabilities make this feasible now. GoodRx success validates demand. |
| Successful proxies | 8 | GoodRx is a direct proxy in a different market; similar models in other verticals (e.g., travel aggregators) show this model works. |
| Years-long commitment | 6 | Healthcare partnerships and pharmacy integrations take time; founder needs multi-year commitment. Unclear if that exists. |
| Scalability | 7 | Platform model scales well across Peru and potentially other LatAm countries. But dependency on pharmacy partnerships could slow expansion. |
| Good idea space | 8 | Addresses a real pain with a clear value proposition. Good balance of B2B revenue and consumer benefit. |

### YC Rules
| Criterion | Score | Note |
|---|---:|---|
| Do not wait for the perfect idea | 8 | Idea is actionable; MVP with 3 pharmacies can start immediately. Founder should not over-optimize. |
| Burn the boats | 5 | Unclear if founder is fully committed to this single idea. Need to avoid splitting focus. |
| Go deep into customer workflow | 7 | OCR-based prescription scanning integrates into patient and insurer workflows. But need to fully understand pharmacy and insurer back-end processes. |
| Build at the edge of AI | 6 | OCR is a standard AI application; real-time aggregation is more API integration than cutting-edge AI. Could leverage AI for price prediction, but not core. |
| Sell outcomes, not tools | 9 | Clear outcome: reduce prescription costs by 40%. B2B pricing tied to savings aligns perfectly. |
| Choose ambitious scope | 7 | Aggregating all pharmacy types in Peru is ambitious, but starting with major chains and independents is sensible. |
| Treat failure as structured data | 5 | No evidence of structured experimentation yet. Founder should plan for systematic A/B testing of partnership models. |
| Pick low-trust, high-expertise markets | 8 | Healthcare is low-trust; expertise in pharma supply chain and insurance is critical. This fits. |
| The process is the product | 6 | Operational excellence in data aggregation and partner management is key, but not yet proven. |
| Avoid early-demand trap | 7 | Per-transaction or per-covered-life pricing aligns with usage; avoid upfront commitments until value is proven. |
| Price per unit or result | 9 | Per-covered-life or per-transaction fee directly ties to value. Excellent alignment. |
| Obsess over COGS | 6 | Variable costs include API fees, support, and pharmacy incentives. Need to ensure margins >60% as SaaS-like. |
| Do not bolt AI onto legacy | 7 | OCR and real-time aggregation are new; not bolting AI onto legacy systems. But reliance on existing pharmacy systems may be a challenge. |
| Cover domain, model, and operations fluency | 6 | Requires deep domain knowledge in pharma, insurance, and logistics. Unclear if team has it all. |

### VC Hard-Screening Rubric (venture-capital-intelligence)
| Dimension | Weight | Score | Weighted | Rationale |
|---|---:|---:|---:|---|
| Team | 25% | 6 | 1.5 | No specific team info; but domain expertise in Peruvian healthcare and pharmacy is critical. Without it, execution risk is high. |
| Market | 20% | 8 | 1.6 | TAM likely >$1B (Peru healthcare spend), growing with chronic diseases and generic adoption. Timing is right due to digital transformation. |
| Product | 15% | 7 | 1.05 | Defensible moat comes from real-time data integration across many pharmacies and OCR workflow. But scalable partnerships are hard to replicate. |
| Traction | 15% | 3 | 0.45 | No tangible traction yet; only evidence needed is survey and MVP. Pre-revenue with no letters of intent or pilots. |
| Business Model | 10% | 8 | 0.8 | Per-covered-life or per-transaction fees provide recurring revenue; potential for high margins if variable costs are low. LTV:CAC likely >3x if cost-effective acquisition. |
| Competition | 8% | 5 | 0.4 | Local players like RecetaFácil exist; large chains may build in-house; GoodRx could expand. Need clear differentiation and faster execution. |
| Financials | 5% | 4 | 0.2 | Burn rate unknown; likely need significant funds for partnerships and technology. Assuming 18+ months runway if funding secured. |
| Risk Profile | 2% | 4 | 0.08 | Major risks: pharmacy partner data accuracy, scaling independents, regulatory (drug pricing transparency in Peru). High execution risk. |

**VC Verdict:** CONDITIONAL_PASS — composite=6.08 / 10

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
We help a specific customer segment solve 'Real-time generic price & availability aggregation across all pharmacy types' through a focused software/AI workflow.

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
El mercado peruano de comparación de precios de medicamentos genéricos está fragmentado. Las cadenas grandes dominan con apps propias pero no priorizan el ahorro en genéricos. Existen pocos agregadores independientes y el uso de OCR para recetas es incipiente. La amenaza principal proviene de la propia inercia del paciente (do‑nothing) y de posibles expansiones de startups regionales o gigantes globales como GoodRx.

- sol_1: Inkafarma App (Farmacia de cadena) — App con búsqueda de medicamentos, cupones y geolocalización de sucursales propias; fuerte lealtad de marca.
- sol_2: Mifarma App (Farmacia de cadena) — Similar a Inkafarma, con integración de delivery a domicilio; pertenece al mismo grupo económico.
- sol_3: RecetaFácil (startup peruana) (Agregador de precios con OCR) — App que escanea recetas y compara precios de genéricos en farmacias afiliadas; enfocada en ahorro.
- sol_4: Tu Farma Online (Marketplace de farmacias) — Plataforma web que lista productos de múltiples farmacias; permite comparación limitada de precios, sin OCR.
- sol_5: EsSalud Digital (App de seguro social) — Agendamiento de citas y entrega de medicamentos en farmacias de la red; no compara precios de genéricos.
- sol_6: Búsqueda manual en Google (Workaround digital) — Pacientes buscan el medicamento, opción genérica y llaman a farmacias; ineficiente pero gratuito.
- sol_7: Botica cerca con consulta verbal (Workaround presencial) — Preguntar en la farmacia más cercana por el genérico; dependiente del criterio del dependiente.
- sol_8: GoodRx (potencial expansión) (Agregador global de precios) — Líder en EE.UU. con cupones y comparación de precios; no opera en Perú pero podría ser una amenaza futura.
- sol_9: Lista de precios del MINSA (Iniciativa gubernamental) — Página web con precios de referencia de medicamentos genéricos; poco conocida y difícil de usar móvil.
- sol_10: Plataformas de e-commerce (MercadoLibre/Linio) (Comercio electrónico general) — Venta de medicamentos sin receta y algunos OTC; no validan receta ni orientan a genéricos.
- sol_11: Farmacia Universal App (Cadena de farmacias) — App con promociones y ubicación de tiendas; enfoque en autoservicio, no en asesoría de genéricos.
- sol_12: Doc24 (telemedicina) (Plataforma de salud) — Consultas virtuales, pueden recetar medicamentos; deriva a farmacias aliadas pero sin comparación abierta.
- sol_13: No hacer nada (do‑nothing) (Inacción) — Comprar exactamente la marca de la receta al precio que diga la farmacia, sin buscar alternativas más baratas.
- sol_14: Seguros privados (Rímac, Pacífico) App (App de aseguradora) — Red de farmacias con reembolsos; útil solo para asegurados, no compara precios de genéricos.
- sol_15: RecetApp (startup chilena) (Agregador regional con OCR) — Opera en Chile con OCR de recetas y comparación de precios; potencial entrada a Perú.

### Competitor Signal Scores (deal-sourcing-signals taxonomy)
| Competitor | Hiring | Funding | Product | Team | Market | Tech | Score | Class |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Inkafarma | 7 | 8 | 6 | 7 | 9 | 5 | 71.5 | MOVE_FAST |
| Mifarma | 7 | 8 | 6 | 7 | 9 | 5 | 71.5 | MOVE_FAST |
| RecetaFácil | 4 | 3 | 7 | 5 | 5 | 8 | 48.0 | ENGAGE |
| Tu Farma Online | 3 | 2 | 5 | 4 | 4 | 4 | 34.5 | MONITOR |
| EsSalud Digital | 2 | 5 | 3 | 3 | 6 | 2 | 35.0 | MONITOR |

## Stage 2 — Market Gaps
Recommended gap: gap_1

- gap_1: Real-time generic price & availability aggregation across all pharmacy types | Pain: Patients waste time manually calling or visiting multiple pharmacies to compare generic prices, often settling for higher prices due to lack of real-time, consolidated information. No existing solution combines OCR-based prescription scanning with live inventory and pricing from both chains and independent pharmacies. | Evidence: Survey 100 prescription holders on current price-comparison behaviors and willingness to switch. Build an MVP with 3 pharmacy partners to test real-time data integration feasibility and user satisfaction.
- gap_2: Digital customer acquisition platform for independent pharmacies | Pain: Small independent pharmacies lack digital channels to attract price-sensitive patients, losing potential revenue to large chains that have their own apps. They need a cost-effective way to pay for qualified leads. | Evidence: Interview at least 10 independent pharmacy owners to assess willingness to pay per referral and technical readiness. Run a manual concierge pilot to measure conversion and average order value for referred customers.
- gap_3: Building trust and education on generic drug equivalence | Pain: Many Peruvian patients distrust generic medications, believing they are inferior to brand-name drugs, leading them to overspend. There is no easy, trustworthy source of information at the point of purchase decision. | Evidence: Design a low-fidelity prototype that presents brand-generic comparisons with official equivalences. Test user understanding and trust change with 20 patients, measuring intent to switch to generic.
- gap_4: End-to-end flow from prescription scan to guaranteed pharmacy pickup | Pain: Even after finding a cheaper generic online, patients face uncertainty about stock and face a disconnect between digital discovery and physical purchase. No service offers reservation or hold functionality tied to the scanned prescription. | Evidence: Run a concierge MVP where a team manually contacts pharmacies to reserve, measuring conversion improvement over a control that only shows prices. Gather pharmacy feedback on reservation willingness.
- gap_5: Mobile-friendly access to Minsa’s generic price reference list | Pain: The official governmental list of generic drug prices is difficult to navigate on mobile, leaving patients without a trusted pricing benchmark. An easily accessible, searchable version could empower cost-conscious patients. | Evidence: Check Minsa website traffic from mobile devices. Build a simple progressive web app that scrapes and displays the data; measure usage and user satisfaction in a public beta.
- gap_6: Integration with telemedicine platforms for generic-first prescribing | Pain: Telemedicine consultations often result in brand-name prescriptions without considering patient cost. Neither doctors nor platforms systematically suggest affordable generics, leaving a gap in the care journey. | Evidence: Form a pilot partnership with a small telemedicine provider (e.g., Doc24) to test an API that suggests generics during e-prescribing. Measure prescription fill rates and pharmacy referral conversion.

## Selected Gap
**gap_1: Real-time generic price & availability aggregation across all pharmacy types**

Pain: Patients waste time manually calling or visiting multiple pharmacies to compare generic prices, often settling for higher prices due to lack of real-time, consolidated information. No existing solution combines OCR-based prescription scanning with live inventory and pricing from both chains and independent pharmacies.

Why now: Smartphone adoption in Peru is high, and the success of GoodRx abroad validates the model. Local attempts (RecetaFácil) show early traction but lack scale, leaving a wide gap for a better-executed aggregator.

Risk: Pharmacy partners may not provide accurate real-time data; scaling partnerships across many independents is resource-intensive; large chains may block integration.

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

- **P1 End user (target customer)** score=0.75 | This sounds promising. I often end up paying more for my prescriptions because I don't have time to call around. If this app can show me the best price nearby instantly and I can just pick up, it would save me both time and money. However, I worry about the accuracy of the price data and whether the pharmacies will honor the listed price. | Concern: The biggest concern is that the real-time prices shown in the app may not match the actual price at the pharmacy counter, leading to frustration and distrust. | Need: I need to see a demo or case study where the app accurately matched the price at a pharmacy for a real prescription, with evidence from independent validation or user testimonials.
- **P10 AI adoption skeptic (conservative professional in Peru)** score=0.15 | This idea sounds promising in theory, but I'm deeply skeptical about relying on AI to steer patients to pharmacies based on real-time prices. In Peru, many prescriptions are handwritten and OCR errors could lead to wrong medications, causing serious health risks. Also, independent pharmacies often lack accurate inventory systems, so the data may be unreliable. | Concern: The biggest risk is that OCR or real-time data errors could direct a patient to the wrong pharmacy or medication, potentially causing harm and legal liability, which would destroy trust in the platform. | Need: I need to see a live demo with at least 100 prescriptions (including handwritten ones) showing 99%+ OCR accuracy and real-time price matches verified by phone calls to independent pharmacies.
- **P2 Economic buyer with budget** score=0.4 | The idea of cutting prescription costs by 40% is tantalizing, but I'm wary of integration complexity with Peru's fragmented pharmacy market and the typical slow pace of B2B adoption. Without a proven pilot showing real savings within my budget quarter, I can't justify the procurement friction. | Concern: The risk that pharmacy partners fail to provide reliable real-time data, leading to inconsistent savings and member dissatisfaction, making the ROI unachievable in my budget cycle. | Need: A pilot with at least 3 self-insured employers or a health insurer in Peru showing a 20%+ cost reduction on a defined drug basket within 90 days, with verified data accuracy and member behavior change.
- **P3 Operations / implementation owner** score=0.25 | From an operational standpoint, this platform requires deep integration with a fragmented pharmacy landscape and depends on real-time data accuracy, which is a high-risk execution challenge. The need to onboard and maintain data feeds from both large chains and independent pharmacies introduces significant coordination complexity and ongoing support load. | Concern: Reliability of real-time inventory and pricing data from independent pharmacies, which often lack digital systems, will create frequent data discrepancies that erode trust and increase support tickets. | Need: I need to see a pilot with at least 10 diverse pharmacies (including 5 independents) demonstrating >95% data accuracy over 30 days, and a clear integration plan for scaling without manual intervention.
- **P4 Incumbent competitor or free substitute** score=0.3 | This idea faces a high barrier because large pharmacy chains like Inkafarma or Mifarma hold the data and have no incentive to share it with a platform that could drive customers to cheaper alternatives. They can easily block integration or launch their own app, protecting their margins. | Concern: Pharmacy chains will refuse to provide real-time pricing and inventory data, as it undermines their ability to control customer choices and maintain higher margins. | Need: A signed letter of intent from at least one of the top three pharmacy chains in Peru committing to provide real-time data integration.
- **P5 YC / LATAM VC partner** score=0.55 | The idea addresses a clear pain point with a proven model (GoodRx), but execution in Peru faces significant fragmentation. The B2B angle with insurers is smart, but I'm skeptical about the ability to aggregate real-time data from all pharmacy types, especially independents. The market size could be substantial if they nail partnerships, but the path to $10M ARR requires convincing multiple stakeholders. | Concern: The ability to secure real-time price and inventory data from both large chains and independent pharmacies, given their likely reluctance to share data and the technical complexity of integration. | Need: Signed letters of intent or pilot agreements with at least 2 health insurers and 10 pharmacies (including 3 chains and 7 independents) to prove initial traction and data access feasibility.
- **P6 Technical builder / CTO** score=0.3 | The idea has merit, but the technical hurdles are steep: aggregating real-time data from a fragmented pharmacy market, many without APIs, and handling OCR on Peruvian prescriptions (often handwritten, in Spanish) will require sophisticated engineering. The per-transaction model may not cover COGS unless scale is massive. | Concern: The biggest risk is that pharmacy partners, especially independents, cannot provide reliable real-time pricing and availability data, leading to a poor user experience and high integration maintenance costs. | Need: Show me a live demo of the MVP scanning 10 real prescriptions, each finding the cheapest generic at a nearby pharmacy with confirmed real-time inventory, using data from at least 2 major chains and 5 independent pharmacies.
- **P7 Peruvian SME buyer (informal sector)** score=0.15 | This sounds like a solution for big companies and insurers, not for my small business. I don't offer health insurance to my workers, so it doesn't address my cash flow or operational headaches. I wouldn't pay for something that doesn't directly help me manage costs or risks. | Concern: As an informal business owner, I have zero incentive to pay for a platform that benefits insured employees—I don't provide insurance, and even if my workers have SIS, I won't spend money to reduce their co-pays. | Need: Show me a simple WhatsApp-based painkiller price-check for my personal use that doesn't require me to sign up or pay—prove it saves me soles without any commitment.
- **P8 Peru institutional / public buyer (government or university)** score=0.2 | The idea addresses a real cost-saving opportunity, but as a public buyer, I cannot adopt a new platform without an existing budget code and a streamlined procurement path. The per-covered-life fee model would trigger a new competitive bidding process, delaying implementation by 12+ months. | Concern: This service does not map to any existing budget line item (e.g., 'farmacia' or 'software') and would require a new procurement category, which is incompatible with our zero-discretionary-budget and long-cycle constraints. | Need: Demonstrate that the service can be classified under an existing MINEDU or PRODUCE budget code (e.g., 'Servicios de Información' or 'Adquisición de Software') and that OSCE has approved similar procurement vehicles for comparable platforms.
- **P9 Peruvian Series A investor (local VC or family office)** score=0.35 | The idea tackles a clear pain point and the B2B model with per-covered-life fees is compelling, but executing real-time data aggregation across Peru's fragmented pharmacy landscape is capital-intensive and partnership-dependent. I need to see a clear path to $1M ARR and international co-investor interest given our thin capital market. | Concern: Pharmacy chains may block integration or refuse to share real-time inventory data, and independents lack the infrastructure to participate, making the core value proposition unattainable in practice. | Need: Show signed letters of intent (LOIs) from at least two major pharmacy chains and one insurer willing to pilot the platform within 6 months.



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
- Conduct 100+ surveys with prescription holders and 20+ interviews with insurance procurement managers.
- Build a prototype with 1-2 pharmacy partners to test real-time data integration and OCR accuracy.
- Run a pilot with one self-insured employer to measure cost savings and user adoption.

## Kill Criteria
- No pharmacy partner willing to share real-time pricing data after 3 months of outreach.
- Insurers express no willingness to pay per-covered-life fees, only one-time discounts.
- Survey shows >60% of prescription holders unwilling to switch pharmacy for generics.
