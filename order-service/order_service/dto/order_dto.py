from pydantic import BaseModel


class OrderDto(BaseModel):
    id: int
    status: str
    username: str
    totalCost: float
    totalAmount: int
