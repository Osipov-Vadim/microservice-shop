import enum


class OrderStatus(enum.Enum):
    COLLECTING = "COLLECTING"
    PAID = "PAID"
    FAILED = "FAILED"
    SHIPPING = "SHIPPING"
    CANCELLED = "CANCELLED"
    COMPLETE = "COMPLETE"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
