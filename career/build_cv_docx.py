#!/usr/bin/env python3
"""Build an ATS-friendly .docx of the Head of AI CV.

Usage:  python3 career/build_cv_docx.py
Output: career/Mehreen_Himani_Head_of_AI_CV.docx
"""

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor, Inches

OUT = Path(__file__).parent / "Mehreen_Himani_Head_of_AI_CV.docx"

ACCENT = RGBColor(0x1F, 0x3A, 0x5F)
GREY = RGBColor(0x44, 0x44, 0x44)


def setup(doc):
    for section in doc.sections:
        section.top_margin = Inches(0.5)
        section.bottom_margin = Inches(0.5)
        section.left_margin = Inches(0.6)
        section.right_margin = Inches(0.6)
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(9.5)
    style.paragraph_format.space_after = Pt(2)
    style.paragraph_format.line_spacing = 1.02


def para(doc, space_before=0, space_after=2):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    return p


def run(p, text, size=9.5, bold=False, italic=False, color=None, caps=False):
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    if color is not None:
        r.font.color.rgb = color
    if caps:
        r.font.all_caps = True
    return r


def section_heading(doc, text):
    p = para(doc, space_before=9, space_after=3)
    run(p, text, size=10.5, bold=True, color=ACCENT, caps=True)
    # thin rule
    rule = para(doc, space_before=0, space_after=4)
    run(rule, "_" * 108, size=5, color=ACCENT)


def role(doc, title, org, dates, subtitle=None):
    p = para(doc, space_before=6, space_after=0)
    run(p, title, size=10, bold=True)
    run(p, "  —  ", size=10, color=GREY)
    run(p, org, size=10, bold=True, color=ACCENT)
    d = para(doc, space_after=1)
    run(d, dates, size=9, italic=True, color=GREY)
    if subtitle:
        s = para(doc, space_after=2)
        run(s, subtitle, size=9, italic=True, color=GREY)


def bullet(doc, segments):
    """segments: list of (text, bold) tuples."""
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Inches(0.19)
    p.paragraph_format.first_line_indent = Inches(-0.13)
    for text, bold in segments:
        run(p, text, size=9.5, bold=bold)
    return p


def labelled(doc, label, body):
    p = para(doc, space_after=3)
    run(p, label + " — ", size=9.5, bold=True, color=ACCENT)
    run(p, body, size=9.5)


