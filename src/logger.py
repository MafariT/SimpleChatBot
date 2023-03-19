import logging
from src.config import LOGGING_ENABLED

def setup_logger(name, log_file, level=logging.DEBUG):
    if LOGGING_ENABLED:
        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
    else:
        class NullHandler(logging.Handler):
            def emit(self, record):
                pass
        logger = logging.getLogger(name)
        logger.addHandler(NullHandler())
    return logger