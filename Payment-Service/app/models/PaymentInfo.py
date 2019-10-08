import enum

from models.base import Base
from sqlalchemy import Column, Integer, Enum, String


class PaymentStatus(enum.Enum):
    PAYING = "PAYING"
    COMPLETED = "COMPLETED"
    RETURNED = "RETURNED"


class PaymentInfo(Base):
    __tablename__ = "pay_info"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, unique=True)
    paymentStatus = Column(Enum(PaymentStatus))

    def __init__(self, order_id):
        self.order_id = order_id
        self.paymentStatus = PaymentStatus.PAYING

    def __repr__(self):
        return """PaymentInfo: {
            "id": \"%s\",
            "order_id": \"%s\",
            "paymentStatus": \"%s\" }""" % (
            self.id,
            self.order_id,
            self.paymentStatus
        )
