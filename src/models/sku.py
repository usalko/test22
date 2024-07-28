from dataclasses import dataclass
from sqlmodel import Field

from .base_model import BaseModel


@dataclass
class Sku(BaseModel, table=True):
    __tablename__ = 'os_sku'
    code: str = Field(index=True, unique=True)
