from pydantic import BaseModel, ConfigDict


class Order(BaseModel):

    model_config: ConfigDict = ConfigDict(from_attributes=True)

    id: int
    order_number: str