def build():
    doc = Document()
    setup(doc)

    # ---------- Header ----------
    p = para(doc, space_after=0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(p, "MEHREEN HIMANI", size=20, bold=True, color=ACCENT)

    p = para(doc, space_after=2)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(p, "Head of AI  |  AI Governance, Risk & Delivery  |  Regulated Financial Services",
        size=10.5, bold=True, color=GREY)

    p = para(doc, space_after=6)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(p, "Stuttgart, Germany  ·  +49 152 1516 2753  ·  himanimehreen@gmail.com  ·  LinkedIn  ·  GitHub",
        size=9, color=GREY)

    # ---------- Summary ----------
    section_heading(doc, "Summary")
    p = para(doc, space_after=3)
    run(p, "AI leader with ", size=9.5)
    run(p, "14 years in regulated financial services", size=9.5, bold=True)
    run(p, " — AML/CFT, credit and market risk, post-trade settlements, cyber security — now building and "
           "leading AI capability end to end. I combine the two things most AI leadership roles struggle to "
           "hire together: ", size=9.5)
    run(p, "hands-on fluency with LLM and multi-agent systems", size=9.5, bold=True)
    run(p, " (7 production AI products shipped in the last 12 months, all built by me) and ", size=9.5)
    run(p, "the regulatory grounding to put them into production inside a bank", size=9.5, bold=True)
    run(p, " (EU AI Act, DORA, GDPR, AML/CFT, Basel III).", size=9.5)

    p = para(doc, space_after=3)
    run(p, "I lead AI the way it has to work in a regulated market: use cases triaged by ", size=9.5)
    run(p, "value × risk", size=9.5, bold=True)
    run(p, ", models selected on ", size=9.5)
    run(p, "cost per resolved case", size=9.5, bold=True)
    run(p, " rather than benchmark scores, agent autonomy bounded by ", size=9.5)
    run(p, "guardrails and human-in-the-loop", size=9.5, bold=True)
    run(p, ", and every decision ", size=9.5)
    run(p, "evidenced in an audit trail a regulator can read", size=9.5, bold=True)
    run(p, ". I have taken AI programmes from a blank page — 12+ use cases prioritised with risk and "
           "delivery, LLM enablement rolled out across 4 business units ($600K+ annual savings identified), "
           "a 3× rise in AI pilot proposals within 3 months — and built and mentored distributed teams of "
           "20+ across four time zones to deliver them.", size=9.5)

    # ---------- Capabilities ----------
    section_heading(doc, "Core Leadership Capabilities")
    labelled(doc, "AI Strategy & Commercial Ownership",
             "AI operating model design · use-case portfolio and intake funnel · value-vs-risk "
             "prioritisation · business case and ROI modelling · build-vs-buy · vendor and model selection · "
             "budget, resourcing and delivery economics · proposal and pitch development")
    labelled(doc, "AI Governance, Risk & Compliance",
             "EU AI Act (risk classification, Art. 9 risk management, Art. 12 logging, Art. 13 "
             "transparency, Art. 14 human oversight, Art. 15 accuracy/robustness) · DORA ICT third-party "
             "risk · GDPR (DPIA, Art. 22) · AML/CFT · Basel III · ISO/IEC 42001 and NIST AI RMF alignment · "
             "model risk management and AI audit readiness")
    labelled(doc, "LLM & Agentic Systems",
             "RAG and hybrid retrieval · multi-agent orchestration and tool design · prompt and context "
             "engineering · three-layer guardrails · LLM-as-judge and golden-set evaluation · hallucination "
             "and drift monitoring · human-in-the-loop design")
    labelled(doc, "AI Cost & FinOps",
             "token economics and cost-per-outcome modelling · model routing and cascades · prompt caching "
             "and batch processing · context budgeting · cost guardrails and per-tenant spend caps · unit "
             "economics and margin management")
    labelled(doc, "Delivery & People Leadership",
             "end-to-end programme delivery in regulated environments · Agile, Scrum, SAFe (PI planning) · "
             "onshore/offshore teams of 20+ · hiring, coaching and capability building · C-level and "
             "CRO/CFO stakeholder management · multi-region rollout (EMEA, US, APAC)")

    # ---------- Experience ----------
    section_heading(doc, "Experience")

    role(doc, "AI Delivery & Enablement Lead (Consultant)", "Capgemini (Sogeti), Stuttgart, Germany",
         "Apr 2023 – Present",
         "AI enablement, quality strategy and programme delivery across banking, capital markets and automotive.")
    bullet(doc, [("Led the LLM-powered AI enablement rollout across 4 business units", True),
                 (" end to end — set the adoption roadmap, ran the cross-functional team of consultants and "
                  "delivery leads, owned Agile cadence, milestones, risks and dependencies. ", False),
                 ("$600K+ in annual savings identified.", True)])
    bullet(doc, [("Built the AI use-case intake and prioritisation model", True),
                 (" — ran risk-based triage of 12+ candidate use cases with delivery and risk stakeholders, "
                  "defining quality gates and delivery milestones per use case. Result: ", False),
                 ("85% stakeholder alignment and a 3× rise in AI pilot proposals within 3 months", True),
                 (" — the practice's demand pipeline went from ad hoc to structured.", False)])
    bullet(doc, [("Designed and stood up the AI evaluation and testing framework", True),
                 (" now used to gate LLM features before release — ", False),
                 ("LLM answer consistency +25%, hallucination rate −40%, model failure rate −30%.", True)])
    bullet(doc, [("Ship production AI products hands-on", True),
                 (" — 7 shipped in 12 months across agentic banking, payments integrity, KYC triage, fraud "
                  "detection, compliance triage and regulatory RAG (portfolio below). This is what lets me "
                  "size an engagement, challenge an architecture and earn the trust of engineers.", False)])
    bullet(doc, [("Lead the testing and delivery-planning workstream of a ", False),
                 ("SAP S/4HANA migration", True),
                 (" — test strategy, delivery plan, workstream and defect-triage coordination, data "
                  "migration validation, hands-on system testing.", False)])

    role(doc, "Project Quality Manager", "Standard Chartered Bank, Warsaw, Poland", "Mar 2022 – Sept 2022",
         "Credit Risk Analytics and cyber-security programmes; audit risk reduced 40% through integrated governance.")
    bullet(doc, [("Owned scope, objectives, deliverables and the full delivery plan for the ", False),
                 ("Credit Risk Analytics Platform", True),
                 (" across ", False), ("50+ stakeholders", True),
                 (" in Risk, Finance and Compliance — validated ", False),
                 ("Basel III stress-testing and ECB FINREP", True),
                 (" workflows, cutting the forecast cycle from ", False),
                 ("5 days to 8 hours.", True)])
    bullet(doc, [("Delivered the ", False), ("ETV (Encrypted Traffic Visibility)", True),
                 (" cyber-security platform — ", False),
                 ("AI/ML-driven network traffic analysis", True),
                 (" via passive monitoring; owned vendor coordination, execution tracking and risk "
                  "resolution. Direct experience validating an ML system whose false positives carry "
                  "operational cost.", False)])
    bullet(doc, [("Ran delivery governance across ", False), ("4 time zones", True),
                 (" (Warsaw, London, Mumbai, Singapore) and served as the ", False),
                 ("escalation point for CRO/CFO", True), (" on regulatory deadlines.", False)])
    bullet(doc, [("Implemented shift-left testing with BDD and 50+ automated validation checks — ", False),
                 ("calculation errors −85%, audit findings −60%", True),
                 ("; built and mentored a distributed team through hiring, interviewing and coaching.", False)])

    role(doc, "Project Manager", "UBS (via Wipro Technologies), Wrocław, Poland", "Dec 2020 – Feb 2022",
         "AML false positives cut 45% through NICE Actimize model testing and tuning.")
    bullet(doc, [("Led end-to-end testing and tuning of the ", False),
                 ("NICE Actimize AML monitoring platform", True), (" — ", False),
                 ("false positives −45%, 2,000+ analyst hours saved annually, suspicious-activity detection "
                  "+30%.", True),
                 (" The clearest analogue in my background to modern AI risk work: a scored decisioning "
                  "system, a precision/recall trade-off with real regulatory consequence, and a defensible "
                  "tuning rationale.", False)])
    bullet(doc, [("Owned ", False),
                 ("estimation, scheduling, resourcing and portfolio invoicing", True),
                 (" across onshore/offshore teams; facilitated PI planning for 3 Agile teams — ", False),
                 ("throughput +25%, cycle time 4 → 2.5 weeks", True), (", 4 major releases on time.", False)])
    bullet(doc, [("Ran defect triage with business and compliance stakeholders across US, Swiss and German "
                  "teams (Corporate Banking, Private Banking, Financial Crime IT).", False)])

    role(doc, "Project Lead", "Credit Suisse (via Wipro Technologies), Wrocław, Poland", "Jul 2018 – May 2019")
    bullet(doc, [("Led functional and UAT delivery for the ", False), ("Loan Stress Testing", True),
                 (" platform (Private Banking, Zurich); built a quality index that cut ", False),
                 ("P&L forecasting errors 20%", True), (" and drove ", False),
                 ("30% faster release cycles.", True)])
    bullet(doc, [("Owned delivery and PI planning for 2 Scrum teams — 30+ features over 4 PIs at ", False),
                 ("90% on-time delivery.", True)])

    role(doc, "Test Lead", "Credit Suisse (via Wipro Technologies), London, UK / Pune, India",
         "Jan 2013 – Jun 2018")
    bullet(doc, [("Led the ", False), ("multi-region rollout", True),
                 (" of the Real-Time Settlements programme across ", False),
                 ("EMEA, US and APAC", True), (" with CI/CD-integrated regression — ", False),
                 ("regression time −60%, settlement failures −25%.", True)])
    bullet(doc, [("Led a ", False), ("23-member offshore team", True),
                 (" across equity, stock borrow/loan, asset servicing and clearing — ", False),
                 ("97% SLA adherence, 35% defect-leakage reduction.", True)])
    bullet(doc, [("Delivered market-risk regulatory programmes (", False),
                 ("VaR Feed Automation, Volcker, FRTB, TSRD", True),
                 (") with VaR/SVaR validation and daily consolidated reporting.", False)])
    bullet(doc, [("Built “Kandoo,” an internal automation product — ", True),
                 ("$205K annual savings", True),
                 (", trade testing time −50%, 99.2% coverage with zero critical defects across 8 "
                  "consecutive releases. My first experience of building an internal product and owning its "
                  "business case.", False)])

    p = para(doc, space_before=4, space_after=2)
    run(p, "Career breaks: Parental leave (Elternzeit) & German language studies — Oct 2022 – Mar 2023; "
           "parental leave — Jun 2019 – Nov 2020.", size=8.5, italic=True, color=GREY)

    # ---------- Portfolio ----------
    section_heading(doc, "AI Product Portfolio — Built & Shipped")
    p = para(doc, space_after=4)
    run(p, "Seven production AI products designed, built and shipped in 12 months. Each scoped as a "
           "regulated-market product: a named user, a measurable outcome, an evaluation framework and a "
           "compliance position.", size=9, italic=True, color=GREY)

    products = [
        ("BankFlow AI", "Agentic banking platform — multi-agent orchestration across 8 tools; three-layer "
                        "guardrails, LLM-as-judge evaluation suite, EU AI Act / AML / DORA compliance "
                        "embedded in agent reasoning and audit trail."),
        ("PayClear AI", "Zero-trust payment integrity — pre-execution invoice interception, IBAN "
                        "verification, visual spoofing detection; composite Trust Index scoring with "
                        "risk-tiered intervention."),
        ("OnboardIQ", "Explainable KYC onboarding triage — routes to auto-approve, fast-track or manual "
                      "review with full decision traceability; a working Art. 14 human-oversight pattern."),
        ("PayGuard AI", "Real-time payments fraud detection — AI-generated explanations, analyst review "
                        "queue, EU AI Act compliance score 87/100."),
        ("ComplianceIQ", "AI compliance alert triage across 6 categories — simulated false positives "
                         "45% → 22%, resolution time 8.4h → 4.2h, ~2,100 analyst hours saved annually."),
        ("PulseAI", "Multi-agent product intelligence — 4-agent pipeline (n8n + Claude API) turning raw "
                    "feedback into PRDs; ~80% reduction in manual analysis."),
        ("RegCopilot", "RAG copilot for EU regulatory compliance — 33,536 chunks across EU AI Act, DORA, "
                       "AMLD6 and GDPR via Supabase pgvector; 82% eval accuracy on a golden set, "
                       "citation-grounded answers, immutable audit trail satisfying EU AI Act Art. 13."),
    ]
    for name, desc in products:
        bullet(doc, [(name + ": ", True), (desc, False)])

    p = para(doc, space_before=4, space_after=2)
    run(p, "Flagship reference case study: ", size=9, bold=True)
    run(p, "Project AEGIS — building an enterprise AI function from zero and shipping the first regulated "
           "agentic product to production. Covers operating model, EU AI Act conformity mapping, model and "
           "vendor strategy, agent architecture, token-level unit economics, risk register and commercial "
           "model.", size=9, italic=True)

    # ---------- Education / Certs / Skills ----------
    section_heading(doc, "Education & Certifications")
    p = para(doc, space_after=2)
    run(p, "M.Sc. Information Technology", size=9.5, bold=True)
    run(p, " — Vellore Institute of Technology, Pune, India · 2013–2017", size=9.5)
    p = para(doc, space_after=3)
    run(p, "M.Sc. Biotechnology", size=9.5, bold=True)
    run(p, " — Bangalore University, Bangalore, India · 2010–2012", size=9.5)
    p = para(doc, space_after=2)
    run(p, "Certifications: ", size=9.5, bold=True)
    run(p, "AI Agents Certified PM — Product School (Feb 2026) · LLM Foundations Certified PM — Product "
           "School (Feb 2026) · Certified Scrum Product Owner® (CSPO®) — Scrum Alliance (Dec 2022) · "
           "PMP® Exam Preparation, 35 contact hours", size=9.5)

    section_heading(doc, "Skills")
    labelled(doc, "AI & Engineering",
             "GenAI, LLMs, multi-agent systems, RAG, hybrid retrieval, prompt & context engineering, AI "
             "evaluation frameworks, LLM-as-judge, guardrail design, human-in-the-loop, AI workflow "
             "automation, Claude API, HuggingFace, n8n, Supabase (pgvector), Python, SQL, PostgreSQL, "
             "Cursor, Lovable, CI/CD")
    labelled(doc, "Governance & Domain",
             "EU AI Act, DORA, GDPR, AML/CFT (NICE Actimize), Basel III, ECB FINREP, credit risk, model "
             "risk management, compliance management, enterprise governance, SAP S/4HANA, data migration "
             "validation")
    labelled(doc, "Leadership & Delivery",
             "AI strategy, operating model design, product roadmapping, OKRs/KPIs, RICE, budget & resource "
             "management, vendor management, risk & issue management, Agile/Scrum/SAFe (PI planning), "
             "Kanban, Jira, Confluence, ServiceNow, stakeholder management, mentorship, negotiation")
    labelled(doc, "Languages", "English (C1) · German (B1) · Hindi (native)")

    doc.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
