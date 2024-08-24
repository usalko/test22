from dataclasses import dataclass

from sqlalchemy import Text
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
    sku_serial_number: Mapped[OsSerialNumber | None] = relationship(
        OsSerialNumber,
    )
