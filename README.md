# Eduardo Gaitán — Portfolio

Static portfolio for Eduardo Gaitán: data science, forecasting, econometrics, AI engineering and the
systems that run them. Bilingual English/Spanish site, English CV downloads. Last content update: November 4, 2026.

## Content and case anchors

The navy/mint identity and all fourteen cases are retained, including the night-lights and poverty
atlas. Authentic product captures lead the page; the project explorer filters evidence by role
(all, AI engineer, data scientist or full-stack) and searches names, technologies and case details.
Project anchors include:

- `#case-receipt-reader`: production receipt reader in the POS case; Claude structured outputs,
  approximate US$0.02 per receipt, local Qwen3-VL fallback.
- `#case-sentinel`: incident analysis with Claude and human approval before execution.
- `#case-agent-control-plane`: coding agents, test execution, draft PRs and human approval gates.
- `#case-market-study` and `#case-housing`: econometrics, validation and pricing studies.
- `#case-forecasting`: demand forecasts by SKU and branch.
- `#case-ntl`: night-lights and poverty atlas.
- `#case-smart-cfo`: client-private SaaS MVP for business valuation and financial projections.
  Related Excel/PowerPoint financial automation with FastAPI is explicitly described separately;
  it is not presented as the MVP's complete stack. No user, revenue or outcome metrics are claimed.

The profile states advanced Python/R, SQL, Power BI/Streamlit, and knowledge of Spark/PySpark and
Databricks backed by certification and experimentation, without claiming production tenure.

## CV downloads

There is one visible CV download action at `#cv`, with an explicit version label:

- All/full-stack view: general CV, `/Eduardo_Gaitan_Resume_2026.pdf`.
- AI/data view: AI/data CV, `/Eduardo_Gaitan_CV_AI_Data_Scientist_2026.pdf`.

The Dockerfile serves each route as its actual PDF, including the targeted AI/data CV under a neutral
public filename. Application-specific filenames are retained for upload and local tracking.

## Language and sharing

The first visit follows the browser language (Spanish or English). A visible EN/ES switch stores the
visitor's choice when local storage is available. `?lang=en` or `?lang=es` takes priority for a shared
link. Role filters use `?perfil=ia`, `?perfil=datos` or `?perfil=fullstack`; search uses `q`.
The page translates its content, labels, project details and metadata locally, without an external
translation service or sending the visitor's search to an LLM.

## Local preview

```bash
python3 serve_preview.py
```

Open `http://127.0.0.1:8764`. The preview maps both public CV routes to the generated files in `output/pdf`.

## Regenerating the resume

The PDF is generated from `build_resume.py` (reportlab). Edit the text there, then:

```bash
uv run --with reportlab python build_resume.py      # writes output/pdf/Eduardo_Gaitan_Resume_2026.pdf
uv run --with reportlab python build_targeted_resume.py  # tailored AI/data version
pdftoppm -png -r 60 output/pdf/Eduardo_Gaitan_Resume_2026.pdf /tmp/cv-preview   # eyeball the two pages
```

`LINKEDIN_UPDATE_COPY.md` holds the matching LinkedIn text (EN + ES) and a click-by-click checklist.

## Production deployment

The production compose file uses the existing `n8n_default` Docker network and Traefik labels on the VPS.
The public route is `https://eduardo.srv1175749.hstgr.cloud`. After merging to `master`:

```bash
ssh vps-n8n 'cd /docker/eduardo-portfolio && git pull --ff-only && docker compose up -d --build eduardo-portfolio'
```

Both generated PDFs are copied into the Nginx image during the build. Generate and check them before publishing.

## Read-only Claude critic

```bash
bash scripts/critique_portfolio_claude.sh
```

Uses the existing Claude CLI login and only Read/Glob/Grep tools. It reviews the current portfolio copy,
composition and optional `output/playwright/` desktop/mobile captures, then proposes improvements.
It cannot edit source, run shell commands, use connected accounts or deploy the site.
Authentic image sources are documented in `assets/SOURCES.txt`.
