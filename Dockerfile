FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --no-cache-dir confluent_kafka

WORKDIR /app

COPY . /app/

CMD ["python", "producer.py"]