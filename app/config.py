from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    # Database fields (match your .env)
    database_hostname: str = "localhost"
    database_port: int = 5432
    database_username: str = "postgres"
    database_password: str = "password"
    database_name: str = "fastapi"

    # Other settings
    secret_key: str = "testsecret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"  # optional safety
    )

    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.database_username}:"
            f"{self.database_password}@"
            f"{self.database_hostname}:"
            f"{self.database_port}/"
            f"{self.database_name}"
        )


settings = Settings()
