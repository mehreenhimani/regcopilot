# 02 — Architecture & Model Strategy

*Project AEGIS. Figures are illustrative targets modelled on realistic parameters.*

---

## 1. Reference architecture

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ANALYST REVIEW SURFACE  (the product — Art. 14 human oversight)         │
│  recommendation · reasoning · every claim clickable to source ·          │
│  agree / override + reason · escalate                                    │
└───────────────────────────────┬──────────────────────────────────────────┘
                                │
┌───────────────────────────────▼──────────────────────────────────────────┐
│  GUARDRAIL LAYER — 3 layers, evaluated on every turn                     │
│  L1 input:  PII scope check · prompt-injection screen · scope validation │
│  L2 tool:   allowlist · argument validation · rate + budget limits       │
│  L3 output: citation verification · unsupported-claim detection ·        │
│             confidence floor · prohibited-language filter                │
└───────────────────────────────┬──────────────────────────────────────────┘
                                │
┌───────────────────────────────▼──────────────────────────────────────────┐
│  AGENT ORCHESTRATION — bounded investigation loop                        │
│  max 12 tool calls · max 6 turns · hard token budget · 90s wall clock    │
│  plan → gather → reconcile → score → draft → self-check                  │
└──────┬──────────────────────┬─────────────────────┬──────────────────────┘
       │                      │                     │
┌──────▼───────┐   ┌──────────▼──────────┐   ┌──────▼───────────────────┐
│ TOOL SURFACE │   │ RETRIEVAL           │   │ MODEL GATEWAY            │
│ 7 read-only  │   │ hybrid: BM25 +      │   │ routing cascade ·        │
│ tools        │   │ vector · policy &   │   │ caching · cost metering ·│
│ (§2)         │   │ typology corpus     │   │ provider abstraction     │
└──────┬───────┘   └──────────┬──────────┘   └──────┬───────────────────┘
       │                      │                     │
┌──────▼──────────────────────▼─────────────────────▼──────────────────────┐
│  SOURCE SYSTEMS (read-only, permissioned)                                │
│  Core banking · TM engine · KYC/CDD · Sanctions & PEP · Case management  │
└──────────────────────────────────────────────────────────────────────────┘
                                │
