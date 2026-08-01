# 04 — Risk Register & EU AI Act Conformity

*Project AEGIS. This is a worked governance model, not legal advice. Regulatory interpretation should be
confirmed with counsel and the competent authority.*

---

## 1. Classification — the decision that shaped everything

The first substantive governance question is not "is this compliant" but **"what is this, under which
regime."** We classified AEGIS Assist under four instruments before any build work started.

### 1.1 EU AI Act

| Question | Determination | Reasoning |
|---|---|---|
| Is it an AI system in scope? | **Yes** | Machine-based system inferring outputs from inputs, influencing a decision environment |
| Prohibited practice (Art. 5)? | **No** | No social scoring, no biometric categorisation, no manipulation, no real-time remote biometric ID |
| Annex III high-risk? | **No — with a caveat** | AML alert triage is not itself an Annex III listed use. But: it supports decisions that can lead to a customer relationship being terminated, so we assessed adjacency to Annex III(5)(b) (creditworthiness/credit scoring) explicitly and documented why it does not apply — the system does not evaluate creditworthiness and cannot deny access to a service. |
| GPAI obligations (Art. 53/55)? | **Provider obligations sit with the model provider; we are a deployer** | Confirmed contractually. We retain deployer obligations. |
| **Final classification** | **Limited-risk AI system with voluntary high-risk-equivalent controls** | See below |

**The decision I would defend hardest: we voluntarily applied high-risk-equivalent controls to a system we
had classified as limited-risk.**

Three reasons, and I would give all three in an interview:

1. **The classification is a judgement call near a boundary.** If a supervisor disagrees with our reading of
   Annex III adjacency, we are already compliant rather than starting a remediation programme. The cost of
   the extra controls was roughly €90k; the cost of being wrong without them is a supervisory finding, a
   remediation plan and a system switched off.
2. **The scope will move.** The business already wants auto-disposition. When that conversation becomes a
   funded project, the conformity work is largely done. Building to the lower standard would have made the
   next step a rebuild.
3. **The controls are good engineering regardless.** Logging, human oversight, accuracy monitoring and
   technical documentation are what makes a system maintainable. Framing them as a regulatory tax is how
   teams end up with systems they cannot debug.

### 1.2 Other regimes

| Regime | Position |
|---|---|
| **DORA** | Model provider registered as a critical ICT third-party provider. Contractual provisions, concentration risk assessment, tested exit strategy, and AI incidents in scope of the ICT incident taxonomy. See [02 §5](02-architecture-and-model-strategy.md). |
| **GDPR** | DPIA completed pre-build. Lawful basis: legal obligation (AMLD6 monitoring duty) plus legitimate interest for the assistive layer. **No Art. 22 automated decision** — a human decides every alert, enforced architecturally by a read-only tool surface. Data minimisation at the tool layer; EU residency; zero retention contractual. |
| **AMLD6 / national AML law** | The system assists the monitoring obligation; it does not replace it. The regulated decision remains with the MLRO function. Documented so that the AML control framework is unchanged in substance. |
| **EBA Guidelines on outsourcing** | Assessed; model provision treated as ICT outsourcing with the associated register entry and governance. |
| **ISO/IEC 42001 & NIST AI RMF** | Not certified. The AI management system was **designed to map** to 42001 clauses and the NIST RMF Govern/Map/Measure/Manage functions, so certification is an audit away rather than a rebuild. |

---

## 2. EU AI Act conformity mapping

Article-by-article, with the concrete artefact that evidences it. This table is the conformity pack's
contents page — it is what I would hand to a supervisor.

