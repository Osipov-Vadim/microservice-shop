from pydantic import BaseModel


class ItemDto(BaseModel):
    id: int
    name: str
    amount: int
    price: float
