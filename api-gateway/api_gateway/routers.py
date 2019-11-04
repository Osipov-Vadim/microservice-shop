from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse


@api_view(http_method_names=["GET", "POST"])
def items_handler(request):
    if request.method == "GET":
        return HttpResponse("<h1>Get items<\h1>")
    elif request.method == "POST":
        return HttpResponse("<h1>Create item<\h1>")


@api_view(http_method_names=["GET"])
def get_item_by_id(request, item_id: int):
    return HttpResponse("<h1>Get item by id<\h1>")


@api_view(http_method_names=["PUT"])
def add_existing_item(request, item_id: int, amount: int):
    return HttpResponse("<h1>Add existing item<\h1>")


@api_view(http_method_names=["PUT"])
def dec_existing_item(request, item_id: int, amount: int):
    return HttpResponse("<h1>Dec existing item<\h1>")


@api_view(http_method_names=["GET"])
def get_orders(request):
    return HttpResponse("<h1>Get orders<\h1>")


@api_view(http_method_names=["GET"])
def get_order_by_id(request, order_id: int):
    return HttpResponse("<h1>Get order by id<\h1>")


@api_view(http_method_names=["POST"])
def create_order(request):
    return HttpResponse("<h1>Create order<\h1>")


@api_view(http_method_names=["POST"])
def add_item_to_order(request, order_id: int):
    return HttpResponse("<h1>Add item to order<\h1>")


@api_view(http_method_names=["PUT"])
def change_order_status(request, order_id: int, new_status: str):
    return HttpResponse("<h1>Change order status<\h1>")


@api_view(http_method_names=["PUT"])
def perform_payment(request, order_id: int):
    return HttpResponse("<h1>Perform payment<\h1>")
