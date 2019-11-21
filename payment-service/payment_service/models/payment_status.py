import enum


class PaymentStatus(enum.Enum):
    PAYING = "PAYING"
    COMPLETED = "COMPLETED"
    RETURNED = "RETURNED"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
