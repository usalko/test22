from fastapi import APIRouter, Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from models import *
from database import get_session

router = APIRouter()


@router.get('/orders', response_model=list[Order])
async def get_orders(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Order))
    orders = result.scalars().all()
    return [Order(name=order.name, id=order.id) for order in orders]


@router.post('/orders')
async def add_order(order: Order, session: AsyncSession = Depends(get_session)):
    order = Order(name=order.name, )
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return order
