import pysftp
import json
import logging
import sys 

def setup_custom_logger(name):

    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('logs/uploader.log', mode='w')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)

    return logger

def transfer( filename ):
    log = setup_custom_logger("TransferThread")

    with open('env.json', "r") as f:
        cred = json.load(f)

    with pysftp.Connection(host=f"{cred['host']}", username=f"{cred['user']}", password=f"{cred['password']}") as sf:
        
        log.info("SFTP connection success")
        local_file = f"./media/{filename}"
        remote_path = f"/usr/local/WowzaStreamingEngine/content/angani/test/{filename}"

        try: 
            sf.put(local_file, remote_path)
            log.info(f"Transfer of {filename} transfer complete")
        except Exception as e:
            log.error(f"{e}: An error occured when transferring {filename}.")
