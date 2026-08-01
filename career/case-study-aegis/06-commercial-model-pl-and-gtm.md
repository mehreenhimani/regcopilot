# 06 — Commercial Model, P&L & Go-to-Market

*Project AEGIS. Two parts: **Part A** is the in-house business case for the AI function. **Part B** packages
the same capability as a consulting practice with its own P&L and BD motion — the shape of a Head of AI role
in a consultancy or venture-builder. All figures are illustrative models.*

---

# PART A — The in-house business case

## 1. Three-year model

| | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| **Benefits** | | | |
| AML triage — analyst hours saved | €172k | €517k | €517k |
| AML triage — backlog clearance & SAR-quality rework avoided | — | €263k | €263k |
| Use case 2 — regulatory Q&A copilot | — | €310k | €310k |
| Use case 3 — credit memo drafting | — | €360k | €640k |
| Use cases 4–6 | — | — | €1,250k |
| **Total benefits** | **€172k** | **€1,450k** | **€2,980k** |
| **Costs** | | | |
| Build (new use cases) | €1,142k | €470k | €290k |
| Run (platform, inference, support, monitoring) | €99k | €185k | €215k |
| Governance & conformity (ongoing) | €100k | €140k | €110k |
| **Total costs** | **€1,342k** | **€795k** | **€615k** |
| **Net** | **−€1,170k** | **+€655k** | **+€2,365k** |
| **Cumulative net** | −€1,170k | −€515k | **+€1,850k** |

**Payback: month 26.** Modelled ROI over three years: **138%.**

Three things I would say about this table before anyone else does:

1. **Year 1 is a loss, and it should be.** Roughly 55% of year-1 cost buys reusable infrastructure —
   gateway, retrieval, evaluation harness, audit logging, review surface, conformity framework. Use cases 2
   and 3 build at 41% of the cost of use case 1 because of it. Any AI business case that shows a year-1
   profit is either not building a platform or is not counting the governance work.
2. **The benefit line is the risk, not the cost line.** Sensitivity analysis
   ([03 §6](03-cost-and-unit-economics.md)) shows the case is insensitive to model pricing and entirely
   sensitive to realised time saved. Benefit tracking is therefore a governed deliverable with a
   pre-go-live measured baseline — not a self-reported number from the sponsor.
3. **I did not claim a financial-crime detection benefit.** Better detection is plausibly the largest real
   value here and it is the one I refused to put in the model, because it cannot be evidenced in the
   timeframe and an unprovable benefit line poisons every other number in the table.

## 2. How benefit is actually tracked

| Benefit | Measurement | Owner | Cadence |
|---|---|---|---|
| Analyst hours saved | Time-to-disposition from the case system, before vs. after, same analyst cohort | Head of AML Ops | Monthly |
| Backlog clearance | Aged-alert count vs. pre-go-live baseline | Head of AML Ops | Monthly |
| SAR-quality rework avoided | Rework rate from QA sampling | MLRO | Quarterly |
| Cost per resolved alert | Instrumented at the gateway | Head of AI | Monthly |

Signed off by the CFO's office quarterly. **The AI function does not self-certify its own benefits** — that
is how AI programmes lose credibility in year two.

---

# PART B — The same capability, as a practice

*How I would build and run a Data & AI unit with its own P&L, client portfolio and team — which is the
commercial shape of the Head of AI roles I am targeting.*

## 3. Positioning

**The proposition:** *We take AI from proof of concept to production inside regulated institutions — and we
own the evidence a supervisor will ask for.*

The market is not short of AI consultancies. It is short of ones that can do both halves of that sentence.
The prevailing pattern is a strategy firm that produces a roadmap it cannot build, or an engineering firm
that ships a demo that Compliance stops. The unit's differentiation is the intersection: **build it, and make
it defensible.**

**Where that comes from concretely:** 14 years inside regulated financial institutions (UBS, Credit Suisse,
Standard Chartered) on AML, credit risk, market risk and post-trade — plus seven AI products designed, built
and shipped hands-on, each with an evaluation framework and a compliance position. That is the credibility to
sit with a CRO and with an engineering team on the same day.

**Target sectors, in priority order:**

