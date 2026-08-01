# Head of AI — German Market Fit, Regulatory Syllabus & 4-Week Plan

*Researched 1 August 2026. Regulatory positions move fast — every date below carries a source link; re-verify
before quoting anything in an interview.*

---

## PART 1 — Is this a match?

### Short answer: yes, and the timing is unusually good.

The German market has effectively split the "Head of AI" title into three different jobs. You are a strong
match for two of them and a weak match for the third. Knowing which one you are reading is the single most
useful filter you can apply to a job board.

| Archetype | What they actually want | Your fit |
|---|---|---|
| **A. Head of AI — Research / Platform** *(tech companies, scale-ups)* | PhD or deep ML background, model training, MLOps at scale, publications. Team of data scientists and ML engineers. | **Weak.** Do not apply. You will lose to a research profile and it will dent your confidence for no reason. |
| **B. Head of AI — Enterprise Adoption & Governance** *(banks, insurers, Mittelstand, corporates)* | Someone who can get AI into production inside a regulated business: strategy, use-case portfolio, EU AI Act and DORA compliance, vendor and model selection, change management, working with Risk and Compliance. | **Strong.** This is your role. It is also the largest and fastest-growing segment. |
| **C. Head of AI — Consulting / Practice Lead** *(Capgemini-type firms, boutiques, venture builders)* | P&L, business development, delivery leadership, hiring, and enough technical credibility to shape solutions. The JD you sent is this one. | **Strong on 6 of 7 criteria; the gap is formal P&L and external sales.** Addressed in your prep doc. |

### Why the timing matters — the regulatory calendar is working for you

This is the part most candidates will not be able to talk about, and it is happening right now:

| Date | What happened / happens | Why it matters to you |
|---|---|---|
| 2 Feb 2025 | **EU AI Act Article 4 (AI literacy)** and the prohibited-practices ban became applicable | Already a live legal obligation for every company using AI |
| 2 Aug 2025 | GPAI obligations, governance structure and penalties applied | |
| **2 Aug 2026 — tomorrow** | **General applicability**, Article 50 transparency obligations, and **supervision/enforcement of the AI literacy rules begins** | Every German company using AI now has an enforceable obligation it probably cannot evidence |
| **29 July 2026 — three days ago** | Germany's **KI-MIG** (AI Market Surveillance and Innovation Promotion Act) entered into force. **Bundesnetzagentur** becomes the central market surveillance authority; **BaFin** becomes the AI market surveillance authority for the financial sector | Your exact sector just got a named AI regulator |
| End of 2026 | **BAIT expires completely** for DORA-subject institutions; MaRisk and § 25b KWG remain for outsourcing | Every German bank is mid-migration on IT governance right now |
| 2 Dec 2027 *(proposed)* | High-risk obligations for standalone Annex III systems — **deferred from 2 Aug 2026** by the Digital Omnibus | Verify formal adoption status before quoting |
| 2 Aug 2028 *(proposed)* | High-risk obligations for AI embedded in regulated products (Annex I) | |

**The interview line this gives you:**

> "BaFin became the AI market surveillance authority for financial institutions on 29 July under the KI-MIG,
> and enforcement of the AI literacy obligation starts on 2 August. Meanwhile the high-risk deadline has
> moved to December 2027 under the Digital Omnibus. So the pressure right now isn't high-risk conformity —
> it's that every institution needs an AI inventory, a classification, and evidence of AI literacy, and most
> have none of the three. That's the wedge offer I'd take to market in month one."

Almost nobody interviewing for these roles will be able to say that. It signals that you track the
regulation as a practitioner rather than having read a summary.

### The honest caveats

- **Salary expectations.** Head of AI in Germany benchmarks around **€100–150k**, average ~€120k. Financial
  services with a governance mandate sits at the upper end and above. Do not anchor low.
- **German language.** B1 is workable for group-level and CRO/CTO conversations in international firms; it is
  a real constraint for Mittelstand and client-facing German-language BD. Ask early, do not discover it at
  offer stage. Push toward B2 — see Week 4.
