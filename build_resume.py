from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output" / "pdf" / "Eduardo_Gaitan_Resume_2026.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

BLUE = colors.HexColor("#1558a6")
BLACK = colors.HexColor("#111111")
GRAY = colors.HexColor("#444444")


styles = getSampleStyleSheet()
title = ParagraphStyle(
    "ResumeTitle", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=19,
    leading=22, alignment=TA_CENTER, textColor=BLACK, spaceAfter=3,
)
contact = ParagraphStyle(
    "Contact", parent=styles["Normal"], fontName="Times-Roman", fontSize=9.6,
    leading=12, alignment=TA_CENTER, textColor=BLACK, spaceAfter=1,
)
section_title = ParagraphStyle(
    "SectionTitle", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10.5,
    leading=12, textColor=BLACK, spaceBefore=4, spaceAfter=3,
)
body = ParagraphStyle(
    "Body", parent=styles["Normal"], fontName="Times-Roman", fontSize=9.55,
    leading=12.25, textColor=GRAY, spaceAfter=2.2,
)
body_tight = ParagraphStyle(
    "BodyTight", parent=body, fontSize=9.2, leading=11.55, spaceAfter=1.5,
)
job = ParagraphStyle(
    "Job", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9.8,
    leading=11.7, textColor=BLACK, spaceAfter=0,
)
job_date = ParagraphStyle(
    "JobDate", parent=job, alignment=TA_LEFT,
)
bullet = ParagraphStyle(
    "Bullet", parent=body, leftIndent=15, firstLineIndent=-9, bulletIndent=5,
    fontSize=9.3, leading=11.55, spaceAfter=1.7,
)
project = ParagraphStyle(
    "Project", parent=job, fontSize=9.7, leading=11.7, spaceBefore=3, spaceAfter=1,
)


def p(text, style=body):
    return Paragraph(text, style)


def bullet_p(text):
    return Paragraph(f"&bull;&nbsp;&nbsp;{text}", bullet)


def section(name):
    return [
        Spacer(1, 2),
        Paragraph(name.upper(), section_title),
        HRFlowable(width="100%", thickness=0.8, color=BLACK, spaceBefore=0, spaceAfter=5),
    ]


def job_header(role, dates):
    table = Table([[Paragraph(role, job), Paragraph(dates, job_date)]], colWidths=[5.95 * inch, 1.65 * inch])
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return table


def project_header(name, dates):
    table = Table([[Paragraph(name, project), Paragraph(dates, job_date)]], colWidths=[5.95 * inch, 1.65 * inch])
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return table


def page_canvas(canvas, doc):
    canvas.saveState()
    canvas.setTitle("Eduardo Gaitán - Resume 2026")
    canvas.setAuthor("Eduardo Gaitán Escalante")
    canvas.restoreState()


class ResumeDocTemplate(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(filename, pagesize=letter, leftMargin=0.45 * inch, rightMargin=0.45 * inch,
                         topMargin=0.31 * inch, bottomMargin=0.35 * inch, title="Eduardo Gaitán - Resume 2026")
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="normal")
        self.addPageTemplates([PageTemplate(id="resume", frames=frame, onPage=page_canvas)])


story = [
    Paragraph("Eduardo Gaitán Escalante", title),
    Paragraph(
        '<a href="mailto:eduardo.gaitan.escalante@gmail.com" color="#1558a6"><u>eduardo.gaitan.escalante@gmail.com</u></a>'
        ' &nbsp;•&nbsp; +52 (241) 117-4551 &nbsp;•&nbsp; '
        '<a href="https://www.linkedin.com/in/eduardo-gaitan-1b143b242/" color="#1558a6"><u>linkedin.com/in/eduardo-gaitan-1b143b242</u></a>',
        contact,
    ),
    Paragraph(
        '<a href="https://github.com/eduardoge13" color="#1558a6"><u>github.com/eduardoge13</u></a>'
        ' &nbsp;•&nbsp; '
        '<a href="https://eduardo.srv1175749.hstgr.cloud" color="#1558a6"><u>eduardo.srv1175749.hstgr.cloud</u></a>',
        contact,
    ),
    HRFlowable(width="100%", thickness=1.05, color=BLACK, spaceBefore=5, spaceAfter=6),
]

