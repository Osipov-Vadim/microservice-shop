from collections import namedtuple
from pydantic import BaseModel


# ItemDto = namedtuple('ItemDto',
#                      ['id', 'name', 'amount', 'price'])
#
# CItemDTO = namedtuple('ItemDto',
#                      ['name', 'amount', 'price'])

class ItemDto(BaseModel):
    id: int
    name: str
    amount: int
    price: float


class CItemDto(BaseModel):
    name: str
    amount: int
    price: float

# class CItemDto(BaseModel):
#     def __init__(self, name, amount, price):
#         self.name = name
#         self.amount = amount
#         self.price = price
#
# def __repr__(self):
#     return """Item: {
#         "name": \"%s\",
#         "amount": \"%s\",
#         "price": \"%s\" """ % (self.name, self.amount, self.price)
