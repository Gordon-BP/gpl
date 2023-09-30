import logging
from logging import StreamHandler, FileHandler

def set_logger_format():
    root_logger = logging.getLogger()
    formatter = logging.Formatter(
        fmt="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    # Create a file handler
    file_handler = FileHandler('logfile.log')
    file_handler.setFormatter(formatter)
    
    # Add the file handler to the logger
    root_logger.addHandler(file_handler)
    
    # Update formatters for existing StreamHandlers
    for handler in root_logger.handlers:
        if isinstance(handler, StreamHandler):
            handler.setFormatter(formatter)