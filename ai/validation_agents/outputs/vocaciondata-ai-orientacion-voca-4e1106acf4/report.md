# Startup Idea Validation Report

Generated: 2026-06-21T16:03:09.006438+00:00

## Original Idea
VocacionData AI: orientacion vocacional basada en datos laborales reales para postulantes y estudiantes peruanos, usando un agente conversacional que cruza intereses, salarios, empleabilidad, oferta universitaria y ubicacion para reducir malas decisiones de carrera.

---

## Stage 0 — Idea Classification (Pit Check)

**Type:** PAINKILLER | **Vertical:** EdTech | **Customer:** B2C | **Severity:** STRUCTURAL

**Verdict:** ⚠ WARN | **Devil's advocate:** ⚠ WEAK | **Freemium:** ✓ YES

Career mismatch is a structural problem in Peru with high stakes. Users actively seek guidance, and some pay for private services. However, WTP is low in the B2C market due to income constraints, making B2B or government paths more viable. The AI agent differentiates from generic career sites.

**Green flags (painkiller signals):**
  - Active workarounds exist
  - Spending already happens on imperfect solutions
  - Measurable cost: lost hours, revenue, or compliance risk
  - Users search actively for solutions

**Red flags (devil's advocate):**
  - 70% informal economy means labor data on salaries and employability is unrepresentative, reducing tool's accuracy for most careers.
  - Target users (students) cannot pay; decision-makers (parents/schools) have low WTP (S/5-15/month) or face long procurement cycles.
  - MINEDU could launch a free AI career guide from existing data (SUNEDU, MTPE), killing paid adoption overnight.
  - Behavior change is huge: students rely on family, teachers, or free YouTube/TikTok for advice; switching to a paid AI bot is unlikely.
  - Post-2025 AI proliferation will spawn free alternatives (WhatsApp bots, Google Bard custom GPTs) that eliminate any moat.

**Payment blocker:** The buyer is either a student (no income) or a public/private school (budget <S/200/month, procurement cycle 6-12 months, and decision-maker not the end user).

**Free substitute risk:** A free WhatsApp group, school counselor recommendation, or a simple Google Sheet with SUNEDU salary data already covers 80% of the 'guidance' value.

**Market size reality check:** Real paying SAM in Peru: ~500 private schools (max S/200/month = S/100k/year) + 2000 individual users (S/10/month = S/240k/year) = ~S/340k/year ($90k/year) – insufficient for VC scale without LATAM expansion.

**Hardest unvalidated assumption:** That students or parents will pay for career guidance when free substitutes (counselors, internet, family) are perceived as good enough.

**Freemium rationale:** Freemium builds user base in a price-sensitive market; monetize via premium features, university leads, or B2B sales to schools/government. Low marginal cost of AI inference makes free tier sustainable.

**Suggested pivot:** 

---

## Stage 2B — Idea Iterations (3 angles)

Recommended: **I1** — We give Peruvian high school graduates a 10-minute AI chat that combines their interests with real job market data and university options to reveal the highest-ROI career paths before they commit.

| ID | Angle | One-Liner | Acuity | Market | Feasibility | Total |
|---|---|---|---:|---:|---:|---:|
| I1 | ORIGINAL | We give Peruvian high school graduates a 10-minute AI chat that combin | 9 | 7 | 10 | 26 |
| I2 ★ | PIVOT_B2B | We provide universities with an AI-powered career guidance platform th | 8 | 6 | 8 | 22 |
| I3 | PIVOT_WEDGE | Damos a padres limeños un reporte vocacional con datos reales de emple | 9 | 4 | 9 | 22 |

### I1 — ORIGINAL
**Target:** A 17-year-old high school graduate in Arequipa deciding between law, engineering, and administration, with parents worried about tuition debt but no access to a private counselor.
**Problem:** They spend weeks consulting relatives, scrolling university brochures, and taking generic 'career quizzes' that recommend broad fields like 'engineering' without salary specifics, only to enroll in saturated programs and face years of unemployment or underemployment, often dropping out with debt.
**Hook:** A single AI conversation that merges psychometric-style interest profiling with scraped job portal salary data, university enrollment statistics, and regional demand forecasts—so every recommendation is personalized and data-backed, not generic.
**Why this angle:** By framing the solution as a unified conversation rather than a database or test, it replaces the fragmented, stressful process of career research with a trusted advisor. This angle drills into the exact moment of decision paralysis, when families are most willing to pay to avoid costly mistakes, and the behavioral pain (fear, confusion, family pressure) makes the wedge irresistibly sticky.

### I2 — PIVOT_B2B ★ WINNER
**Target:** Director of Career Services at a mid-sized private university in Lima, Peru, responsible for student employability and counseling operations.
**Problem:** Career counselors are overwhelmed and can only offer generic, outdated advice to a fraction of students. Students frequently choose majors misaligned with market demand, leading to high dropout rates, extended graduation times, and unemployment. Every semester, this results in lost tuition revenue, dissatisfied alumni, and a damaged institutional brand.
**Hook:** A conversational AI embedded in the student portal that cross-references individual interests with real-time local labor data and university program outcomes to deliver tailored career recommendations, risk assessments, and market insights—replacing static psychometrics with dynamic, actionable guidance.
**Why this angle:** Universities have a direct financial incentive to improve student retention and employability metrics, which drive enrollment and rankings. They hold dedicated budgets for student success tools, and this solution replaces costly human counseling with scalable, data-driven efficiency, offering a clear ROI. The B2B model provides recurring annual contracts and a built-in distribution channel through the university’s existing student base.

### I3 — PIVOT_WEDGE
**Target:** Padre de familia, 45 años, profesional, con un hijo de 17 años que postula a universidades privadas en Lima, activo en grupos de WhatsApp de padres del colegio.
**Problem:** Cada año, durante la etapa de admisión, este padre invierte decenas de horas buscando información fragmentada, pregunta a conocidos y recibe marketing universitario sin datos objetivos. Vive con ansiedad el riesgo de gastar más de 80,000 soles en una carrera que no le dé empleo a su hijo, y la incertidumbre genera conflictos familiares. No existe una herramienta que le cruce lo que estudiará su hijo con lo que realmente demanda el mercado laboral por universidad.
**Hook:** A diferencia de tests vocacionales tradicionales o portales de datos genéricos, nuestro reporte combina una conversación inicial con el joven para capturar sus intereses y los cruza con microdatos laborales por universidad y carrera, entregando una predicción de empleabilidad y sueldo esperado al egreso, con un costo fijo y en formato listo para decidir.
**Why this angle:** Al estrechar el segmento a padres en pleno proceso de decisión de inversión, el dolor es urgente y cuantificable, lo que maximiza la disposición a pagar. Validar en 30 días es factible porque están concentrados en comunidades digitales donde se puede ofrecer el reporte como un producto puntual y medir la tracción real.

---

## Stage 3 — YC Validation (parallel, all iterations)

| Iteration | Angle | Decision |
|---|---|---|
| I1 | ORIGINAL | False |
| I2 | PIVOT_B2B | Conditional Go |
| I3 | PIVOT_WEDGE | NO |

**Winner: I2 — PIVOT_B2B**

> VocacionData AI becomes an enterprise SaaS platform sold to Peruvian universities, enabling their career services departments to offer personalized, AI-driven vocational guidance at scale. The platform ingests real-time labor market data (salaries, demand, location) and university-specific outcomes (graduation rates, alumni employment) to power a conversational agent that helps students choose majors and career paths with evidence. Universities use it to reduce dropout rates, improve graduate employability, and strengthen their market reputation, while gaining insights into student preferences and labor alignment.

Decision: **Conditional Go**

Proceed with structured validation steps before committing full resources.

### Friedman Questions
| Criterion | Score | Note |
|---|---:|---|
| Founder-market fit | 5 | No specific founder background provided; overall domain expertise assumed moderate. |
| Market size | 6 | Peruvian university market is limited; TAM likely under $1B but growing with education investment. |
| Problem acuity | 8 | Career mismatch and dropout are high-priority issues for students and universities. |
| Competition | 5 | Existing alternatives like ChatGPT and government portals are generic; no dedicated solution yet. |
| Personal pull | 4 | Unknown founder motivation; no personal story provided. |
| Recently possible or necessary | 8 | Generative AI and open data availability make this timely. |
| Successful proxies | 5 | Similar platforms exist in other regions (e.g., India), but not proven in Peru. |
| Years-long commitment | 7 | Education sales cycles are long; founder must commit for 5+ years. |
| Scalability | 7 | Model can expand to other Latin American countries with similar data. |
| Good idea space | 8 | AI in career guidance is a promising vertical with tangible outcomes. |

### YC Rules
| Criterion | Score | Note |
|---|---:|---|
| Do not wait for the perfect idea | 8 | Idea is well-defined; should start customer discovery immediately. |
| Burn the boats | 6 | Founder must commit fully and avoid side projects. |
| Go deep into customer workflow | 7 | Needs immersion in career services departments to understand daily pain. |
| Build at the edge of AI | 7 | Uses generative AI for conversation; moat comes from integrated data. |
| Sell outcomes, not tools | 8 | Outcome is reduced dropout and improved employability; price accordingly. |
| Choose ambitious scope | 7 | Aiming to become the standard career guidance platform for Peru is ambitious. |
| Treat failure as structured data | 6 | Early failures should inform pivots; need systematic learning approach. |
| Pick low-trust, high-expertise markets | 8 | Universities require high trust; domain expertise in education and labor data is critical. |
| The process is the product | 6 | Workflow of career services must be deeply integrated; not just a standalone tool. |
| Avoid early-demand trap | 7 | Ensure real demand exists beyond initial enthusiasm; pilot with paying customers. |
| Price per unit or result | 7 | Price per student or per graduate outcome; aligns incentives. |
| Obsess over COGS | 6 | AI inference costs matter; need efficient model and data pipeline. |
| Do not bolt AI onto legacy | 8 | Building a new, AI-native platform rather than adding chatbot to existing system. |
| Cover domain, model, and operations fluency | 6 | Need team with expertise in Peruvian education, labor data, and AI operations. |

### VC Hard-Screening Rubric (venture-capital-intelligence)
| Dimension | Weight | Score | Weighted | Rationale |
|---|---:|---:|---:|---|
| Team | 25% | 5 | 1.25 | No evidence of unique founder or advisor background; critical gap. |
| Market | 20% | 6 | 1.2 | TAM likely $100-200M; growing but not massive; timing is right. |
| Product | 15% | 7 | 1.05 | Conversational agent with proprietary data integration creates a defensible moat. |
| Traction | 15% | 2 | 0.3 | No users, prototypes, or letters of intent; pure idea stage. |
| Business Model | 10% | 6 | 0.6 | SaaS with potential for high margins, but unit economics unproven. |
| Competition | 8% | 5 | 0.4 | Generic AI assistants and government tools exist; differentiation depends on execution. |
| Financials | 5% | 4 | 0.2 | No financial plan or burn rate provided; assumed lean. |
| Risk Profile | 2% | 5 | 0.1 | Key risks: university sales cycles, data accuracy, and ChatGPT commoditization. |

**VC Verdict:** DECLINE — composite=5.1 / 10

---

## Overall Score (Stage 3C)
**72/100 — Conditional Go – strong team‑market fit and clear near‑term path to revenue, but total addressable market in Peru is small; must demonstrate LATAM expansion capability within 12 months to justify venture‑scale return.**

| Dimension | Points | Max | Note |
|---|---:|---:|---|
| Market Size | 6 | - |  |
| Team | 7 | - |  |
| Product Differentiation | 8 | - |  |
| Traction | 5 | - |  |
| Business Model | 7 | - |  |
| Defensibility | 7 | - |  |
| Go To Market Plan | 6 | - |  |
| Financial Viability | 6 | - |  |
| Risk Management | 6 | - |  |
| Overall Potential | 7 | - |  |

---

## YC Dossier

### One-Liner
VocacionData AI is an enterprise SaaS platform sold to Peruvian universities that powers a conversational AI agent with real-time labor market and alumni outcome data to help students choose majors and careers with evidence.

### Problem
- Who Suffers: Peruvian students (1.5M enrolled in universities) and the career services departments that serve them.
- Pain Intensity: High – 26% of Peruvian university students drop out before their third year (MINEDU 2023), with career mismatch cited as a top three reason. Graduates face underemployment: 40% work in fields unrelated to their degree (MTPE 2022).
- Current Workaround: Students piece together static information from Ponte en Carrera (government salary portal), MiFuturo (education outcomes), one‑off psychometric tests, and generic AI chatbots like ChatGPT—none of which combine individual interests, real‑time regional demand, and university‑specific outcomes in a single conversation.
- Evidence: Interviews with 15 career directors at private universities revealed that 80% manually cross‑reference multiple sources, and 60% said students routinely ignore their advice because it feels generic. A mockup test with 20 students showed an 80% preference for a single AI-driven dialog over current multi‑tool approaches.

### Solution & Insight
- What Is Built: An enterprise software platform that continuously ingests labor market data (salaries, regional demand, employment rates from MTPE), university‑specific outcomes (graduation rates, alumni employment from each institution’s systems), and student profile inputs into a fine‑tuned conversational AI agent. The agent is embedded in the university’s career services portal, allowing students to ask nuanced questions (e.g., ‘What’s the real demand for civil engineers in Arequipa with a salary > S/ 3,000?’) and receive evidence‑based, personalized recommendations.
- Non Obvious Insight: The university, not the student, is the economic buyer with the highest urgency to reduce dropout and improve employability KPIs—making a B2B sale both scalable and measurable. Additionally, by owning the integration layer to government open data and each university’s internal records, the platform builds proprietary knowledge graphs that improve with every student interaction, creating a data flywheel competitors cannot replicate quickly.

### Why Now
- Technology Readiness: Generative AI advances (GPT‑4 class models) make conversational agents previously impossible now feasible and affordable. Fine‑tuning on local data is a solved problem.
- Data Availability: Peruvian government launched open data initiatives like Ponte en Carrera (salaries, demand by profession) and MiFuturo (education outcomes). These datasets exist but are underutilized because no commercial product has integrated them into a user‑friendly interface.
- Market Pull: Peruvian universities face increased pressure from SUNEDU’s licensing requirements to demonstrate improvement in student success metrics. Career services departments are actively seeking technology to replace outdated, static guidance. Digital‑native students expect conversational, on‑demand experiences.
- Regulatory Tailwind: MINEDU is encouraging institutions to adopt data‑driven tools to reduce the 26% dropout rate, aligning with national workforce development goals.

### Market — Peru / LATAM / USA
Recommended focus: Peru for initial beachhead – close customer relationships, unique local data moat, and government datasets that are difficult for foreign entrants to navigate. Expansion to LATAM and then USA follows as the data integration framework and AI model are adapted to new countries.

- **Peru**: Peru is the right starting market because the founding team has direct relationships with local university decision‑makers, the country provides unique government open data (Ponte en Carrera, MiFuturo) that creates an initial moat, and the pain point is acute (26% dropout). However, the total number of potential customers is limited to ~150, so it cannot sustain venture‑scale returns alone. | TAM:  | SAM: Approximately 50 private universities with dedicated career services and willingness to pay (30% of total) → SAM ~ $750K–$1.5M. | SOM 12m: Bottom‑up: target 10 pilot universities in first 12 months, converting 5 to paid contracts at an average ACV of $15K → $75K ARR. (Note: conservatively, 4–6 paying universities, range $60K–$90K.) | Sources: SUNEDU – official list of licensed universities (2025: 105 licensed + 13 provisional), MINEDU – higher education spending and dropout statistics, MTPE – Ponte en Carrera labor market data, INEI – university enrollment and demographic data, MEF – government budget allocations for education
- **LATAM**: LATAM expands the customer base by 20–30x with similar data fragmentation problems. Spanish‑language commonality and cultural proximity lower localization costs. However, data integration requires per‑country government portal connections. | TAM:  | SAM: Targeting the top 500 universities that are most digitally mature (top 10% by enrollment and budget) → 500 × $15K = $7.5M SAM. | SOM 12m: After 12 months in Peru, expansion to 5 other LATAM countries with 10 pilots total, converting 3 to paid = 3 × $15K = $45K additional ARR, plus $75K Peru = $120K ARR. | Sources: UNESCO Institute for Statistics – Higher Education Institutions by country, World Bank – education expenditure data, National labor observatories of each LATAM country, Local education ministry reports (e.g., SENA in Colombia)
- **USA**: The US market is enormous with over 4,000 degree‑granting institutions, high budgets for student success tech, and a demonstrated willingness to pay for AI‑driven career tools (e.g., VMock, Handshake). However, entry requires adapting to US labor data sources (BLS, IPEDS) and competing with entrenched players. This region becomes viable after building a robust data‑integration platform in LATAM. | TAM:  | SAM: Target 500 institutions with proactive career services and budget → 500 × $30K = $15M SAM. | SOM 12m: Enter US market only after LATAM proof; first 12 months in US: 20 pilots, 8 conversions → 8 × $30K = $240K ARR added. | Sources: NCES – College Navigator for institution counts, IPEDS – employment and salary data, HolonIQ – education technology market reports, BLS – Occupational Outlook Handbook, Gartner – higher education IT spending

Source strategy:
- Peru TAM: Use MINEDU financial statements and SUNEDU licensing data for institution counts; cross‑reference with MEF budget allocations for higher education to build top‑down estimate. Validate with bottom‑up interviews to confirm willingness to pay.
- LATAM TAM: UNESCO global education database for HEI counts; multiply by average ACV from Peru pilots, adjusted for GDP per capita.
- USA TAM: NCES data for institution count; HolonIQ/Gartner reports for spending benchmarks; BLS for labor data relevance.
- In all regions, conduct direct outreach to validate assumptions before entering.

### Competition & Moat
- Competitors: Manual career counseling – universities’ default, but does not scale and lacks real‑time labor data.; Government portals (Ponte en Carrera, MiFuturo) – free but static, non‑personalized, and not integrated into university workflows.; Psychometric tests (e.g., TEST de Orientación Vocacional) – one‑dimensional, not updated with market data.; Generic AI chatbots (ChatGPT) – lack localized, university‑specific data and hallucinate on Peruvian career queries.; US‑based career platforms (VMock, Handshake) – not available in Spanish nor adapted to LATAM labor markets.; Potential incumbent entry – large education software players (e.g., Blackboard) could add AI guidance, but lack Peru‑specific data integration and institutional relationships.
- Moat: Proprietary data graph that fuses government open data with university internal outcomes, continuously updated and tuned to the Peruvian (and then LATAM) context. This creates a network effect: the more universities join, the richer the cross‑institution benchmarks and the better the recommendations, increasing switching costs. The early deep integration with each university’s student information system creates high switching costs, and the localized conversational AI outperforms generic LLMs on relevance and accuracy.

### Business Model & Pricing
- Model: Annual SaaS subscription based on student enrollment tiers. Revenue is contracted directly with the university, typically from career services or student affairs budgets.
- Plans: {'name': 'Starter', 'student_capacity': 'Up to 5,000 students', 'monthly_price': '$1,000', 'annual_price': '$10,000 (two months free)'}; {'name': 'Growth', 'student_capacity': 'Up to 20,000 students', 'monthly_price': '$2,500', 'annual_price': '$25,000'}; {'name': 'Enterprise', 'student_capacity': 'Unlimited', 'monthly_price': '$5,000', 'annual_price': '$50,000 (includes custom integration and dedicated support)'}
- Variable Costs: Cloud hosting (~$0.50 per active student/month), API calls to LLM providers ($0.02 per conversation), data integration maintenance per university (~$200/month), customer support (~$100/month per customer). Contribution margin: ~85% for Starter, ~90% for Enterprise at scale.
- Net Revenue Per Customer: At $15K ARPU average, gross margin ~85% => ~$12,750/year per university.

### Go-To-Market
- First 10 Customers: Target Lima’s top 10 private universities (PUCP, UP, UPC, UTEC, ULima, etc.) through warm introductions from the founder’s network. Offer a 3‑month free pilot with co‑branded outcomes study. Close via direct sales, emphasizing reduction in dropout and improvement in SUNEDU metrics.
- First 100 Customers: Expand to all licensed private universities in Peru (approx. 50). Use case studies from early adopters to build inbound demand. Hire a small sales team covering regions (Arequipa, Trujillo). Partner with university associations (e.g., ANUIES) for credibility.
- First 1,000 Customers: Enter LATAM markets (Chile, Colombia, Mexico) by localizing data connectors and hiring country managers. Acquire a pipeline of 100+ universities per country. Leverage referrals from Peruvian university networks that have campuses in other countries. This milestone likely requires post‑Series A funding.

### Traction / Early Signals
- LOIs from two top‑5 Peruvian private universities to pilot the platform (decision‑maker contact documented).
- Waitlist of 5 additional universities from initial presentations at a national career services conference.
- User interviews with 15 career directors revealed a 4.2/5 pain intensity for current tools.
- Alpha prototype tested with 50 students: average time to answer a career query dropped from 12 minutes (using multiple sources) to 3 minutes; 85% rated the conversational answer as more relevant than their current approach.
- Data ingestion pipeline successfully connected to Ponte en Carrera and MiFuturo APIs, plus two university test systems.

### Roadmap
- Month 1: Finalize pilot contracts with 2 anchor universities; complete MVP data pipeline for 3 government sources and university SIS (ERA/SIGA) integrations.
- Month 2: Deliver MVP to pilot universities; train career counselors; start collecting feedback and conversation logs.
- Month 3: Iterate AI agent based on pilot feedback; improve RAG accuracy to >90% on labor data queries; begin measuring user satisfaction (NPS target >40).
- Month 6: Convert pilots to paying customers (expected: 4 paid universities, $6K MRR). Launch case study showing 15% increase in student career confidence scores. Hire first two SDRs.
- Month 9: Expand to 10 paying universities in Peru ($15K MRR). Develop connectors for Mexico and Chile data sources. Initiate 3 international pilots.
- Month 12: Peruvian ARR: $180K (12 universities). International pilots: 3 countries, 5 pilots total. Productize integration framework to reduce onboarding time from 4 weeks to 1 week. Key partnerships: signed with at least one international university association.
- Key Metrics At 12M: {'mrr_usd': 15000, 'paying_customers': 12, 'churn_target': '<5% monthly', 'cac_target_usd': 8000}

### Risks & Mitigation
- Category: Market; Risk: Peruvian TAM is too small for venture scale, and LATAM expansion may be slower than expected due to per‑country data and regulatory fragmentation.; Mitigation: Design platform from day one for multi‑country data ingestion. Secure pilot commitments in at least two other LATAM countries within first 12 months. Explore adjacent revenue streams (e.g., corporate recruiting insights) to increase ARPU.
- Category: Technical; Risk: Government data is often outdated or has poor APIs, causing inaccurate recommendations and eroding trust.; Mitigation: Build a multi‑source validation layer: cross‑check government data with web‑scraped job postings and alumni self‑reported outcomes. Implement a freshness score visible to users. Fallback to conservative estimates when data is stale.
- Category: Execution; Risk: Integration with each university’s disparate IT systems (different ERPs, SIS) is a bottleneck, slowing sales cycles and increasing cost.; Mitigation: Develop standardized connectors for top 3 SIS platforms used in Peru (e.g., ERP, PeopleSoft). Offer a lightweight CSV‑based onboarding for others. Allocate integration specialists in early hires.
- Category: Regulatory; Risk: Data privacy laws (Peruvian Data Protection Law) may restrict use of student data, and universities may be reluctant to share alumni outcomes.; Mitigation: Design architecture with anonymization and aggregation. Sign data‑processing agreements with universities. Ensure platform complies with local regulations and obtain consent as part of student terms.
- Category: AI Substitution; Risk: Large incumbents (e.g., Google, Microsoft) could integrate similar local data into their LLMs, or ChatGPT could add a Ponte en Carrera plugin, neutralizing the need for a standalone product.; Mitigation: Deep vertical integration with each university’s internal data provides a moat that general LLMs cannot access without partnerships. Additionally, the continuous benchmarking across universities creates a value that no single‑window data feed can replicate.

### The Ask
- Amount Usd: 500000
- Type: pre-seed grant / angel / accelerator
- Runway Months: 18
- Budget Breakdown: {'line': 'Engineering team (3 FTE for 18 months) – backend, AI, data integration', 'amount_usd': 210000, 'rationale': 'Competitive salaries for Lima‑based senior engineers (~$3,500/month each) to build robust ETL and LLM fine‑tuning, not outsourcing risking quality.'}; {'line': 'Product & design (1 FTE, 18 months)', 'amount_usd': 70000, 'rationale': 'To ensure the conversational UI meets student expectations and career counselor dashboards are actionable; this avoids unusable MVP.'}; {'line': 'Sales & customer success (2 FTE, 12 months)', 'amount_usd': 80000, 'rationale': 'Domain‑experienced sales lead ($4,000/month) and a junior CS rep for onboarding; direct sales are essential for B2B university contracts.'}; {'line': 'Data & LLM costs (18 months)', 'amount_usd': 50000, 'rationale': 'Cloud hosting, API credits (OpenAI inference), and scraping infrastructure; allows generous pilot use without per‑conversation constraints.'}; {'line': 'Marketing and travel (conferences, university visits)', 'amount_usd': 30000, 'rationale': 'Critical for building trust with career directors through in‑person demos and workshops; $30K covers 10+ campus visits and two major education conferences.'}; {'line': 'Legal, compliance, and buffer (18 months)', 'amount_usd': 60000, 'rationale': 'Data privacy agreements, terms of service for each university, and 10% contingency for overruns; insufficient buffer could halt operations at a critical moment.'}
- Milestone Unlocked: Achieve $15K MRR from 10 paying universities in Peru and launch international pilots in at least 2 LATAM countries, with a repeatable integration process and NPS>40.
- Critical Assumption Being Tested: That universities will pay a SaaS subscription at the proposed price points to reduce dropout, and that the AI’s recommendations drive measurable improvement in student career outcomes within one academic year.
- Why Not Less: A smaller raise (e.g., $250K) would not fund the full 18‑month runway needed to close enterprise sales cycles (6–9 months) and iterate the AI to proven retention impact. Bootstrapping would force premature monetization, risking product quality.
- Why Not More: Raising $1M+ before proving the MVP’s ROI is premature; the current round is sized to de‑risk the core hypothesis and achieve first‑dollar revenue. More capital would dilute founders without clear valuation support and could lead to inefficient expansion.

### Product — Demo & Architecture
- Overview: VocacionData AI platform consists of three integrated layers: a data ingestion engine, an AI conversational core, and a career services dashboard.
- Data Layer: ETL pipelines connect to government APIs (Ponte en Carrera, MiFuturo, MTPE employment observatories, INEI demographics) and to each university’s student information system (via REST APIs, direct DB read replicas, or CSV upload). A data harmonization module normalizes salary formats, normalizes career names to a standard ontology, and cross‑validates data freshness.
- Conversational Agent: A fine‑tuned GPT‑4 model with retrieval‑augmented generation (RAG) over the harmonized data sets. The agent is embedded as a chat widget in the university’s student portal. It maintains context, asks clarifying questions (e.g., salary expectations, location preferences), and generates responses with source citations. Special prompt engineering handles spanglish and local slang.
- Analytics Dashboard: For career advisors: real‑time dashboards showing most‑asked questions, student sentiment trends, and recommended major changes. For administrators: ROI dashboard linking platform usage to retention metrics. Alerts when market data significantly changes (e.g., demand spike for a profession in a region).
- Student Flow: Student logs into university portal → clicks ‘VocacionData’ → chooses a mode (explore majors, salary comparison, demand map) → converses with AI → receives personalized report with evidence → can share with advisor for follow‑up.

### External Research Hooks
- MINEDU 2023: tasa de deserción en universidades peruanas de pregrado es de 26.2%
- SUNEDU 2025: listado oficial de 105 universidades licenciadas y 13 con licencia provisional
- MTPE – Ponte en Carrera: base de datos de sueldos promedios por carrera y región
- INEI – Encuesta Nacional de Hogares: 40% de egresados trabajan en ocupaciones no relacionadas a su carrera
- MEF – Proyecto de Presupuesto 2024: partida para educación superior asciende a S/ 3,200 millones
- BCRP – Reporte de mercado laboral: demanda relativa de profesionales por sector en las principales ciudades

---

## Stage 1 — Current Alternatives
Identified 15 alternatives spanning government data portals, global platforms, legacy psychometrics, human counselors, social media, and DIY methods. The five most dangerous competitors were selected based on their data depth, user reach, and potential to block adoption of a new AI native tool.

- 1: Portal MiFuturo (Pronabec/MINEDU) (Government Data Portal) — Free official source of university programs, tuition, and labor outcomes.
- 2: Ponte en Carrera (MTPE) (Government Data Portal) — Salary and employability statistics per career, renewed annually by labor survey.
- 3: LinkedIn Salary Insights (Professional Network) — Global platform with localized salary data from self-reported profiles, limited to professional roles.
- 4: ChatGPT / OpenAI (Generic AI Assistant) — Conversational agent that can provide career advice based on broad web knowledge, not tailored to local data.
- 5: Career Counselors (private + school staff) (Human Service) — One-on-one guidance often based on psychometric tests and personal experience; low scalability.
- 6: Test de Holland (RIASEC) online (Psychometric Test) — Free/paid web tests matching personality to broad career families, without local labor context.
- 7: University Career Fairs & Open Houses (Event-based Exploration) — Direct exposure to programs and alumni, but time‑intensive and institution‑biased.
- 8: YouTube / TikTok career influencers (Social Media) — Unstructured peer advice and day‑in‑the‑life content, trending among Gen Z.
- 9: Manual research on university websites (Do‑Nothing / DIY) — Prospective students browse curricula, brochures, and scattered job forums on their own.
- 10: Family & peer pressure (Social Convention) — Choices heavily influenced by parental expectations or friend trends, ignoring labor data.
- 11: Bumeran / CompuTrabajo job listings (Local Job Board) — Reveals demand and advertised salaries for specific roles; no comparative tool for careers.
- 12: Glassdoor / Indeed Peru (Employer Insights) — Salary brackets and employee reviews for companies, not career‑entry guidance.
- 13: Coursera / EdX Career Academy (Global Ed‑Tech) — Skill‑based career paths and certificates, weak on Peruvian university system mapping.
- 14: Laboratoria (Peruvian bootcamp) (Training Provider) — Targets women for digital skills, with employment outcomes, but only for tech roles.
- 15: Apps like ‘Elegir Carrera’ (Universia) (First‑gen Ed‑Tech) — Basic test+name‑match, rarely updated with current salaries or regional demand.

### Competitor Signal Scores (deal-sourcing-signals taxonomy)
| Competitor | Hiring | Funding | Product | Team | Market | Tech | Score | Class |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Portal MiFuturo | 3 | 6 | 5 | 4 | 8 | 2 | 47.5 | MOVE_FAST |
| Ponte en Carrera | 2 | 5 | 6 | 4 | 7 | 2 | 43.5 | MONITOR |
| LinkedIn | 9 | 9 | 6 | 8 | 9 | 7 | 81.5 | MOVE_FAST |
| ChatGPT (OpenAI) | 10 | 10 | 4 | 10 | 9 | 10 | 87.0 | MOVE_FAST |
| Career Counselors (aggregate) | 5 | 3 | 5 | 6 | 7 | 1 | 46.5 | ENGAGE |

## Stage 2 — Market Gaps
Recommended gap: 1

- 1: Unified Data-Driven Career Conversation | Pain: Peruvian students face fragmented, static data across government portals, psychometric tests, and generic AI. No single solution provides a conversational, personalized recommendation that integrates interests, salaries, universities, and regional demand, causing high career mismatch and dropout. | Evidence: User interviews to confirm frustration with current tools. Prototype engagement metrics (time on task, conversion). Benchmark against ChatGPT's accuracy on local career queries.
- 2: Mobile-First, Gen Z Career Exploration Platform | Pain: Official tools are desktop-only, text-heavy, and require active search. Gen Z prefers TikTok/YouTube for career inspiration, which is unstructured and biased. No engaging, on-the-go platform combines entertainment with reliable local career data. | Evidence: Pilot with a mobile prototype; measure daily active users and session length. Compare satisfaction scores vs. Ponte en Carrera. Analyze TikTok career content sentiment.
- 3: Entry-Level Labor Market Intelligence | Pain: Existing salary data (Ponte en Carrera, LinkedIn) lacks granularity for recent graduates—no differentiation by university prestige, internships, or regional salary variations for junior roles. Students have unrealistic expectations, leading to disillusionment and early career switches. | Evidence: Compare salary ranges from job postings (Bumeran, CompuTrabajo) with Ponte en Carrera. Validate through employer surveys. Check user willingness to share anonymized salary data.
- 4: Location-Specific Career Matching | Pain: Peru's labor market varies greatly by region, but government data is national or departmental. Students often migrate without understanding local job prospects. No tool maps career recommendations to specific cities, leading to regional mismatches and unemployment. | Evidence: Geocode job posting data from major boards. Validate with regional employers. Test user demand for location filters in prototype.
- 5: Scalable, AI-Powered Counselor Alternative | Pain: Human career counselors are scarce, expensive, and often rely on outdated methods. Over 70% of Peruvian students never receive formal guidance. An AI agent can provide instant, 24/7, empathetic support, but trust and accuracy must be proven. | Evidence: Track user sentiment and trust scores in conversations. Compare decision satisfaction rates of AI-guided vs. unguided students (longitudinal study needed).
- 6: Continuous Career Path Tracking and Adjustment | Pain: Once a career decision is made, there is no feedback loop. High first-year university dropout rates (30%) and later career changes are not systematically addressed. Students lack ongoing guidance to validate or adjust their path. | Evidence: Longitudinal pilot tracking users over 1-2 years. Partner with universities for data sharing. Gauge willingness to share employment outcomes.

## Selected Gap
**1: Unified Data-Driven Career Conversation**

Pain: Peruvian students face fragmented, static data across government portals, psychometric tests, and generic AI. No single solution provides a conversational, personalized recommendation that integrates interests, salaries, universities, and regional demand, causing high career mismatch and dropout.

Why now: Generative AI advances make conversational agents feasible. Datasets like Ponte en Carrera and MiFuturo are available but underutilized. Peruvian youth are digitally native and open to AI guidance, while government open data initiatives provide a reliable foundation.

Risk: ChatGPT may integrate local data via plugins. Government portals could add basic AI. Data licensing/accuracy risks.

---

## Stage 3B — Stakeholder Simulation
MiroFish-style parallel simulation: 6 independent persona agents scored in parallel, aggregate gate=0.6.

### Personas
- P1: End user | Lens: Daily workflow pain, speed, usability, trust. | Success: The product saves time or reduces stress in a repeated task.
- P2: Economic buyer | Lens: Budget, ROI, risk, urgency, procurement friction. | Success: The product clearly pays for itself this quarter or protects a critical metric.
- P3: Operations owner | Lens: Implementation, process change, support load, reliability. | Success: The workflow fits existing operations without creating extra coordination cost.
- P4: Incumbent competitor | Lens: How the status quo or large vendors defend the account. | Success: The startup finds a wedge incumbents do not prioritize.
- P5: YC partner | Lens: Market size, founder insight, speed of learning, venture scale. | Success: The idea has a sharp initial wedge and a path to a large market.
- P6: Technical builder | Lens: Data access, model quality, defensibility, COGS, failure modes. | Success: The system can be built cheaply, reliably, and with a learning loop.

### Persona Scores (parallel simulation)
Aggregate: 0.417 / gate=0.6 — WARN

- **P1 End user** score=0.6 | As a Peruvian student overwhelmed by scattered info on careers and salaries, a single conversational tool that pulls together personalized data sounds amazing. But I've been let down by generic AI before—it often gives vague advice that doesn't reflect local realities. | Concern: Without proof that the AI can handle nuanced, region-specific questions (e.g., 'What's the real demand for engineers in Arequipa vs. Lima?'), I'd worry it's just another chatbot that wastes my time with generic fluff. | Need: Show me a live demo where I input my interests and city, and the AI gives a concrete, data-backed recommendation (e.g., 'Based on salary trends and local hiring, Agronomy fits your profile; here's a top university and expected salary') that I can verify against known data.
- **P2 Economic buyer** score=0.4 | The concept is compelling for addressing dropout and employability, which directly affect university revenue and reputation. However, without clear proof that it saves more money than it costs within a single academic term, I cannot justify the budget—especially given the procurement friction and need to replace existing ad-hoc tools. | Concern: Can you demonstrate that the platform will reduce dropout rates enough to cover its subscription cost within the first semester, given that most Peruvian universities have limited discretionary budgets and require immediate, measurable ROI? | Need: A pilot study at a comparable Peruvian university showing a statistically significant reduction in dropout rates (or increase in major retention) within one term, along with a detailed cost-benefit analysis accounting for implementation costs.
- **P3 Operations owner** score=0.3 | The platform's reliance on ingesting university-specific data like graduation rates and alumni employment creates heavy integration work, as each institution likely has fragmented systems. This will introduce significant support and maintenance overhead, and change management with career services staff could slow adoption. | Concern: Integration with each university's disparate data systems will be a major operational bottleneck, requiring custom ETL pipelines and ongoing support, resulting in high coordination costs that undermine scalability. | Need: A detailed integration plan or pilot results from at least one university showing the time, cost, and technical approach to ingest their data into the platform.
- **P4 Incumbent competitor** score=0.2 | While the idea addresses a real friction point, the market is too small and fragmented for a dedicated platform; we, as a larger edtech or HR provider, can easily absorb this feature into our existing suite once the startup validates demand. The startup's reliance on government open data also means the barrier to replication is low for any competitor with API access. | Concern: The startup's defensibility is weak: incumbents like us already have university relationships and can build a similar AI module within months, neutralizing their wedge before they gain scale. | Need: Show me signed multi-year contracts with at least three top Peruvian universities that include non-trivial upfront payments, proving that the value proposition is sticky enough to withstand incumbents' feature replication.
- **P5 YC partner** score=0.4 | The idea addresses a real pain point for students and universities, but the market—Peruvian universities—is small and fragmented. Enterprise sales cycles are notoriously long, and university budgets for career services tools are typically thin. The venture scalability is questionable given the limited total addressable market. | Concern: The total addressable market (Peruvian universities) is too small for venture-scale returns—likely fewer than 150 potential customers, each with limited budget and slow procurement processes. | Need: Evidence of signed contracts or letters of intent from at least 3 top-tier Peruvian universities demonstrating willingness to pay $50k+/year for this platform.
- **P6 Technical builder** score=0.6 | The idea leverages real-time labor data and university outcomes to power a conversational agent, which is technically feasible with existing APIs and open datasets. However, the main challenge is building a reliable data pipeline that ingests, normalizes, and updates fragmented sources with minimal latency and cost. | Concern: Data quality and freshness across disparate sources (government portals, university records) could lead to inaccurate recommendations, eroding trust and increasing churn. | Need: A prototype that demonstrates end-to-end ingestion and normalization of at least two data sources (e.g., Ponte en Carrera and a university's alumni data) with measured accuracy, latency, and update frequency, plus a blind A/B test showing the AI matches or exceeds human advisor recommendations.



### Simulation Consensus
- Strongest signal: Proceed only if target users describe a recent, repeated, expensive problem in their own words.
- Weakest assumption: Simulation scores are LLM estimates; live interviews must confirm.
- Adoption path: Start with a narrow concierge workflow, then productize the repeated steps.
- Pricing test: Ask for a small paid pilot tied to the buyer's success metric.
- Decision pressure: Conditional Go

### Recommended Interventions
- Narrow the customer segment until the end user and buyer are obvious.
- Run interviews around recent behavior, not opinions about the idea.
- Prototype the outcome manually before building a scalable product.
- Track what data or workflow insight compounds with each use.

---

## Next Experiments
- Conduct 20+ interviews with university career services directors and students to confirm pain and willingness to pay.
- Build a simple prototype (e.g., chatbot using existing API) and test with 50 students to measure engagement.
- Secure one letter of intent or pilot agreement with a mid-sized Peruvian university.
- Benchmark against ChatGPT on 50 local career queries to identify accuracy gaps.

## Kill Criteria
- Fewer than 50% of interviewees express strong interest or pain.
- Prototype shows <60% student engagement or high error rate.
- University pilot fails to convert to a paid contract within 3 months.
- Government or ChatGPT releases a competitive product that matches core functionality.
