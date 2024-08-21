from fastapi import APIRouter, Depends

from database import get_session
from models import *

router = APIRouter()


@router.get('/orders', response_model=list[OsOrder])
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
