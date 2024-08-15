# private_api.py
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from miniopy_async import Minio
from api import orders
from app import app

async_minio_client = Minio(
    'play.min.io',
    access_key='Q3AM3UQ867SPQQA43P2F',
    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
    secure=True  # http for False, https for True
)


@app.get('/')
async def home():
    return {'description': 'Test 22 API'}


@app.get('/test')
async def pong():
    return {'test': 'ok'}


def openapi_schema():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title='Test22 API',
        version='0.1.0',
        summary='This is a private API for test22',
        description='The private API contains couple of methods for deal with images',
        routes=app.routes,
    )
    openapi_schema['info']['x-logo'] = {
        'url': 'https://test22.qstand.art/img/logo-margin/logo-teal.png'
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = openapi_schema
