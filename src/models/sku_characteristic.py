from dataclasses import dataclass

from sqlmodel import Relationship

from .base_model import BaseModel
from .invariants import *
from .sku import *


@dataclass
class SkuCharacteristics(BaseModel, table=True):
    '''
    # SKU characteristics (weight, volume)
        - sku_characteristics_sku:      Sku
        - sku_characteristics_weight:   float
        - sku_characteristics_volume:   float
        # _
    '''
    __tablename__ = 'os_sku_characteristics'
    sku_characteristics_sku: Sku = Relationship(back_populates='sku_characteristics')
    sku_characteristics_weight: float | None
    sku_characteristics_volume: float | None
