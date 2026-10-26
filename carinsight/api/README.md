# CarInsight AI API

This API wraps the existing Gradio app's `predict()` function. It does not retrain, replace, or alter the trained model or prediction calculation.

## Endpoints

- `GET /` — service information
- `GET /health` — health check
- `POST /predict` — multipart form upload using the field name `images` (1–8 image files)
- `GET /docs` — interactive API docs

## Deploy with Docker

Build from the repository root (the Dockerfile copies the original files from `carinsight/app/`):

```bash
docker build -f carinsight/api/Dockerfile -t carinsight-api .
docker run --rm -p 8000:8000 -e FRONTEND_ORIGINS="https://YOUR-USER.github.io" carinsight-api
```

Check `http://localhost:8000/health`. The first prediction may take longer while the DINOv2/CLIP image encoders download their weights. Ensure the server has enough RAM and persistent disk/cache space.

## Persistent HTTPS deployment (Oracle Cloud VM)

1. Create an Ubuntu VM using the **Always Free eligible** Ampere A1 shape, within the currently available free limits. This is the suggested host for an always-on CPU backend; capacity can be unavailable, and free-resource policies can change.
2. Point a DNS hostname (for example, one from a dynamic DNS provider) to the VM's public IP.
3. Install Docker Engine and the Docker Compose plugin on the VM. Allow inbound TCP ports 80 and 443 in both the cloud network security rules and the VM firewall.
4. Copy/clone this repository onto the VM and enter `carinsight/api/`.
5. Copy `.env.example` to `.env` and set `API_DOMAIN` to your hostname.
6. In `compose.yaml`, keep `FRONTEND_ORIGINS` set to `https://mega-eng.github.io` (or change it to the exact origin that serves your Pages site).
7. Start the services:

```bash
docker compose --env-file .env up -d --build
docker compose logs -f api
```

Caddy will request and renew HTTPS certificates automatically once DNS and ports 80/443 are correct. Test `https://YOUR_API_DOMAIN/health`. The first image prediction may download DINOv2/CLIP weights, so it can take several minutes.

After the API works over HTTPS, update `docs/api-config.js` in GitHub Pages:

```js
window.CARINSIGHT_API_URL = "https://YOUR_API_DOMAIN";
```

Commit and push that change so the website can call the API. Never put cloud passwords or private keys in the repository.

## Local development

Install `carinsight/api/requirements.txt`, then change to the original app folder before starting the API:

```bash
cd carinsight/app && uvicorn main:api --app-dir ../api --reload
```

The original model bundle must be present at `carinsight/app/bundle.joblib`.

## Notes

- CPU inference is supported, but can be slower.
- The API limits uploads to 8 images and 12 MiB per image.
- Set `FRONTEND_ORIGINS` to the exact GitHub Pages origin when deploying. Use `*` only for temporary testing.
- The model encoder weights are downloaded on first use from their upstream model repositories; the trained `bundle.joblib` stays the original project artifact.
