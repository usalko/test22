from dataclasses import dataclass

from .base_model import BaseModel


@dataclass
class Sku(BaseModel, table=True):
    ...