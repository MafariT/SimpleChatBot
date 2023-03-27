import logging
from logging.handlers import RotatingFileHandler
from src.config import LOGGING_ENABLED, CONSOLE_LOGGING_ENABLED


def setup_logger(name, log_file, level=logging.DEBUG):
    logger = logging.getLogger(name)

    if not LOGGING_ENABLED:
        logger.addHandler(logging.NullHandler())
        return logger

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s] %(message)s",
        "%Y-%m-%d %H:%M:%S")
    
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1024 * 1024,
        backupCount=10,
        encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    if CONSOLE_LOGGING_ENABLED:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    logging.addLevelName(15, "VERBOSE")
    logger.setLevel(logging.VERBOSE if level == 15 else level)

    return logger

logger = setup_logger('chatbot', 'chatbot.log')