| Article | Requirement | How AEGIS satisfies it | Evidence artefact |
|---|---|---|---|
| **Art. 9** — Risk management system | Continuous, iterative risk management across the lifecycle | Risk register (§3) reviewed monthly at AI Council; every release re-assesses residual risk; incidents feed back into the register | `AEGIS-RM-001` Risk Management Plan + register with dated revisions |
| **Art. 10** — Data governance | Training/validation/testing data relevant, representative, free of errors, examined for bias | We do not train models. Applies to the **retrieval corpus and evaluation set**: corpus provenance documented, versioned and change-controlled; golden set built with AML SMEs, reviewed for typology and geographic coverage bias | `AEGIS-DG-002` Corpus provenance & versioning; `AEGIS-EV-004` Golden set design & bias review |
| **Art. 11 / Annex IV** — Technical documentation | Complete system documentation | Architecture, agent design, tool surface, model configuration, evaluation methodology and results, known limitations | `AEGIS-TD-003` Technical File |
| **Art. 12** — Record-keeping / logging | Automatic recording of events over lifetime, enabling traceability | **Write-before-surface** immutable audit log: alert ID, every tool call with arguments and result hash, retrieved chunk IDs, model ID and version, prompt hash, full output, guardrail verdicts, human decision and reason, latency, tokens, cost. Fails closed. | `AEGIS-LOG-005` Logging specification + retention policy (7 years, aligned to AML) |
| **Art. 13** — Transparency & information to users | Users understand capabilities, limitations, and how to interpret output | Every claim in the recommendation is clickable to its source. In-product limitations notice. Analyst training and a written user manual covering known failure modes. | `AEGIS-UM-006` User Manual + in-product disclosures |
| **Art. 14** — Human oversight | Humans can understand, monitor, override, and decide not to use | Analyst decides every alert. One-click override with mandatory reason. Analyst can request escalation re-run, discard the recommendation entirely, or work the alert without it. **Automation-bias controls** (§4). | `AEGIS-HO-007` Human Oversight Design + override analytics |
| **Art. 15** — Accuracy, robustness, cybersecurity | Appropriate accuracy, resilience, and security over the lifecycle | Golden-set evaluation with hard release gates; adversarial and prompt-injection red-teaming; online drift monitoring; graceful degradation to manual on any ceiling breach | `AEGIS-EV-004` Evaluation methodology & results; `AEGIS-SEC-008` Red-team report |
| **Art. 26** — Deployer obligations | Use per instructions, ensure input data relevance, monitor, retain logs, inform workers | Operating procedures; input relevance controlled at the tool layer; post-market monitoring live; logs retained 7 years; **works council informed and consulted before deployment** | `AEGIS-OPS-009` Operating procedures; works council consultation record |
| **Art. 50** — Transparency for certain systems | Disclosure where users interact with AI | Analysts know they are using an AI assistant; the recommendation is labelled as AI-generated in the UI and in the case record | In-product labelling; case-record annotation |

**The Art. 14 point is the one worth dwelling on.** Human oversight is frequently implemented as "a human
clicks approve," which is oversight in name only — it produces automation bias, not oversight. What makes it
real is that overriding must be **as easy as agreeing**, the reasoning must be **inspectable rather than
asserted**, and the override rate must be **monitored as a control** (§4). Anything else is a rubber stamp
with an audit trail.

---

## 3. Risk register

Scored on inherent risk (likelihood × impact, 1–5 each), controls applied, residual risk. Reviewed monthly at
the AI Council; any residual score ≥12 needs a documented CRO acceptance.

