FROM python:3.11

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir -r ./requirements.txt

RUN mkdir -p logs
VOLUME logs

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD curl --fail http://localhost:8000/ || exit 1

CMD ["uvicorn", "app/main:app", "--host", "0.0.0.0", "--port", "8000"]
