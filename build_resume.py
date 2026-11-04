"""Builds output/pdf/Eduardo_Gaitan_Resume_2026.pdf (two pages, US letter).

Run:  uv run --with reportlab python build_resume.py

Uses embedded Arial and Times New Roman to retain the original sans/serif
design. Set RESUME_FONT_DIR to a directory containing those .ttf files when
running outside macOS. Importing this module never writes a PDF.
"""

from io import BytesIO
import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output" / "pdf" / "Eduardo_Gaitan_Resume_2026.pdf"

UPDATED = "Updated November 2026"
DOC_TITLE = "Eduardo Gaitán - Resume (November 2026)"
DOC_SUBJECT = "Data Scientist & AI Engineer · Economist · Independent consultant"
CONTENT_WIDTH = letter[0] - 0.9 * inch - 12  # Default Frame padding: 6 pt per side.


def register_resume_fonts():
    font_dir = Path(os.environ.get("RESUME_FONT_DIR", "/System/Library/Fonts/Supplemental"))
    families = {"ResumeSans": "Arial", "ResumeSerif": "Times New Roman"}
    variants = {"": "", "-Bold": " Bold", "-Italic": " Italic", "-BoldItalic": " Bold Italic"}
    for family, filename in families.items():
        for suffix, file_suffix in variants.items():
            path = font_dir / f"{filename}{file_suffix}.ttf"
            if not path.is_file():
                raise FileNotFoundError(f"Missing font: {path}. Set RESUME_FONT_DIR to the font directory.")
            pdfmetrics.registerFont(TTFont(f"{family}{suffix}", str(path)))
        pdfmetrics.registerFontFamily(
            family, normal=family, bold=f"{family}-Bold",
            italic=f"{family}-Italic", boldItalic=f"{family}-BoldItalic",
        )


register_resume_fonts()

BLUE = colors.HexColor("#1558a6")
BLACK = colors.HexColor("#111111")
GRAY = colors.HexColor("#444444")
LIGHT = colors.HexColor("#6b6b6b")

styles = getSampleStyleSheet()
title = ParagraphStyle("ResumeTitle", parent=styles["Normal"], fontName="ResumeSans-Bold", fontSize=18.5,
                       leading=21, alignment=TA_CENTER, textColor=BLACK, spaceAfter=2)
headline = ParagraphStyle("Headline", parent=styles["Normal"], fontName="ResumeSans", fontSize=9.8,
                          leading=12, alignment=TA_CENTER, textColor=BLUE, spaceAfter=3)
contact = ParagraphStyle("Contact", parent=styles["Normal"], fontName="ResumeSerif", fontSize=9.3,
                         leading=11.4, alignment=TA_CENTER, textColor=BLACK, spaceAfter=1)
updated = ParagraphStyle("Updated", parent=contact, fontSize=8.2, textColor=LIGHT, spaceAfter=0)
section_title = ParagraphStyle("SectionTitle", parent=styles["Normal"], fontName="ResumeSans-Bold", fontSize=10.2,
                               leading=11.6, textColor=BLACK, spaceBefore=3, spaceAfter=2, keepWithNext=True)
body = ParagraphStyle("Body", parent=styles["Normal"], fontName="ResumeSerif", fontSize=9.3,
                      leading=11.7, textColor=GRAY, spaceAfter=2.0)
summary = ParagraphStyle("Summary", parent=body, fontSize=9.4, leading=12, textColor=BLACK, spaceAfter=1)
job = ParagraphStyle("Job", parent=styles["Normal"], fontName="ResumeSans-Bold", fontSize=9.6,
                     leading=11.4, textColor=BLACK, spaceAfter=0)
job_date = ParagraphStyle("JobDate", parent=job, alignment=TA_RIGHT, fontName="ResumeSans", fontSize=9.0)
bullet = ParagraphStyle("Bullet", parent=body, leftIndent=14, firstLineIndent=-9, bulletIndent=5,
                        fontSize=9.1, leading=11.2, spaceAfter=1.3)
