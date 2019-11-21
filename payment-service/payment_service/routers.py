from django.http.response import JsonResponse, HttpResponse, HttpResponseServerError
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist

from microservices_api import dto, serializers

from payment_service.models import PaymentStatus, PaymentInfo


@require_http_methods(["PUT"])
def perform_payment(request, order_id: int):
    try:
        _data = serializers.parse_raw_data(request.body)
    except:
        # TODO
        return HttpResponseServerError("cant deserialize")

    serializer = serializers.UserDetailsSerializer(
        data=_data
    )
    if not serializer.is_valid():
        # TODO
        return HttpResponseServerError("cant parse user detail")

    user_details = serializer.save()
    if user_details.cardAuthorizationInfo != dto.CardAuthorizationInfo.AUTHORIZED.value:
        # TODO
        return HttpResponseServerError("un auth")

    if PaymentInfo.objects.filter(order_id=order_id).exists():
        # TODO
        return HttpResponseServerError("payment exist")

    # TODO need to check order id status and check existing order id in order-service
    payment_info = PaymentInfo(order_id=order_id, paymentStatus=PaymentStatus.PAYING)
    payment_info.save()

    return JsonResponse(
        dto.OrderId(
            id=payment_info.id
        ).dict()
    )


@require_http_methods(["PUT"])
def cancel_payment(request, payment_id: int):
    try:
        payment_info = PaymentInfo.objects.get(id=payment_id)
    except ObjectDoesNotExist:
        return HttpResponseServerError("not payment_info with id=%s" % payment_id)

    if payment_info.paymentStatus != PaymentStatus.PAYING.value:
        return HttpResponseServerError("payment status with id=%s is %s" % payment_id, payment_info.paymentStatus)

    # TODO change order status
    # TODO return items to warehouse
    payment_info.paymentStatus = PaymentStatus.RETURNED
    payment_info.save()
    return JsonResponse(
        payment_info.to_dict()
    )


@require_http_methods(["PUT"])
def payment_paid(request, payment_id: int):
    try:
        payment_info = PaymentInfo.objects.get(id=payment_id)
    except ObjectDoesNotExist:
        return HttpResponseServerError("not payment_info with id=%s" % payment_id)

    if payment_info.paymentStatus != PaymentStatus.PAYING.value:
        return HttpResponseServerError("payment status with id=%s is %s" % payment_id, payment_info.paymentStatus)

    # TODO return items to warehouse
    payment_info.paymentStatus = PaymentStatus.COMPLETED
    payment_info.save()
    return JsonResponse(
        payment_info.to_dict()
    )
