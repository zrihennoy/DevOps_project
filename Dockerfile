FROM python:latest


WORKDIR /usr/app

COPY rest_app.py ./
COPY db_connector.py ./
COPY requirements.txt ./


CMD [ "python", "./rest_app.py"]