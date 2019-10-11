from models.base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.Order import Order


class ReservedItem(Base):
    __tablename__ = "reserved_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    item_id = Column(Integer)
    amount = Column(Integer)

    order = relationship("Order", backref="items")

    def __init__(self, order_id, item_id, amount):
        self.order_id = order_id
        self.item_id = item_id
        self.amount = amount
