from dataclasses import dataclass

from sqlalchemy import Column, String

from .base_model import BaseModel
from .invariants import *


@dataclass
class OsOrder(BaseModel):
    order_number: str = Column(
        String,
        index=True,
        # max_length=MAX_ORDER_NUMBER_LENGTH,
        unique=True,
    )
