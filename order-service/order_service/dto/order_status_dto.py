from pydantic import BaseModel


class OrderStatusDto(BaseModel):
    id: int
    status: str
