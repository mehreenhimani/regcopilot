#!/usr/bin/env python3
"""Build an ATS-friendly .docx of the Head of AI Governance & Transformation CV.

Usage:  python3 career/build_governance_cv_docx.py
Output: career/Mehreen_Himani_Head_of_AI_Governance_CV.docx

Shares layout helpers with build_cv_docx.py.
"""

import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from build_cv_docx import (  # noqa: E402
    ACCENT,
    GREY,
    bullet,
    labelled,
    para,
    role,
    run,
    section_heading,
    setup,
)

OUT = HERE / "Mehreen_Himani_Head_of_AI_Governance_CV.docx"


def build():
    doc = Document()
    setup(doc)

    # ---------- Header ----------
    p = para(doc, space_after=0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(p, "MEHREEN HIMANI", size=20, bold=True, color=ACCENT)

    p = para(doc, space_after=2)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(p, "Head of AI Governance & Transformation  |  AI Strategy · Process Excellence · EU AI Act",
        size=10.5, bold=True, color=GREY)

    p = para(doc, space_after=6)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run(p, "Stuttgart, Germany  ·  +49 152 1516 2753  ·  himanimehreen@gmail.com  ·  LinkedIn  ·  GitHub",
        size=9, color=GREY)

    # ---------- Summary ----------
    section_heading(doc, "Summary")
    p = para(doc, space_after=3)
    run(p, "Process transformation is what I have done for 14 years — I now do it with AI.", size=9.5, bold=True)
    run(p, " Forecast cycle cut from 5 days to 8 hours. Regression cycle time down 60%. AML false positives "
           "down 45%. Alert resolution from 8.4 to 4.2 hours. Every one of those is an as-is process "
           "analysed, a bottleneck quantified, a to-be process designed, and a benefit measured — in "
           "regulated financial services, where the redesign has to satisfy Risk, Compliance and an auditor "
           "before it satisfies anyone else.", size=9.5)

    p = para(doc, space_after=3)
    run(p, "In the last 12 months I have added the AI half. I led an ", size=9.5)
    run(p, "LLM enablement rollout across 4 business units", size=9.5, bold=True)
    run(p, " ($600K+ annual savings identified), built the ", size=9.5)
    run(p, "use-case intake and prioritisation model", size=9.5, bold=True)
    run(p, " that took the pipeline from ad hoc to structured (12+ use cases triaged, ", size=9.5)
    run(p, "3× rise in AI pilot proposals in 3 months", size=9.5, bold=True)
    run(p, "), and designed the ", size=9.5)
    run(p, "AI evaluation framework", size=9.5, bold=True)
    run(p, " that now gates LLM features before release. Alongside that I have designed and shipped ", size=9.5)
    run(p, "7 production AI products", size=9.5, bold=True)
    run(p, " myself — agentic orchestration, RAG, guardrails, evaluation harnesses — each with an ", size=9.5)
    run(p, "EU AI Act compliance position", size=9.5, bold=True)
    run(p, " built in from the start.", size=9.5)

    p = para(doc, space_after=3)
    run(p, "That combination is the whole job: find the process opportunity, quantify the business case, "
           "design the AI-enabled to-be, deliver it, prove the benefit, and keep it compliant. ",
        size=9.5, bold=True)
    run(p, "Most candidates have one half.", size=9.5)

    # ---------- Capabilities ----------
    section_heading(doc, "Core Capabilities")
    labelled(doc, "AI Strategy & Portfolio Management",
             "company-wide AI strategy and roadmap · AI use-case discovery across departments · intake "
             "funnel and value × risk × feasibility prioritisation · portfolio governance and stage gates · "
             "build-vs-buy · vendor and model selection · business case development and ROI modelling")
    labelled(doc, "Process Excellence & Transformation",
             "as-is process analysis and bottleneck quantification · AI-enabled to-be process design · "
             "shift-left and quality-gate design · cycle-time, throughput and defect-leakage improvement · "
             "benefit baselining and measured realisation · value stream thinking · Agile, Scrum, SAFe "
             "(PI planning), Kanban")
    labelled(doc, "AI Governance & Regulatory Compliance",
             "EU AI Act (risk classification, Art. 9 risk management, Art. 12 logging, Art. 13 "
             "transparency, Art. 14 human oversight, Art. 15 accuracy) · DORA ICT third-party risk · GDPR "
             "(DPIA, Art. 22) · AML/CFT · Basel III · ECB FINREP · ISO/IEC 42001 and NIST AI RMF alignment · "
             "model risk management · working alongside Legal, Compliance and IT Security")
    labelled(doc, "GenAI, Agentic & Automation Delivery",
             "LLMs and multi-agent orchestration · RAG and retrieval design · NLP-based document and alert "
             "triage · AI workflow automation · prompt and context engineering · guardrail design · "
             "LLM-as-judge and golden-set evaluation · human-in-the-loop design · AI cost and unit economics")
    labelled(doc, "Change Leadership & Facilitation",
             "cross-functional workshop facilitation · PI planning across multiple teams · 50+ stakeholder "
             "programmes · C-level and CRO/CFO engagement · adoption roadmaps, training material and "
             "operational handover · onshore/offshore teams of 20+ · hiring, coaching and capability building")

    # ---------- Experience ----------
    section_heading(doc, "Experience")

    role(doc, "AI Transformation & Delivery Lead (Consultant)", "Capgemini (Sogeti), Stuttgart, Germany",
         "Apr 2023 – Present",
         "AI strategy, use-case portfolio and delivery across banking, capital markets and automotive.")
    bullet(doc, [("Led the LLM-powered AI enablement rollout across 4 business units", True),
                 (" — analysed existing workflows, designed the AI-enabled target processes, and owned the "
                  "adoption roadmap, milestones, risks and dependencies with a cross-functional team of "
                  "consultants and delivery leads. ", False),
                 ("$600K+ annual savings identified.", True)])
    bullet(doc, [("Built the AI use-case discovery and prioritisation model", True),
                 (" now used to govern the portfolio — ran risk-based triage of ", False),
                 ("12+ candidate use cases", True),
                 (" with delivery and risk stakeholders, defining quality gates and delivery milestones per "
                  "use case. ", False),
                 ("85% stakeholder alignment and a 3× rise in AI pilot proposals within 3 months.", True)])
    bullet(doc, [("Established the KPI and benefit framework", True),
                 (" for AI initiatives — baseline capture, measured realisation and stage-gate criteria, so "
                  "value is evidenced rather than asserted.", False)])
    bullet(doc, [("Designed the AI evaluation and testing framework", True),
                 (" that gates LLM features before release — ", False),
                 ("answer consistency +25%, hallucination rate −40%, model failure rate −30%.", True)])
    bullet(doc, [("Embedded EU AI Act and regulatory considerations into use-case triage", True),
                 (" — risk classification and compliance position agreed with risk stakeholders before "
                  "build, not retrofitted after.", False)])
    bullet(doc, [("Lead the testing and delivery-planning workstream of a ", False),
                 ("SAP S/4HANA migration", True),
                 (" — test strategy, delivery plan, workstream and defect-triage coordination, data "
                  "migration validation.", False)])

    role(doc, "Project Quality Manager", "Standard Chartered Bank, Warsaw, Poland", "Mar 2022 – Sept 2022",
         "Credit Risk Analytics and cyber-security programmes; audit risk reduced 40% through integrated governance.")
    bullet(doc, [("Redesigned the regulatory forecasting process end to end", True),
                 (" for the Credit Risk Analytics Platform — analysed the as-is workflow with Risk, Finance "
                  "and Compliance across ", False),
                 ("50+ stakeholders", True), (", validated ", False),
                 ("Basel III stress-testing and ECB FINREP", True), (" flows, and cut the ", False),
                 ("forecast cycle from 5 days to 8 hours.", True)])
    bullet(doc, [("Implemented shift-left quality gates with BDD and 50+ automated validation checks", True),
                 (" — moved defect detection upstream and cut ", False),
                 ("calculation errors 85% and audit findings 60%.", True)])
    bullet(doc, [("Delivered the ", False), ("ETV (Encrypted Traffic Visibility)", True),
                 (" platform — ", False), ("AI/ML-driven network traffic analysis", True),
                 ("; owned vendor coordination, execution tracking and risk resolution.", False)])
    bullet(doc, [("Ran delivery governance across ", False), ("4 time zones", True),
                 (" (Warsaw, London, Mumbai, Singapore); ", False),
                 ("escalation point for CRO/CFO", True),
                 (" on regulatory deadlines. Built and mentored a distributed team through hiring and "
                  "coaching, and produced manuals and training material for operational handover.", False)])

    role(doc, "Project Manager", "UBS (via Wipro Technologies), Wrocław, Poland", "Dec 2020 – Feb 2022",
         "AML false positives cut 45% through NICE Actimize model tuning — 2,000+ analyst hours saved annually.")
    bullet(doc, [("Re-engineered the AML alert triage process", True),
                 (" — led end-to-end testing and tuning of the NICE Actimize monitoring platform, cutting ",
                  False),
                 ("false positives 45%", True), (", saving ", False),
                 ("2,000+ analyst hours annually", True), (" and raising ", False),
                 ("suspicious-activity detection 30%.", True),
                 (" A scored decisioning system with a precision/recall trade-off and a defensible tuning "
                  "rationale — the closest analogue in traditional banking to modern AI risk work.", False)])
    bullet(doc, [("Improved delivery flow across 3 Agile teams", True),
                 (" — facilitated PI planning and removed hand-off bottlenecks: ", False),
                 ("throughput +25%, cycle time 4 → 2.5 weeks", True),
                 (", 4 major releases delivered on time.", False)])
    bullet(doc, [("Owned estimation, scheduling, resourcing and portfolio invoicing across onshore/offshore "
                  "teams; ran defect triage with business and compliance stakeholders across US, Swiss and "
                  "German entities.", False)])

    role(doc, "Project Lead", "Credit Suisse (via Wipro Technologies), Wrocław, Poland", "Jul 2018 – May 2019")
    bullet(doc, [("Led functional and UAT delivery for the ", False), ("Loan Stress Testing", True),
                 (" platform (Private Banking, Zurich); built a ", False), ("quality index", True),
                 (" that cut ", False), ("P&L forecasting errors 20%", True), (" and drove ", False),
                 ("30% faster release cycles.", True)])
    bullet(doc, [("Owned delivery and PI planning for 2 Scrum teams — 30+ features over 4 PIs at ", False),
                 ("90% on-time delivery.", True)])

    role(doc, "Test Lead", "Credit Suisse (via Wipro Technologies), London, UK / Pune, India",
         "Jan 2013 – Jun 2018")
    bullet(doc, [("Led the ", False), ("multi-region rollout", True),
                 (" of the Real-Time Settlements programme across ", False), ("EMEA, US and APAC", True),
                 ("; introduced CI/CD-integrated regression — ", False),
                 ("regression cycle time −60%, settlement failures −25%.", True)])
    bullet(doc, [("Built “Kandoo,” an internal automation product — ", True),
                 ("$205K annual savings", True), (", ", False), ("trade testing time −50%", True),
                 (", 99.2% coverage with zero critical defects across 8 consecutive releases. Identified the "
                  "manual bottleneck, built the tool, and owned the business case.", False)])
    bullet(doc, [("Led a ", False), ("23-member offshore team", True),
                 (" across equity, stock borrow/loan, asset servicing and clearing — ", False),
                 ("97% SLA adherence, 35% defect-leakage reduction.", True)])
    bullet(doc, [("Delivered market-risk regulatory programmes (", False),
                 ("VaR Feed Automation, Volcker, FRTB, TSRD", True),
                 (") with VaR/SVaR validation and daily consolidated reporting.", False)])

    p = para(doc, space_before=4, space_after=2)
    run(p, "Career breaks: Parental leave (Elternzeit) & German language studies — Oct 2022 – Mar 2023; "
           "parental leave — Jun 2019 – Nov 2020.", size=8.5, italic=True, color=GREY)

    # ---------- Portfolio ----------
    section_heading(doc, "AI Product Portfolio — Built & Shipped")
    p = para(doc, space_after=4)
    run(p, "Seven production AI products designed, built and shipped in 12 months. Each targets a specific "
           "process bottleneck, with a measured outcome and a compliance position.",
        size=9, italic=True, color=GREY)

    products = [
        ("ComplianceIQ", "Compliance alert triage across 6 categories — false positives 45% → 22%, "
                         "resolution time 8.4h → 4.2h, ~2,100 analyst hours saved annually."),
        ("BankFlow AI", "Multi-step banking operations via agentic orchestration across 8 tools — "
                        "three-layer guardrails, LLM-as-judge evaluation, EU AI Act / AML / DORA compliance "
                        "in agent reasoning and audit trail."),
        ("OnboardIQ", "KYC onboarding triage — routes to auto-approve, fast-track or manual review with "
                      "full decision traceability; a working Art. 14 human-oversight pattern."),
        ("PayGuard AI", "Payments fraud review — AI-generated explanations, analyst review queue, EU AI Act "
                        "compliance score 87/100."),
        ("PayClear AI", "Pre-execution payment integrity — invoice interception, IBAN verification, visual "
                        "spoofing detection, composite Trust Index scoring."),
        ("PulseAI", "Product feedback analysis into requirements — 4-agent pipeline (n8n + Claude API) "
                    "turning raw feedback into PRDs; ~80% reduction in manual analysis."),
        ("RegCopilot", "Regulatory research across EU AI Act, DORA, AMLD6 and GDPR — 33,536 indexed chunks "
                       "via Supabase pgvector; 82% eval accuracy, citation-grounded answers, immutable "
                       "audit trail satisfying EU AI Act Art. 13."),
    ]
    for name, desc in products:
        bullet(doc, [(name + ": ", True), (desc, False)])

    p = para(doc, space_before=4, space_after=2)
    run(p, "Reference case study: ", size=9, bold=True)
    run(p, "Project AEGIS — standing up an enterprise AI function from zero and taking a regulated agentic "
           "product to production. Operating model and use-case intake scoring, EU AI Act conformity "
           "mapping, agent architecture, unit economics, risk register, benefit tracking and business case.",
        size=9, italic=True)

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
    p = para(doc, space_after=3)
    run(p, "In progress: ", size=9.5, bold=True, color=ACCENT)
    run(p, "IAPP AIGP (AI Governance Professional) · BPMN 2.0 & SAP Signavio · Celonis process mining · "
           "Lean Six Sigma Green Belt", size=9.5, italic=True)

    section_heading(doc, "Skills")
    labelled(doc, "AI & Automation",
             "GenAI, LLMs, multi-agent systems, RAG, NLP, prompt & context engineering, AI evaluation "
             "frameworks, LLM-as-judge, guardrail design, human-in-the-loop, AI workflow automation, "
             "Claude API, HuggingFace, n8n, Supabase (pgvector), Python, SQL, PostgreSQL, Cursor, Lovable, "
             "CI/CD")
    labelled(doc, "Process & Delivery",
             "as-is/to-be process design, process improvement, shift-left testing, quality gates, "
             "cycle-time and throughput optimisation, benefit baselining and realisation, business case "
             "development, OKRs/KPIs, RICE, product roadmapping, Agile, Scrum, SAFe (PI planning), Kanban, "
             "Jira, Confluence, ServiceNow, SAP S/4HANA, data migration validation")
    labelled(doc, "Governance & Domain",
             "EU AI Act, DORA, GDPR, AML/CFT (NICE Actimize), Basel III, ECB FINREP, credit risk, model "
             "risk management, compliance management, enterprise governance, vendor management, risk & "
             "issue management")
    labelled(doc, "Leadership",
             "cross-functional workshop facilitation, stakeholder management, strategic planning, "
             "analytical thinking, decision making, negotiation, mentorship")
    labelled(doc, "Languages", "English (C1) · German (B1) · Hindi (native)")

    doc.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
