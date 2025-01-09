import logging
import os
from datetime import datetime

def setup_logger():
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)

    # Set up logging
    logger = logging.getLogger('linkedin_automation')
    logger.setLevel(logging.INFO)

    # Create handlers
    log_file = f"logs/app_{datetime.now().strftime('%Y%m%d')}.log"
    file_handler = logging.FileHandler(log_file)
    console_handler = logging.StreamHandler()

    # Create formatters and add it to handlers
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(log_format)
    console_handler.setFormatter(log_format)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger 