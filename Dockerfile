FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk add -u zlib-dev jpeg-dev gcc musl-dev

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

