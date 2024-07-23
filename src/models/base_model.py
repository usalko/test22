from sqlmodel import Field, SQLModel


class BaseModel(SQLModel):
    id: int | None = Field(
        default=None,
        primary_key=True,
    )
