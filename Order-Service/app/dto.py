from pydantic import BaseModel


class OrderDto(BaseModel):
    id: int
    status: str
    username: str
    totalCost: float
    totalAmount: int
    items: list


class ItemAdditionParametersDto(BaseModel):
    id: int
    amount: int
    username: str


class AddingItemDto(BaseModel):
    id: int


class ChangingStatusDto(BaseModel):
    id: int
    status: str
