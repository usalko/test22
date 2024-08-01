from dataclasses import dataclass
from sqlmodel import Field

from .base_model import BaseModel
from .invariants import *


@dataclass
class Sku(BaseModel, table=True):
    __tablename__ = 'os_sku'
    sku_code: str = Field(index=True, max_length=MAX_SKU_CODE_LENGTH, unique=True)
