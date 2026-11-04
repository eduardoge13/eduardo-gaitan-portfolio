"""Build the English Airtm AI Data Scientist CV (at most two US-letter pages).

Run: uv run --with reportlab python build_targeted_resume.py
Optional: --output /absolute/path/to/resume.pdf

Content is editable below. Shared typography, Unicode font embedding and the
two-page guard live in build_resume.py. This module does not build the general
CV. Facts are grounded in the existing CV and applicant confirmations dated
2026-11-04; the Smart CFO SaaS MVP has no independently confirmed start date.
"""

import argparse
from pathlib import Path

from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import HRFlowable, PageBreak, Paragraph, Spacer

import build_resume as base


OUTPUT = base.ROOT / "output" / "pdf" / "Eduardo_Gaitan_CV_Airtm_AI_Data_Scientist_2026.pdf"
DOC_TITLE = "Eduardo Gaitán - AI Data Scientist (November 2026)"
DOC_SUBJECT = "AI agent workflows, analytics automation, machine learning and financial analytics"

# Readable, single-column text with the same restrained design as the general CV.
body = ParagraphStyle("AirtmBody", parent=base.body, fontSize=10.2, leading=12.6, spaceAfter=3)
summary = ParagraphStyle("AirtmSummary", parent=body, textColor=base.BLACK, spaceAfter=2)
bullet = ParagraphStyle("AirtmBullet", parent=body, leftIndent=14, firstLineIndent=-9,
                        bulletIndent=5, fontSize=10.1, leading=12.5, spaceAfter=2)
job = ParagraphStyle("AirtmJob", parent=base.job, fontSize=10, leading=12.2)
job_date = ParagraphStyle("AirtmDate", parent=base.job_date, fontSize=9.2, leading=12.2)
project = ParagraphStyle("AirtmProject", parent=job, spaceBefore=3, spaceAfter=1)
section_title = ParagraphStyle("AirtmSection", parent=base.section_title,
                               fontSize=10.5, leading=12.5, spaceBefore=4)


def p(text, style=body):
    return Paragraph(text, style)


def section(name):
    return base.section(name, section_title)


def job_entry(role, dates, *bullets):
    return base.entry(base.job_header(role, dates, job, job_date), *bullets, bullet_style=bullet)


def project_entry(name, dates, *bullets):
    return base.entry(base.project_header(name, dates, project, job_date), *bullets, bullet_style=bullet)


