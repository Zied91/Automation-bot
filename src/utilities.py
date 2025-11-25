import logging
import os

LOG_FILE = "logs/bot.log"

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
)


def log(msg):
    print(msg)
    logging.info(msg)
