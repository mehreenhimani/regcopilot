# Project AEGIS — Building an Enterprise AI Function From Zero

### A 0→1 Head of AI case study: from no AI capability to a regulated agentic product in production, in 9 months

> **What this document is.** A complete reference case study for a Head of AI mandate — the artefacts,
> decisions and numbers a Head of AI is actually accountable for. It is written as a portfolio and interview
> reference: the operating model, governance mapping, architecture, cost model, risk register and commercial
> model are all real, reusable frameworks, and the financial and performance figures are **illustrative
> targets modelled on realistic mid-market European bank parameters**, not reported results from a completed
> engagement. Use it to structure how you talk about 0→1 AI leadership, and as the blueprint to build against.
> Where figures come from live products, they are marked and linked.

---

## The mandate

**Client:** European mid-market bank. ~€4.2bn assets, ~2,800 staff, operations in Germany and Austria,
regulated by BaFin and the ECB (SSM), in scope for **EU AI Act**, **DORA**, **GDPR** and **AMLD6**.

**Situation at start:** No AI function. Roughly 14 shadow-IT GenAI experiments running across business units
with no inventory, no risk classification and no procurement oversight. The board had approved an AI budget
in principle but had rejected two prior proposals because neither answered the two questions the CRO kept
asking: *how do we prove this thing to a regulator, and what does it cost per decision?*

**The mandate I was given:**

1. Stand up an AI function — operating model, governance, team, and an approved use-case portfolio.
2. Get the shadow estate under control before the EU AI Act's high-risk obligations bite.
3. Ship one production AI product that proves the model works, end to end, including conformity evidence.
4. Do it inside an approved budget, with a defensible business case for year two.

**Why this matters more than a demo:** anyone can build a GenAI proof of concept. The hard part in a
regulated institution is the path from *demo* to *a system the Second Line, Internal Audit and the regulator
will all sign off on* — and doing it at a unit cost that survives contact with a CFO.

---

## What I delivered

| Outcome | Target | Where it's covered |
|---|---|---|
| AI operating model — AI Council, intake funnel, RACI, decision rights | Live in 60 days | [01 — Operating Model](01-operating-model-and-first-180-days.md) |
| AI inventory & risk classification of the shadow estate | 14 systems classified, 3 shut down | [01](01-operating-model-and-first-180-days.md) · [04 — Risk & Conformity](04-risk-register-and-eu-ai-act-conformity.md) |
| Use-case portfolio triaged by value × risk × feasibility | 23 candidates → 6 funded | [01](01-operating-model-and-first-180-days.md) |
| Model & vendor strategy incl. DORA third-party position and exit plan | Approved by Risk Committee | [02 — Architecture & Model Strategy](02-architecture-and-model-strategy.md) |
| **AEGIS Assist** — agentic AML alert triage in production | Live month 9 | [02](02-architecture-and-model-strategy.md) · [05 — Eval & Guardrails](05-evaluation-guardrails-and-incident-response.md) |
| Cost-per-resolved-alert model and FinOps controls | €0.19 → €0.07 per alert | [03 — Cost & Unit Economics](03-cost-and-unit-economics.md) |
| EU AI Act conformity pack + DORA register entries | Audit-ready | [04](04-risk-register-and-eu-ai-act-conformity.md) |
| Evaluation harness, guardrails, incident runbook | Gates every release | [05](05-evaluation-guardrails-and-incident-response.md) |
| Three-year business case and practice P&L | €1.85m cumulative net, payback month 26 | [06 — Commercial Model & P&L](06-commercial-model-pl-and-gtm.md) |
| Team | 1 → 9 (7 FTE, 2 partner) | [01](01-operating-model-and-first-180-days.md) · [06](06-commercial-model-pl-and-gtm.md) |

---

## The product: AEGIS Assist

**Problem.** The AML operations team received ~4,100 transaction-monitoring alerts a month from a rules-based
engine. Roughly 92% were false positives. Twelve analysts spent most of their week gathering the same context
— customer profile, transaction history, counterparty exposure, adverse media, prior alert outcomes — before
they could form a view. Median time-to-disposition was 34 minutes; the backlog was structural, not seasonal.

**What AEGIS Assist does.** It does *not* decide. It is an agentic **investigation assistant**: for each
alert it gathers evidence across five systems, reconstructs the narrative, cites every fact to its source,
scores the alert on a calibrated risk scale, and drafts a disposition recommendation with reasoning. A human
analyst always makes the call. Every retrieval, tool call, model version, prompt hash and human decision is
written to an immutable audit log before the recommendation is surfaced.

**Why agentic rather than a single prompt.** Alert investigation is genuinely multi-step and
context-dependent: which systems you query depends on what the first query returns. A fixed pipeline either
over-fetches (expensive, noisy context) or under-fetches (misses the material fact). A bounded agent with a
tool budget explores conditionally — and, critically, produces a **trace** that is itself the audit evidence.

**Why it stayed a Tier-2 system, deliberately.** Under the EU AI Act, an AI system that *makes* AML
decisions carries substantially heavier obligations than one that *assists* a human who decides. We scoped
autonomy down on purpose: the agent cannot close an alert, cannot file a SAR, cannot contact a customer.
That single design decision — made in week 3, before a line of code — is why the conformity work took
6 weeks rather than 6 months. **The governance position drove the architecture, not the other way round.**

