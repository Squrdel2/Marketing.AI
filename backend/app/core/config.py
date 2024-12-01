from pydantic_settings import BaseSettings # type: ignore

class Settings(BaseSettings):
    ALLOWED_ORIGINS: list = ["http://localhost:3000"]
    DATABASE_URL: str = "postgresql://postgres.hvynedzqykzhgmjyupuv:[YOUR-PASSWORD]@aws-0-eu-west-2.pooler.supabase.com:6543/postgres"
    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"

settings = Settings()