from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from microservices_api import api, dto, serializers
import json


@api_view(http_method_names=["GET", "POST"])
@require_http_methods(["GET", "POST"])
def items_handler(request):
    if request.method == "GET":
        res, status_code = api.get_items(do_not_create=True)
        return HttpResponse(res, status=status_code)
    elif request.method == "POST":
        res, status_code = api.create_item(
            data=request.body,
            raw_data=True,
            do_not_create=True
        )
        return HttpResponse(res, status=status_code)


@api_view(http_method_names=["GET"])
@require_http_methods(["GET"])
def get_item_by_id(request, item_id: int):
    res, status_code = api.get_item_by_id(
        item_id=item_id,
        do_not_create=True
    )
    return HttpResponse(res, status=status_code)


@api_view(http_method_names=["PUT"])
@require_http_methods(["PUT"])
def add_existing_item(request, item_id: int, amount: int):
    res, status_code = api.add_existing_item(
        item_id=item_id,
        amount=amount,
        do_not_create=True
    )
    return HttpResponse(res, status=status_code)


@api_view(http_method_names=["PUT"])
@require_http_methods(["PUT"])
def dec_existing_item(request, item_id: int, amount: int):
    res, status_code = api.dec_existing_item(
        item_id=item_id,
        amount=amount,
        do_not_create=True
    )
    return HttpResponse(res, status=status_code)


@api_view(http_method_names=["GET"])
@require_http_methods(["GET"])
def get_orders(request):
    res, status_code = api.get_orders(
        do_not_create=True
    )
    return HttpResponse(res, status=status_code)


@api_view(http_method_names=["GET"])
@require_http_methods(["GET"])
def get_order_by_id(request, order_id: int):
    res, status_code = api.get_order_by_id(
        order_id=order_id,
        do_not_create=True
    )
    return HttpResponse(res, status=status_code)


@api_view(http_method_names=["POST"])
@require_http_methods(["POST"])
def create_order(request):
    res, status_code = api.create_order(
        data=request.body,
        raw_data=True,
        do_not_create=True
    )
    return HttpResponse(res, status=status_code)


@api_view(http_method_names=["POST"])
@require_http_methods(["POST"])
def add_item_to_order(request, order_id: int):
    res, status_code = api.add_item_to_order(
        order_id=order_id,
        data=request.body,
        raw_data=True,
        do_not_create=True
    )
    return HttpResponse(res, status=status_code)


@api_view(http_method_names=["PUT"])
@require_http_methods(["PUT"])
def change_order_status(request, order_id: int, new_status: str):
    res, status_code = api.change_order_status(
        order_id=order_id,
        status=new_status,
        do_not_create=True
    )
    return HttpResponse(res, status=status_code)


@api_view(http_method_names=["PUT"])
@require_http_methods(["PUT"])
def perform_payment(request, order_id: int):
    # check data
    # serializer = serializers.UserDetailsSerializer(
    #     data=data
    # )
    # serializer.is_valid(raise_exception=True)
    # print(data)
    res, status_code = api.perform_payment(
        order_id=order_id,
        data=request.body,
        raw_data=True,
        do_not_create=True
    )
    return HttpResponse(res, status=status_code)

    # return JsonResponse(
    #     api.perform_payment(
    #         order_id,
    #         dto.UserDetails(
    #             **json.loads(request.body)
    #         )
    #     ).dict()
    # )
