from dataclasses import dataclass

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel
from .os_sku import *


@dataclass
class OsSkuCharacteristics(BaseModel):
    '''
    # SKU characteristics (weight, volume)
        - sku_characteristics_sku           :: Sku
        - sku_characteristics_weight:       :: float
        - sku_characteristics_volume:       :: float
        # _
    '''
    sku_characteristics_sku_id = mapped_column(Integer, ForeignKey('os_sku.id'))
    sku_characteristics_sku: Mapped[OsSku] = relationship(
        OsSku,
        foreign_keys='[OsSkuCharacteristics.sku_characteristics_sku_id]',
    )

    sku_characteristics_weight: Mapped[float | None] = mapped_column()
    sku_characteristics_volume: Mapped[float | None] = mapped_column()
