"""Module for load settings form `...env` or if server running with parameter
`dev` from `...env.dev`"""

from functools import lru_cache
from typing import List

from dotenv import find_dotenv
from pydantic.env_settings import BaseSettings
from pydantic.types import PositiveInt, SecretStr

__all__ = ['Settings', 'get_settings']


class _Settings(BaseSettings):
    class Config:
        """Configuration of settings."""

        #: str: ..env file encoding.
        env_file_encoding = 'utf-8'
        #: str: allow custom fields in model.
        arbitrary_types_allowed = True


class Settings(_Settings):
    """Server settings.

    Formed from `...env` or `...env.dev`.
    """
    # email
    EMAIL_USE_TLS : SecretStr
    EMAIL_HOST : SecretStr
    EMAIL_PORT : SecretStr
    EMAIL_HOST_USER : SecretStr
    EMAIL_HOST_PASSWORD : SecretStr
    EMAIL_REPORT : SecretStr
    # Redis
    CELERY_BROKER_URL : SecretStr
    CELERY_RESULT_BACKEND : SecretStr

    # Yookassa
    ACCOUNT_ID : SecretStr
    SECRET_KEY : SecretStr

    # SecretStr: secret django
    SECRET_KEY: SecretStr
    # Mode work django, develop or prod
    DEBUG: bool

    #: SecretStr: secret x-token for authority.
    X_API_TOKEN: SecretStr
    #: str: Trusted host.
    ALLOWED_HOSTS: List[str]

    #: str: Postgresql host.
    POSTGRES_HOST: str
    #: PositiveInt: positive int (x > 0) port of postgresql.
    POSTGRES_PORT: PositiveInt
    #: str: Postgresql user.
    POSTGRES_USER: str
    #: SecretStr: Postgresql password.
    POSTGRES_PASSWORD: SecretStr
    #: str: Postgresql database name.
    POSTGRES_DATABASE_NAME: str

    #: SecretStr:
    DRF_RECAPTCHA_SECRET_KEY: SecretStr
    #: SecretStr:
    RECAPTCHA_PUBLIC_KEY: SecretStr


@lru_cache()
def get_settings(env_file: str = '.env') -> Settings:
    """Create settings instance."""
    return Settings(_env_file=find_dotenv(env_file))
