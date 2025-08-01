from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import ValidationError

load_dotenv()


class Settings(BaseSettings):
    ENV: str
    DATABASE_URL: str

    class Config:
        case_sensitive = True


try:
    settings = Settings()
except ValidationError as e:
    print("❌ Environment variables are misconfigured or missing.\n")
    print(e)
    exit(1)

IS_DEV = settings.ENV == "development"
