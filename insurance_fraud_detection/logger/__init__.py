import logging
import os
from datetime import datetime
from from_root import from_root

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Creates a timestamped log filename

log_dir = 'logs'  # Directory for logs

# Correct way to join paths: first get the root path, then join with log_dir and LOG_FILE
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

# Ensure the log directory exists before logging starts
os.makedirs(os.path.join(from_root(), log_dir), exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%m/%d/%Y %I:%M:%S %p"
)
