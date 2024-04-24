FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip 
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ADD generate.py /generate.py

ENV TZ="Asia/Amman"
ENV STORAGEIP="10.132.173.99"
ENV SENSORNAME="Sensor 1"

CMD python3 generate.py
