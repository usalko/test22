
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    echo_sql: bool = True
    test: bool = False
    project_name: str = 'Test22 project'
    log_level: str = 'DEBUG'


settings = Settings()  # type: ignore
