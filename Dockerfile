FROM python:3.12-slim

WORKDIR /app

COPY requirements.lock.txt .

RUN pip install -r "requirements.lock.txt"

COPY mathsketch/ .

COPY static/ .

CMD ["uvicorn", "mathsketch.main:app", "--host 0.0.0.0", "--port 8080"]
