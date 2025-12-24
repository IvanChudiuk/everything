import os

from config import app_config
from modules import logger

current_file = os.path.basename(__file__)
logger = logger.Logger(current_file)


def main():
    logger.info("Application started.")


if __name__ == "__main__":
    main()
