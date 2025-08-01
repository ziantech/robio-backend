from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import ValidationError

load_dotenv()


class Settings(BaseSettings):
    ENV: str
    DATABASE_URL: str
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_STARTTLS: bool
    MAIL_SSL_TLS: bool
    USE_CREDENTIALS: bool
    MAIL_FROM_NAME: str = "RoBio"
    class Config:
        case_sensitive = True


try:
    settings = Settings()
except ValidationError as e:
    print("❌ Environment variables are misconfigured or missing.\n")
    print(e)
    exit(1)

IS_DEV = settings.ENV == "development"
