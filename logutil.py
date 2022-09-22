import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.DEBUG)

def get_logger(name: str) -> logging.Logger:
    logger = logging.Logger(name)
    logger.setLevel(logging.DEBUG)
    
    logger.addHandler(RotatingFileHandler('myloggfile.log', maxBytes=10000, backupCount=3))
    logger.addHandler(logging.StreamHandler())
    
    return logger
all = (get_logger)