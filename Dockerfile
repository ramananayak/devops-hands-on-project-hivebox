FROM python:3.12-slim

ARG VERSION=0.0.0
ENV APP_VERSION=$VERSION

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENTRYPOINT [ "python", "app.py" ]
