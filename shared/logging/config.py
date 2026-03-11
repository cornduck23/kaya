import os
import logging
import logging.config
import sys

from shared.config import settings

def setup_logging(service_name: str) -> None:
    log_level = settings.LOG_LEVEL
    log_format = settings.LOG_FORMAT
    log_file = settings.LOG_FILE

    if os.path.isdir(log_file) and service_name:
        log_file = os.path.join(log_file, f"{service_name}.log")
    
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "{asctime} [{levelname}] {name}: {message}",
                "style": "{",
                "datefmt": "%Y-%m-%d %H:%M:%S"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": sys.stdout,
                "formatter": log_format,
                "level": log_level,
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": log_file,
                "maxBytes": 10485760,
                "backupCount": 5,
                "formatter": log_format,
                "level": log_level,
            }
        },
        "root": {
            "handlers": ["console", "file"],
            "level": log_level,
        },
        "loggers": {
            "aiogram": {
                "level": "INFO",
                "propagate": False,
                "handlers": ["console", "file"],
            },
            "uvicorn": {
                "level": "INFO",
                "propagate": False,
                "handlers": ["console", "file"],
            },
            "uvicorn.error": {
                "level": "INFO",
                "propagate": False,
                "handlers": ["console", "file"],
            },
            "uvicorn.access": {
                "level": "INFO",
                "propagate": False,
                "handlers": ["console", "file"],
            },
            "fastapi": {
                "level": "INFO",
                "propagate": False,
                "handlers": ["console", "file"],
            },
        }
    }

    logging.config.dictConfig(config)