- **Title inflation cuts both ways.** Some "Head of AI" postings are one-person roles with no team and no
  budget. Screen for: does it name a team size, a budget, or a P&L? If none of the three, it is an IC role
  with a senior title.

---

## PART 2 — The regulatory syllabus

This is the complete list of what you need to hold in your head. Organised by priority: **Tier 1 you must
know cold**, **Tier 2 you must be able to discuss**, **Tier 3 you need to know exists**.

### Tier 1 — Know cold

#### 1. EU AI Act (Regulation (EU) 2024/1689)

The centre of everything. You need the structure, not memorised articles.

| What to know | Depth |
|---|---|
| Risk tiers: prohibited (Art. 5), high-risk (Art. 6 + Annex I/III), limited-risk transparency (Art. 50), minimal | Cold |
| Provider vs deployer obligations — and which you are | Cold |
| Art. 4 AI literacy | Cold — this is the live enforcement item |
| Art. 9 risk management, Art. 10 data governance, Art. 11 + Annex IV technical documentation, Art. 12 logging, Art. 13 transparency, Art. 14 human oversight, Art. 15 accuracy/robustness/cybersecurity | Cold — these are the eight you will be asked about |
| Art. 26 deployer obligations, Art. 27 fundamental rights impact assessment (FRIA) | Solid |
| GPAI: Art. 53 and Art. 55 systemic-risk obligations | Solid |
| Art. 72 post-market monitoring, Art. 73 serious incident reporting | Solid |
| Penalties: up to €35m / 7% global turnover for prohibited practices; €15m / 3% for most other breaches | Cold |

