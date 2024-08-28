# private_api.py
from fastapi import Request
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from miniopy_async import Minio

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


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exception: Exception):
    return JSONResponse(
        status_code=418,
        content={'message': f'Exception: {exception}'},
    )


def openapi_schema():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title='Test22 API',
        version='1.0.0',
        summary='This is an API for test22',
        description='The private API contains couple of methods for deal with images',
        routes=app.routes,
    )
    openapi_schema['info']['x-logo'] = {
        'url': 'https://test22.qstand.art/img/logo-margin/logo-teal.png',
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = openapi_schema
