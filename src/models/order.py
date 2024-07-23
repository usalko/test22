from dataclasses import dataclass

from .base_model import BaseModel


@dataclass
class Order(BaseModel, table=True):
    ...