import hug

from db import SQlAlchemySession
from models.Order import Order
from models.OrderStatus import OrderStatus
from models.ReservedItem import ReservedItem
from dto import OrderDto, ItemAdditionParametersDto, AddingItemDto, ChangingStatusDto
from models.TrafficLightMachine import is_possible_to_change_status


@hug.get('/orders')
def get_orders(session: SQlAlchemySession):
    res = []
    for order in session.query(Order):
        res.append(OrderDto(
            id=order.id,
            status=order.status,
            username=order.username,
            totalCost=order.totalCost,
            totalAmount=order.totalAmount,
            items=list([])).dict())
    return res


@hug.get('/orders/{order_id}')
def get_order_by_id(session: SQlAlchemySession, order_id: int):
    order = session.query(Order). \
        filter_by(id=order_id).first()
    if not order:
        return
    return OrderDto(
        id=order.id,
        status=order.status,
        username=order.username,
        totalCost=order.totalCost,
        totalAmount=order.totalAmount,
        items=list([])).dict()


@hug.post("/orders/null/item")
def create_order(session: SQlAlchemySession, body):
    addition_dto = None
    try:
        addition_dto = ItemAdditionParametersDto(**body)
    except ValueError as e:
        # TODO
        return e
    order = Order(addition_dto.username)
    session.add(order)
    r_item = ReservedItem(order.id, addition_dto.id, addition_dto.amount)
    session.add(r_item)
    session.flush()
    session.commit()
    return AddingItemDto(
        id=order.id
    ).dict()


@hug.post("/orders/{order_id}/item")
def add_item_to_order(session: SQlAlchemySession, order_id: int, body):
    addition_dto = None
    try:
        addition_dto = ItemAdditionParametersDto(**body)
    except ValueError as e:
        return e
    try:
        order = session.query(Order).filter_by(id=order_id).first()
        if not order:
            # TODO id not found
            return
    except ValueError as e:
        # TODO Bad value
        return e
    r_item = ReservedItem(order_id, addition_dto.id, addition_dto.amount)
    session.add(r_item)
    session.flush()
    session.commit()
    return AddingItemDto(
        id=order_id
    ).dict()


@hug.put('/orders/{order_id}/status/{new_status}')
def change_order_status(session: SQlAlchemySession, order_id: int, new_status: str):
    order = session.query(Order).filter_by(id=order_id).first()
    if not is_possible_to_change_status(order.status, new_status):
        # TODO change return
        return
    # TODO
    if new_status == OrderStatus.PAID:
        pass
    elif new_status == OrderStatus.SHIPPING:
        pass
    elif new_status == OrderStatus.COMPLETE:
        pass
    elif new_status == OrderStatus.FAILED:
        pass
    elif new_status == OrderStatus.CANCELLED:
        pass

    order.status = new_status
    session.flush()
    session.commit()
    return ChangingStatusDto(
        id=order_id,
        status=order.status
    ).dict()
