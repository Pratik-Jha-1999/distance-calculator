import logging
from logging.handlers import RotatingFileHandler

# --------------------------------------------------------------
# LOGGING CONFIGURATION
# --------------------------------------------------------------
logger = logging.getLogger("distance_app")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    "app.log", maxBytes=2_000_000, backupCount=5  # 2MB per file, keep 5 backups
)
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)
