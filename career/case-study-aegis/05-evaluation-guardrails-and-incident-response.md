# 05 — Evaluation, Guardrails & Incident Response

*Project AEGIS. Thresholds are modelled targets.*

---

## 1. Evaluation is infrastructure

The single biggest difference between an AI demo and an AI product is that the product has an evaluation
harness and the demo has an opinion. In a regulated environment it is stronger than that: **Art. 15 requires
appropriate accuracy over the lifecycle, and you cannot evidence "over the lifecycle" without a regression
suite.** Evaluation is not a phase before launch. It is the thing that lets you change anything afterwards.

### 1.1 The golden set

**240 cases, built with the AML analysts, not by the AI team.**

This distinction cost six weeks and was worth it. Our first 90-case set was written by the AI team from
policy documents. When we rebuilt it with four senior analysts, roughly a third of the expected answers
changed — not because the policy was different, but because the analysts' actual decision practice
incorporated context the documents did not encode. An evaluation set that measures what the AI team thinks
good looks like measures the wrong thing.

Composition, stratified deliberately:

| Stratum | Cases | Why |
|---|---|---|
| Clear false positives | 60 | The volume case — must be resolved cheaply and confidently |
| Clear true positives | 40 | The cases that must never be missed |
| Genuinely ambiguous | 45 | Where the system should express low confidence and escalate, not guess |
| Multi-entity / complex structures | 30 | The escalation-tier justification |
| Adversarial / injection attempts | 25 | Robustness (Art. 15) |
| Segment and corridor coverage | 40 | Bias testing (R8) — stratified by customer segment, nationality, transaction corridor |

Every case carries: the alert, the underlying data, the expected disposition, the **facts that must be cited**
to support it, and the analyst's written reasoning. That last field is what makes LLM-as-judge possible.

The set is versioned, change-controlled, and grows: **every production override and every incident becomes a
candidate case.** By month 9 it had grown to 310.

### 1.2 What we score

| Dimension | Method | Gate |
|---|---|---|
| **Citation accuracy** — every factual claim traceable to a real retrieved source | Deterministic: claims parsed, matched against retrieved chunk IDs | **Hard gate ≥98%** |
| **Unsupported-claim rate** — claims with no source | Deterministic + LLM-as-judge | **Hard gate: 0% surfaced** |
| **Disposition agreement** — does the recommendation match the analyst's expected call | Exact match | Soft target ≥85% |
| **Reasoning quality** — is the reasoning sound and complete, independent of the conclusion | LLM-as-judge, rubric-scored, human-adjudicated sample | Soft target ≥4.0/5 |
| **Evidence completeness** — were the material facts gathered | Rubric against the case's required-facts list | Soft target ≥90% |
| **Calibration** — does stated confidence track actual correctness | Reliability curve over the set | Monitored, no gate |
| **Escalation appropriateness** — did it escalate when it should and not when it shouldn't | Against expected tier | Soft target ≥88% |
| **Per-segment disparity** | Per-stratum performance vs. aggregate | **Hard gate: within threshold** |
| **Cost per resolved alert** | Instrumented | **Gate: no >10% regression without sign-off** |
| **p95 latency** | Instrumented | **Gate: ≤90s** |

**Hard gates block the release. Soft targets require an explanation.** The distinction matters: a team where
every metric is blocking will start gaming metrics; a team where nothing blocks will ship regressions.

### 1.3 LLM-as-judge — and its limits

Rubric-scoring 310 cases by hand on every release is not viable, so reasoning quality and evidence
completeness are scored by a judge model. Three design decisions keep it honest:

1. **The judge sees the analyst's written reasoning as the reference.** It is scoring against a human
   standard, not against its own notion of a good answer.
2. **The judge is a different model from the one under test**, and never the same version. Same-model
   evaluation produces self-consistency, not quality.
3. **A stratified 15% sample is human-adjudicated every release, and judge–human agreement is itself a
   tracked metric.** When agreement drops below 85%, the rubric gets rewritten. The judge is a measurement
   instrument and instruments need calibration.

**What LLM-as-judge is not used for:** anything that is a hard gate. Citation accuracy and unsupported-claim
detection are deterministic checks against retrieved chunk IDs, because a gate you cannot fully explain is a
gate you cannot defend to an auditor.

### 1.4 Where evaluation runs

- **CI, every PR** — a 60-case fast subset. Fails the build.
- **Pre-release, full set** — all hard gates. Blocks the release.
- **Monthly in production** — full set against the live configuration, to catch drift in the corpus or
  underlying data even when nothing was deployed.
- **Quarterly, second-source model** — the DORA exit-strategy test ([02 §5](02-architecture-and-model-strategy.md)).
- **On every model version change** — including a provider's minor version bump. Model versions are pinned;
  an unpinned model is an untested change in production.

---

## 2. Guardrails — three layers

Guardrails are controls, and like any control they need to be independently evaluated. Ours are tested by the
same harness that tests the model.

### Layer 1 — Input

| Check | Action on failure |
|---|---|
| PII scope validation — is this data in scope for this analyst's entitlement | Block, log, alert |
| Prompt-injection screening on all externally-sourced content (adverse media, customer free-text) | Strip / quarantine the content, continue with a flag, log |
| Alert-payload schema validation | Reject to manual |
| Data-freshness check | Warn in output if a source is stale |

### Layer 2 — Tool

