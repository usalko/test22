from dataclasses import dataclass

from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, relationship

from .base_model import BaseModel
from .os_serial_number import *


@dataclass
class OsSku(BaseModel):
    '''
        # Stock keeper unit
            - id                :: int
            - sku_code          :: str
    '''
    sku_code: Mapped[str] = mapped_column(
        Text, # String(MAX_SKU_CODE_LENGTH),
        index=True,
        unique=True,
    )
    sku_serial_number_id = mapped_column(Integer, ForeignKey('os_serial_number.id'))
    sku_serial_number: Mapped[OsSerialNumber | None] = relationship(
        OsSerialNumber,
        foreign_keys='[OsSku.sku_serial_number_id]',
    )
