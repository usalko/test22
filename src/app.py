from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from miniopy_async import Minio
from src.api import orders

app = FastAPI()

app.include_router(orders.router)
