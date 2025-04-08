# from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    APP_NAME: str = "LLM API"
    DEBUG: bool = True

    GOOGLE_CLOUD_STORAGE_KEY: str = "etc/secret/google-cloud-storage.json"
    GOOGLE_CLOUD_STORATE_BUCKET: str = "sarana"

    # LLM Settings
    DEFAULT_MODEL: str = "gemini-2.0-flash-001"
    DEFAULT_TEMPERATURE: float = 0.1

    # DB Settings
    DB_USER: str = ""
    DB_PASSWORD: str = ""
    DB_HOST: str = ""
    DB_PORT: str = ""
    DB_NAME: str = ""

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
