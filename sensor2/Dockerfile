FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip 
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD generate.py /generate.py

ENV TZ="America/New_York"
ENV STORAGEIP="10.132.173.99"
ENV SENSORNAME="Sensor 2"

CMD python3 generate.py
