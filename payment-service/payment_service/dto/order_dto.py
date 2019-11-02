from pydantic import BaseModel


class OrderDto(BaseModel):
    id: int