project = ParagraphStyle("Project", parent=job, fontSize=9.5, leading=11.4, spaceBefore=2.5, spaceAfter=0.5)


def p(text, style=body):
    return Paragraph(text, style)


def bullet_p(text, style=bullet):
    return Paragraph(f"&bull;&nbsp;&nbsp;{text}", style)


def section(name, style=section_title):
    return [
        Spacer(1, 1.5),
        Paragraph(name.upper(), style),
        HRFlowable(width="100%", thickness=0.8, color=BLACK, spaceBefore=0, spaceAfter=4),
    ]


def _header_row(left, right, left_style, right_style):
    table = Table([[Paragraph(left, left_style), Paragraph(right, right_style)]],
                  colWidths=[CONTENT_WIDTH - 1.8 * inch, 1.8 * inch])
    table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "ResumeSans"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return table


def job_header(role, dates, left_style=job, right_style=job_date):
    return _header_row(role, dates, left_style, right_style)


def project_header(name, dates, left_style=project, right_style=job_date):
    return _header_row(name, dates, left_style, right_style)


def entry(header, *bullets, bullet_style=bullet):
    """Keep a heading with its bullets on the same page."""
    return KeepTogether([header, *[bullet_p(b, bullet_style) for b in bullets]])


def page_canvas(canvas, doc):
    canvas.saveState()
    canvas.setTitle(doc.document_title)
    canvas.setAuthor("Eduardo Gaitán Escalante")
    canvas.setSubject(doc.document_subject)
    canvas.setFont("ResumeSans", 7.5)
    canvas.setFillColor(LIGHT)
    canvas.drawRightString(letter[0] - 0.45 * inch, 0.22 * inch, f"Eduardo Gaitán · {UPDATED} · page {doc.page}")
    canvas.restoreState()


class ResumeDocTemplate(BaseDocTemplate):
    def __init__(self, filename, document_title=DOC_TITLE, document_subject=DOC_SUBJECT, max_pages=2):
        self.document_title = document_title
        self.document_subject = document_subject
        self.max_pages = max_pages
        super().__init__(filename, pagesize=letter, leftMargin=0.45 * inch, rightMargin=0.45 * inch,
                         topMargin=0.3 * inch, bottomMargin=0.4 * inch, title=document_title,
                         initialFontName="ResumeSans", lang="en-US")
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="normal")
        self.addPageTemplates([PageTemplate(id="resume", frames=frame, onPage=page_canvas)])

    def afterPage(self):
        if self.page > self.max_pages:
            raise ValueError(f"Resume exceeds {self.max_pages} pages; shorten the content before saving.")


def build_pdf(content, output, document_title=DOC_TITLE, document_subject=DOC_SUBJECT):
    """Only replace the output once the complete, at-most-two-page PDF builds."""
    buffer = BytesIO()
    doc = ResumeDocTemplate(buffer, document_title, document_subject)
    doc.build(content)
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(buffer.getvalue())
    return output


def link(url, label=None):
    return f'<a href="{url}" color="#1558a6"><u>{label or url.replace("https://", "")}</u></a>'


story = [
    Paragraph("Eduardo Gaitán Escalante", title),
    Paragraph("Data Scientist &amp; AI Engineer &nbsp;·&nbsp; Economist &nbsp;·&nbsp; "
              "Freelance / project work, 10-20 h/week (UTC-6, Mexico)", headline),
    Paragraph(
        f'{link("mailto:eduardo.gaitan.escalante@gmail.com", "eduardo.gaitan.escalante@gmail.com")}'
        ' &nbsp;•&nbsp; +52 (241) 117-4551 &nbsp;•&nbsp; '
        f'{link("https://www.linkedin.com/in/eduardo-gaitan-1b143b242/", "linkedin.com/in/eduardo-gaitan-1b143b242")}',
        contact,
    ),
    Paragraph(
        f'{link("https://github.com/eduardoge13")} &nbsp;•&nbsp; {link("https://eduardo.srv1175749.hstgr.cloud")}'
        f' &nbsp;•&nbsp; English (fluent) / Spanish (native) &nbsp;•&nbsp; {UPDATED}',
        updated,
    ),
    HRFlowable(width="100%", thickness=1.05, color=BLACK, spaceBefore=4, spaceAfter=5),
]