| Check | Action on failure |
|---|---|
| Tool allowlist — only the 7 approved tools, no dynamic tool construction | Hard block, incident |
| Argument validation — types, ranges, entitlement scope | Reject the call, agent retries with a corrected call |
| Rate and budget limits — per alert and per tool | Ceiling breach → route to manual with partial trace |
| **Write attempt** | Hard block, **incident** — the agent should be architecturally incapable of this; an attempt means something is wrong |

### Layer 3 — Output

| Check | Action on failure |
|---|---|
| **Citation verification** — every factual claim matched to a retrieved chunk ID | Claim stripped; if material, whole recommendation suppressed → manual |
| **Unsupported-claim detection** | Suppress recommendation, log as incident-candidate |
| Confidence floor — below threshold, do not recommend | Escalate rather than recommend |
| Prohibited-language filter — no determinative language ("this customer is laundering money"); recommendations must be framed as assessments | Rewrite or suppress |
| PII leakage check on the output | Suppress, incident |
| Schema and completeness check | Suppress, retry once, then manual |

**The suppression default is deliberate: when a guardrail fires, the analyst gets no recommendation rather
than a degraded one.** A missing recommendation costs an analyst 34 minutes — the pre-existing process. A
wrong one costs credibility, and credibility is what the entire adoption case rests on. Fail closed.

### Guardrail evaluation

Guardrails are tested independently: the adversarial stratum of the golden set plus a quarterly external
red-team engagement covering prompt injection, tool abuse, data exfiltration, and jailbreak of the
prohibited-language filter. **Findings feed the golden set** — every successful red-team technique becomes a
permanent regression case.

---

## 3. Online monitoring

Offline evaluation tells you the system was good when you tested it. Online monitoring tells you it still is.

| Signal | What it detects | Alert |
|---|---|---|
| Override rate, weekly | Quality degradation (rising) or automation bias (falling) | Outside 5–30% |
| Override *reasons*, categorised | *What* is degrading, not just that something is | Category spike |
| Retrieval relevance score distribution | Corpus drift, indexing failure | Distribution shift |
| Output length and structure distribution | Model behaviour change after a provider update | Distribution shift |
| Guardrail firing rate by layer | Injection campaign, upstream data problem, or an over-tight guardrail | Rate change |
| Blind-control detection rate | Whether human oversight is real | Below threshold |
| Escalation-tier distribution | Routing degradation | Shift >5pp |
| Cache-hit rate | Cost regression | Below threshold |
| p95 latency | Adoption risk | >90s |
| Cost per resolved alert | Cost creep | >10% MoM |

**The override-reason taxonomy is the most useful monitoring artefact in the system.** "Override rate rose
from 14% to 22%" tells you something is wrong. "Override rate rose because *missing counterparty context*
went from 3% to 11% of overrides" tells you a source connection is degrading. Categorised free text from the
people using the system is a better drift detector than any statistical measure we implemented.

---

## 4. AI incident runbook

AI incidents are not standard IT incidents. The system is usually **up**; it is being **wrong**, which
monitoring designed for availability will not catch.

### 4.1 Severity

| Sev | Definition | Example | Response |
|---|---|---|---|
| **S1** | Incorrect output may have led to a materially wrong regulatory decision | Hallucinated fact contributed to closing a genuine suspicious alert | Immediate: system to manual mode |
| **S2** | Systemic quality degradation affecting many outputs | Retrieval index corruption; override rate doubles | 4h: assess, likely suspend |
| **S3** | Control failure without confirmed wrong outputs | Audit logging gap; guardrail bypass found in testing | 24h |
| **S4** | Degradation without quality impact | Latency breach; cost spike; cache regression | Next business day |

### 4.2 S1/S2 response

1. **Contain (0–1h)** — switch to manual mode. The pre-existing analyst process is the fallback and it is
   always available. Never debug a suspected-wrong AI system while it is still producing outputs people act on.
2. **Scope (1–4h)** — the audit log is the instrument. Query every affected output by model version, prompt
   hash, retrieval config and time window. **This is why write-before-surface logging is non-negotiable** —
   without it, scoping an AI incident is guesswork.
3. **Assess affected decisions (4–24h)** — with AML Ops, re-review every decision in the affected window that
   the recommendation could have influenced. Wrongly-closed alerts are re-opened.
4. **Reportability assessment (within 24h)** — documented assessment against EU AI Act Art. 73 serious-incident
   criteria, DORA ICT incident thresholds, and AML regulatory notification duties. **Documented whether or
   not it is reportable.** DPO involved if personal data is implicated.
5. **Root cause (1–5 days)** — reproduce against the golden set. If it does not reproduce, the golden set has
   a gap and closing it is part of the fix.
6. **Remediate and re-gate** — fix, add the incident as a permanent golden-set case, pass the full gate suite,
   restore in shadow mode before returning to production.
7. **Post-incident review at the AI Council** — the risk register is updated in the same meeting.

### 4.3 The scenario I plan for

**A subtle retrieval regression.** Not an outage — a change to the corpus indexing that makes retrieval
slightly worse for one typology class. Citations still verify (the cited chunks exist and support the
claims), latency is normal, availability is 100%, and aggregate disposition agreement moves 2 points, which
is inside noise. Nothing alerts.

What catches it: **override reasons, categorised**. Analysts start writing "missed the structuring pattern"
in override reasons for one typology, and the per-stratum breakdown of the monthly production golden-set run
shows one stratum down 11 points while the aggregate barely moves.

The lesson generalises: **aggregate metrics hide the failures that matter.** Everything is monitored per
stratum — per typology, per segment, per corridor — and human free-text feedback is treated as a
first-class monitoring signal rather than a support channel.
