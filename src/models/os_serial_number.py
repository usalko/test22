
from sqlalchemy import Column, String

from .base_model import BaseModel
from .invariants import *


class OsSerialNumber(BaseModel):
    '''
    # Series of goods
        [Reference](https://en.wikipedia.org/wiki/Serial_number)
        - serial_number_code:      str
        # _
    '''
    serial_number_code: str = Column(
        String,
        index=True,
        # max_length=MAX_SERIAL_NUMBER_CODE_LENGTH,
        unique=True,
    )
