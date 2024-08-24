
from os import environ

from pydantic_settings import BaseSettings

from global_constants import *


class Settings(BaseSettings):
    database_url: str = environ.get(DATABASE_URL_KEY)
    echo_sql: bool = True
    test: bool = False
    project_name: str = 'Test22 project'
    log_level: str = 'DEBUG'


settings = Settings()  # type: ignore
