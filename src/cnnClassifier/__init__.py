# Usage of custom logging

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # to log the data in a file
        logging.StreamHandler(sys.stdout) # to log the data in the terminal
    ]
)

logger = logging.getLogger("cnnClassifierLogger") # Giving the name of the logger. We can give any name