**Sources:**
- Official consolidated text — [EUR-Lex, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Best free navigator, article by article with recitals — [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) (see the AI Act Explorer and Implementation Timeline)
- German-language text, well structured — [ai-act-law.eu/de](https://ai-act-law.eu/de/)
- Commission's own hub — [European Commission: Regulatory framework for AI](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- Practical German business explainers — [IHK München AI Act guide](https://www.ihk-muenchen.de/ratgeber/digitalisierung/kuenstliche-intelligenz/ai-act/) · [activeMind.legal AI Act guide](https://www.activemind.legal/de/guides/ai-act/)

#### 2. The Digital Omnibus on AI — the deferral

Proposed by the Commission on 19 November 2025; a provisional political agreement was reached in 2026 that
defers high-risk obligations for standalone Annex III systems to **2 December 2027** and for AI embedded in
Annex I products to **2 August 2028**. **Confirm the formal adoption status before you cite it** — this is
exactly the kind of detail an interviewer will test.

- [DLA Piper: The Digital AI Omnibus — proposed deferral](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act)
- [Gibson Dunn: EU AI Act Omnibus Agreement](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
- [Legiscope: EU AI Act deadlines 2026–2027](https://www.legiscope.com/blog/eu-ai-act-timeline-deadlines.html)

#### 3. Germany: KI-MIG and the supervisory map

Your differentiator in the German market. Passed by the Bundestag 11 June 2026, in force **29 July 2026**.

| Authority | Scope |
|---|---|
| **Bundesnetzagentur** | Central market surveillance authority, single point of contact, complaints body. Directly supervises Annex III high-risk AI where no sectoral regulator exists (HR, education, general administration). |
| **BaFin** | AI market surveillance for the financial sector — BaFin- and ECB-supervised firms, significant asset-referenced token issuers, VBL (§ 2(3) KI-MIG) |
| **Landesmedienanstalten** | Media |
| **BfArM** | Medical devices |

- [BaFin: KI-Marktüberwachung](https://www.bafin.de/DE/unternehmen-maerkte/aufsicht/alle-unternehmen/ki-marktueberwachung/ki-marktueberwachung_node.html) — **read this properly, it is your sector's primary source**
- [BaFin press release, 29 July 2026](https://www.bafin.de/SharedDocs/Veroeffentlichungen/DE/Pressemitteilung/2026/pm_2026_07_29_ki_verordnung.html)
- [TÜV: KI-MIG Deutschland — Behörden, Bußgelder, Fristen](https://consulting.tuv.com/aktuelles/ki-im-fokus/ki-mig-deutschland-umsetzung)
- [Bundesnetzagentur](https://www.bundesnetzagentur.de/)

#### 4. DORA (Regulation (EU) 2022/2554)

You already list DORA. Deepen it — this is where AI meets operational resilience in banking.

| What to know | Why |
|---|---|
| ICT risk management framework | The container AI sits inside |
| **ICT third-party risk (Art. 28–30)** and the register of information | Your model provider is a third party. This is the article set you will be asked about. |
| Contractual requirements — audit rights, SLAs, incident notification, **exit strategies** | The exit-strategy test is your strongest talking point |
| Critical ICT third-party provider designation and oversight | Relevant if the model provider gets designated |
| ICT incident classification and reporting | AI incidents fall inside this taxonomy |
| Digital operational resilience testing | Where provider-outage scenarios live |

- [EUR-Lex: DORA, Regulation (EU) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)
- **BaFin guidance on ICT risks in AI use, published 18 December 2025** — the explicit AI↔DORA bridge for German firms. Find it via [bafin.de](https://www.bafin.de/) → search "KI IKT-Risiken".
- [EBA](https://www.eba.europa.eu/) and [EIOPA](https://www.eiopa.europa.eu/) for the ESA-level technical standards

#### 5. German banking supervision: MaRisk, BAIT, KWG

Neither MaRisk nor BAIT names AI explicitly — they govern it through **outsourcing** and **IT governance**
requirements. That subtlety is worth knowing.

- **MaRisk** — Minimum Requirements for Risk Management; AT 9 covers outsourcing. Still the basis for
  outsourcing management alongside **§ 25b KWG**.
- **BAIT** — Supervisory Requirements for IT. **Being phased out for DORA-subject institutions and expiring
  completely at end of 2026.** Knowing this transition is happening right now is a strong signal.
- Source: [bafin.de](https://www.bafin.de/) → Rechtsgrundlagen → MaRisk / BAIT. Practitioner overview:
  [MaRisk, BAIT und KI](https://www.agentic360.de/blog/marisk-bait-ai-banking)

#### 6. GDPR — the AI-relevant parts only

You do not need to re-learn GDPR. You need the six intersections:

- **Art. 5** principles — purpose limitation and data minimisation are the ones AI projects break
- **Art. 6 / 9** lawful basis, including special-category data
- **Art. 22** automated decision-making — the article that decides whether your system needs a human
- **Art. 35** DPIA — when it is mandatory, and how it relates to a FRIA under the AI Act
- **Chapter V** international transfers — the reason EU model residency matters
- **Data subject rights** against a model and a retrieval corpus

- [GDPR full text](https://gdpr-info.eu/) · [EDPB guidelines and opinions](https://www.edpb.europa.eu/) (look for the opinion on AI models and personal data)

### Tier 2 — Be able to discuss

| Framework | Why it matters | Link |
|---|---|---|
| **ISO/IEC 42001** — AI Management System | The certifiable standard. Becoming the default answer to "how do we prove we manage AI responsibly." Strong in the German market where certification carries weight. | [iso.org/standard/42001](https://www.iso.org/standard/42001) |
| **ISO/IEC 23894** — AI risk management guidance | Complements 42001 | [iso.org](https://www.iso.org/) |
| **NIST AI Risk Management Framework** | Govern / Map / Measure / Manage. Free, and the common vocabulary in US-headquartered firms. | [nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework) |
| **AMLD6 / AMLR + the new AMLA** | Your AML background is an asset — keep it current | [eur-lex.europa.eu](https://eur-lex.europa.eu/) |
| **Basel / EBA guidance on ML in IRB models** | Model risk management for AI in credit | [eba.europa.eu](https://www.eba.europa.eu/) |
| **EU Data Act, Data Governance Act** | Increasingly cited in AI procurement | [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/) |

### Tier 3 — Know it exists

NIS2 · Cyber Resilience Act · EU Product Liability Directive (revised, now covers software and AI) ·
Council of Europe Framework Convention on AI · sector codes of practice for GPAI.

---

## PART 3 — Certifications

### The honest position: no certification is legally required, and none will get you the job on its own.

Nobody is hiring a Head of AI because they hold a certificate. But in the German market, and specifically in
financial services, a governance credential does three useful things: it gets you past HR screens that filter
on keywords, it gives an interviewer a shorthand for "this person has studied the regulation systematically,"
and — if you go the consulting route — **it is a billable credential you can put on a proposal**.

### Recommended: one certification, not three

| Certification | Verdict | Cost | Why |
|---|---|---|---|
| **IAPP AIGP** — AI Governance Professional | **Do this one** | Exam $649 member / $799 non-member; IAPP membership $295/yr; official training $995–1,195 (optional); realistic all-in **$1,500–2,000**, or ~$950 exam + membership only | The recognised AI governance credential globally. Maps directly to how you are positioning. Vendor-neutral. Covers AI Act, NIST RMF, ISO 42001, risk, and lifecycle governance — i.e. it *is* your syllabus. [iapp.org/certify/aigp](https://iapp.org/certify/aigp/) |
| **ISO/IEC 42001 Lead Implementer** | Strong second, later | ~€1,000–2,500 depending on provider; 32h training | Do this **if** you go consulting — it is directly sellable as an offer. In Germany, **TÜV** and **DNV** carry more weight than online-only providers. [PECB](https://pecb.com/en/education-and-certification-for-individuals/iso-iec-42001) · [DNV](https://www.dnv.com/training/iso-iec-42001-auditor-lead-auditor-course/) · [TÜV](https://consulting.tuv.com/) |
| **ISO/IEC 42001 Lead Auditor** | Only if you sell assurance | ~$799+ | Different buyer (second line, internal audit). Useful for the assurance offer in your case study, not before. |
| IAPP CIPP/E (privacy) | Skip for now | — | Valuable but adjacent. Only if a role is explicitly privacy-weighted. |
| "Chief AI Officer" programmes on Udemy/Coursera | **Skip** | — | No market recognition. Your shipped products are worth more. |
| PMP (full certification) | Skip | — | You are moving *away* from PM positioning. The 35 hours on your CV is enough. |

**My recommendation: book the AIGP exam now for a date ~6 weeks out.** A booked exam date is what converts a
study plan into studying. Skip the official training initially — the AI Act text plus the free resources
below cover most of the body of knowledge, and you can add the practice exam ($50–60) at week 4.

**One thing worth more than any certification:** publish your EU AI Act conformity mapping and the KI-MIG
supervisory map as public artefacts. In this market, demonstrable method beats a credential — and it doubles
as the inbound pipeline strategy in your case study.

---

## PART 4 — The four-week plan

**Assumption: ~10 hours a week.** 90 minutes on weekday evenings, one 3-hour block at the weekend. Adjust
freely — but protect the deliverables, because they are what you take into interviews.

Each week has: **study**, **a deliverable**, and **a checkpoint**.

---

### WEEK 1 — The AI Act, cold

**Goal:** you can explain the Act's structure, obligations and current timeline without notes.

| Day | Focus | Time | Source |
|---|---|---|---|
| Mon | Structure and risk tiers. Read Art. 1–6, Annex I and Annex III end to end. | 90m | [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) |
| Tue | **The Big Eight.** Art. 9, 10, 11, 12, 13, 14, 15 + Annex IV. Take notes in your own words. | 90m | [EUR-Lex 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) |
| Wed | Deployer obligations (Art. 26–27), transparency (Art. 50), post-market monitoring (Art. 72–73), penalties. | 90m | Same |
| Thu | Art. 4 AI literacy — obligation, scope, enforcement from 2 Aug 2026. Read two law-firm analyses. | 90m | [Latham & Watkins](https://www.lw.com/en/insights/upcoming-eu-ai-act-obligations-mandatory-training-and-prohibited-practices) · [Travers Smith](https://www.traverssmith.com/knowledge/knowledge-container/the-eu-ai-acts-ai-literacy-requirement-key-considerations/) |
| Fri | GPAI: Art. 53, Art. 55. Provider vs deployer — where the line falls when you use a foundation model API. | 90m | AI Act Explorer |
| Sat | **Timeline + Digital Omnibus.** Build your own one-page dated timeline. Verify the Omnibus adoption status. | 3h | [DLA Piper](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act) · [Legiscope](https://www.legiscope.com/blog/eu-ai-act-timeline-deadlines.html) |

> **Deliverable 1 — "EU AI Act on one page."** Risk tiers, the eight core obligations, provider vs deployer,
> penalties, and a dated timeline including the Omnibus. This becomes a published artefact and a leave-behind.

> **Checkpoint:** explain to someone non-technical, in under three minutes, why RegCopilot is not a high-risk
> system and what would make it one. If you hesitate, re-read Art. 6 and Annex III.

**Also this week:** book the AIGP exam. Update your LinkedIn headline.

---

### WEEK 2 — The German and financial-services stack

**Goal:** you are the candidate who knows what BaFin did last week and why BAIT is expiring.

| Day | Focus | Time | Source |
|---|---|---|---|
| Mon | **KI-MIG.** Supervisory map, § 2(3), Bundesnetzagentur vs BaFin vs sectoral regulators, penalties. | 90m | [BaFin KI-Marktüberwachung](https://www.bafin.de/DE/unternehmen-maerkte/aufsicht/alle-unternehmen/ki-marktueberwachung/ki-marktueberwachung_node.html) · [TÜV KI-MIG](https://consulting.tuv.com/aktuelles/ki-im-fokus/ki-mig-deutschland-umsetzung) |
| Tue | **DORA Art. 28–30** — ICT third-party risk, register of information, contractual requirements, exit strategies. | 90m | [EUR-Lex DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) |
| Wed | **BaFin guidance on ICT risks in AI use** (18 Dec 2025). This is the AI↔DORA bridge for German firms. | 90m | [bafin.de](https://www.bafin.de/) → search "KI IKT-Risiken" |
| Thu | **MaRisk (AT 9 outsourcing), BAIT phase-out, § 25b KWG.** Understand the DORA transition. | 90m | [bafin.de](https://www.bafin.de/) · [MaRisk/BAIT & KI overview](https://www.agentic360.de/blog/marisk-bait-ai-banking) |
| Fri | **GDPR × AI**: Art. 22, Art. 35 DPIA, Chapter V transfers, and how a DPIA relates to a FRIA. | 90m | [gdpr-info.eu](https://gdpr-info.eu/) · [EDPB](https://www.edpb.europa.eu/) |
| Sat | **ISO/IEC 42001 + NIST AI RMF.** Clause structure of 42001; Govern/Map/Measure/Manage in the NIST RMF. Map both onto your AEGIS conformity table. | 3h | [ISO 42001](https://www.iso.org/standard/42001) · [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) |

> **Deliverable 2 — "German AI Supervisory Map."** One page: who regulates AI in Germany, for whom, from
> when, under which instrument, and what a BaFin-supervised firm must do in the next 18 months. **Almost
> nobody has this. Publish it.**

> **Checkpoint:** answer out loud — *"You use a US foundation model provider. Walk me through your DORA
> position."* You should cover: third-party register entry, criticality, contractual provisions, concentration
> risk, exit strategy and how you test it.

---

### WEEK 3 — Technical depth and the numbers

**Goal:** survive a technical interview with an engineering leader, and defend your cost model to a CFO.

| Day | Focus | Time | What to do |
|---|---|---|---|
| Mon | **Your own portfolio, re-examined.** For each of the 7 products: what would you do differently, what is the weakest part, what would production hardening cost? | 90m | Write it down. You will be asked. |
| Tue | **Agent design and failure modes.** Tool design, bounded loops, why agents fail, orchestration patterns. | 90m | [Anthropic engineering blog](https://www.anthropic.com/engineering) · [Claude docs: agents & tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) |
| Wed | **Evaluation.** Golden sets, LLM-as-judge and its limits, regression gating, drift. Re-read `05-evaluation-guardrails-and-incident-response.md` and be able to defend every threshold. | 90m | Your case study |
| Thu | **Cost mechanics, hands-on.** Prompt caching, model routing, batch processing, context management. Verify current pricing. | 90m | [Anthropic pricing](https://www.anthropic.com/pricing) · [prompt caching docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) |
| Fri | **RAG depth.** Hybrid retrieval (BM25 + vector), chunking strategy, re-ranking, why RegCopilot's AMLD6 corpus underperforms and what v2 does. | 90m | Your RegCopilot repo + eval results |
| Sat | **Build something small that proves a point.** Best option: add hybrid search to RegCopilot and re-run the eval to show a measured improvement. A before/after number is worth more than any bullet point. | 3h | Your repo |

> **Deliverable 3 — a measured improvement on a live product.** "82% → X% by adding BM25 to the retrieval
> path" is the single most credible thing you can bring to a technical interview.

> **Checkpoint:** whiteboard the AEGIS architecture from memory in 10 minutes, then answer *"why not just
> fine-tune?"* and *"what's your unit cost and how do you control it?"*

---

### WEEK 4 — Commercial, and go to market

**Goal:** the P&L answer is fluent, applications are out, and you are interview-ready.

| Day | Focus | Time | What to do |
|---|---|---|---|
| Mon | **P&L mechanics.** Utilisation, blended day rate, contribution margin, recurring revenue mix. Rebuild the Part B P&L in a spreadsheet yourself so the numbers are *yours*. | 90m | `06-commercial-model-pl-and-gtm.md` |
| Tue | **Rehearse the gap answers out loud.** P&L, external BD, self-built portfolio, German language. Record yourself; listen back once. | 90m | `JD_Mapping_and_Interview_Prep.md` §3 |
| Wed | **Pipeline and offer design.** Price your wedge offer for the German market. Draft a one-page AI Governance Readiness Assessment brochure in English and German. | 90m | Case study §4 |
| Thu | **Applications.** Tailor and send 5. Screen out archetype A. | 90m | Target: banks, insurers, RegTech, consulting practices |
| Fri | **Publish.** Deliverables 1 and 2 as LinkedIn articles or GitHub pages. Add the case study to LinkedIn Featured. | 90m | This is your inbound engine |
| Sat | **Full mock interview**, 90 minutes, with someone who will push back. Then AIGP practice exam. | 3h | [IAPP practice exam](https://iapp.org/certify/aigp/) |

> **Deliverable 4 — 5 applications out, 2 artefacts published, P&L rebuilt in your own spreadsheet.**

> **Checkpoint:** deliver the full 90-day plan from your prep doc, out loud, in under four minutes.

**Also this week:** book a German B2 course or intensive tandem. It is the slowest-moving item on this list,
so start it while everything else is in motion.

---

## PART 5 — Keep current after week 4

Thirty minutes a week, permanently. AI regulation moves faster than any other area you have worked in.

| Source | What for | Cadence |
|---|---|---|
| [BaFin news](https://www.bafin.de/) | Your sector's regulator — subscribe to the newsletter | Weekly |
| [Bundesnetzagentur AI pages](https://www.bundesnetzagentur.de/) | Central AI market surveillance | Monthly |
| [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) | Implementation timeline and guidance updates | Monthly |
| [European Commission digital strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | Codes of practice, guidance, the AI Office | Monthly |
| [IAPP](https://iapp.org/) | AI governance news — genuinely good, member access | Weekly |
| [EDPB](https://www.edpb.europa.eu/) | Data protection × AI opinions | Monthly |
| DLA Piper / Gibson Dunn / Latham AI alerts | Free law-firm analysis, faster than official channels | As published |
| [Anthropic engineering blog](https://www.anthropic.com/engineering) | Agent and eval practice | Monthly |

---

## PART 6 — Budget and time

| Item | Cost | Priority |
|---|---|---|
| IAPP AIGP exam | $649 (member) / $799 | **Do it** |
| IAPP membership (1 yr) — includes cert maintenance | $295 | **Do it** — pays for itself against the non-member exam price |
| AIGP practice exam | $50–60 | Recommended |
| AIGP official training | $995–1,195 | Optional — skip on the first attempt |
| ISO/IEC 42001 Lead Implementer (TÜV/DNV/PECB) | €1,000–2,500 | Later, and only if you go consulting |
| German B2 course | €300–800 | **Start now** — longest lead time |
| **Minimum viable** | **~$1,000** | AIGP + membership + practice exam |
| **Full programme** | **~€3,000** | Adds ISO 42001 and German |

**Time: ~40 hours over four weeks.** The certification adds roughly 20–30 hours of revision on top, but
Weeks 1–2 of this plan already cover most of the AIGP body of knowledge — which is why the exam is booked for
week 6, not week 12.

---

## The one thing to take from this

You are not short of qualifications. You are short of a **crisp story about a market that just changed**.
BaFin became your sector's AI regulator three days ago, AI literacy enforcement starts tomorrow, and the
high-risk deadline has moved to 2027 — so the demand right now is for inventory, classification, literacy
evidence and operating models, which is precisely what you can build and precisely what your case study
describes.

Study the regulation for two weeks so you can speak about it without hedging, spend one week making sure the
technical and cost answers are airtight, and spend the fourth week selling. The certificate is useful. The
timing is the actual advantage.

---

### Sources

[StepStone Head of AI jobs](https://www.stepstone.de/jobs/head-of-ai) ·
[Glassdoor: Head of AI jobs Germany](https://www.glassdoor.com/Job/head-of-artificial-intelligence-jobs-SRCH_IN96_KO0,31.htm) ·
[LinkedIn Germany: Head of AI](https://de.linkedin.com/jobs/head-of-artificial-intelligence-stellen) ·
[Indeed.de: Head of AI](https://de.indeed.com/q-head-of-ai-jobs.html) ·
[EUR-Lex: EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) ·
[EUR-Lex: DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) ·
[artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/) ·
[European Commission: AI regulatory framework](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) ·
[BaFin: KI-Marktüberwachung](https://www.bafin.de/DE/unternehmen-maerkte/aufsicht/alle-unternehmen/ki-marktueberwachung/ki-marktueberwachung_node.html) ·
[BaFin press release 29.07.2026](https://www.bafin.de/SharedDocs/Veroeffentlichungen/DE/Pressemitteilung/2026/pm_2026_07_29_ki_verordnung.html) ·
[TÜV: KI-MIG Umsetzung](https://consulting.tuv.com/aktuelles/ki-im-fokus/ki-mig-deutschland-umsetzung) ·
[MaRisk, BAIT und KI](https://www.agentic360.de/blog/marisk-bait-ai-banking) ·
[DLA Piper: Digital AI Omnibus](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act) ·
[Gibson Dunn: Omnibus agreement](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) ·
[Legiscope: AI Act deadlines](https://www.legiscope.com/blog/eu-ai-act-timeline-deadlines.html) ·
[Latham & Watkins: AI literacy & prohibited practices](https://www.lw.com/en/insights/upcoming-eu-ai-act-obligations-mandatory-training-and-prohibited-practices) ·
[Travers Smith: AI literacy requirement](https://www.traverssmith.com/knowledge/knowledge-container/the-eu-ai-acts-ai-literacy-requirement-key-considerations/) ·
[IAPP AIGP certification](https://iapp.org/certify/aigp/) ·
[PECB ISO/IEC 42001](https://pecb.com/en/education-and-certification-for-individuals/iso-iec-42001) ·
[DNV ISO/IEC 42001 Lead Auditor](https://www.dnv.com/training/iso-iec-42001-auditor-lead-auditor-course/) ·
[ISO/IEC 42001](https://www.iso.org/standard/42001) ·
[NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) ·
[GDPR text](https://gdpr-info.eu/) ·
[EDPB](https://www.edpb.europa.eu/) ·
[IHK München: AI Act](https://www.ihk-muenchen.de/ratgeber/digitalisierung/kuenstliche-intelligenz/ai-act/) ·
[activeMind.legal: AI Act guide](https://www.activemind.legal/de/guides/ai-act/) ·
[ai-act-law.eu (DE)](https://ai-act-law.eu/de/) ·
[neue fische: Head of AI Gehalt](https://www.neuefische.de/en/community/career/what-does-a-head-of-ai-earn)
