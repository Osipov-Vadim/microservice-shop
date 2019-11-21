from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from microservices_api import api, dto
import json


@api_view(http_method_names=["GET", "POST"])
@require_http_methods(["GET", "POST"])
def items_handler(request):
    if request.method == "GET":
        return JsonResponse(
            api.get_items(),
            safe=False
        )
    elif request.method == "POST":
        return JsonResponse(
            api.create_item(
                dto.CItemDto(**json.loads(request.body))
            ).dict()
        )


@api_view(http_method_names=["GET"])
@require_http_methods(["GET"])
def get_item_by_id(request, item_id: int):
    return JsonResponse(
        api.get_item_by_id(
            item_id
        ).dict()
    )


@api_view(http_method_names=["PUT"])
@require_http_methods(["PUT"])
def add_existing_item(request, item_id: int, amount: int):
    return JsonResponse(
        api.add_existing_item(
            item_id,
            amount
        ).dict()
    )


@api_view(http_method_names=["PUT"])
@require_http_methods(["PUT"])
def dec_existing_item(request, item_id: int, amount: int):
    return JsonResponse(
        api.dec_existing_item(
            item_id,
            amount
        ).dict()
    )


@api_view(http_method_names=["GET"])
@require_http_methods(["GET"])
def get_orders(request):
    return JsonResponse(
        api.get_orders(),
        safe=False
    )


@api_view(http_method_names=["GET"])
@require_http_methods(["GET"])
def get_order_by_id(request, order_id: int):
    return JsonResponse(
        api.get_order_by_id(
            order_id
        ).dict()
    )


@api_view(http_method_names=["POST"])
@require_http_methods(["POST"])
def create_order(request):
    return JsonResponse(
        api.create_order(
            dto.ItemAdditionParametersDto(
                **json.loads(request.body)
            )
        ).dict()
    )


@api_view(http_method_names=["POST"])
@require_http_methods(["POST"])
def add_item_to_order(request, order_id: int):
    return JsonResponse(
        api.add_item_to_order(
            order_id,
            dto.ItemAdditionParametersDto(
                **json.loads(request.body)
            )
        ).dict()
    )


@api_view(http_method_names=["PUT"])
@require_http_methods(["PUT"])
def change_order_status(request, order_id: int, new_status: str):
    return JsonResponse(
        api.change_order_status(
            order_id,
            new_status
        ).dict()
    )


@api_view(http_method_names=["PUT"])
@require_http_methods(["PUT"])
def perform_payment(request, order_id: int):
    return JsonResponse(
        api.perform_payment(
            order_id,
            dto.UserDetailsDto(
                **json.loads(request.body)
            )
        ).dict()
    )
