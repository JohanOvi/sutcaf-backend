from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    external_api_base_url: str
    external_api_version: str

    external_client_id: str
    external_client_secret: str
    external_username: str
    external_password: str

    class Config:
        env_file = ".env"

settings = Settings()
