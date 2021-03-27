FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python-pip \
    python3-pip 

WORKDIR /data

COPY /img/sampleimage  /data/img/sampleimage

COPY /shipping/samplefile  /data/shipping/samplefile

COPY /template/video.html  /data/template/video.html

COPY index.html /data/index.html

COPY index.py /data/index.py

COPY requirements.txt /data/requirements.txt 

VOLUME [ "/opt/uploaderapp" ]

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "index.py"] 

EXPOSE 8000