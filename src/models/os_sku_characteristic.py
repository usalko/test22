from dataclasses import dataclass

from sqlalchemy import Column, Float
from sqlalchemy.orm import relationship

from .base_model import BaseModel
from .invariants import *
from .os_sku import *


@dataclass
class OsSkuCharacteristics(BaseModel):
    '''
    # SKU characteristics (weight, volume)
        - sku_characteristics_sku:      Sku
        - sku_characteristics_weight:   float
        - sku_characteristics_volume:   float
        # _
    '''
    sku_characteristics_sku: Mapped[OsSku] = relationship(
        OsSku,
    )
    sku_characteristics_weight: float | None = Column(
        Float,
    )
    sku_characteristics_volume: float | None = Column(
        Float,
    )