story += section("Summary")
story += [
    p("Economist (UNAM, honors) working as a data scientist and AI engineer. I build forecasting, econometric "
      "and machine-learning models that answer concrete business questions, then ship them as working systems: "
      "data pipelines, LLM-powered automation, dashboards and containerized services on cloud or VPS. "
      "Freelance and contract work for small and mid-size companies in Mexico and for remote clients; "
      "deliverables are reproducible code, a written report and the system running in production.", summary),
]

story += section("Technical Skills")
story += [
    p("<b>Machine learning &amp; statistics:</b> Python and R (advanced); scikit-learn, XGBoost, LightGBM, H2O, "
      "statsmodels, Isolation Forest, K-Means/DBSCAN; forecasting (Prophet, SARIMA, ETS, Croston), spatial "
      "econometrics, held-out and spatial-block validation, Monte Carlo/Sobol. PyTorch/TensorFlow for satellite imagery."),
    p("<b>AI engineering:</b> Anthropic Claude API with structured outputs, local models with Ollama (Qwen3-VL), "
      "Gemini, n8n, REST APIs, webhooks, OAuth2, schema validation with Pydantic/Zod, per-call cost control "
      "and human-approval gates."),
    p("<b>Data engineering &amp; cloud:</b> SQL, PostgreSQL, SQLite, BigQuery, Polars, pandas, Dask, Parquet, Kedro, MLflow, ETL; "
      "Google Cloud (Cloud Run, Cloud Build, Cloud Storage), Spark/PySpark and Databricks (certifications and one experiment), "
      "web scraping with Playwright."),
    p("<b>Analytics &amp; reporting:</b> Power BI, Streamlit, Plotly, MapLibre/PMTiles, GeoPandas; R tidyverse, "
      "ggplot2, sf and R Markdown; Excel/openpyxl and python-pptx financial reporting; INEGI/CONEVAL/NASA data."),
    p("<b>Applications &amp; delivery:</b> TypeScript/JavaScript, React, Next.js, Astro, Tailwind CSS, Vite, "
      "FastAPI/Flask, Node.js/Fastify/Express, Stripe/Openpay, Telegram/WhatsApp; Docker Compose, Linux, "
      "Traefik/nginx, GitHub Actions, pytest, Vitest, Playwright, Trivy and CrowdSec. "
      "Project-specific: C#/.NET 8 Windows print agent with xUnit tests."),
]

