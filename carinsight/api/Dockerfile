FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/model

COPY carinsight/api/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Include the original trained bundle and inference code unchanged.
COPY carinsight/app/ /app/model/
COPY carinsight/api/main.py /app/api/main.py

ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "uvicorn main:api --host 0.0.0.0 --port ${PORT:-8000} --app-dir /app/api"]