| # | Risk | Inh. | Controls | Res. | Owner |
|---|---|---|---|---|---|
| **R1** | **Hallucinated fact in a recommendation leads an analyst to close a genuine suspicious alert** | 20 | Mandatory citation for every factual claim; L3 output guardrail rejects unsupported claims; unsupported-claim rate is a **hard release gate at 0% surfaced**; analyst sees sources inline | 6 | Head of AI |
| **R2** | **Automation bias — analysts accept recommendations without genuine review** | 20 | Override rate monitored with a **floor** (<5% triggers investigation); periodic blind-control alerts with known answers; recommendation deliberately presents evidence before conclusion; analyst training | 9 | Head of AML Ops |
| **R3** | Prompt injection via adverse media or customer free-text field causes unauthorised tool use or data exfiltration | 16 | Read-only tool surface (nothing to exfiltrate *to*); tool allowlist and argument validation; L1 injection screening; source allowlist for media; quarterly red-team | 6 | AI/ML Engineering |
| **R4** | Retrieval returns outdated policy or superseded typology guidance | 16 | Corpus versioning with effective dates; retrieval filters on validity date; corpus change control; citations show document version | 6 | AI Risk & Governance Lead |
| **R5** | Model provider outage or degradation halts alert triage | 12 | Graceful degradation to manual (the pre-existing process, unchanged); circuit breaker; pre-tested second-source model; DORA resilience testing | 4 | Head of AI / CTO |
| **R6** | Model deprecation forces unplanned migration | 12 | Contractual notice period; pinned model versions; quarterly second-source evaluation quantifies the switch cost in advance | 4 | Head of AI |
| **R7** | Performance drift — quality degrades silently as data or typologies evolve | 16 | Online drift monitoring on retrieval relevance, output distribution and override rate; monthly golden-set regression; alert thresholds | 6 | AI/ML Engineering |
| **R8** | Bias — systematically worse performance for a customer segment, nationality or transaction corridor | 20 | Golden set stratified by segment, geography and typology; **per-segment performance reported, not just aggregate**; disparity threshold triggers investigation and can block release | 8 | AI Risk & Governance Lead |
| **R9** | Personal data leaves the EU or is retained by the provider | 15 | EU-resident endpoints; contractual zero retention; gateway blocks non-approved regions; annual provider assurance review | 4 | DPO |
| **R10** | Uncontrolled cost — runaway loops, injection-driven spend, volume shock | 9 | Hard per-alert ceilings; gateway spend caps per use case and tenant; degradation to triage-only on breach; unit cost as a release gate | 3 | Head of AI |
| **R11** | Scope creep in autonomy without re-classification | 12 | Autonomy level is a G2 Council decision; any change to the tool surface's write capability triggers re-classification; architectural enforcement (read-only tools) | 4 | AI Council |
| **R12** | Shadow AI re-emerges outside the governed estate | 15 | Procurement gate; gateway is the only approved egress path; quarterly discovery scan; AI policy in the annual attestation | 6 | CTO / Head of AI |
| **R13** | Loss of institutional AML judgement as analysts rely on the assistant | 12 | Assistive-only by design; blind-control alerts; rotation so analysts still work alerts unassisted; competency assessment unchanged | 6 | Head of AML Ops |
| **R14** | Audit log incomplete or tampered | 20 | Write-before-surface with fail-closed; append-only store with integrity hashing; completeness is a **hard gate at 100%**; log reconciliation in Internal Audit's annual plan | 4 | CTO |

**R2 and R13 are the risks most AI programmes miss**, because they are not technology risks — they are risks
to the human control the whole compliance position depends on. If analysts stop genuinely reviewing, the
Art. 14 oversight claim becomes false and the system's classification is wrong. Monitoring override rate with
a **floor** as well as a ceiling is how you evidence that oversight is real.

---

## 4. Automation-bias controls, specifically

Because R2 carries the highest residual risk in the register, the controls are worth setting out:

1. **Evidence before conclusion.** The review surface shows gathered evidence and reasoning first; the
   recommended disposition is below the fold. Presenting the answer first measurably increases acceptance
   rate without increasing accuracy.
2. **Override is one click, same as agree.** No friction asymmetry. An override reason is required — this is
   the friction, and it is deliberate because it produces evaluation data.
3. **Override rate has a floor.** Below 5% sustained triggers a review of whether analysts are genuinely
   engaging. This is the inverse of the intuitive metric and it is the one that actually detects the failure.
4. **Blind controls.** A small proportion of alerts carry a deliberately flawed or incomplete recommendation
   with a known correct answer. Detection rate is a monitored control, reported to 2LoD. Analysts know the
   programme exists; they do not know which alerts.
5. **Unassisted rotation.** Analysts work a proportion of alerts without the assistant, preserving skill and
   giving a live comparison baseline.
6. **Confidence is shown honestly.** Where the agent's evidence is thin, it says so and recommends escalation
   rather than producing a confident-sounding weak recommendation. Calibration is evaluated.

---

## 5. Post-market monitoring

Art. 72-style monitoring, operating from day one of production:

| Monitored | Frequency | Threshold / action |
|---|---|---|
| Citation accuracy | Continuous, sampled | <98% → investigate; <95% → roll back |
| Unsupported-claim rate | Continuous | Any surfaced instance → incident, root cause within 5 days |
| Analyst override rate | Weekly | <5% or >30% → investigate (both directions) |
| Per-segment performance disparity | Monthly | Disparity beyond threshold → investigate, may block next release |
| Retrieval relevance drift | Weekly | Trend break → corpus review |
| Golden-set regression | Every release + monthly | Any hard-gate failure → no release |
| Audit-log completeness | Continuous | <100% → system fails closed automatically |
| Incidents and near-misses | As they occur | Runbook in [05](05-evaluation-guardrails-and-incident-response.md) |
| Serious incident reportability assessment | As they occur | Documented assessment against Art. 73 criteria for every incident |

The last row matters: **every incident gets a documented reportability assessment**, even when the conclusion
is "not reportable." A file of dated non-reportability assessments is far stronger evidence of a functioning
system than an empty incident log.
