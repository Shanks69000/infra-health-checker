FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY checker.py config.yml ./
RUN mkdir reports

USER 1000

CMD ["python", "checker.py"]