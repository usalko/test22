from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dao.dao_orders import *
from database import *
from models import *
from schemas import *

router = APIRouter(
    prefix='/api/v1/orders',
    tags=['orders'],
    responses={404: {'description': 'Not found'}},
)


@router.get(
    '/{order_id}',
    response_model=Order,
)
async def order_details(
    order_id: int,
    db_session: Session = Depends(get_db_session),
):
    '''
    Get any order details
    '''
    order = await get_order_by_id(db_session, order_id)
    return order


@router.get('/')
async def read_orders(
    skip: int = 0,
    limit: int = 10,
    search: str | None = None,
    db_session: Session = Depends(get_db_session),
):
    orders = await fetch_orders(db_session, skip=skip, limit=limit, search_query=search)
    return {'orders': orders, 'skip': skip, 'limit': limit}
