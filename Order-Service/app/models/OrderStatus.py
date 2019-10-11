import enum


class OrderStatus(enum.Enum):
    COLLECTING = "COLLECTING"
    PAID = "PAID"
    FAILED = "FAILED"
    SHIPPING = "SHIPPING"
    CANCELLED = "CANCELLED"
    COMPLETE = "COMPLETE"