┌───────────────────────────────▼──────────────────────────────────────────┐
│  IMMUTABLE AUDIT LOG  (write-before-surface — EU AI Act Art. 12)         │
│  alert id · every tool call + args + result hash · retrieved chunk ids · │
│  model id + version · prompt hash · full output · guardrail verdicts ·   │
│  human decision + reason · latency · token + cost                        │
└──────────────────────────────────────────────────────────────────────────┘
```

**The non-negotiable design rule: the audit record is written before the recommendation is surfaced to the
analyst.** If logging fails, the system fails closed and the alert routes to manual handling. An AI system in
a regulated environment that can produce an output it cannot evidence is worse than one that is unavailable.

---

## 2. Agent design

### 2.1 Tool surface — all read-only, by design

| Tool | Purpose | Notes |
|---|---|---|
| `get_customer_profile` | KYC/CDD record, risk rating, ownership structure | Field-level redaction by analyst entitlement |
| `get_transaction_history` | Windowed transactions, configurable lookback | Hard row cap; forces the agent to narrow |
| `get_counterparty_exposure` | Aggregate exposure and relationship graph, 2 hops | Depth capped to bound cost |
| `check_sanctions_pep` | Sanctions/PEP screening status | Returns status, never re-screens |
| `get_prior_alerts` | Prior alerts on this customer and their dispositions | The single highest-value tool for precision |
| `search_typologies` | RAG over FATF/BaFin typologies and internal policy | Hybrid retrieval; citations mandatory |
| `search_adverse_media` | Vetted media sources only | Allowlisted sources; no open web |

**No tool writes.** The agent cannot close an alert, file a SAR, contact a customer, or modify a record. This
is the architectural expression of the risk classification, and it is what keeps the system assistive rather
than decisioning. When the business asked for auto-close on low-risk alerts in month 7, the answer was: that
is a different system, with a different EU AI Act classification, requiring a new conformity assessment and a
new G2 decision. Scope creep in AI autonomy is a compliance event, not a backlog item.

### 2.2 Bounded exploration

The agent runs a fixed loop with hard ceilings: **12 tool calls, 6 turns, a per-alert token budget, and a
90-second wall clock.** Exceeding any ceiling routes the alert to manual handling with the partial trace
attached — a graceful degradation, not an error.

The ceilings exist for three reasons and I would defend all three: **cost** (unbounded agents have unbounded
unit economics), **latency** (an analyst assistant that takes four minutes gets bypassed), and **auditability**
(a trace a human can read in two minutes is evidence; a 60-step trace is not).

Tuning to 12 was empirical: the 95th percentile of successful investigations used 9 tool calls. Setting the
cap at the p95 plus headroom bounds cost without truncating real work.

### 2.3 Why not a fixed pipeline, and why not full autonomy

| Approach | Why rejected |
|---|---|
| **Fixed deterministic pipeline** | Alert investigation is conditional — which system you query next depends on what the last one returned. A fixed pipeline either over-fetches every source (expensive, noisy context degrades output quality) or under-fetches and misses the material fact. |
| **Single large prompt with all context** | Context stuffing degrades precision on long contexts and makes cost proportional to the worst case for every alert, not the actual case. |
| **Fully autonomous agent, auto-disposition** | Higher EU AI Act obligations, no analyst trust, no path to sign-off in 9 months, and — genuinely — not better. The analysts' judgement on ambiguous cases outperformed anything we could evaluate. |
| **Fine-tuning a model on prior dispositions** | Cannot guarantee citation to source; prior dispositions encode prior bias; retraining cadence unworkable under a monitoring obligation; and the model becomes the system of record, which is exactly what you cannot audit. |

**Bounded agentic + retrieval + mandatory citation** was the only option that satisfied the cost, latency,
quality and evidence constraints simultaneously.

---

## 3. Build vs buy

| Layer | Decision | Rationale |
|---|---|---|
| Foundation model | **Buy** | Commodity input, improving fast, no defensible advantage in owning it |
| Model gateway | **Buy + wrap** | Commercial gateway wrapped in a thin internal interface we control |
| Agent orchestration | **Build** | This is where domain logic and bounded autonomy live — our differentiation |
| Retrieval / indexing | **Build on managed infra** | Managed vector store; retrieval strategy and chunking are ours |
| Guardrails | **Build (with bought components)** | Bought PII detection and injection screening; built the domain-specific output checks |
| Evaluation harness | **Build** | No vendor knows what a good AML investigation looks like at this bank |
| Audit logging | **Build** | Must map exactly to our Art. 12 position; too important to depend on a vendor's schema |
| Analyst review surface | **Build** | It *is* the product |

**The principle: buy the commodity, build the evidence.** Anything a regulator will ask us to justify, we
own. Anything that is a fungible input, we rent — and we make sure we can switch supplier.

---

## 4. Model gateway and provider strategy

### 4.1 Why a gateway on day one

Every model call goes through an internal gateway. It gives us five things, and four of them are governance:

1. **Provider abstraction** — switching model or provider is a config change, not a rebuild
2. **Cost metering** — per-request cost attributed to use case, team and tenant (see [03](03-cost-and-unit-economics.md))
3. **Routing** — the cascade that drives unit economics
4. **Caching** — prompt caching at the gateway, transparent to callers
5. **Policy enforcement** — no unapproved model, no unapproved region, no call without an audit record

The fifth is the one that matters most in a regulated firm. Without a gateway, "which models are we using and
where does the data go" is an answer you assemble by asking people. With one, it is a query.

### 4.2 Model selection

Selection was on **cost per resolved alert at acceptable quality**, not benchmark scores. We ran the golden
set against candidates and measured quality, latency and cost together. The current configuration (Anthropic
Claude family, EU data residency, enterprise agreement with zero-retention terms):

| Tier | Model | List price (per MTok in / out) | Used for |
|---|---|---|---|
| Triage | `claude-haiku-4-5` | $1.00 / $5.00 | Alert classification, routing, structured extraction |
| Workhorse | `claude-sonnet-5` | $3.00 / $15.00 | Standard investigations (~78% of alerts) |
| Escalation | `claude-opus-5` | $5.00 / $25.00 | Complex multi-entity cases, ambiguous typologies |

Pricing as published at time of writing; verify current rates before committing a business case. Prompt-cache
reads price at roughly 0.1× base input, cache writes at 1.25×; the Batch API runs at 50% for non-urgent work.
Those three mechanics do most of the work in [03](03-cost-and-unit-economics.md).

### 4.3 Selection criteria beyond price and quality

For a regulated buyer these are not tie-breakers, they are gates:

| Criterion | Why it gates |
|---|---|
| **EU data residency** | GDPR Ch. V transfer position; supervisory expectation |
| **Zero data retention / no training on our data** | Contractual, not policy-page. Written into the MSA. |
| **Enterprise agreement with an entity we can contract with** | DORA requires a contractual counterparty with defined obligations |
| **Auditability of model versions** | Art. 12/15 — we must be able to state which model version produced which output, and pin it |
| **Deprecation notice period** | A provider that can retire your model in 30 days is an operational-resilience risk |
| **Subprocessor transparency** | DORA ICT third-party register requires the chain, not just the vendor |
| **Availability of a credible second source** | Exit strategy is a DORA obligation, not a preference |

We disqualified two otherwise-strong providers on retention terms and one on deprecation notice period. In a
regulated context, **contract terms are an architectural constraint.**

---

## 5. DORA third-party risk and exit strategy

The model provider is a **critical ICT third-party service provider** and is registered as such. The
obligations that shaped the architecture:

| DORA requirement | How the architecture satisfies it |
|---|---|
| ICT third-party register | Provider, subprocessors, data flows, criticality rating, contract references |
| Contractual provisions (audit rights, SLAs, incident notification, exit) | Negotiated into the MSA before build started, not after |
| Concentration risk assessment | Documented; mitigated by the gateway making substitution feasible |
| **Documented, tested exit strategy** | See below — this is the one most firms leave as a paragraph |
| Incident reporting | AI incidents in scope of the ICT incident taxonomy; runbook in [05](05-evaluation-guardrails-and-incident-response.md) |
| Resilience testing | Provider outage and degradation scenarios in the annual test plan |

**The exit strategy, made real.** A paragraph saying "we could switch providers" is not an exit strategy. Ours
is three concrete things:

1. **The gateway** makes provider substitution a configuration change with no application-code change.
2. **The evaluation harness** is provider-agnostic, so we can quantify — before switching — exactly what
   quality change a substitute produces on our golden set. This turns "could we switch" into "here is what it
   would cost us in quality and unit economics."
3. **We test it.** Once a quarter we run the full golden set against the designated second-source model and
   report the delta to the Risk Committee. In the last test the substitute passed all hard gates with a
   4-point drop on the composite quality score and a 9% increase in cost per resolved alert — an acceptable,
   *known* degradation, which is the entire point.

That quarterly test is the single cheapest piece of regulatory credibility in the programme.

---

## 6. Data protection position

- **No customer personal data leaves the EU.** Provider endpoints are EU-resident; contractually confirmed.
- **Zero retention** contractually agreed; no training on our data.
- **Minimisation at the tool layer** — tools return only fields required for the investigation; entitlement
  is enforced at the tool, not by prompting the model. Prompting is not an access control.
- **Pseudonymisation where it doesn't degrade the task** — names and account numbers are tokenised in the
  typology-search path, where they add nothing.
- **DPIA completed** before build, covering the agent, the retrieval corpus and the audit log.
- **No Art. 22 automated decision** — a human decides every alert. This is documented and architecturally
  enforced by the read-only tool surface, not merely asserted.

Detail in [04 — Risk Register & EU AI Act Conformity](04-risk-register-and-eu-ai-act-conformity.md).
