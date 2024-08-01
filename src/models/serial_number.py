from dataclasses import dataclass

from sqlmodel import Field

from .base_model import BaseModel
from .invariants import *


@dataclass
class SerialNumber(BaseModel, table=True):
    '''
    # Series of goods
    [Reference](https://en.wikipedia.org/wiki/Serial_number)
        - serial_number_code:      str
        # _
    '''
    __tablename__ = 'os_serial_number'
    serial_number_code: str = Field(
        index=True,
        max_length=MAX_SERIAL_NUMBER_CODE_LENGTH,
        unique=True,
    )
