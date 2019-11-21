from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from payment_service.models.payment_info import PaymentInfo, PaymentStatus
from payment_service.dto.order_dto import OrderDto
from payment_service.dto.user_detail_dto import UserDetailsDto, CardAuthorizationInfo


@require_http_methods(["PUT"])
def perform_payment(request, order_id=None):
    # if request.method != 'PUT':
    #     return HttpResponseNotAllowed(['PUT'])
    user_details = UserDetailsDto(**json.loads(request.body))
    if user_details.cardAuthorizationInfo == CardAuthorizationInfo.UNAUTHORIZED:
        # TODO
        return HttpResponseServerError("hmm")

    if PaymentInfo.objects.filter(order_id=order_id).exists():
        # TODO
        return HttpResponseServerError("hmm")

    payment_info = PaymentInfo(order_id=order_id, paymentStatus=PaymentStatus.PAYING)
    payment_info.save()
    return JsonResponse(
        OrderDto(
            id=payment_info.id
        ).dict()
    )
