from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dao.dao_orders import *
from database import *
from models import *
from schemas import *

router = APIRouter(
    prefix='/api/v1/orders',
    tags=['users'],
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
