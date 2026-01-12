import logging

logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        # logging.FileHandler('app11.log'),
        logging.StreamHandler()
    ],
    force=True
)
logging.debug('This is a debug message')