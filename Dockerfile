ARG PYTHON_VERSION
FROM python:$PYTHON_VERSION-slim-buster

EXPOSE 80
WORKDIR /wd

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt