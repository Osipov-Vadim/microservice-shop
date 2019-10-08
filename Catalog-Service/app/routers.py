import hug
import json

from db import SQlAlchemySession
from models.item import Item
from dto import ItemDto, CItemDto
from falcon.status_codes import HTTP_400, HTTP_200


@hug.get('/api/warehouse/items')
def get_items(session: SQlAlchemySession):
    res = []
    for item in session.query(Item):
        res.append(ItemDto(
                id=item.id,
                name=item.name,
                amount=item.amount,
                price=item.price).dict())
    return res


@hug.get('/api/warehouse/items/{item_id}', output=hug.output_format.json)
def get_item_by_id(session: SQlAlchemySession, item_id: int):
    item = session.query(Item).\
        filter_by(id=item_id).first()
    if not item:
        return HTTP_400
    return ItemDto(
        id=item.id,
        name=item.name,
        amount=item.amount,
        price=item.price).dict()


@hug.put('/api/warehouse/items/{item_id}/addition/{amount}')
def add_existing_item(session: SQlAlchemySession, item_id: int, amount: int):
    item = session.query(Item).filter_by(id=item_id).first()
    item.amount = item.amount + amount
    session.flush()
    session.commit()
    return ItemDto(
        id=item.id,
        name=item.name,
        amount=item.amount,
        price=item.price).dict()


@hug.post("/api/warehouse/items")
def create_item(session: SQlAlchemySession, body):
    item = None
    try:
        item_dto = CItemDto(**body)
        item = Item(item_dto.name, item_dto.amount, item_dto.price)
    except ValueError as e:
        return e
    session.add(item)
    session.flush()
    session.commit()
    return ItemDto(
        id=item.id,
        name=item.name,
        amount=item.amount,
        price=item.price).dict()
