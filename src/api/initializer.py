from fastapi import FastAPI

from src.api.config import OPENAPI_DEPLOYED_SERVER_URL_LIST
from src.api.methods import router


def init_api():
    api = FastAPI(
        title="Python playground",
        description="Service to respond to lessons requests",
        version="1.0.0",
        servers=OPENAPI_DEPLOYED_SERVER_URL_LIST,
    )

    api.include_router(router, tags=["python playground"])

    return api
