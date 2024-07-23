from dataclasses import dataclass

from sqlmodel import Field

from .base_model import BaseModel


@dataclass
class Order(BaseModel, table=True):
    number: str = Field(index=True, unique=True)
