FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip 

WORKDIR /data

COPY /media/sampleimage  /data/media/sampleimage

COPY /static-html/samplefile  /data/static-html/samplefile

COPY /template/video.html  /data/template/video.html

COPY /logs/uploader.log  /data/logs/uploader.log 

COPY index.html /data/index.html

COPY transfer.py /data/transfer.py 

COPY index.py /data/index.py

COPY env.json /data/env.json 

COPY requirements.txt /data/requirements.txt 

VOLUME [ "/opt/uploaderapp" ]

RUN python3 -m pip install -r /data/requirements.txt

CMD ["python3", "/data/index.py"] 

EXPOSE 8000