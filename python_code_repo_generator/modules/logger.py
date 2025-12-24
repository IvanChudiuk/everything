import logging
import os

from logging import config as cnfg

from config import logging_config


class Logger:
    """Custom Logger class to create a logger configured from config."""

    def __init__(self, name: str = None) -> None:
        """Initializes the Logger instance."""
        if name is None:
            name = os.path.basename(__file__)

        os.makedirs("logs", exist_ok=True)
        cnfg.dictConfig(logging_config)
        self.logger = logging.getLogger(name)

    def info(self, message: str) -> None:
        """Log an info message."""
        self.logger.info(message)

    def error(self, message: str) -> None:
        """Log an error message."""
        self.logger.error(message)

    def warning(self, message: str) -> None:
        """Log a warning message."""
        self.logger.warning(message)

    def debug(self, message: str) -> None:
        """Log a debug message."""
        self.logger.debug(message)

    def critical(self, message: str) -> None:
        """Log a critical message."""
        self.logger.critical(message)

    def exception(self, message: str) -> None:
        """Log an exception message with traceback."""
        self.logger.exception(message)
