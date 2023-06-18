FROM python:latest


WORKDIR /usr/app

COPY rest_app.py ./
COPY web_app.py ./
COPY db_connector.py ./
COPY requirements.txt ./


CMD [ "python", "./web_app.py"]
CMD [ "python", "./rest_app.py"]