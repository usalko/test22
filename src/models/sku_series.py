from dataclasses import dataclass

from .base_model import BaseModel


@dataclass
class SkuSeries(BaseModel, table=True):
    ...