story += section("Education")
story += [
    job_header("Universidad Nacional Autónoma de México | Ciudad Universitaria, CDMX, México", "Oct 2024"),
    p("<b>B.A. in Economics, graduated with honors</b> | GPA: 9.4/10.0"),
    p("<b>Relevant Coursework:</b> Econometrics, Statistics, Time Series, Mathematics, Linear Algebra, Game Theory, Economic Development."),
    p("<b>Certifications:</b> Machine Learning with Apache Spark &amp; PySpark; Databricks Fundamentals; Geographic Data Science with Python (Center for Spatial Data Science - University of Chicago); Intro to Deep Learning &amp; Time Series - Kaggle; Learning Amazon SageMaker - LinkedIn Learning; Unlock Your Data with Data Cloud - Salesforce."),
]

story += section("Technical Skills")
story += [
    p("<b>Programming &amp; Data:</b> Python (advanced), R (advanced), JavaScript/TypeScript, SQL, PostgreSQL, SQLite, Scikit-learn, TensorFlow, GeoPandas, Parquet."),
    p("<b>Applications &amp; Integrations:</b> FastAPI, Flask, Next.js, Astro, React, python-telegram-bot, Google Sheets API, Gemini, Amadeus, Stripe, n8n, webhooks."),
    p("<b>Infrastructure &amp; Operations:</b> Docker, Docker Compose, Traefik, Linux, GitHub Actions, Hostinger VPS, HTTPS/TLS routing, systemd, PM2, UFW, fail2ban, Trivy."),
    p("<b>IT Operations:</b> PC and server hardware/software installation and configuration; endpoint and peripheral support; hardware/software inventory control; cloud service support."),
    p("<b>Operating Systems:</b> Windows 10/11, Linux."),
]

story += section("Relevant Experience")
story += [
    job_header("Freelance Systems &amp; Automation Engineer", "Jan 2025 - Present"),
    bullet_p("Designed and deployed client-facing digital operations including Telegram lookup, sales and commission bots, a WhatsApp service platform, an e-commerce storefront, flight monitoring, and VPS observability."),
    bullet_p("Automated workflows with n8n, Google Sheets, API/webhook integrations, and Telegram notifications; implemented caching, retries, multi-step state machines, health checks, and audit logs."),
    bullet_p("Containerized services with Docker/Compose and Traefik, operating HTTPS routes on a Hostinger VPS and documenting repeatable deployment, rollback, and service-verification patterns."),
    bullet_p("Built Sentinel monitoring for service health, system resources, certificates, SSH/firewall posture, exposed ports, security updates, and Trivy CVEs, with approval-gated remediation actions."),
    Spacer(1, 2),
    job_header("Naturgy | Data Science Specialist", "Jan 2025 - Present"),
    bullet_p("Led a cross-functional team in designing and deploying an <b>Isolation Forest</b> model for anomaly detection, including ETL pipelines, automation workflows, orchestration, hyperparameter tuning, and performance analysis using H2O and R."),
    bullet_p("Modernized a legacy <b>K-Means</b> customer-segmentation model, achieving a 15% improvement in accuracy and a 10% reduction in training time."),
    bullet_p("Partnered with Economics and Finance to automate 7 manual processes, reducing processing time from 5 hours per task to under 1 minute and saving hundreds of hours annually."),
    bullet_p("Proposed and developed a hybrid boosted forecasting model (XGBoost + seasonality) for annual natural-gas consumption."),
    Spacer(1, 2),
    job_header("National Council of Evaluation of the Social Development Policy | Head of the Small Area Estimation Methodologies Department", "Jan 2024 - Dec 2025"),
    bullet_p("Led a data-pipeline project using Docker, Kedro, PostgreSQL, pgAdmin4, and Git, improving storage and analysis workflows."),
    bullet_p("Fitted supervised and unsupervised models including Random Forest, XG/Gradient Boosting, Regression/Logistic, SVM, neural networks, and hybrid boosted time-series models."),
    bullet_p("Used SQL to manage queries and manipulate datasets efficiently in pgAdmin4; contributed to poverty-analysis publications within the technical estimation team."),
]

