from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import BaseModel
from .invariants import *


class OsOrder(BaseModel):
    '''
        # Customer order
            - order_number      :: str
    '''
    order_number: Mapped[str] = mapped_column(
        Text,  # String(MAX_ORDER_NUMBER_LENGTH),
        index=True,
        unique=True,
    )
