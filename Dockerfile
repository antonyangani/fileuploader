FROM faucet/python3

COPY .  /opt/uploaderapp

WORKDIR /opt/uploaderapp

RUN python3 -m pip install -r requirements.txt

RUN python3 index.py 