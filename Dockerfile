FROM python:3.8-slim-buster

WORKDIR /opt/uploaderapp

COPY /img/sampleimage  /opt/uploaderapp/img/sampleimage

COPY /shipping/samplefile  /opt/uploaderapp/shipping/samplefile

COPY /template/video.html  /opt/uploaderapp/template/video.html

COPY index.html /opt/uploaderapp/index.html

COPY index.py /opt/uploaderapp/index.py

COPY requirements.txt /opt/uploaderapp/requirements.txt 

RUN python3 -m pip install -r requirements.txt

RUN python3 index.py 