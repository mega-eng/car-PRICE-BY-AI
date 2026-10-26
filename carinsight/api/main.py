import os
import sys
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

MODEL_DIR = Path("/app/model")
if MODEL_DIR.exists():
    sys.path.insert(0, str(MODEL_DIR))
else:
    # Local development: run from the repository root.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

import app as model_app  # Reuse the existing model and prediction function unchanged.

allowed_origins = [
    item.strip()
    for item in os.getenv("FRONTEND_ORIGINS", "*").split(",")
    if item.strip()
]

api = FastAPI(
    title="CarInsight AI API",
    description="Image-only car price estimation API. Uses the existing CarInsight model.",
    version="1.0.0",
)

api.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins if allowed_origins != ["*"] else ["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

MAX_IMAGES = 8
MAX_BYTES_PER_IMAGE = 12 * 1024 * 1024
ALLOWED_TYPES = {"image/jpeg", "image/png", "image/webp", "image/gif"}


@api.get("/")
def root():
    return {"service": "CarInsight AI API", "docs": "/docs", "health": "/health"}


@api.get("/health")
def health():
    return {"status": "ok", "model_loaded": hasattr(model_app, "BUNDLE")}


@api.post("/predict")
async def predict(images: list[UploadFile] = File(...)):
    if not images:
        raise HTTPException(status_code=400, detail="ارفع صورة واحدة على الأقل.")
    if len(images) > MAX_IMAGES:
        raise HTTPException(status_code=400, detail=f"الحد الأقصى {MAX_IMAGES} صور.")

    temp_paths = []
    try:
        with tempfile.TemporaryDirectory(prefix="carinsight-") as temp_dir:
            for index, image in enumerate(images):
                if image.content_type not in ALLOWED_TYPES:
                    raise HTTPException(
                        status_code=415,
                        detail=f"الملف رقم {index + 1} ليس صورة مدعومة.",
                    )
                content = await image.read(MAX_BYTES_PER_IMAGE + 1)
                if not content:
                    raise HTTPException(status_code=400, detail="إحدى الصور فارغة.")
                if len(content) > MAX_BYTES_PER_IMAGE:
                    raise HTTPException(
                        status_code=413,
                        detail="حجم الصورة الواحدة يجب ألا يتجاوز 12 ميغابايت.",
                    )
                suffix = {
                    "image/jpeg": ".jpg",
                    "image/png": ".png",
                    "image/webp": ".webp",
                    "image/gif": ".gif",
                }[image.content_type]
                target = Path(temp_dir) / f"image_{index}{suffix}"
                target.write_bytes(content)
                temp_paths.append(str(target))

            # The same prediction function used by the original Gradio app.
            result = model_app.predict(temp_paths)
            return {"result": result}
    finally:
        for image in images:
            await image.close()
