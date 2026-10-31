# Eduardo Gaitán — Portfolio

Static portfolio for Eduardo Gaitán: data science, forecasting, econometrics, AI engineering and the
systems that run them. Spanish site, English resume. Last content update: October 2026.

## Local preview

```bash
docker compose up --build
```

Open `http://localhost:8080` after adding a local port mapping, or serve the files with any static web server.

## Regenerating the resume

The PDF is generated from `build_resume.py` (reportlab). Edit the text there, then:

```bash
uv run --with reportlab python build_resume.py      # writes output/pdf/Eduardo_Gaitan_Resume_2026.pdf
pdftoppm -png -r 60 output/pdf/Eduardo_Gaitan_Resume_2026.pdf /tmp/cv-preview   # eyeball the two pages
```

`LINKEDIN_UPDATE_COPY.md` holds the matching LinkedIn text (EN + ES) and a click-by-click checklist.

## Production deployment

The production compose file uses the existing `n8n_default` Docker network and Traefik labels on the VPS.
The public route is `https://eduardo.srv1175749.hstgr.cloud`. After merging to `master`:

```bash
ssh vps-n8n 'cd /docker/eduardo-portfolio && git pull && docker compose up -d --build'
```

The PDF linked from the site is copied into the Nginx image during the build.
