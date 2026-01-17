from pydantic_settings import BaseSettings
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Settings(BaseSettings):
    environment: str = "dev"
    debug: bool = True
    database_url: str = f"sqlite:///{os.path.join(BASE_DIR, 'miso.db')}"

settings = Settings()