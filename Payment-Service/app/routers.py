import hug

from db import SQlAlchemySession
from models.PaymentInfo import PaymentInfo
from dto import CardAuthorizationInfo, UserDetailsDto, OrderDto


@hug.put('/orders/{order_id}/payment')
def perform_payment(session: SQlAlchemySession, order_id: int, body):
    item = None
    user_details = UserDetailsDto(**body)
    if user_details.cardAuthorizationInfo == CardAuthorizationInfo.UNAUTHORIZED:
        # TODO
        return

    if session.query(PaymentInfo).filter_by(order_id=order_id).first():
        # TODO
        return

    payment_info = PaymentInfo(order_id=order_id)
    session.add(payment_info)
    session.flush()
    session.commit()
    return OrderDto(id=payment_info.id).dict()

