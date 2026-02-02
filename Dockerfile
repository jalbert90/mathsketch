FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements/runtime.txt .
RUN pip install --no-cache-dir -r "runtime.txt"

COPY mathsketch/ mathsketch/

COPY static/ static/

COPY models/trained_model.onnx models/

CMD ["python", "-m", "mathsketch.main"]
