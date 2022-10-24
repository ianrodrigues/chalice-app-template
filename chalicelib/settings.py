import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
CHALICE_DEBUG = bool(os.getenv("CHALICE_DEBUG", False))

CHALICE_STAGE = os.getenv("CHALICE_STAGE", "dev")

# The following describe the loggers, handlers, filters and formatters
# that you want in your logging setup, and the log levels and other
# properties that you want those components to have.
# https://docs.python.org/3.9/library/logging.config.html#logging.config.dictConfig
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "{levelname} {name} {message}",
            "style": "{",
        },
        "verbose": {
            "format": "{asctime} {levelname} {name} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "cloudwatch": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "local": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "logs/chalice.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "root": {
            "handlers": ["cloudwatch", "local"],
            "level": "DEBUG",
        },
    },
}

SENTRY_DSN = None
