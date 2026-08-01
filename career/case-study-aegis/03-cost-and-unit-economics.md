# 03 — Cost & Unit Economics

*Project AEGIS. Model prices are list prices as published at time of writing — verify before committing a
business case. FX assumption: 1 USD = 0.92 EUR. Volumes and token profiles are modelled, not measured.*

---

## 1. The metric that matters

Most AI cost conversations are about **cost per token**. That is an input price, not a metric, and optimising
it in isolation reliably makes things worse: you move to a cheaper model, quality drops, analyst override and
rework rise, and total cost of the decision goes up while your dashboard shows a saving.

The metric I instrumented from day one is **cost per resolved alert** — total inference and platform cost
divided by alerts carried to a disposition the analyst accepted. It has three properties a token metric does
not:

- It goes **up** when quality goes down, because failed investigations get retried or fall back to manual.
- It is directly comparable to the **human cost** of the same outcome (€19.40 per alert at baseline).
- It survives a model price change, a provider switch, and a model upgrade — so the target doesn't need
  rewriting every time the market moves.

Everything below optimises that number.

---

## 2. Token profile of one investigation

An agentic investigation is not one call. The agent loop resends conversation history on every turn, so
**input tokens accumulate across turns** — this is the single most misunderstood driver of agent cost, and
the reason naive agent designs are 5–10× more expensive than expected.

Modelled profile for one standard investigation (6 turns, ~9 tool calls):

| Component | Tokens | Behaviour |
|---|---|---|
| System prompt + agent instructions | 3,200 | Stable across every alert → **cacheable** |
| Tool definitions (7 tools) | 2,400 | Stable → **cacheable** |
| Typology / policy corpus excerpt | 8,400 | Stable per typology class → **cacheable** |
| Alert payload + customer context | 4,100 | Volatile |
| Accumulated tool results across turns | 33,900 | Volatile, and the dominant term |
| Thinking + intermediate reasoning | 3,000 | Volatile |
| **Total input (billed, cumulative)** | **55,000** | |
| **Total output** | **2,800** | Recommendation, reasoning, citations, risk score |

**Naive cost, single-model, no optimisation** (Claude Sonnet 5 at $3.00 / $15.00 per MTok):

```
input   55,000 × $3.00/1M  = $0.1650
output   2,800 × $15.00/1M = $0.0420
                             ───────
                             $0.2070  ≈  €0.19 per alert
```

At 4,100 alerts/month that is **€9,348/year** in inference — already trivially affordable against €780k of
value. The optimisation below is therefore *not* about affordability. It is about two other things that
matter more: **headroom to scale to six use cases on the same budget envelope**, and **proving to the CFO
that the unit economics are understood and controlled** before asking for year-2 funding. An AI leader who
cannot explain their unit cost does not get the second budget.

---

## 3. The optimisation waterfall

| # | Lever | Mechanism | Cost/alert | Δ |
|---|---|---|---|---|
| 0 | Naive baseline | Single model, no caching, full context | €0.190 | — |
| 1 | **Prompt caching** | 14,000-token stable prefix cached; reads at ~0.1× base input | €0.128 | −33% |
| 2 | **Routing cascade** | Haiku triages all; 17% resolve at triage; Sonnet 78%; Opus 5% | €0.096 | −25% |
| 3 | **Batch processing** | 40% of alerts are non-urgent (aged queue) → Batch API at 50% | €0.078 | −19% |
| 4 | **Context budgeting** | Row caps, result summarisation between turns, drop superseded tool output | €0.071 | −9% |
| | **Optimised** | | **€0.071** | **−63%** |

### 3.1 Prompt caching — the highest-leverage single lever

14,000 of the 55,000 input tokens are byte-identical across every alert: system prompt, tool definitions, and
the typology corpus excerpt for the alert's class. Because caching is a **prefix match**, this only works if
those blocks are ordered stably at the front and nothing volatile is interleaved.

Two implementation details that decide whether it works at all:

