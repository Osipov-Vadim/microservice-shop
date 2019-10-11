from statemachine import StateMachine, State
from models.OrderStatus import OrderStatus as OrS


class OrderStatusMachine(StateMachine):
    COLLECTING = State(OrS.COLLECTING, initial=True)
    PAID = State(OrS.PAID)
    FAILED = State(OrS.FAILED)
    SHIPPING = State(OrS.SHIPPING)
    CANCELLED = State(OrS.CANCELLED)
    COMPLETE = State(OrS.COMPLETE)

    paid = COLLECTING.to(PAID)
    failed = COLLECTING.to(FAILED)
    shipping = PAID.to(SHIPPING)
    cancelled = PAID.to(CANCELLED)
    complete = SHIPPING.to(COMPLETE)


def is_possible_to_change_status(cur_state: str, new_state: str):
    if cur_state == OrS.COLLECTING.value and \
            (new_state == OrS.PAID.value or new_state == OrS.FAILED.value) or \
            cur_state == OrS.PAID.value and \
            (new_state == OrS.SHIPPING.value or new_state == OrS.CANCELLED.value) or \
            cur_state == OrS.SHIPPING.value and \
            (new_state == OrS.COMPLETE.value):
        return True
    return False
