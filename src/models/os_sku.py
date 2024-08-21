from dataclasses import dataclass

from sqlalchemy import Column
from sqlalchemy.orm import Mapped, relationship

from .base_model import BaseModel
from .invariants import *
from .os_serial_number import *


@dataclass
class OsSku(BaseModel):
    sku_code: str = Column(
        String,
        index=True,
        # max_length=MAX_SKU_CODE_LENGTH,
        unique=True,
    )
    sku_serial_number: Mapped[OsSerialNumber | None] = relationship(
        OsSerialNumber,
    )
