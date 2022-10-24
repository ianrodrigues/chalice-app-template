import logging.config

from chalicelib import settings


def configure_logging() -> None:
    """
    Configure logging using dictConfig.
    """
    logging.config.dictConfig(settings.LOGGING)
