from dataclasses import dataclass
from sqlmodel import Field

from .base_model import BaseModel


@dataclass
class ModelNumber(BaseModel, table=True):
    code: str = Field(index=True, unique=True)
