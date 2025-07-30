FROM python:3.11-slim

# 🚨 SECURITY: Non-root user
RUN groupadd -r stakc && useradd -r -g stakc stakc

# 🚨 SECURITY: System packages
RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY --chown=stakc:stakc . .

# 🚨 SECURITY: Switch to non-root
USER stakc

# 🚨 SECURITY: Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000
CMD ["uvicorn", "core.main:app", "--host", "0.0.0.0", "--port", "8000"]
