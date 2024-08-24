from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import BaseModel


class OsSerialNumber(BaseModel):
    '''
    # Series of goods
        [Reference](https://en.wikipedia.org/wiki/Serial_number)
        - serial_number_code:       :: str
        # _
    '''
    serial_number_code: Mapped[str] = mapped_column(
        Text,  # String(MAX_SERIAL_NUMBER_CODE_LENGTH),
        index=True,
        unique=True,
    )
