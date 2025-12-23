import logging
import os
from logging.handlers import TimedRotatingFileHandler


def _create_log_dir(log_file: str) -> None:
    """Create log directory if it doesn't exist."""
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)


class Logger:
    """Custom Logger class to create a logger with timed rotating file handler."""

    def __init__(self, name: str, level: str, log_file: str, format_str: str) -> None:
        """Initializes the Logger instance.

        Args:
            name (str): Name of the logger.
            level (str): Logging level as a string (e.g., 'DEBUG', 'INFO').
            log_file (str): Path to the log file.
            format_str (str): Format string for log messages.
        """
        self.logger = logging.getLogger(name)

        # Validate and set level
        try:
            numeric_level = getattr(logging, level.upper(), None)
            if not isinstance(numeric_level, int):
                raise ValueError(f"Invalid log level: {level}")
            self.logger.setLevel(numeric_level)
        except AttributeError:
            raise ValueError(f"Invalid log level: {level}")

        self.logger.propagate = False  # Avoid duplicate logs

        # Ensure log directory exists
        _create_log_dir(log_file)

        # Stream handler (prints to stdout)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        # Create timed rotating file handler for daily rotation
        handler = TimedRotatingFileHandler(
            log_file, when="midnight", interval=1, backupCount=30
        )
        handler.setLevel(numeric_level)

        # Create formatter and apply to both handlers
        formatter = logging.Formatter(format_str)
        handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # Add handlers to logger if not already added
        if not self.logger.handlers:
            self.logger.addHandler(handler)
            self.logger.addHandler(stream_handler)

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
