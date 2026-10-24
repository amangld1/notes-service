FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app

COPY app ./app

EXPOSE 8080

USER 1000:1000

CMD ["python3", "-m", "app.main"]
