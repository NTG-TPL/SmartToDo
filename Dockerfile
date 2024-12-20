FROM python:3.11-slim

WORKDIR /code

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./app ./app

RUN mkdir -p logs
VOLUME logs

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD curl --fail http://localhost:8000/ || exit 1

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
