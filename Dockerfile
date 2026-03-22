FROM python:3.11-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 🔥 Use start script instead of uvicorn directly
CMD ["bash", "start.sh"]