FROM python:3.11-slim

# Non-root user — container compromise ≠ root shell
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Dependencies first: this layer caches until requirements.txt changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code last: edits here don't bust the pip layer
COPY app.py .

USER appuser

EXPOSE 5001

CMD ["python", "app.py"]