def make_story():
    story = [
        p("Eduardo Gaitán Escalante", base.title),
        p("Data Scientist &amp; AI Engineer · Economist · Mexico City, Mexico (UTC-6)", base.headline),
        p(
            f'{base.link("mailto:eduardo.gaitan.escalante@gmail.com", "eduardo.gaitan.escalante@gmail.com")}'
            ' &nbsp;•&nbsp; +52 (241) 117-4551 &nbsp;•&nbsp; '
            f'{base.link("https://www.linkedin.com/in/eduardo-gaitan-1b143b242/", "linkedin.com/in/eduardo-gaitan-1b143b242")}',
            base.contact,
        ),
        p(
            f'{base.link("https://github.com/eduardoge13")} &nbsp;•&nbsp; '
            f'{base.link("https://eduardo.srv1175749.hstgr.cloud")}',
            base.contact,
        ),
        p(f"English: fluent · Spanish: native · Remote · {base.UPDATED}", base.updated),
        HRFlowable(width="100%", thickness=1.05, color=base.BLACK, spaceBefore=4, spaceAfter=5),
    ]

    story += section("Summary")
    story += [p(
        "Economist (UNAM, honors) with <b>5+ years building data pipelines and models in Python/R</b> "
        "and 1+ year shipping LLM systems to production. Build Claude API agents that automate document "
        "processing and incident analysis, with structured outputs, cost controls, local-model fallback "
        "and human approvals. Combine SQL analytics, machine learning, econometrics and stakeholder "
        "reporting with end-to-end delivery, including financial analytics and a Smart CFO SaaS MVP.", summary
    )]

    story += section("Core Skills")
    story += [
        p("<b>AI agent workflows:</b> Anthropic Claude API, structured outputs, prompt design, "
          "receipt extraction, incident analysis, per-call cost control, Ollama/Qwen3-VL fallback, "
          "human-approval gates; coding-agent orchestration with tests and draft pull requests."),
        p("<b>Analytics foundations:</b> SQL, PostgreSQL, BigQuery, Python, R, pandas, Parquet, ETL; "
          "Kedro pipelines, MLflow experiment tracking, Google Cloud Run and Cloud Build, Docker, Git. "
          "Spark/PySpark and Databricks: certifications and one experiment."),
        p("<b>Statistics &amp; ML:</b> controlled experiments, A/B test design, hypothesis testing, "
          "econometrics, out-of-sample validation, spatial-block cross-validation, forecasting "
          "(Prophet, SARIMA, XGBoost, Croston), Isolation Forest, K-Means, Monte Carlo, Sobol sensitivity."),
        p("<b>Dashboards &amp; reporting:</b> Power BI, Streamlit, Plotly, Jupyter, Excel, "
          "reproducible analytical reports and investor decks; cross-functional delivery with "
          "Economics and Finance teams."),
    ]

    story += section("Professional Experience")
    story += [
        job_entry("Independent Data Scientist &amp; AI Engineer (freelance / contract)", "Jan 2025 - Present",
            "Ship production agents directly on the <b>Claude API</b>: a receipt-reading accounting bot "
            "with structured outputs at approximately <b>US$0.02 per receipt</b> and a local "
            "<b>Qwen3-VL fallback</b>; a server-incident analyst whose actions require <b>human approval</b>.",
            "Build an agent control plane that runs coding agents, executes their tests and opens draft "
            "pull requests. Use explicit output structure, per-call cost controls and review gates "
            "to constrain production LLM workflows.",
            "With <b>Smart CFO</b>: develop per-SKU/branch forecasting pipelines using Kedro, MLflow, "
            "BigQuery and Cloud Run; cost/revenue analytics and opportunity dashboards. Contribute to "
            "a <b>SaaS MVP for business valuation and financial projections</b>.",
            "Deliver demand, pricing and capital studies as reproducible Python reports and investor "
            "decks: spatial econometrics, forecasting, price elasticity and Monte Carlo/Sobol analysis.",
        ),
        Spacer(1, 3),
        job_entry("Naturgy | Data Science Specialist", "Jan 2025 - Jul 2025",
            "Led a cross-functional team to deploy <b>Isolation Forest anomaly detection</b> end to end: "
            "ETL, orchestration, tuning and performance analysis in H2O and R.",
            "Partnered with Economics and Finance to automate <b>7 manual processes</b>, reducing "
            "processing time from <b>5 hours per task to under 1 minute</b>.",
            "Modernized K-Means segmentation (+15% accuracy, -10% training time); developed a hybrid "
            "XGBoost-plus-seasonality model for annual natural-gas consumption.",
        ),
        Spacer(1, 3),
        job_entry("CONEVAL | Head of the Small Area Estimation Methodologies Department", "Jan 2024 - Jan 2025",
            "Led a Docker/Kedro/PostgreSQL data-pipeline project; used SQL for dataset querying and "
            "manipulation, and contributed to poverty-analysis publications.",
            "Fitted supervised and unsupervised models: Random Forest, boosting, regression/logistic "
            "regression, SVM, neural networks and hybrid time-series models.",
        ),
        PageBreak(),
        p("Eduardo Gaitán Escalante · AI Data Scientist", base.headline),
    ]

    story += section("Professional Experience (continued)")
    story += [
        job_entry("JGCDMX | Environment, Tourism &amp; Economic Development Coordinator", "Oct - Nov 2023",
            "Automated ETL in Python, reducing project-creation time by 20%; built interactive "
            "geospatial dashboards in GeoPandas, Leaflet and Folium for decisions and route planning.",
            "Deployed K-Means and spatial-lag models for heatmaps, pattern analysis and reporting.",
        ),
        Spacer(1, 3),
        job_entry("UNAM, Program for Development Studies | Python &amp; R Developer", "Jan 2020 - Sep 2023",
            "Led a night-time-light geospatial data pipeline with Parquet for analysis, storage and "
            "reporting; conducted socioeconomic geospatial estimations.",
            "Built Docker development environments integrating PostgreSQL, Python and R.",
        ),
    ]

    story += section("Selected Projects")
    story += [
        project_entry("Distributor forecasting pipeline | SmartCFO AI", "Sep 2025 - May 2026",
            "Kedro pipeline over approximately <b>4,940 branch × manufacturer series</b>, a "
            "<b>52-week horizon</b> and 4-week validation; Prophet, SARIMA, XGBoost and Croston/SBC. "
            "MLflow tracking, BigQuery and Cloud Build; <b>93× speed-up</b> through vectorization and "
            "a documented fix for a flat-forecast regression.",
        ),
        project_entry("Market, demand &amp; capital study | confidential restaurant client", "Sep - Oct 2026",
            "Validated a Huff gravity demand model out of sample: <b>23% median absolute error "
            "versus 74% for a naive baseline</b>. Used OLS/SAR/SEM with spatial-block CV, "
            "competition clustering, ETS/SARIMA forecasts and 20,000-run Monte Carlo with Sobol sensitivity.",
        ),
        project_entry("Housing price model &amp; decision deck | Monterrey", "Aug 2026",
            "Scraped and cleaned <b>936 houses across 12 municipalities</b>. Hedonic model fitted on "
            "791 observations: R² 0.85 and 19% median out-of-sample error with 5-fold CV; "
            "interpretable coefficients and a 17-slide decision deck.",
        ),
        project_entry("Production POS platform &amp; receipt automation | bearandchimps.com", "Jul - Oct 2026",
            "Fastify, SQLite and React/TypeScript system with order intake, kitchen screens, payments "
            "and a Claude/Qwen3-VL receipt reader. <b>1,300+ automated tests on the platform</b>; "
            "scripted deployments with verification and rollback.",
        ),
    ]

    story += section("Experimentation &amp; Reliability")
    story += [
        p("<b>Controlled experiments:</b> independently designed and ran controlled experiments; "
          "A/B test design and hypothesis testing. Designed an alternating-week free versus paid "
          "delivery protocol with fixed menu/promotions and channel-level measurement."),
        p("<b>LLM reliability controls:</b> structured extraction, a local-model fallback, cost tracking "
          "and approval before incident-response actions. Statistical/ML model validation includes "
          "held-out forecast validation, spatial-block CV and regression diagnosis."),
    ]

    story += section("Education &amp; Certifications")
    story += [
        job_entry("Universidad Nacional Autónoma de México | B.A. in Economics, honors", "Oct 2024",
            "GPA 9.4/10. Coursework: Econometrics, Statistics, Time Series, Mathematics, Linear Algebra "
            "and Game Theory.",
            "Certifications: Machine Learning with Apache Spark &amp; PySpark; Databricks Fundamentals; "
            "Geographic Data Science with Python (University of Chicago). Databricks project: "
            "one air-quality Gradient Boosting/MLflow experiment (Dec 2024).",
        ),
    ]
    return story


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    print(base.build_pdf(make_story(), args.output, DOC_TITLE, DOC_SUBJECT))


if __name__ == "__main__":
    main()
