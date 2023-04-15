import logging
from logging.handlers import RotatingFileHandler
from src.config import LOGGING_ENABLED, CONSOLE_LOGGING_ENABLED

"""
This module contains the logger for the chatbot.
"""

def setup_logger(name: str, log_file: str, level: int = logging.DEBUG) -> logging.Logger:
    # create a new logger instance with the given name
    inner_logger = logging.getLogger(name)

    # if logging is not enabled, add a null handler and return the logger
    if not LOGGING_ENABLED:
        inner_logger.addHandler(logging.NullHandler())
        return inner_logger

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
    inner_logger.addHandler(file_handler)

    # if console logging is enabled, create a console handler
    if CONSOLE_LOGGING_ENABLED:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        inner_logger.addHandler(console_handler)

    inner_logger.setLevel(level)

    return inner_logger

logger = setup_logger('chatbot', 'chatbot.log')


