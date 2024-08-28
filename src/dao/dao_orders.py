from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import OsOrder


async def get_order_by_id(db_session: AsyncSession, order_id: int):
    order = (await db_session.scalars(select(OsOrder).where(OsOrder.id == order_id))).first()
    if not order:
        raise HTTPException(status_code=404, detail='Order not found')
    return order


async def get_order_by_number(db_session: AsyncSession, order_number: str):
    return (await db_session.scalars(select(OsOrder).where(OsOrder.order_number == order_number))).first()


async def fetch_orders(db_session: AsyncSession, skip: int, limit: int, search_query: str):
    return (await db_session.scalars(select(OsOrder).offset(skip).limit(limit))).all()