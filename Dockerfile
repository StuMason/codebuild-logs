FROM python:3.10-slim AS builder
ADD . /app
WORKDIR /app

# Install dependencies
RUN pip install --target=/app -r requirements.txt
ENV PYTHONPATH=/app
CMD ["python", "/app/main.py"]
