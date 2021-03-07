from starlette.config import Config

config = Config(".env")

RUNTIME_ENV = config("RUNTIME_ENV", cast=str, default=None)

FASTAPI_LOG_LEVEL = config("FASTAPI_LOG_LEVEL", cast=str, default="info")

OPENAPI_DEPLOYED_SERVER_URL = config("OPENAPI_DEPLOYED_SERVER_URL", default=None)
OPENAPI_DEPLOYED_SERVER_URL_LIST = [{"url": OPENAPI_DEPLOYED_SERVER_URL}] if OPENAPI_DEPLOYED_SERVER_URL else None