| Sector | Why | Entry offer |
|---|---|---|
| **Mid-market banks & payment institutions (DACH)** | EU AI Act + DORA obligations, real budget, no in-house AI function, and my deepest domain credibility | AI Governance Readiness Assessment |
| **Insurance** | Same regulatory pressure, high-volume document and claims work, less crowded | Claims/underwriting document intelligence |
| **RegTech & fintech vendors** | Need to demonstrate EU AI Act conformity to sell into banks — commercial urgency, faster cycles | Conformity pack for their product |
| **Asset & wealth management** | Research, reporting and suitability workloads with clear governance boundaries | Advisory copilot with audit trail |

**Deliberately not chased in year 1:** healthcare and public sector. Different regulatory literacy, longer
cycles, and no reference base. A new practice wins by being *the obvious choice* in a narrow segment, not a
plausible option in six.

## 4. Offer portfolio

A new unit needs a ladder: something cheap to say yes to at the top, something that pays the bills in the
middle, something that compounds at the bottom.

| # | Offer | Shape | Price | Purpose |
|---|---|---|---|---|
| 1 | **AI Governance Readiness Assessment** | Fixed fee, 4 weeks: AI inventory, EU AI Act classification of the estate, gap analysis, prioritised remediation plan | €38–55k | **The wedge.** Cheap, urgent, board-visible, produces the finding that justifies offer 2 or 3 |
| 2 | **AI Use-Case Portfolio & Operating Model** | Fixed fee, 6 weeks: intake funnel, scoring model, portfolio triage, operating model, business case for the top 3 | €65–90k | Converts a governance conversation into a funded programme |
| 3 | **0→1 Build** | T&M or fixed-price phases, 4–9 months: architecture, build, evaluation, conformity pack, production | €350k–1.4m | **The revenue engine.** Everything in this case study. |
| 4 | **AI Assurance & Evaluation** | Fixed fee or retainer: independent evaluation of a client's existing AI system — quality, guardrails, conformity, unit economics | €45–70k | Sells to the *second* line. Different buyer, different budget, no competition with their build partner. |
| 5 | **Managed AI Run** | Annual retainer: monitoring, evaluation regression, drift management, model migration, conformity maintenance | €90–180k p.a. | **The compounding line.** Recurring, high-margin, and the reason clients don't leave. |

**The strategic point about offer 5.** A consultancy that only builds has to re-win every year. AI systems
need continuous evaluation, drift management and model migration by regulatory obligation, not by preference
— which makes the run retainer an easy sell, not an upsell. Every build should be sold with the run attached
from the first proposal, because retrofitting it after go-live is a much harder conversation.

## 5. BD motion

A first-time practice has no brand and no reference base. The motion has to generate proof, not just leads.

**Sequence:**

1. **Publish the method, not the pitch.** The EU AI Act conformity mapping, the risk register template, the
   cost-per-outcome model — published openly. Regulated-market buyers are looking for someone who has
   clearly done this before; showing the artefacts is more persuasive than describing them. This is the
   cheapest credible pipeline source available to a new unit, and it is what my public AI portfolio already
   does.
2. **Lead with the assessment, not the build.** €45k with a 4-week payback in board comfort is an easy
   internal approval. €600k is a procurement process. Land the assessment; the finding sells the build.
3. **Sell to Risk as well as to the business.** The business sponsor wants the outcome; the CRO controls
   whether it ships. Practices that only court the business lose at the last gate. **The assurance offer
   exists specifically to open the Risk door**, and a CRO who has bought from you once will sponsor a build.
4. **Mine the group ecosystem before the cold market.** Existing group clients, shared infrastructure and
   parallel ventures are warm introductions with a credibility transfer already in place. A new unit that
   starts with cold outbound while sitting inside a group with an existing client base is leaving the
   cheapest pipeline on the table.
5. **Turn every delivery into two references** — a public case study and a named client reference. No build
   engagement closes without agreeing the reference deliverable up front.
6. **Partner where I am thin.** Specialist evaluation and red-teaming subcontracted in year 1 rather than
   hired. Buys credibility on day one and converts to a hire when the volume justifies it.

**Pipeline model, year 1:** 45 qualified conversations → 14 assessments proposed → 8 assessments won →
4 converted to build → 2 converted to run retainer. The assessment-to-build conversion rate is the number I
would manage the practice on; if it drops below 40% the assessment is being scoped as a report rather than
as a decision.

## 6. Practice P&L

### Year 1 — build the base, expect a small loss

