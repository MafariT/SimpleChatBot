import logging
from logging.handlers import RotatingFileHandler
from src.config import LOGGING_ENABLED
from src.config import CONSOLE_LOGGING_ENABLED

def setup_logger(name, log_file, level=logging.DEBUG):
    if LOGGING_ENABLED:
        # Define the log formatter
        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')

        # Define the file handler and set the formatter
        file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=10)
        file_handler.setFormatter(formatter)
        
        # Define the console handler and set the formatter
        if CONSOLE_LOGGING_ENABLED:
            logger = logging.getLogger(name)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)  

        # Define the logger and set the level and handlers
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(file_handler)

        # Define custom log levels
        logging.addLevelName(15, "VERBOSE")
        logging.VERBOSE = 15
        logger.setLevel(logging.VERBOSE)

    else:
        class NullHandler(logging.Handler):
            def emit(self, record):
                pass
        logger = logging.getLogger(name)
        logger.addHandler(NullHandler())

    return logger