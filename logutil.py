import os
import logging
from logging.handlers import RotatingFileHandler

_level = logging.INFO

try:
    os.stat('log')
except:
    os.mkdir('log')

logging.basicConfig(level=_level)

def get_logger(name: str) -> logging.Logger:
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(name)s %(message)s')
    
    logger = logging.Logger(name)
    logger.setLevel(_level)

    rotatingFileHandler = RotatingFileHandler('log/myloggfile.log', maxBytes=10000, backupCount=10)
    rotatingFileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    
    logger.addHandler(rotatingFileHandler)
    logger.addHandler(streamHandler)
    
    return logger
all = (get_logger)