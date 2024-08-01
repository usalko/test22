from dataclasses import dataclass

from sqlmodel import Field

from .base_model import BaseModel
from .invariants import *


@dataclass
class Order(BaseModel, table=True):
    __tablename__ = 'os_order'
    order_number: str = Field(
        index=True,
        max_length=MAX_ORDER_NUMBER_LENGTH,
        unique=True,
    )
