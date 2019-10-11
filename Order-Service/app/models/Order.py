from models.base import Base
from sqlalchemy import Column, Integer, String, Float, Enum
from models.OrderStatus import OrderStatus


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    status = Column(Enum(OrderStatus))
    totalCost = Column(Float)
    totalAmount = Column(int)

    def __init__(self, username,):
        self.username = username
        self.status = OrderStatus.COLLECTING
        self.totalCost = 0.0
        self.totalAmount = 0