- **No timestamps, no request IDs, no alert-specific text in the cached prefix.** A single interpolated
  variable invalidates everything after it. Our first implementation put the alert ID in the system prompt
  header "for traceability" and achieved a 0% cache-hit rate for two weeks before anyone noticed. The fix
  was to move it into the first user turn. **Verify with cache-read token counts in the response — do not
  assume.**
- **TTL choice follows the arrival pattern.** At ~5.7 alerts/hour, a 5-minute cache expires between alerts
  most of the time. We use the 1-hour TTL (2× write cost, ~0.1× read) which breaks even at three reads and
  is comfortably positive at our volume. During overnight quiet periods we let it lapse rather than pay to
  keep it warm.

### 3.2 Routing cascade — the highest-leverage architectural lever

Not every alert needs the same model. A cheap triage pass classifies the alert and extracts structured
fields; a meaningful share resolve there.

| Tier | Model | Share | Cost/alert (this tier) |
|---|---|---|---|
| Triage — all alerts | Claude Haiku 4.5 ($1 / $5) | 100% | €0.007 |
| Resolved at triage, no investigation | — | 17% | €0 additional |
| Standard investigation | Claude Sonnet 5 ($3 / $15) | 78% | €0.101 |
| Complex / multi-entity escalation | Claude Opus 5 ($5 / $25) | 5% | €0.189 |

**The escalation tier is not a cost problem — it is a quality investment.** The 5% of alerts that are
genuinely complex are also where the false negatives that matter live. Spending 2.7× more on them is the
correct trade, and being able to say that in cost terms is how you defend it to a CFO who sees only the
per-token gap.

Routing is a classifier, and like any classifier it can be wrong. Two safeguards: the analyst can request an
escalation re-run on any alert with one click (logged and fed into the routing evaluation set), and
**routing accuracy is itself a tracked metric** — under-escalation is a quality risk, not a saving.

### 3.3 Batch processing

Roughly 40% of alerts are aged queue items with no same-hour SLA. These run through the Batch API at 50% of
standard price with a completion window measured in hours. Same model, same prompts, same evaluation gates —
purely a scheduling decision. It is the cheapest 19% in the waterfall and the one most teams never take
because nobody asks the business which work is actually urgent.

### 3.4 Context budgeting

Accumulated tool results are the largest volatile term. Three controls:

- **Hard row caps at the tool layer** — `get_transaction_history` returns at most 200 rows and forces the
  agent to narrow rather than dump.
- **Summarise-and-drop between turns** — once a tool result has been reasoned over, the raw result is
  replaced with the agent's structured extraction. The full raw result stays in the audit log; it just stops
  being resent to the model.
- **Drop superseded results** — if turn 4 re-queries with a narrower window, turn 2's broad result leaves the
  working context.

The audit log keeps everything. **What you log and what you resend to the model are different questions**,
and conflating them is a common and expensive mistake.

---

## 4. Full cost picture — inference is not the cost

This is the point I would make in any Head of AI interview, because it is the one most AI cost discussions
get backwards.

| Cost line (year 1) | Amount | % |
|---|---|---|
| Model inference | €3,500 | 0.3% |
| Platform & infrastructure (gateway, vector store, observability, logging) | €96,000 | 7.2% |
| Data engineering — source-system access, pipelines, permissioning | €310,000 | 23.1% |
| Build — engineering, product, orchestration, guardrails, review surface | €424,000 | 31.6% |
| Governance & conformity — risk lead, conformity pack, DPIA, external review | €188,000 | 14.0% |
| Evaluation — golden set build with SMEs, harness, red-team engagement | €142,000 | 10.6% |
| Change, training, adoption | €78,000 | 5.8% |
| Contingency | €100,000 | 7.5% |
| **Total year 1** | **€1,341,500** | |

