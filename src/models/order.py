from dataclasses import dataclass

from sqlmodel import Field

from .base_model import BaseModel


@dataclass
class Order(BaseModel, table=True):
    __tablename__ = 'os_order'
    number: str = Field(index=True, unique=True)
