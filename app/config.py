import os


class Settings:
    PROJECT_NAME = "MaskForge"

    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = os.getenv("REDIS_PORT", "6379")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "admin123")
    REDIS_DB = os.getenv("REDIS_DB", "0")

    USER_RATE_LIMIT = int(os.getenv("USER_RATE_LIMIT", 120))
    WRITE_RATE_LIMIT = int(os.getenv("WRITE_RATE_LIMIT", 30))
    IP_RATE_LIMIT = int(os.getenv("IP_RATE_LIMIT", 600))
    RATE_LIMIT_WINDOW = int(os.getenv("RATE_LIMIT_WINDOW", 60))


settings = Settings()
