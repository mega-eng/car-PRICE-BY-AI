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