**Inference is 0.3% of the cost of the programme.** The expensive parts are getting to the data, proving the
thing works, and proving it to a regulator. Any AI business case that models token spend carefully and treats
data access and conformity as line items to be estimated later is going to be wrong by an order of magnitude
in the direction that ends careers.

The corollary for prioritisation: **optimise the expensive resource.** In year 1 that was data-access
engineering, which is why use case #2 was chosen partly because it reuses four of the same five source
connections.

---

## 5. Cost risk — the failure modes that actually bite

Unit economics are a planning exercise. Cost *risk* is an operational one, and agentic systems have failure
modes that traditional software does not.

| Risk | Mechanism | Control |
|---|---|---|
| **Runaway agent loop** | Agent fails to converge, retries the same tool with variations until context or budget exhausts | Hard ceilings: 12 tool calls, 6 turns, per-alert token budget, 90s wall clock. Breach = route to manual, alert engineering. |
| **Retry storm** | Transient provider error triggers application retries which trigger more retries | Exponential backoff with jitter, circuit breaker at the gateway, retry budget per alert |
| **Prompt-injection-driven spend** | Adversarial content in adverse media or a customer free-text field instructs the agent to loop or fetch repeatedly | L1 injection screening, tool allowlist, per-alert budget is the backstop regardless of cause |
| **Context creep over time** | Prompts and policy corpus grow release over release; unit cost drifts up 2–3% a month unnoticed | Unit cost is a **tracked release gate** — a build that raises cost/alert >10% needs explicit sign-off |
| **Cache invalidation regression** | A well-meaning change interpolates a variable into the cached prefix; cost silently triples | Cache-hit rate monitored and alerted; regression test asserts a minimum hit rate |
| **Model deprecation forcing a rushed migration** | Provider retires the pinned model version at short notice | Contractual notice period; quarterly second-source evaluation means the fallback is pre-tested |
| **Volume shock** | A rules-engine change or a sanctions event triples alert volume overnight | Per-tenant and per-use-case monthly spend caps at the gateway; breach degrades to triage-only mode rather than failing or overspending |
| **Price change** | Provider repricing | Business case built on cost per *outcome* with sensitivity analysis (§6), not on a fixed token price |

**The gateway spend cap is the control I would insist on anywhere.** It converts an unbounded financial
exposure into a bounded, graceful service degradation. Every AI platform should have one before it has its
first production user.

---

## 6. Sensitivity analysis

The business case must survive the market moving. Sensitivities on cost per resolved alert:

| Scenario | Cost/alert | Annual inference | Verdict |
|---|---|---|---|
| Base case | €0.071 | €3,500 | — |
| Model prices +50% | €0.107 | €5,260 | Immaterial |
| Model prices −40% (likely direction) | €0.043 | €2,100 | Upside, don't bank it |
| Alert volume 3× (sanctions event) | €0.071 | €10,500 | Within gateway cap |
| Caching fails entirely | €0.106 | €5,200 | Immaterial to the case; material to hygiene |
| Escalation tier rises to 20% (worse routing) | €0.096 | €4,700 | Immaterial |
| **Analyst time saving 50% below target** | €0.071 | €3,500 | **This is the one that breaks the case** |

**The business case is not sensitive to model pricing. It is entirely sensitive to realised analyst time
saved.** That is why benefit tracking — measured, not asserted, with the baseline captured before go-live —
is a first-class deliverable and not an afterthought. It is also why I would push back on any AI business
case whose risk section is mostly about model costs: that is the variable you can most afford to be wrong
about.

---

## 7. What gets reported, monthly

| Metric | To whom |
|---|---|
| Cost per resolved alert, trend vs. prior 6 months | AI Council, CFO |
| Total AI spend vs. cap, by use case and tenant | AI Council, CFO |
| Cache-hit rate and routing distribution | Engineering |
| Realised analyst hours saved vs. modelled | AI Council, business sponsor |
| Cost per resolved alert vs. human cost per alert | Board (quarterly) |

One page. The board sees two numbers — what it costs us and what it saves us — and the trend on both.
