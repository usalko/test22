from fastapi import APIRouter, Depends

from database import get_session
from models import *

router = APIRouter(
    prefix='/api/v1/orders',
    tags=['users'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/{order_id}', response_model=list[OsOrder])
async def get_orders(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(OsOrder))
    orders = result.scalars().all()
    return [OsOrder(name=order.name, id=order.id) for order in orders]


@router.post('/orders')
async def add_order(order: OsOrder, session: AsyncSession = Depends(get_session)):
    order = OsOrder(name=order.name, )
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return order



from fastapi import APIRouter, Depends

from api.auth import validate_is_authenticated
from api.core import DBSessionDep
from app.crud.user import get_user

router = APIRouter(
    prefix='/api/users',
    tags=['users'],
    responses={404: {'description': 'Not found'}},
)

@router.get(
    '/{user_id}',
    response_model=User,
    dependencies=[Depends(validate_is_authenticated)],
)
async def user_details(
    user_id: int,
    db_session: DBSessionDep,
):
    '''
    Get any user details
    '''
    user = await get_user(db_session, user_id)
    return user