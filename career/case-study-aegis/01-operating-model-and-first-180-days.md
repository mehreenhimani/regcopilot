# 01 — Operating Model & First 180 Days

*Project AEGIS. Figures are illustrative targets modelled on realistic mid-market European bank parameters.*

---

## 1. The problem with the starting position

Three months before I arrived, the bank had no AI function but plenty of AI. An informal survey found
**14 GenAI systems in some state of use**: two vendor products procured through business budgets without ICT
risk review, four browser-based tools used with customer data, five internal prototypes on personal API keys,
and three genuinely useful automations nobody could explain the failure modes of.

This is the normal starting state, and it defines the first job. It is not "pick a use case." It is
**establish the inventory, the risk position and the decision rights** — because every week that passes adds
systems you will later have to unwind, and because under the EU AI Act you cannot claim compliance for
systems you cannot enumerate.

---

## 2. Operating model

### 2.1 Decision rights

The single most common failure in AI functions is ambiguity about who can say yes and who can say no. I set
four decision gates with named owners:

| Gate | Question | Decision owner | Advisory |
|---|---|---|---|
| **G0 — Intake** | Is this a real problem worth AI? | Head of AI | Business sponsor |
| **G1 — Risk classification** | What is this under the EU AI Act / DORA / GDPR? | Chief Risk Officer (2LoD) | Head of AI, DPO, Legal |
| **G2 — Build approval** | Do we fund it, and at what autonomy level? | AI Council | Head of AI, CFO |
| **G3 — Production release** | Does it pass evaluation, guardrails, conformity? | Head of AI **jointly with** 2LoD | Internal Audit (observer) |

The important asymmetry: **the Head of AI owns G0 and, jointly, G3. The Second Line owns G1 and can veto at
any gate.** An AI leader who can approve their own system into production in a regulated firm has a
governance design problem, not a power problem. Making 2LoD a joint signatory at G3 was what got the CRO to
sponsor the function rather than police it.

### 2.2 The AI Council

Meets monthly, 60 minutes, standing agenda. Members: CRO (chair), Head of AI, CTO, DPO, Head of Compliance,
COO, CFO representative. Internal Audit attends as observer.

Standing agenda:
1. Portfolio status — what's in flight, what's blocked, what's burning budget
2. New intake decisions (G2)
3. Risk register deltas and open incidents
4. Spend against budget and unit-cost trend
5. Regulatory horizon — what changed in the last month

Deliberately not on the agenda: technology choices, model selection, architecture. Those are mine. Councils
that debate model choice become architecture-review boards and stop making the decisions only they can make.

### 2.3 The three-line model, applied to AI

| Line | Owns | In practice |
|---|---|---|
| **1LoD — AI function + business** | Building it, running it, monitoring it, first-line controls | My team owns evaluation, guardrails, monitoring, incident response |
| **2LoD — Risk & Compliance** | Independent challenge, risk classification, control effectiveness | Owns G1; independently reviews the evaluation methodology, not just the results |
| **3LoD — Internal Audit** | Assurance over the whole framework | Observer at Council; annual audit of the AI framework itself |

The line I fought for: **2LoD must review the evaluation methodology, not just the pass/fail numbers.** A
first line that designs its own test and reports its own score is not a control.

---

## 3. Use-case intake and triage

### 3.1 The funnel

```
Intake (anyone, 1-page form)
   → 23 candidates
   ↓ G0: is this a real problem? is AI the right tool?
   → 15 qualified
   ↓ G1: risk classification by 2LoD
   → 11 within risk appetite  (2 prohibited-adjacent, 2 deferred pending DPIA)
   ↓ Scoring: value × feasibility ÷ risk
   → 6 funded for the year, 1 selected as first build
```

The intake form is one page and asks four things: what decision or task is this, who does it today and how
long does it take, what happens when it goes wrong, and what data does it need. Anything longer gets filled
in by the AI team on the requester's behalf, and anything that cannot answer question three does not proceed.

### 3.2 The scoring model

Standard RICE does not work for regulated AI because it has no risk term and treats confidence as a proxy for
feasibility. I used a modified score:

**Priority = (Value × Confidence × Strategic fit) ÷ (Effort × Risk multiplier)**

| Dimension | Scale | Notes |
|---|---|---|
| **Value** | € annualised | Hours saved × loaded rate, or loss avoided, or revenue enabled. Must be sponsor-signed. |
| **Confidence** | 0.3 / 0.6 / 0.9 | Is the value estimate anecdotal, sampled, or measured? |
| **Strategic fit** | 0.5 – 1.5 | Does it build reusable capability (retrieval, eval harness, gateway) or is it a one-off? |
| **Effort** | person-months | **Including data access work**, which is where estimates break |
| **Risk multiplier** | 1.0 / 1.8 / 3.5 / ∞ | Minimal / Limited / High-risk under EU AI Act / Prohibited |

The risk multiplier is the part that makes it an *AI* prioritisation model. A high-risk use case is not
forbidden — it carries a 3.5× effort weighting because conformity assessment, technical documentation,
post-market monitoring and human oversight design are real, expensive work. Making that visible at intake
stopped the recurring argument about why "the same thing" cost four times as much in Compliance as in
Marketing.

### 3.3 Why AML alert triage won

