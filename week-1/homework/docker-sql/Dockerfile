FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY ingest-data.py ingest-data.py

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "ingest-data.py" ]