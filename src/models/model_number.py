from dataclasses import dataclass
from sqlmodel import Field

from .base_model import BaseModel


@dataclass
class SerialNumber(BaseModel, table=True):
    '''
    # Series of goods
    [Reference](https://en.wikipedia.org/wiki/Serial_number)
    '''
    __tablename__ = 'os_model_number'
    code: str = Field(index=True, unique=True)