**Modelled results at month 9 (steady state):**

| Metric | Baseline | Target | Guardrail |
|---|---|---|---|
| Median time to disposition | 34 min | 11 min | — |
| Analyst hours / month on triage | 1,870 | 640 | — |
| False-positive rate reaching analyst review | 92% | 61% | Must not rise |
| Citation accuracy (facts traceable to source) | n/a | ≥ 98% | Hard gate |
| Unsupported-claim rate ("hallucination") | n/a | 0% surfaced | Hard gate — blocks release |
| Analyst override rate | n/a | 12–18% | Below 5% = automation bias; above 30% = model not trusted |
| Cost per resolved alert | €0 (labour only) | €0.07 | Cap €0.15 |
| Audit-log completeness | n/a | 100% | Hard gate |

Note what is *not* in that table: no "accuracy" headline, and no claim about detecting more financial crime.
Both would have been unprovable in nine months and indefensible in front of a regulator. We measured what we
could evidence.

---

## The five decisions I'd defend in any interview

**1. Governance before architecture.** We classified the system under the EU AI Act and wrote the human
oversight design *before* choosing a model or a framework. The risk classification then constrained every
downstream choice — autonomy level, logging depth, data residency, evaluation thresholds. Teams that build
first and govern afterwards rebuild. ([04](04-risk-register-and-eu-ai-act-conformity.md))

**2. Buy the model, own the orchestration, own the evaluation.** Foundation models are a commodity input and
will keep getting cheaper and better; our differentiation is in retrieval quality, guardrails, domain
evaluation and audit evidence. We abstracted the model behind an internal gateway from day one so switching
providers is a config change — which is also the DORA exit-strategy requirement.
([02](02-architecture-and-model-strategy.md))

**3. Cost per resolved alert, not cost per token.** Token price is an input, not a metric. Optimising it in
isolation produces cheap models that fail more and cost more in human rework. We instrumented cost per
*outcome* and used a routing cascade — a cheap model triages, an expensive model handles the hard 22% — plus
prompt caching and batch processing for non-urgent work. Result: a **63% reduction in cost per resolved
alert** with no measured quality loss. ([03](03-cost-and-unit-economics.md))

**4. Human-in-the-loop as a product feature, not a compliance tax.** Art. 14 oversight is often bolted on as
a checkbox. We designed the analyst review surface as the primary product: recommendation with reasoning,
every claim clickable to source, one-click agree/override, and override reasons fed straight back into the
evaluation set. Compliance obligation and product feedback loop are the same mechanism.
([05](05-evaluation-guardrails-and-incident-response.md))

**5. Evaluation is infrastructure, not a phase.** A 240-case golden set built with the AML analysts
themselves, LLM-as-judge for scale plus human adjudication on a sampled subset, regression gates in CI, and
online drift monitoring. No model, prompt or retrieval change ships without passing. This is what makes the
system *maintainable* under a regulation that requires ongoing accuracy monitoring.
([05](05-evaluation-guardrails-and-incident-response.md))

---

## What I'd do differently

- **I under-resourced data engineering in the first plan.** Roughly 40% of build effort went into getting
  clean, permissioned access to five source systems. AI programme plans that budget for model work and treat
  data access as a given are wrong; I now size data access as the critical path.
- **I introduced the AI Council two weeks too late.** Three shadow experiments got further along than they
  should have while we were still defining decision rights. Governance forums should exist before you need
  them.
- **The first evaluation set was built by the AI team, not the analysts.** It measured what we thought good
  looked like. Rebuilding it with the AML analysts changed roughly a third of the expected answers — and
  changed how much I trusted the first month of results.
- **I should have priced the second use case during the first.** Coming back to the CFO with a fresh business
  case for use case #2 cost six weeks. Fund the portfolio, not the project.

---

## Contents

| # | Document | What's in it |
|---|---|---|
| 01 | [Operating Model & First 180 Days](01-operating-model-and-first-180-days.md) | Mandate, AI Council and decision rights, intake funnel, use-case triage scoring, org design and hiring plan, 30/60/90/180-day plan |
| 02 | [Architecture & Model Strategy](02-architecture-and-model-strategy.md) | Reference architecture, agent design and tool surface, build-vs-buy, model gateway, provider selection, data residency, DORA exit strategy |
| 03 | [Cost & Unit Economics](03-cost-and-unit-economics.md) | Token economics, cost-per-outcome model, routing cascade, caching and batching, cost guardrails, sensitivity analysis |
| 04 | [Risk Register & EU AI Act Conformity](04-risk-register-and-eu-ai-act-conformity.md) | Risk classification, article-by-article conformity mapping, DORA and GDPR positions, full risk register with owners and controls |
| 05 | [Evaluation, Guardrails & Incident Response](05-evaluation-guardrails-and-incident-response.md) | Golden sets, LLM-as-judge design, three-layer guardrails, release gates, online monitoring, drift, AI incident runbook |
| 06 | [Commercial Model, P&L & GTM](06-commercial-model-pl-and-gtm.md) | Business case, practice P&L, pricing and delivery models, pipeline and BD motion, team economics, year-2 scaling plan |
