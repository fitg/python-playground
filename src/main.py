import uvicorn

from src.api.config import FASTAPI_LOG_LEVEL
from src.api.initializer import init_api

api = init_api()


def start_app():
    uvicorn.run(
        api,
        host="0.0.0.0",
        port=8000,
        log_level=FASTAPI_LOG_LEVEL,
        use_colors=True,
    )
