import hug

from models.Item import Item
from db import SQlAlchemySession

# from falcon.status_codes import HTTP_400, HTTP_200


@hug.get('/api/warehouse/items')
def getItems(session: SQlAlchemySession):
    res = []
    for i in session.query(Item):
        res.append([i.id, i.name, i.amount, i.price])
    return res


@hug.get('/api/warehouse/items/{item_id}')
def getItemById(session: SQlAlchemySession, item_id: int):
    i = session.query(Item). \
        filter_by(id=item_id).first()
    return [i.id, i.name, i.amount, i.price]


@hug.put('/api/warehouse/items/{item_id}/addition/{amount}')
def addExistingItem(session: SQlAlchemySession, item_id: int, amount: int):
    item = session.query(Item).filter_by(id=item_id).first()
    item.amount = item.amount + amount
    session.flush()
    session.commit()

    # TODO
    return


@hug.post("/api/warehouse/items")
def createItem(session: SQlAlchemySession, body):
    name = body["name"]
    amount = body["amount"]
    price = body["price"]
    session.add(Item(name, amount, price))
    session.flush()
    session.commit()

    
    # TODO
    return 

# {
#     "name":"",
#     "amount": "100",
#     "price": "79.0"
# }

# {
#     "name":"Mandarin",
#     "amount": "300",
#     "price": "49.0"
# }
