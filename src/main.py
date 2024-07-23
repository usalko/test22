# private_api.py
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from miniopy_async import Minio

private_app = FastAPI()

async_minio_client = Minio(
    'play.min.io',
    access_key='Q3AM3UQ867SPQQA43P2F',
    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
    secure=True  # http for False, https for True
)


@private_app.get('/')
async def home():
    return {'description': 'PRIVATE API'}

# [PUT] /images

# [GET] /images/{image_id}


def openapi_schema():
    if private_app.openapi_schema:
        return private_app.openapi_schema
    openapi_schema = get_openapi(
        title='Private test21 API',
        version='1.0.0',
        summary='This is a private API for test21',
        description='The private API contains couple of methods for deal with images',
        routes=private_app.routes,
    )
    openapi_schema['info']['x-logo'] = {
        'url': 'https://test21.qstand.art/img/logo-margin/logo-teal.png'
    }
    private_app.openapi_schema = openapi_schema
    return private_app.openapi_schema


private_app.openapi = openapi_schema
