FROM python:3.10-slim

MAINTAINER Dmitrey Kazin

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app

CMD ["python", "app.py"]