| | Value | Conf. | Fit | Effort | Risk | Score |
|---|---|---|---|---|---|---|
| **AML alert triage** | €780k | 0.9 | 1.4 | 9 pm | 1.8 | **60.7** |
| Regulatory Q&A copilot | €310k | 0.6 | 1.5 | 5 pm | 1.0 | 55.8 |
| Credit memo drafting | €640k | 0.6 | 1.2 | 8 pm | 3.5 | 16.5 |
| Customer service agent | €1.2m | 0.3 | 0.9 | 12 pm | 3.5 | 7.7 |
| Onboarding KYC decisioning | €920k | 0.6 | 1.1 | 14 pm | 3.5 | 12.4 |
| Internal HR assistant | €95k | 0.9 | 0.6 | 3 pm | 1.0 | 17.1 |

The customer service agent had the biggest headline number and was the executive favourite. It scored sixth:
low confidence in the value estimate, high-risk classification, longest build, and least reusable capability.
Being able to show *why* on one slide — rather than saying "not yet" — is most of what stakeholder alignment
actually is.

**The second-order reason AML triage won:** it forced us to build the reusable spine — retrieval over
internal systems, the model gateway, the evaluation harness, the audit-log service, the human review surface.
Use cases 2 and 3 inherit all five. Choosing the first use case is really choosing what infrastructure you
build.

---

## 4. Org design

### 4.1 Target team (end of year 1)

| Role | FTE | Why this role exists |
|---|---|---|
| Head of AI | 1 | Strategy, governance, delivery, commercial |
| AI/ML Engineer | 2 | Agent orchestration, retrieval, gateway, guardrails |
| Data Engineer | 1.5 | Source-system access, pipelines, permissioning — the actual critical path |
| AI Product Manager | 1 | Use-case discovery, requirements, adoption, value tracking |
| AI Risk & Governance Lead | 1 | Conformity artefacts, risk register, 2LoD interface, audit readiness |
| MLOps / Platform | 0.5 | CI/CD, observability, cost instrumentation |
| **Partner (contracted)** | 2 | Specialist evaluation build + penetration/red-team testing |

**The hire I made first and would make first again: the AI Risk & Governance Lead.** Not an engineer. In a
regulated institution, the constraint on shipping is never model capability — it is the ability to produce
credible evidence at the pace the build moves. Hiring that role first meant conformity artefacts were written
alongside the build rather than reconstructed afterwards.

**The hire I under-sized: data engineering.** Budgeted at 1 FTE, needed 1.5, and the half-FTE gap was the
single largest source of schedule slip.

### 4.2 Federated, not centralised

The AI function does not build everything. It owns the platform, the governance and the standards; business
units own their use cases and their value realisation. Concretely:

- **Central:** model gateway, retrieval infrastructure, evaluation harness, guardrail library, audit logging,
  risk classification, conformity artefacts, cost controls, standards and patterns.
- **Federated:** use-case identification, domain evaluation content (business SMEs write the golden-set
  answers), adoption, benefit tracking.

This is the model that scales past three use cases. A fully centralised team becomes a queue; a fully
federated one recreates the shadow estate you just cleaned up.

---

## 5. The first 180 days

### Days 1–30 — Establish the facts

- Complete AI inventory of the shadow estate (14 systems found; 3 shut down immediately — customer data in
  consumer-tier tools with no DPA)
- 22 stakeholder interviews across Risk, Compliance, Ops, IT, and three business units
- Draft AI policy: acceptable use, prohibited categories, intake requirement, procurement gate
- Baseline: current AI spend (€180k/yr, entirely uncontrolled, across four cost centres)
- **Deliverable to the board:** the inventory and the risk exposure. Not a strategy. Establish credibility on
  facts before asking for money.

### Days 31–60 — Establish the machinery

- AI Council chartered and first meeting held
- Intake funnel and scoring model live; 23 candidates logged
- Risk classification framework agreed with 2LoD and signed off
- Model gateway procurement started (long lead time — start it early)
- Two hires opened: AI Risk & Governance Lead, AI/ML Engineer

### Days 61–90 — Decide and fund

- G1 and G2 completed on the full candidate list; 6 use cases funded
- AEGIS Assist selected; risk classification confirmed as limited-risk assistive with Art. 14 oversight
- Architecture and model strategy approved by Risk Committee
- Year-1 budget approved: €1.34m
- Team at 4

### Days 91–135 — Build the spine

- Model gateway live; all shadow API usage migrated behind it (spend now visible and capped)
- Retrieval layer over 5 source systems — the long pole
- Golden set v1 built **with the AML analysts** (240 cases)
- Guardrail layer and audit-log service
- First internal demo at day 118; deliberately *not* to the board

### Days 136–180 — Prove and ship

- Shadow mode: agent runs on live alerts, output visible to the AI team only, compared against analyst
  decisions for 4 weeks
- Evaluation gates passed; conformity pack completed and reviewed by 2LoD and Internal Audit
- Pilot with 4 of 12 analysts, then full rollout
- Production release at month 9 with joint G3 sign-off
- Post-market monitoring live from day one of production

**The four weeks of shadow mode were the most valuable in the programme.** They produced the real
false-positive baseline, exposed two retrieval failure modes that the golden set had missed, and — most
importantly — gave the analysts four weeks to see the system be right before they were asked to rely on it.
Adoption is a trust problem, and trust is built with evidence over time, not with a launch.