story += section("Experience")
story += [
    entry(job_header("Independent Data Scientist &amp; AI Engineer (freelance / contract)", "Jan 2025 - Present"),
          "Market, demand and pricing studies for small businesses: Huff gravity demand model validated out of "
          "sample, spatial econometric models with spatial-block cross-validation, competition clustering, "
          "ETS/SARIMA forecasts, price-elasticity and seasonality analysis, and Monte Carlo capital planning with "
          "Sobol sensitivity; delivered as reproducible Python reports and investor decks.",
          "With SmartCFO AI (data and finance consultancy): per-SKU, per-branch demand-forecasting pipelines "
          "(Kedro, Prophet, SARIMA, XGBoost, Croston, Mexican-calendar features) tracked in MLflow on BigQuery and "
          "Cloud Run; trip-level cost and revenue analytics; revenue-opportunity dashboards. Contributed to "
          "Smart CFO's SaaS MVP for business valuation and financial projections.",
          "LLM automation in production: a receipt-reading accounting bot on the Claude API with structured "
          "outputs (about US$0.02 per receipt) and a local Qwen3-VL fallback; a Claude-based incident analyst for "
          "server monitoring whose actions require human approval; an agent control plane that runs coding agents, "
          "their tests and opens draft pull requests.",
          "Full systems for restaurants and online stores: point-of-sale and kitchen screens by station, order "
          "intake from WhatsApp, web and delivery platforms, Stripe/Openpay payments, hex-grid sales coverage maps "
          "and automatic delivery assignment; e-commerce for four brands with live Stripe checkout.",
          "Operations: Docker Compose and Traefik on a hardened VPS, scripted deploys with SHA-256 verification "
          "and rollback, Telegram-based tooling, 1,300+ automated tests on the largest codebase."),
    Spacer(1, 2),
    entry(job_header("Naturgy | Data Science Specialist", "Jan 2025 - Jul 2025"),
          "Led a cross-functional team in designing and deploying an <b>Isolation Forest</b> model for anomaly "
          "detection, including ETL pipelines, automation workflows, orchestration, hyperparameter tuning, and "
          "performance analysis using H2O and R.",
          "Modernized a legacy <b>K-Means</b> customer-segmentation model, achieving a 15% improvement in accuracy "
          "and a 10% reduction in training time.",
          "Partnered with Economics and Finance to automate 7 manual processes, reducing processing time from "
          "5 hours per task to under 1 minute and saving hundreds of hours annually.",
          "Proposed and developed a hybrid boosted forecasting model (XGBoost + seasonality) for annual "
          "natural-gas consumption."),
    Spacer(1, 2),
    entry(job_header("National Council of Evaluation of the Social Development Policy | Head of the Small Area "
                     "Estimation Methodologies Department", "Jan 2024 - Jan 2025"),
          "Led a data-pipeline project using Docker, Kedro, PostgreSQL, pgAdmin4, and Git, improving storage and "
          "analysis workflows.",
          "Fitted supervised and unsupervised models including Random Forest, XG/Gradient Boosting, "
          "Regression/Logistic, SVM, neural networks, and hybrid boosted time-series models.",
          "Used SQL to manage queries and manipulate datasets efficiently in pgAdmin4; contributed to "
          "poverty-analysis publications within the technical estimation team."),
    Spacer(1, 2),
    entry(job_header("General Coordination for Planning and Investment - JGCDMX | Environment, Tourism, and "
                     "Economic Development Coordinator", "Oct - Nov 2023"),
          "Automated ETL processes with Python scripts, reducing project-creation times by 20% and making "
          "information available to land teams sooner.",
          "Developed interactive geospatial dashboards using GeoPandas, Leaflet, and Folium for decision-making "
          "and route planning.",
          "Deployed two geospatial models (K-means and Spatial Lag Model) for heatmaps, analytical reporting, and "
          "pattern distribution."),
    Spacer(1, 2),
    entry(job_header("Python &amp; R Developer | Program for Development Studies - UNAM", "Jan 2020 - Sep 2023"),
          "Led the creation of a geospatial night-time-light data pipeline, optimizing analysis, storage, and "
          "reporting with Parquet.",
          "Designed Docker containers for developer environments integrating PostgreSQL databases, Python, and "
          "R tools.",
          "Conducted advanced geospatial estimations for socioeconomic research purposes."),
]