story += [PageBreak()]
story += section("Relevant Experience (continued)")
story += [
    job_header("General Coordination for Planning and Investment - JGCDMX | Environment, Tourism, and Economic Development Coordinator", "Oct - Nov 2023"),
    bullet_p("Automated ETL processes with Python scripts, reducing project-creation times by 20% and making information available to land teams sooner."),
    bullet_p("Developed interactive geospatial dashboards using GeoPandas, Leaflet, and Folium for decision-making and route planning."),
    bullet_p("Deployed two geospatial models (K-means and Spatial Lag Model) for heatmaps, analytical reporting, and pattern distribution."),
    Spacer(1, 2),
    job_header("Python &amp; R Developer | Program for Development Studies - UNAM", "Jan 2020 - Sep 2023"),
    bullet_p("Led the creation of a geospatial night-time-light data pipeline, optimizing analysis, storage, and reporting with Parquet."),
    bullet_p("Designed Docker containers for developer environments integrating PostgreSQL databases, Python, and R tools."),
    bullet_p("Conducted advanced geospatial estimations for socioeconomic research purposes."),
]

story += section("Selected Freelance Projects")
story += [
    project_header("Customer &amp; Operations Automation Platform | GitHub: telegram-bot-agency", "2025 - 2026"),
    bullet_p("Built a Telegram client-data lookup service and extended the platform with multi-tenant WhatsApp handlers for product questions, orders, QA, and guided flight search."),
    bullet_p("Added Google Sheets product access with caching, asynchronous wrappers, order state machines, Amadeus integration, Docker packaging, Traefik routing, and a tested FastAPI service."),
    Spacer(1, 2),
    project_header("Punto Clave MX E-commerce | GitHub: spike-ecommerce-web", "2026"),
    bullet_p("Developed and deployed a Next.js/TypeScript storefront with product management, Stripe Checkout, SPEI fallback scaffolding, media routes, SEO, and GitHub Actions over SSH."),
    Spacer(1, 2),
    project_header("VPS Sentinel &amp; Operations Hub | Private client infrastructure", "2026"),
    bullet_p("Implemented health and security monitoring for Docker services, systemd units, HTTP/TLS endpoints, disk/memory, SSH hardening, UFW, fail2ban, CrowdSec, and container CVEs."),
    bullet_p("Added operator-readable Telegram alerts and a kill-switched approval layer for a small allowlist of deterministic remediation actions."),
    Spacer(1, 2),
    project_header("Payment Reminder System | GitHub: payments-reminder", "2025"),
    bullet_p("Created an automated reminder workflow using RFM segmentation, ML-based channel selection, WhatsApp/Twilio messaging, Notion, and scheduled GitHub Actions execution."),
]

story += section("Additional Projects")
story += [
    project_header("Databricks Experiment | Personal Project", "Dec 2024"),
    bullet_p("Built a Gradient Boosting classifier for air-quality labels and configured MLflow for experiment tracking, metrics logging, and model-performance optimization."),
    project_header("Estimation of Poverty Using Nighttime Satellite Light Data | Academic Project", "Jan 2023"),
    bullet_p("Implemented SLX, spatial-lag, and spatial-error-lag models to examine the relationship between luminosity and poverty levels, identifying an inverse correlation."),
]

doc = ResumeDocTemplate(str(OUTPUT))
doc.build(story)
print(OUTPUT)
