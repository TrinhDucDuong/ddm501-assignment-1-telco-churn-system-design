FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --timeout 180 --retries 5 -r requirements.txt
COPY churn churn
COPY config.yaml .
COPY data data
RUN python -m churn
EXPOSE 8000
CMD ["uvicorn", "churn.api:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
