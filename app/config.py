from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from urllib.parse import quote_plus


class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: int = 5432
    database_username: str = "postgres"
    database_password: str = "mohit#2003"
    database_name: str = "fastapi_test"

    secret_key: str = "testsecret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )

    @property
    def database_url(self) -> str:
        password = quote_plus(self.database_password)
        return (
            f"postgresql://{self.database_username}:"
            f"{password}@"
            f"{self.database_hostname}:"
            f"{self.database_port}/"
            f"{self.database_name}"
        )


settings = Settings()
