FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY coming-soon coming-soon

EXPOSE 8000
CMD ["gunicorn", "app:application", "--bind", "0.0.0.0:8000"]
