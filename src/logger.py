import logging
from logging.handlers import RotatingFileHandler
from src.config import LOGGING_ENABLED, CONSOLE_LOGGING_ENABLED


def setup_logger(name: str, log_file: str, level: int = logging.DEBUG) -> logging.Logger:
    # create a new logger instance with the given name
    logger = logging.getLogger(name)

    # if logging is not enabled, add a null handler and return the logger
    if not LOGGING_ENABLED:
        logger.addHandler(logging.NullHandler())
        return logger

    # configure the log formatter
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s] %(message)s",
        "%Y-%m-%d %H:%M:%S")
    
    # create a rotating file handler for the log file
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1024 * 1024,
        backupCount=10,
        encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # if console logging is enabled, create a console handler
    if CONSOLE_LOGGING_ENABLED:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    # and add a custom logging level called VERBOSE if level == 15
    logging.addLevelName(15, "VERBOSE")
    logger.setLevel(logging.VERBOSE if level == 15 else level)

    return logger

logger = setup_logger('chatbot', 'chatbot.log')


