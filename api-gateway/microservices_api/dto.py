import enum
from pydantic import BaseModel


class ItemDto(BaseModel):
    id: int
    name: str
    amount: int
    price: float


class CItemDto(BaseModel):
    name: str
    amount: int
    price: float


class ItemAdditionParametersDto(BaseModel):
    id: int
    amount: int
    username: str


class OrderDto(BaseModel):
    id: int
    status: str
    username: str
    totalCost: float
    totalAmount: int


class OrderIdDto(BaseModel):
    id: int


class OrderStatusDto(BaseModel):
    id: int
    status: str


class OrderStatus(enum.Enum):
    COLLECTING = "COLLECTING"
    PAID = "PAID"
    FAILED = "FAILED"
    SHIPPING = "SHIPPING"
    CANCELLED = "CANCELLED"
    COMPLETE = "COMPLETE"


class CardAuthorizationInfo(enum.Enum):
    AUTHORIZED = "AUTHORIZED"
    UNAUTHORIZED = "UNAUTHORIZED"


class UserDetailsDto(BaseModel):
    username: str
    cardAuthorizationInfo: CardAuthorizationInfo