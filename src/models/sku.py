from dataclasses import dataclass

from sqlmodel import Field, Relationship

from .base_model import BaseModel
from .invariants import *
from .serial_number import *


@dataclass
class Sku(BaseModel, table=True):
    __tablename__ = 'os_sku'
    sku_code: str = Field(index=True, max_length=MAX_SKU_CODE_LENGTH, unique=True)
    sku_serial_number: SerialNumber | None = Relationship(back_populates='sku_serial_number')
