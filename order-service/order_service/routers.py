from django.http import HttpResponse, HttpResponseServerError
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist

from microservices_api import api, dto, serializers
from .models import Order, OrderStatus, ReservedItem, is_possible_to_change_status


@require_http_methods(["GET"])
def get_orders(request):
    return JsonResponse(
        list(Order.objects.all().values()),
        safe=False
    )


@require_http_methods(["GET"])
def get_order_by_id(request, order_id=None):
    try:
        order = Order.objects.get(id=order_id)
    except ObjectDoesNotExist:
        return HttpResponseServerError("not order with id=%s" % order_id)
    return JsonResponse(
        order.to_dict()
    )


@require_http_methods(["POST"])
def create_order(request):
    # create items
    try:
        _data = serializers.parse_raw_data(request.body)
    except:
        # TODO
        return HttpResponseServerError("cant deserialize")

    serializer = serializers.ItemAdditionParametersSerializer(
        data=_data
    )
    if not serializer.is_valid():
        # TODO
        return HttpResponseServerError("cant parse item")

    a_param = serializer.save()
    order = Order(
        username=a_param.username,
        status=OrderStatus.COLLECTING.value
    )
    order.save()

    order_id = add_item_dto_to_order(a_param, order.id)
    return JsonResponse(
        order_id.dict()
    )


@require_http_methods(["POST"])
def add_item_to_order(request, order_id=None):
    try:
        _data = serializers.parse_raw_data(request.body)
    except:
        # TODO
        return HttpResponseServerError("cant deserialize")

    serializer = serializers.ItemAdditionParametersSerializer(
        data=_data
    )
    if not serializer.is_valid():
        # TODO
        return HttpResponseServerError("cant parse item")

    a_param = serializer.save()

    # TODO handle exc
    order_id_dto = add_item_dto_to_order(a_param, order_id)
    return JsonResponse(
        order_id_dto.dict()
    )


@require_http_methods(["PUT"])
def change_order_status(request, order_id: int, new_status: str):
    try:
        order = Order.objects.get(id=order_id)
    except ObjectDoesNotExist:
        return HttpResponseServerError("not order with id=%s" % order_id)
    if not is_possible_to_change_status(order.status, new_status):
        return HttpResponseServerError("cant change status from %s to %s" % order.status, new_status)
    # TODO RabbitMQ tasks
    if new_status == OrderStatus.PAID.value:
        pass
    elif new_status == OrderStatus.SHIPPING.value:
        pass
    elif new_status == OrderStatus.COMPLETE.value:
        pass
    elif new_status == OrderStatus.FAILED.value:
        pass
    elif new_status == OrderStatus.CANCELLED.value:
        pass

    order.status = new_status
    order.save()
    return JsonResponse(
        dto.OrderStats(
            id=order.id,
            status=order.status
        ).dict()
    )


def add_item_dto_to_order(addition_param: dto.ItemAdditionParameters, order_id: int):
    try:
        order = Order.objects.get(id=order_id)
    except ObjectDoesNotExist:
        return HttpResponseServerError("not order with id=%s" % order_id)

    # TODO request to warehouse: update totalCost, decrease amount
    item, status_code = api.dec_existing_item(addition_param.id, addition_param.amount)
    if status_code != 200:
        return HttpResponseServerError("kakaya-to oshibka c order_id=%s i item_id=%s" % order_id, addition_param.id)
    order.totalAmount += addition_param.amount
    order.totalCost += item.price * addition_param.amount
    order.save()
    r_item = ReservedItem(
        order_id_id=order.id,
        item_id=addition_param.id,
        amount=addition_param.amount
    )
    r_item.save()
    return dto.OrderId(id=order.id)
