from logging import Filter
from logging.config import dictConfig

from app.application.core.config import settings


class ReadinnessFilter(Filter):
    def filter(self, record):
        return record.getMessage().find("/readiness") == -1


class HealthzFilter(Filter):
    def filter(self, record):
        return record.getMessage().find("/healthz") == -1


def configure_logging() -> None:
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "filters": {
                "readiness_filter": {"()": ReadinnessFilter},
                "healthz_filter": {"()": HealthzFilter},
            },
            "formatters": {
                "console": {
                    "class": "logging.Formatter",
                    "datefmt": "%H:%M:%S",
                    "format": "%(levelname)s:\t\b%(asctime)s %(name)s:%(lineno)d %(message)s",  # noqa
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "filters": ["readiness_filter", "healthz_filter"],
                    "formatter": "console",
                },
            },
            "loggers": {
                "app": {
                    "handlers": ["console"],
                    "level": settings.LOG_LEVEL,
                    "propagate": True,
                },
                "uvicorn": {"handlers": ["console"], "level": "INFO"},
                "databases": {"handlers": ["console"], "level": "WARNING"},
                "httpx": {"handlers": ["console"], "level": "INFO"},
            },
        }
    )
