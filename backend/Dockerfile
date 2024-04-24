FROM python:3.11-bookworm

WORKDIR /web

COPY requirements.txt requirements.txt

COPY server.py server.py

COPY cert.pem cert.pem
COPY key.pem key.pem

RUN pip3 install -r requirements.txt

ENV TZ="Europe/Stockholm"

EXPOSE 80
EXPOSE 443

CMD python3 server.py
