from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "{{cookiecutter.project_name}}"
    LOG_LEVEL: str = "INFO"
    ROOT_PATH: str = ""

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
