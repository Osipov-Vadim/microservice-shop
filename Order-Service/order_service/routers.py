from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError
from django.http.response import JsonResponse
import json

from order_service.models.order import Order, OrderStatus
from order_service.models.reserved_item import ReservedItem
from order_service.models.traffic_light_machine import is_possible_to_change_status

from order_service.dto.order_dto import OrderDto
from order_service.dto.item_addition_parameters_dto import ItemAdditionParametersDto
from order_service.dto.order_status_dto import OrderStatusDto
from order_service.dto.order_id_dto import OrderIdDto


def get_orders(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    return JsonResponse(list(Order.objects.all().values()), safe=False)


def get_order_by_id(request, order_id=None):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    return JsonResponse(Order.objects.get(id=order_id).to_dict())


def create_order(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    addition_dto = None
    try:
        addition_dto = ItemAdditionParametersDto(**json.loads(request.body))
    except ValueError as e:
        # TODO
        return HttpResponseServerError("hmm")
    order = Order(
        username=addition_dto.username,
        status=OrderStatus.COLLECTING.value
    )
    order.save()
    # TODO handle exc
    order_id_dto = add_item_dto_to_order(addition_dto, order.id)
    return JsonResponse(order_id_dto.dict())


def add_item_to_order(request, order_id=None):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    addition_dto = None
    try:
        addition_dto = ItemAdditionParametersDto(**json.loads(request.body))
    except ValueError as e:
        # TODO
        return HttpResponseServerError("hmm")
    # TODO handle exc
    order_id_dto = add_item_dto_to_order(addition_dto, order_id)
    return JsonResponse(order_id_dto.dict())


def change_order_status(request, order_id=None, new_status=None):
    if request.method != 'PUT':
        return HttpResponseNotAllowed(['PUT'])
    order = Order.objects.get(id=order_id)
    if not is_possible_to_change_status(order.status, new_status):
        # TODO change return
        return HttpResponseServerError("hmm")
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
    order.save()
    return JsonResponse(
        OrderStatusDto(
            id=order.id,
            status=order.status
        ).dict()
    )


def add_item_dto_to_order(addition_dto: ItemAdditionParametersDto, order_id: int):
    # TODO request to warehouse: update totalCost, decrease amount
    order = Order.objects.get(id=order_id)
    order.totalAmount += addition_dto.amount
    r_item = ReservedItem(
        order_id_id=order.id,
        item_id=addition_dto.id,
        amount=addition_dto.amount
    )
    r_item.save()
    return OrderIdDto(id=order.id)
