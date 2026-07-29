# Eduardo Gaitán — Portfolio

Static portfolio for Eduardo Gaitán, focused on automation, data systems, bots, cloud support, and practical infrastructure.

## Local preview

```bash
docker compose up --build
```

Open `http://localhost:8080` after adding a local port mapping, or serve the files with any static web server.

## Production deployment

The production compose file uses the existing `n8n_default` Docker network and Traefik labels on the VPS. The public route is:

`https://eduardo.srv1175749.hstgr.cloud`

The PDF linked from the site is generated under `output/pdf/` and copied into the Nginx image during deployment.