| | Amount |
|---|---|
| **Revenue** | |
| Assessments & operating-model work (8 × ~€52k avg) | €416k |
| Build engagements (2 × ~€185k recognised in-year) | €370k |
| Run retainers (2, part-year) | €35k |
| **Total revenue** | **€821k** |
| **Costs** | |
| Delivery team (4 FTE, fully loaded) | €424k |
| Practice lead | €165k |
| Subcontracted specialists (evaluation, red-team) | €60k |
| Sales, marketing, proposals, events | €45k |
| Tooling, infrastructure, demo environments, licences | €38k |
| Training & certification | €22k |
| Overhead allocation (12% of revenue) | €99k |
| **Total costs** | **€853k** |
| **Contribution** | **−€32k** *(−3.9%)* |

**A small planned loss in year 1 is the correct answer**, and saying so up front is more credible than
promising a profit. The unit is buying three things that do not appear as revenue: two reference case
studies, a reusable delivery asset base (accelerators, templates, evaluation harness, conformity pack), and
a team that has now done it together. A year-1 P&L that breaks even usually means nobody invested in the
assets that make year 2 profitable.

### Years 2–3 — scale on the asset base

| | Year 2 | Year 3 |
|---|---|---|
| Revenue | €1,980k | €3,400k |
| Delivery team | 8 FTE | 13 FTE |
| Blended day rate | €1,320 | €1,410 |
| Utilisation | 72% | 75% |
| Recurring revenue (run retainers) | €290k (15%) | €720k (21%) |
| Total costs | €1,642k | €2,652k |
| **Contribution** | **€338k** *(17.1%)* | **€748k** *(22.0%)* |

**The three levers that move margin**, in order of impact:

1. **Reusable assets** — accelerators, the evaluation harness, the conformity pack template, the risk-register
   library. They raise effective rate on fixed-price work without raising the price. This is why the offer
   ladder is deliberately narrow: five offers delivered repeatedly compound; fifteen bespoke engagements do
   not.
2. **Recurring revenue mix** — run retainers carry the highest margin and de-risk utilisation. Target 20%+ of
   revenue by year 3.
3. **Pyramid shape** — year 1 is deliberately senior-heavy (credibility wins the first deals). Years 2–3
   introduce a junior tier delivering under senior oversight, which is where blended margin comes from.
   Doing this too early destroys the quality reputation the practice is built on; too late caps growth.

## 7. Team & hiring ladder

| | Y1 | Y2 | Y3 | Notes |
|---|---|---|---|---|
| Practice Lead / Head of AI | 1 | 1 | 1 | P&L, BD, governance authority, key-account ownership |
| Principal AI Consultant | 1 | 2 | 3 | Engagement leadership, architecture, client trust |
| AI Engineer | 2 | 3 | 5 | Build |
| AI Risk & Governance Lead | 1 | 2 | 2 | **First hire.** Conformity, assurance offer delivery |
| AI Product Manager | — | 1 | 2 | Discovery, adoption, value realisation |
| Junior Consultant / Analyst | — | — | 3 | Margin tier, introduced only once delivery is repeatable |
| Subcontracted specialists | 2 | 2 | 1 | Converts to hires as volume justifies |

**Why the risk and governance lead is hire number one in a consulting practice too:** it is the
differentiator. Every competitor can hire AI engineers. The ability to hand a client a conformity pack their
Second Line accepts is what wins the deal and what justifies the rate — and it is what turns a build client
into an assurance and run client.

**Hiring principle:** I hire for one of three things — domain credibility in regulated financial services,
hands-on AI build capability, or governance depth. Candidates with two are rare and are hired immediately.
Nobody is hired for AI enthusiasm without one of the three.

## 8. What I would commit to in the first year

| Commitment | Measure |
|---|---|
| A funded, governed practice with a live offer portfolio | 5 offers, priced, with delivery assets |
| Pipeline built from a standing start | 45 qualified conversations, 8 assessments won |
| Revenue | €800k+ |
| Reference base | 2 publishable case studies, 2 named references |
| Recurring revenue established | 2 run retainers signed |
| Team | 4 delivery FTE hired and productive, first hire = governance |
| Reusable asset base | Evaluation harness, conformity pack template, risk-register library, cost model |
| Contribution | Break-even ±5% — with the investment case for the gap stated up front |
