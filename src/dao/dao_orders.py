from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import OsOrder
from schemas import Order


async def get_order_by_id(db_session: AsyncSession, order_id: int):
    order = (await db_session.scalars(select(OsOrder).where(OsOrder.id == order_id))).first()
    if not order:
        raise HTTPException(status_code=404, detail='Order not found')
    return order


async def get_order_by_number(db_session: AsyncSession, order_number: str):
    return (await db_session.scalars(select(OsOrder).where(OsOrder.order_number == order_number))).first()


async def fetch_orders(db_session: AsyncSession, skip: int, limit: int, search_query: str):
    return (await db_session.scalars(select(OsOrder).offset(skip).limit(limit))).all()


async def post_order(db_session: AsyncSession, order: Order):
    await db_session.add(OsOrder(
        order_number=order.order_number
    ))
    # TODO: fix below code
    order.id = 0
    return order


async def put_order(db_session: AsyncSession, order_id: int, order: Order):
    os_order = await db_session.get(order_id)
    os_order.order_number = order.order_number
    await db_session.refresh(os_order)
    return order


async def remove_order(db_session: AsyncSession, order_id: int):
    os_order: OsOrder = await db_session.get(order_id)
    await db_session.delete(os_order)
    # TODO: general conversion from alembic to pydantic models
    return Order(
        id=order_id,
        order_number=os_order.order_number
    )
