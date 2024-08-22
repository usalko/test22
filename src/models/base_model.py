# src/models/base_model.py

from itertools import pairwise

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Mapped, mapped_column


def _upper_case_chars(x):
    return [0] + [i for i in range(len(x)) if x[i].isupper()] + [len(x)]


def CAMEL_TO_LOWER_CASE_SNAKE(x):
    return '_'.join([x[i].lower() + x[i+1: j] for i, j in pairwise(_upper_case_chars(x)) if j > i])


@as_declarative()
class BaseModel:
    '''
        # Base class for all application entities   
            - id        :: int
    '''
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        l: str = ''.isupper()
        return CAMEL_TO_LOWER_CASE_SNAKE(cls.__name__)

    id: Mapped[int | None] = mapped_column(primary_key=True)
