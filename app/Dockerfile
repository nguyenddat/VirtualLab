FROM python:3.12.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y netcat-openbsd

RUN mkdir /app
WORKDIR /app

COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
