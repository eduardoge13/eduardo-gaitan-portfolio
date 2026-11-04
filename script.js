(() => {
  'use strict';

  // Spanish is the complete no-JavaScript baseline; English is deterministic.
  const copy = {
  "es": {
    "metaTitle": "Eduardo Gaitán | Ciencia de datos e ingeniería de IA",
    "metaDescription": "Portafolio de Eduardo Gaitán. Investigación económica, ciencia de datos, modelos, software y sistemas con IA. Proyectos, experiencia y CV.",
    "evidence.todos": "14 proyectos de investigación, datos, IA y software. Elige un perfil para explorar el trabajo relacionado.",
    "evidence.ia": "Extracción estructurada con Claude API, respaldo local con Qwen3-VL y agentes con aprobación humana. APIs y pruebas automatizadas.",
    "evidence.datos": "Econometría espacial, validación fuera de muestra y pronósticos. Python/R, INEGI/CONEVAL, Kedro y MLflow.",
    "evidence.fullstack": "Interfaces, APIs, bases de datos y despliegue. React/TypeScript, Fastify, PostgreSQL/SQLite, Stripe y GitHub Actions.",
    "cv.general": "General · PDF en inglés",
    "cv.specialist": "IA y datos · PDF en inglés",
    "search.resetRole": "Ver todos los proyectos",
    "count.one": "proyecto",
    "count.many": "proyectos",
    "count.of": "de",
    "count.search": "Búsqueda activa"
  },
  "en": {
    "case-ntl.date": "2023 – 2026",
    "case-ntl.tech": "Python / R · Spatial econometrics · MapLibre · INEGI / CONEVAL",
    "case-ntl.detail0": "NASA VIIRS Black Marble imagery compared with CONEVAL poverty data for 2,469 municipalities; SLX, spatial-lag and spatial-error models for a book chapter. An atlas built with Next.js, MapLibre and PMTiles; an audit documented three errors in the original analysis.",
    "case-ntl.extra": "The atlas brings together data from 2019 to 2024.",
    "case-ntl.link": "View repository",
    "case-ntl.title": "Nighttime lights and poverty",
    "case-ntl.scope": "Research",
    "case-ntl.lead": "Research combining satellite imagery and municipal poverty data, with an atlas to explore the results.",
    "case-ntl.previewTech": "Python / R · Spatial econometrics · MapLibre · INEGI / CONEVAL",
    "project.details": "Project details",
    "case-smart-cfo.date": "MVP SaaS",
    "case-smart-cfo.tech": "MVP SaaS · Valuation · Financial projections",
    "case-smart-cfo.detail0": "Contributed to a SaaS MVP for business valuation and financial projections. Private client product, with no public demo.",
    "case-smart-cfo.detail1": "Related financial automation at Smart CFO: Excel models with openpyxl and presentations with python-pptx, with FastAPI APIs.",
    "case-smart-cfo.note": "Private client · No public code or data",
    "case-smart-cfo.title": "Smart CFO",
    "case-smart-cfo.scope": "Private client",
    "case-smart-cfo.lead": "A SaaS MVP for business valuation and financial projections. Private client work, with no public demo.",
    "case-smart-cfo.previewTech": "MVP SaaS · Valuation · Financial projections",
    "case-receipt-reader.date": "Jul–Oct 2026",
    "case-receipt-reader.tech": "Fastify · React · Stripe · Claude API · Qwen3-VL · SQLite · Zod · Playwright",
    "case-receipt-reader.alt": "Bear & Chimps kitchen screen showing received and cooking orders, with actions to mark them ready",
    "case-receipt-reader.caption": "Kitchen screen · Bear & Chimps",
    "case-receipt-reader.detail0": "Built with Fastify, SQLite and React, with screens for kitchen, packing and delivery; orders from the website and delivery platforms through signed webhooks, card payments and Telegram operations bots. More than 1,300 automated tests and deployments with rollback.",
    "case-receipt-reader.detail1": "Accounting receipt reader in production: Claude API with structured outputs, at approximately US$0.02 per receipt, with a local Qwen3-VL fallback.",
    "case-receipt-reader.link": "Visit the business",
    "case-receipt-reader.title": "Bear & Chimps: point of sale and receipt reader",
    "case-receipt-reader.scope": "Production system",
    "case-receipt-reader.lead": "A point-of-sale system with station-specific screens and an accounting receipt reader using Claude API, both in production.",
    "case-receipt-reader.previewTech": "Fastify · React · Stripe · Claude API",
    "case-housing.date": "Aug 2026",
    "case-housing.tech": "Playwright · Python · Hedonic regression · KFold",
    "case-housing.alt": "Municipal distributions of listing price per square metre of land: median and interquartile range",
    "case-housing.caption": "Published prices per m² of land · Median and interquartile range, not causal effects from the model.",
    "case-housing.detail0": "Playwright scraping of public listings (9,653 published listings, 936 cleaned houses across 12 municipalities). Hedonic regression on 791 observations with cross-validation: R² 0.85 and 19% median out-of-sample error. A 17-slide deck for developers.",
    "case-housing.note": "Developer pitch · Public data",
    "case-housing.title": "Housing prices in Monterrey",
    "case-housing.scope": "Price model · Public data",
    "case-housing.lead": "Public listings, data cleaning and a hedonic price model covering 12 municipalities.",
    "case-housing.previewTech": "Playwright · Python · Hedonic regression · KFold",
    "case-tide.date": "Oct 2026",
    "case-tide.tech": "React · TypeScript · Vite · Vitest · Statistics · Privacy",
    "case-tide.alt": "Tide Today screen showing fictional data loaded through the demo option",
    "case-tide.caption": "Tide · Sample data",
    "case-tide.detail0": "A React and TypeScript PWA that stores everything on the phone and sends nothing to a server. Statistical prediction engine: median with few cycles, recency-weighted mean with six or more, and confidence rules. Ovulation estimates learned from LH tests, Vitest tests and deployment on GitHub Pages.",
    "case-tide.link": "View repository",
    "case-tide.title": "Tide",
    "case-tide.scope": "Open source",
    "case-tide.lead": "A serverless menstrual cycle tracker. Data stays on the phone.",
    "case-tide.previewTech": "React · TypeScript · Statistics · Privacy",
    "case-yoga-verde.date": "Aug–Oct 2026",
    "case-yoga-verde.tech": "Astro · Stripe · Python · INEGI",
    "case-yoga-verde.alt": "Yoga Verde public product page featuring coconut milk body cream",
    "case-yoga-verde.caption": "Yoga Verde · Product page",
    "case-yoga-verde.detail0": "An Astro store with a private Stripe Checkout backend and SQLite inventory, plus a reproducible study of channel unit economics, price elasticity, seasonality and INEGI income geography, published as an interactive report.",
    "case-yoga-verde.link": "Visit store",
    "case-yoga-verde.title": "Yoga Verde",
    "case-yoga-verde.scope": "E-commerce and market research",
    "case-yoga-verde.lead": "An online store and market study, covering inventory, payments and channel analysis.",
    "case-yoga-verde.previewTech": "Astro · Stripe · Python · INEGI",
    "case-punto-clave.date": "2026",
    "case-punto-clave.tech": "Next.js · TypeScript · Stripe · three.js",
    "case-punto-clave.alt": "Punto Clave mobile catalogue showing an iPhone photo, price, availability and payment options",
    "case-punto-clave.caption": "Punto Clave · Mobile catalogue",
    "case-punto-clave.detail0": "A Next.js storefront with a 3D showroom, production Stripe Checkout with 3D Secure, SPEI and WhatsApp-assisted sales; chargeback hardening and deployment with GitHub Actions.",
    "case-punto-clave.note": "puntoclaveshop.com.mx · Private client code",
    "case-punto-clave.link": "Visit store",
    "case-punto-clave.title": "Punto Clave",
    "case-punto-clave.scope": "E-commerce",
    "case-punto-clave.lead": "A Next.js store with a 3D showroom and live payments.",
    "case-punto-clave.previewTech": "Next.js · TypeScript · Stripe · three.js",
    "case-market-study.date": "Sep–Oct 2026",
    "case-market-study.tech": "Python · INEGI · Spatial econometrics · LightGBM · Monte Carlo",
    "case-market-study.detail0": "A Huff gravity model calibrated with out-of-sample validation (23% median error versus 74% for a baseline), OLS/SAR/SEM spatial models with block validation, DENUE-based competition clustering, ETS and SARIMA forecasts, and 20,000 Monte Carlo simulations with Sobol sensitivity for the capital plan. Delivered as a reproducible report and an investor deck.",
    "case-market-study.note": "Confidential client · Model methods and metrics",
    "case-market-study.title": "Dark kitchen market study",
    "case-market-study.scope": "Data consulting · Confidential client",
    "case-market-study.lead": "Demand, competition and capital planning using DENUE data and spatial models.",
    "case-market-study.previewTech": "Python · INEGI · Spatial econometrics · LightGBM",
    "case-forecasting.date": "2025 – 2026",
    "case-forecasting.tech": "Kedro · Polars / Dask · Prophet / XGBoost · MLflow · BigQuery / Cloud Storage",
    "case-forecasting.detail0": "A Kedro pipeline using Prophet, SARIMA, XGBoost and Croston, a Mexican calendar, MLflow tracking and BigQuery data; a 52-week horizon with 4-week validation. A 93× speedup through vectorisation and a documented fix for a flat-forecast regression. Also, revenue and cost-per-trip analytics for a transport company.",
    "case-forecasting.extra": "Approximately 4,940 series. Work with SmartCFO AI; private client systems.",
    "case-forecasting.note": "Private client systems",
    "case-forecasting.title": "Demand forecasting",
    "case-forecasting.scope": "With SmartCFO AI",
    "case-forecasting.lead": "Approximately 4,940 branch-by-manufacturer series, with a 52-week horizon and 4-week validation.",
    "case-forecasting.previewTech": "Kedro · Prophet / XGBoost · MLflow · BigQuery",
    "case-sentinel.date": "2026",
    "case-sentinel.tech": "Python · Claude API · Trivy · Telegram · Human approval",
    "case-sentinel.detail0": "Sentinel monitors services, resources, certificates, firewall/SSH and CVEs, with Telegram alerts. Its incident analyst uses Claude to propose validated actions.",
    "case-sentinel.detail1": "Human control: nothing executes without human approval and a second factor.",
    "case-sentinel.link": "Project link",
    "case-sentinel.title": "Sentinel",
    "case-sentinel.scope": "AI in production",
    "case-sentinel.lead": "Service monitoring and a Claude-powered incident analyst. Every action requires human approval and a second factor.",
    "case-sentinel.previewTech": "Python · Claude API · Trivy · Telegram",
    "case-agent-control-plane.date": "2026",
    "case-agent-control-plane.tech": "Node.js · Docker API · LLM agents · Tests · Draft PRs",
    "case-agent-control-plane.detail0": "A dashboard that discovers containers, systemd services and web routes. Its agent control plane assigns work to Claude and Codex coding agents, runs their tests and opens draft pull requests.",
    "case-agent-control-plane.detail1": "Review before publishing: it never merges or deploys without human approval.",
    "case-agent-control-plane.link": "Project link",
    "case-agent-control-plane.title": "Coding agents",
    "case-agent-control-plane.scope": "Operations platform",
    "case-agent-control-plane.lead": "A service dashboard that assigns tasks to Claude and Codex, runs tests and opens draft pull requests.",
    "case-agent-control-plane.previewTech": "Node.js · Docker API · LLM agents · Tests",
    "case-flights.date": "2026",
    "case-flights.tech": "FastAPI · Statistics · n8n · Google Drive",
    "case-flights.detail0": "A watchlist with dynamic route thresholds (mean minus one or two standard deviations for domestic or international routes), a collector running as a Windows PC service, a FastAPI API on the VPS and Excel reports uploaded to Drive through n8n.",
    "case-flights.link": "Project link",
    "case-flights.title": "Flight price monitor",
    "case-flights.scope": "Data product",
    "case-flights.lead": "Route-level tracking with statistical thresholds and Excel reports.",
    "case-flights.previewTech": "FastAPI · Statistics · n8n · Google Drive",
    "case-clinic.date": "2025 – 2026",
    "case-clinic.tech": "Express · PostgreSQL · React · Playwright",
    "case-clinic.detail0": "An 8-step consultation flow with autosave, digital prescriptions, an audit log and the complete ICD-10 catalogue (14,498 codes). Express, PostgreSQL and React, with Playwright end-to-end tests and CI/CD deployment.",
    "case-clinic.note": "Private client system · No public code",
    "case-clinic.title": "Clinical records",
    "case-clinic.scope": "Private client system",
    "case-clinic.lead": "A private system for consultations, prescriptions and autosave at a clinic.",
    "case-clinic.previewTech": "Express · PostgreSQL · React · Playwright",
    "case-bots.date": "2025 – 2026",
    "case-bots.tech": "Python · FastAPI · Pydantic · Telegram · WhatsApp · n8n",
    "case-bots.detail0": "Telegram bots for customer lookups, sales recording and commissions with per-operator reports; a WhatsApp agent for a travel agency; Google Sheets, Drive and n8n integrations, with caching, retries and logs.",
    "case-bots.link": "Project link",
    "case-bots.title": "Sales, commissions and support bots",
    "case-bots.scope": "Automation",
    "case-bots.lead": "Telegram and WhatsApp bots for sales recording, reporting and integrations.",
    "case-bots.previewTech": "Python · Telegram · WhatsApp · n8n",
    "skip": "Skip to content",
    "nav.projects": "Projects",
    "nav.tools": "Tools",
    "nav.about": "About",
    "nav.contact": "Contact",
    "menu": "Menu",
    "hero.role": "Economist · Data Scientist · AI Engineer",
    "hero.bio": "From economic research to production systems: a poverty atlas, demand forecasts and agents built on the Claude API.",
    "cv.download": "Download CV",
    "hero.caption": "Nighttime lights and poverty · NASA VIIRS, INEGI and CONEVAL",
    "work.intro": "Research, models and software. Private projects describe methods and scope without exposing client data.",
    "profile.all": "All",
    "search.label": "Search projects or technologies",
    "search.reset": "Show all and clear search",
    "search.emptyTitle": "No projects match this combination.",
    "search.emptyHelp": "Try another name or technology, or choose “Show all and clear search”.",
    "tools.models": "Statistics and visualisation",
    "tools.modelsText": "Advanced Python and R; statsmodels, scikit-learn, XGBoost and LightGBM. Power BI, Streamlit, Plotly, GeoPandas, MapLibre and PMTiles.",
    "tools.ai": "AI and automation",
    "tools.aiText": "Claude API, n8n, Gemini and Ollama/Qwen3-VL. REST integrations, webhooks and OAuth2; structured outputs, cost controls and human approval.",
    "tools.software": "Full-stack and APIs",
    "tools.softwareText": "TypeScript/JavaScript, React, Next.js, Astro, Tailwind CSS and Vite. Node.js with Fastify/Express; Python with FastAPI/Flask.",
    "tools.data": "Data and MLOps",
    "tools.dataText": "SQL, PostgreSQL, SQLite, BigQuery and Cloud Storage. Polars, pandas, Dask and Parquet; Kedro pipelines and MLflow model tracking.",
    "tools.quality": "Testing and validation",
    "tools.qualityText": "pytest, Vitest and Playwright; data contracts with Pydantic and Zod. Regression, integration and end-to-end user-flow tests.",
    "tools.delivery": "Deployment and operations",
    "tools.deliveryText": "Docker Compose, Linux, Traefik, nginx, GitHub Actions and Google Cloud Run/Cloud Build. Monitoring with Trivy, CrowdSec and Telegram alerts.",
    "tools.more": "Other project-specific uses",
    "tools.r": "Reproducible R analysis: tidyverse, dplyr, ggplot2, sf and R Markdown, in visualisation and geospatial projects.",
    "tools.reports": "Financial automation: openpyxl and python-pptx to turn Excel models into reports and presentations.",
    "tools.windows": "Windows thermal printing: a C#/.NET 8 agent with xUnit tests. Used specifically in this project.",
    "contact.availability": "Freelance and project work · 10–20 hours/week · Remote from Mexico",
    "about.experience": "I hold an Economics degree from UNAM with honours. I have worked independently since January 2025; until July that year, I also worked as a data science specialist at Naturgy. Previously, I headed the Small Area Estimation Methodologies Department at CONEVAL and worked as a Python and R developer at UNAM.",
    "about.practice": "My work includes reproducible research, demand and pricing models, financial analytics and application development. I use Python and R at an advanced level, SQL with PostgreSQL and BigQuery, Power BI and Streamlit.",
    "about.learning": "I also have knowledge of Spark/PySpark and Databricks through certification and experimentation.",
    "about.collaboration": "I work with teams and clients in Mexico and abroad, in Spanish and English. I am currently available for freelance and project work: 10–20 hours per week, remotely (UTC−6).",
    "footer.top": "Back to top",
    "brand.label": "Eduardo Gaitán, home",
    "nav.label": "Main navigation",
    "nav.mobileLabel": "Mobile navigation",
    "language.label": "Language",
    "hero.artLink": "View the Nighttime lights and poverty project",
    "hero.artAlt": "Mexico atlas showing municipal nighttime radiance and its relationship with CONEVAL poverty data",
    "search.placeholder": "Python, React, Claude…",
    "profile.label": "Explore by professional role",
    "metaTitle": "Eduardo Gaitán | Data Science & AI Engineering",
    "metaDescription": "Eduardo Gaitán's portfolio. Economic research, data science, models, software and AI systems. Projects, experience and CV.",
    "evidence.todos": "14 projects in research, data, AI and software. Choose a role to explore related work.",
    "evidence.ia": "Structured extraction with Claude API, a local Qwen3-VL fallback and agents with human approval. APIs and automated tests.",
    "evidence.datos": "Spatial econometrics, out-of-sample validation and forecasting. Python/R, INEGI/CONEVAL, Kedro and MLflow.",
    "evidence.fullstack": "Interfaces, APIs, databases and deployment. React/TypeScript, Fastify, PostgreSQL/SQLite, Stripe and GitHub Actions.",
    "cv.general": "General · English PDF",
    "cv.specialist": "AI and data · English PDF",
    "search.resetRole": "Show all projects",
    "count.one": "project",
    "count.many": "projects",
    "count.of": "of",
    "count.search": "Search active"
  }
};
  const textBindings = [...document.querySelectorAll('[data-i18n]')];
  const attributeBindings = [
    ['data-i18n-label', 'aria-label'],
    ['data-i18n-alt', 'alt'],
    ['data-i18n-placeholder', 'placeholder']
  ];
  textBindings.forEach((element) => {
    copy.es[element.dataset.i18n] = element.textContent.trim();
  });
  attributeBindings.forEach(([binding, attribute]) => {
    document.querySelectorAll('[' + binding + ']').forEach((element) => {
      copy.es[element.getAttribute(binding)] = element.getAttribute(attribute);
    });
  });

  const projectList = document.getElementById('project-list');
  const projects = [...projectList.querySelectorAll('.project-card')];
  const byId = new Map(projects.map((project) => [project.id, project]));
  const originalOrder = projects.map((project) => project.id);
  const roleOrder = {
    todos: originalOrder,
    ia: ['case-receipt-reader', 'case-sentinel', 'case-agent-control-plane',
      'case-smart-cfo', 'case-forecasting', 'case-bots'],
    datos: ['case-ntl', 'case-market-study', 'case-housing', 'case-forecasting',
      'case-smart-cfo', 'case-yoga-verde', 'case-flights', 'case-tide'],
    fullstack: ['case-receipt-reader', 'case-tide', 'case-yoga-verde',
      'case-punto-clave', 'case-clinic', 'case-bots', 'case-agent-control-plane',
      'case-smart-cfo', 'case-ntl', 'case-flights']
  };
  const cvFiles = {
    general: '/Eduardo_Gaitan_Resume_2026.pdf?v=20261104-skills',
    specialist: '/Eduardo_Gaitan_CV_AI_Data_Scientist_2026.pdf?v=20261104-skills'
  };
  const search = document.getElementById('project-search');
  const reset = document.querySelector('.reset-button');
  const profileButtons = [...document.querySelectorAll('[data-profile]')];
  const languageButtons = [...document.querySelectorAll('[data-language]')];
  const normalise = (value) => value.normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9+#.]+/g, ' ').trim();

  // Search both languages, including collapsed technical details.
  const searchIndex = new Map(projects.map((project) => {
    const terms = [project.id, project.textContent];
    project.querySelectorAll('[data-i18n]').forEach((element) => {
      terms.push(copy.es[element.dataset.i18n] || '', copy.en[element.dataset.i18n] || '');
    });
    if (roleOrder.ia.includes(project.id)) terms.push('AI IA artificial intelligence inteligencia artificial LLM');
    if (roleOrder.datos.includes(project.id)) terms.push('data science ciencia datos');
    if (roleOrder.fullstack.includes(project.id)) terms.push('fullstack full-stack software');
    return [project.id, normalise(terms.join(' ')).split(' ')];
  }));

  function storedLanguage() {
    try {
      const value = localStorage.getItem('eg-portfolio-language');
      return value === 'en' || value === 'es' ? value : null;
    } catch { return null; }
  }

  const browserLanguage = () => (
    (navigator.languages?.[0] || navigator.language || 'es').toLowerCase().startsWith('es')
      ? 'es' : 'en'
  );
  let preferredLanguage = storedLanguage() || browserLanguage();

  function readLocation() {
    const params = new URLSearchParams(location.search);
    const requestedLanguage = params.get('lang');
    const requestedProfile = params.get('perfil');
    return {
      language: requestedLanguage === 'en' || requestedLanguage === 'es'
        ? requestedLanguage : preferredLanguage,
      profile: Object.hasOwn(roleOrder, requestedProfile) ? requestedProfile : 'todos',
      query: params.get('q') || ''
    };
  }

  let state = readLocation();

  function translate() {
    const dictionary = copy[state.language];
    document.documentElement.lang = state.language;
    document.title = dictionary.metaTitle;
    document.querySelector('meta[name="description"]').content = dictionary.metaDescription;
    textBindings.forEach((element) => {
      const value = dictionary[element.dataset.i18n];
      if (typeof value === 'string') element.textContent = value;
    });
    attributeBindings.forEach(([binding, attribute]) => {
      document.querySelectorAll('[' + binding + ']').forEach((element) => {
        const value = dictionary[element.getAttribute(binding)];
        if (typeof value === 'string') element.setAttribute(attribute, value);
      });
    });
    languageButtons.forEach((button) => {
      button.setAttribute('aria-pressed', String(button.dataset.language === state.language));
    });
  }

  function render() {
    const focused = document.activeElement;
    translate();
    search.value = state.query;
    profileButtons.forEach((button) => {
      button.setAttribute('aria-pressed', String(button.dataset.profile === state.profile));
    });

    const ranked = roleOrder[state.profile];
    const members = new Set(ranked);
    const queryTerms = normalise(state.query).split(' ').filter(Boolean);
    const desiredOrder = [...ranked, ...originalOrder.filter((id) => !members.has(id))];

    // Move existing nodes, preserving expanded details and their contents.
    desiredOrder.forEach((id, index) => {
      const node = byId.get(id);
      if (projectList.children[index] !== node) {
        projectList.insertBefore(node, projectList.children[index] || null);
      }
    });

    let count = 0;
    projects.forEach((project) => {
      const visible = members.has(project.id) &&
        queryTerms.every((term) => searchIndex.get(project.id).some((word) => word.startsWith(term)));
      project.hidden = !visible;
      if (visible) count += 1;
    });

    const dictionary = copy[state.language];
    document.getElementById('profile-evidence').textContent = dictionary['evidence.' + state.profile];
    const countText = count === projects.length
      ? count + ' ' + dictionary['count.many']
      : count + ' ' + dictionary['count.of'] + ' ' + projects.length + ' ' + dictionary['count.many'];
    const result = document.getElementById('result-count');
    const message = countText + (state.query.trim() ? ' · ' + dictionary['count.search'] : '');
    if (result.textContent !== message) result.textContent = message;
    reset.hidden = state.profile === 'todos' && !state.query;
    reset.textContent = dictionary[state.query.trim() ? 'search.reset' : 'search.resetRole'];
    document.querySelector('.empty-state').hidden = count > 0;

    const specialist = state.profile === 'ia' || state.profile === 'datos';
    document.querySelector('.cv-link').href = specialist ? cvFiles.specialist : cvFiles.general;
    document.getElementById('cv-variant').textContent = dictionary[specialist ? 'cv.specialist' : 'cv.general'];

    // Filter controls never get replaced. Preserve a focused project on history updates.
    if (focused && focused !== document.body) {
      if (focused.closest('.project-card')?.hidden) {
        search.focus({ preventScroll: true });
      } else if (document.activeElement !== focused && focused.isConnected) {
        focused.focus({ preventScroll: true });
      }
    }
  }

  function writeLocation(mode) {
    const url = new URL(location.href);
    state.profile === 'todos'
      ? url.searchParams.delete('perfil')
      : url.searchParams.set('perfil', state.profile);
    state.query.trim()
      ? url.searchParams.set('q', state.query)
      : url.searchParams.delete('q');
    url.searchParams.set('lang', state.language);
    // A hidden old project anchor must not override a newly chosen profile on reload.
    const target = document.getElementById(url.hash.slice(1))?.closest('.project-card');
    if (target?.hidden) url.hash = '';
    if (url.href !== location.href) {
      history[mode === 'push' ? 'pushState' : 'replaceState'](null, '', url);
    }
  }

  profileButtons.forEach((button) => {
    button.addEventListener('click', () => {
      if (state.profile === button.dataset.profile) return;
      state.profile = button.dataset.profile;
      render();
      writeLocation('push');
    });
  });
  languageButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const language = button.dataset.language;
      preferredLanguage = language;
      try { localStorage.setItem('eg-portfolio-language', language); } catch { /* Storage can be unavailable. */ }
      if (state.language === language) return;
      state.language = language;
      render();
      writeLocation('push');
    });
  });

  search.addEventListener('input', () => {
    state.query = search.value;
    render();
    writeLocation('replace');
  });
  document.querySelector('.project-search').addEventListener('submit', (event) => {
    event.preventDefault();
    state.query = search.value;
    render();
    writeLocation('replace');
  });
  reset.addEventListener('click', () => {
    state.profile = 'todos';
    state.query = '';
    // Keep focus on a stable, visible control when the reset button disappears.
    search.focus({ preventScroll: true });
    render();
    writeLocation('push');
  });

  function revealAnchor() {
    const project = document.getElementById(location.hash.slice(1))?.closest('.project-card');
    if (!project?.hidden) return;
    state.profile = 'todos';
    state.query = '';
    render();
    writeLocation('replace');
    project.scrollIntoView({ behavior: 'instant', block: 'start' });
  }

  window.addEventListener('popstate', () => {
    state = readLocation();
    render();
    revealAnchor();
  });
  window.addEventListener('hashchange', revealAnchor);

  const menuButton = document.querySelector('.menu-button');
  const mobileNav = document.getElementById('mobile-nav');
  function setMenu(open) {
    mobileNav.hidden = !open;
    menuButton.setAttribute('aria-expanded', String(open));
  }
  menuButton.addEventListener('click', () => setMenu(mobileNav.hidden));
  mobileNav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => setMenu(false));
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !mobileNav.hidden) {
      setMenu(false);
      menuButton.focus({ preventScroll: true });
    }
  });
  document.addEventListener('click', (event) => {
    if (!mobileNav.hidden && !mobileNav.contains(event.target) && !menuButton.contains(event.target)) {
      setMenu(false);
    }
  });
  matchMedia('(min-width: 851px)').addEventListener('change', (event) => {
    if (event.matches) setMenu(false);
  });

  document.getElementById('year').textContent = new Date().getFullYear();
  document.documentElement.dataset.enhanced = 'true';
  document.querySelector('.language-switch').hidden = false;
  document.querySelector('.project-explorer').hidden = false;
  menuButton.hidden = false;
  render();
  revealAnchor();
  writeLocation('replace');
})();
