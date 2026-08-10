import os
from pathlib import Path


class Settings:
    PROJECT_NAME = "MaskForge"
    DATABASE_HOST = os.getenv("POSTGRES_HOST", "localhost")
    DATABASE_PORT = os.getenv("POSTGRES_PORT", 5432)
    DATABASE_USER = os.getenv("POSTGRES_USER", "postgres")
    DATABASE_PASSWORD = os.getenv("POSTGRES_PASSWORD", "admin123")
    DATABASE_DB = os.getenv("POSTGRES_DB", "maskforge")

    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = os.getenv("REDIS_PORT", "6379")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "admin123")
    REDIS_DB = os.getenv("REDIS_DB", "0")

    CELERY_BROKER_URL = f"redis://@{REDIS_HOST}:{REDIS_PORT}/1"
    CELERY_BACKEND_URL = f"redis://@{REDIS_HOST}:{REDIS_PORT}/2"

    MINIO_ENDPOINT = f"{os.getenv('MINIO_HOST', 'localhost')}:{os.getenv('MINIO_PORT', '9000')}"
    MINIO_ACCESS_KEY = os.getenv(
        "MINIO_ROOT_USER",
        "minioadmin"
    )
    MINIO_SECRET_KEY = os.getenv(
        "MINIO_ROOT_PASSWORD",
        "minioadmin"
    )
    MINIO_BUCKET = "maskforge"

    USER_RATE_LIMIT = int(os.getenv("USER_RATE_LIMIT", 120))
    WRITE_RATE_LIMIT = int(os.getenv("WRITE_RATE_LIMIT", 30))
    IP_RATE_LIMIT = int(os.getenv("IP_RATE_LIMIT", 600))
    RATE_LIMIT_WINDOW = int(os.getenv("RATE_LIMIT_WINDOW", 60))

    TORTOISE_ORM = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.asyncpg",
                "credentials": {
                    "host": DATABASE_HOST,
                    "port": DATABASE_PORT,
                    "user": DATABASE_USER,
                    "password": DATABASE_PASSWORD,
                    "database": DATABASE_DB,
                    "min_size": 1,
                    "max_size": 5,
                    "command_timeout": 60,
                },
            }
        },
        "apps": {
            "models": {
                "models": ["app.models", "aerich.models"],
                "default_connection": "default",
            },
        },
        "use_tz": True,
        "timezone": "UTC",
    }


settings = Settings()