story += section("Selected Projects (2026)")
story += [
    entry(project_header("Demand, competition and capital study for a dark kitchen (client confidential)",
                         "Sep - Oct 2026"),
          "Huff gravity model calibrated with leave-one-municipality-out validation (median absolute error 23% "
          "vs 74% for a naive baseline); OLS/SAR/SEM models with spatial-block CV; DBSCAN/KDE competition "
          "clustering on INEGI DENUE; damped ETS vs SARIMA forecasts; 20,000-run Monte Carlo with Sobol "
          "sensitivity for the capital plan. Python, pandas, LightGBM, ENIGH/Census data, Sentinel-2 CNN features."),
    entry(project_header("Point-of-sale and kitchen-display platform for a dark kitchen | "
                         f"{link('https://bearandchimps.com', 'bearandchimps.com')}", "Jul - Oct 2026"),
          "Fastify + SQLite + React/TypeScript system with kitchen, packing and delivery station screens, "
          "web and delivery-platform order intake via signed webhooks, card payments, Telegram operations bots "
          "and an LLM receipt reader (Claude API with a local Qwen3-VL fallback); 1,300+ automated tests, "
          "scripted deploys with rollback."),
    entry(project_header("Housing price model and data pitch for developers, Monterrey", "Aug 2026"),
          "Playwright scrape of public listings (9,653 published, 936 clean houses across 12 municipalities); "
          "hedonic regression (n=791, R² 0.85, 19% median out-of-sample error, 5-fold CV) with interpretable "
          "coefficients per bathroom, land, parking and bedroom; 17-slide deck and PDF."),
    entry(project_header("Demand-forecasting pipeline for a distributor | with SmartCFO AI", "Sep 2025 - May 2026"),
          "Kedro pipeline (Prophet, SARIMA, XGBoost, Croston/SBC) over ~4,940 branch × manufacturer series, "
          "52-week horizon with 4-week validation, MLflow tracking, BigQuery and Cloud Build; 93× speed-up from "
          "vectorization and a documented fix for a flat-forecast regression."),
    entry(project_header("Yoga Verde: online store and market study | "
                         f"{link('https://yogaverdemx.com', 'yogaverdemx.com')}", "Aug - Oct 2026"),
          "Astro storefront with a private Stripe Checkout backend and SQLite inventory; reproducible study of "
          "unit economics by channel, price elasticity, seasonality and INEGI income geography, published as an "
          "interactive report."),
    entry(project_header("Tide: open-source, offline-first cycle tracker | "
                         f"{link('https://github.com/eduardoge13/tide-cycle-tracker', 'github.com/eduardoge13/tide-cycle-tracker')}",
                         "Oct 2026"),
          "React/TypeScript PWA with no backend and a strict CSP; statistical prediction engine (median for short "
          "histories, recency-weighted mean for 6+ cycles, confidence rules), ovulation estimate learned from "
          "LH tests, Vitest suite, CI and GitHub Pages deploy."),
]

story += section("Additional Projects &amp; Public Code")
story += [
    entry(project_header("Night-time lights and poverty atlas | "
                         f"{link('https://github.com/eduardoge13/luces-noche-pobreza', 'github.com/eduardoge13/luces-noche-pobreza')}",
                         "2023 - 2026"),
          "NASA VIIRS Black Marble vs CONEVAL poverty for 2,469 municipalities (2019-2024) for an academic book "
          "chapter; SLX, spatial-lag and spatial-error models; Next.js + MapLibre + PMTiles atlas whose audit "
          "documented three errors in the original analysis."),
    entry(project_header("Punto Clave MX e-commerce | puntoclaveshop.com.mx", "2026"),
          "Next.js 16 storefront with 3D showroom, live Stripe Checkout with 3-D Secure, SPEI, chargeback "
          "hardening and GitHub Actions deploys."),
    entry(project_header("Payment reminder system | "
                         f"{link('https://github.com/eduardoge13/payments-reminder', 'github.com/eduardoge13/payments-reminder')}",
                         "2025"),
          "RFM segmentation, ML-based channel selection, WhatsApp/Twilio messaging, Notion and scheduled "
          "GitHub Actions."),
    entry(project_header("Databricks experiment | MLflow", "Dec 2024"),
          "Gradient Boosting classifier for air-quality labels with MLflow experiment tracking."),
]

story += section("Education &amp; Certifications")
story += [
    entry(job_header("Universidad Nacional Autónoma de México | B.A. in Economics, graduated with honors "
                     "(GPA 9.4/10)", "Oct 2024"),
          "Coursework: Econometrics, Statistics, Time Series, Mathematics, Linear Algebra, Game Theory, "
          "Economic Development.",
          "Certifications: Machine Learning with Apache Spark &amp; PySpark; Databricks Fundamentals; Geographic "
          "Data Science with Python (Center for Spatial Data Science, University of Chicago); Intro to Deep "
          "Learning &amp; Time Series (Kaggle); Learning Amazon SageMaker (LinkedIn Learning); Unlock Your Data "
          "with Data Cloud (Salesforce)."),
]

if __name__ == "__main__":
    print(build_pdf(story, OUTPUT))
