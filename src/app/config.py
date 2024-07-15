from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_HOST: str
    MONGO_USERNAME: str
    MONGO_PASS: str
    MONGO_DBNAME: str
    REPLICA_SET: str
    TLS: str
    AUTH_SOURCE: str
    # SECRET_KEY: str
    # ALGORITHM: str
    # ACCESS_TOKEN_EXPIRE_MINUTES: int

settings = Settings()