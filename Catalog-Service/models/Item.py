from models.base import Base
from sqlalchemy import Column, Integer, Text, String, Float

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Integer)
    price = Column(Float)

    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def __repr__(self):
        return "Item: {     \
            name: '%s',     \
            amount: '%s',   \
            price: '%s'" % (self.name, self.amount, self.price)
