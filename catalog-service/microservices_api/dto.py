from enum import Enum
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    amount: int
    price: float


class CItem(BaseModel):
    name: str
    amount: int
    price: float


class ItemAdditionParameters(BaseModel):
    id: int
    amount: int
    username: str


class Order(BaseModel):
    id: int
    status: str
    username: str
    totalCost: float
    totalAmount: int


class OrderId(BaseModel):
    id: int


class OrderStats(BaseModel):
    id: int
    status: str


class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class OrderStatus(ExtendedEnum):
    COLLECTING = "COLLECTING"
    PAID = "PAID"
    FAILED = "FAILED"
    SHIPPING = "SHIPPING"
    CANCELLED = "CANCELLED"
    COMPLETE = "COMPLETE"


class CardAuthorizationInfo(ExtendedEnum):
    AUTHORIZED = "AUTHORIZED"
    UNAUTHORIZED = "UNAUTHORIZED"


class UserDetails(BaseModel):
    username: str
    cardAuthorizationInfo: str
