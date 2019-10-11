from statemachine import StateMachine, State
from models.OrderStatus import OrderStatus


class OrderStatusMachine(StateMachine):
    COLLECTING = State(OrderStatus.COLLECTING, initial=True)
    PAID = State(OrderStatus.PAID)
    FAILED = State(OrderStatus.FAILED)
    SHIPPING = State(OrderStatus.SHIPPING)
    CANCELLED = State(OrderStatus.CANCELLED)
    COMPLETE = State(OrderStatus.COMPLETE)

    paid = COLLECTING.to(PAID)
    failed = COLLECTING.to(FAILED)
    shipping = PAID.to(SHIPPING)
    cancelled = PAID.to(CANCELLED)
    complete = SHIPPING.to(COMPLETE)


def is_possible_to_change_status(cur_state: str, new_state: str):
    if cur_state == OrderStatus.COLLECTING and \
            (new_state == OrderStatus.PAID or new_state == OrderStatus.FAILED) or \
            cur_state == OrderStatus.PAID and \
            (new_state == OrderStatus.SHIPPING or new_state == OrderStatus.CANCELLED) or \
            cur_state == OrderStatus.SHIPPING and \
            (new_state == OrderStatus.COMPLETE):
        return True
    return False
