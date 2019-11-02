from pydantic import BaseModel


class CItemDto(BaseModel):
    name: str
    amount: int
    price: float
