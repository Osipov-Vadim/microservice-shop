import requests
import json
import enum
from microservices_api.dto import *


# TODO Integrate Discovery service
class ServiceNames(enum.Enum):
    CatalogService = "CATALOG"
    OrderService = "ORDER"
    PaymentService = "PAYMENT"


# TODO Integrate Discovery service
def get_service_address(service_name: ServiceNames):
    if service_name == ServiceNames.CatalogService:
        return "catalog-service:80"
    elif service_name == ServiceNames.OrderService:
        return "order-service:80"
    elif service_name == ServiceNames.PaymentService:
        return "payment-service:80"
    else:
        return None


# Catalog service api
def get_items():
    address = get_service_address(ServiceNames.CatalogService)
    request_url = "http://%s/items/" % (
        address
    )
    response = requests.get(request_url)
    return response.json()


def get_item_by_id(item_id: int):
    address = get_service_address(ServiceNames.CatalogService)
    request_url = "http://%s/items/%s/" % (
        address,
        item_id
    )
    response = requests.get(request_url)
    return ItemDto(**response.json())


def create_item(item: CItemDto):
    address = get_service_address(ServiceNames.CatalogService)
    request_url = "http://%s/items/" % (
        address
    )
    response = requests.post(request_url, json.dumps(item.dict()))
    return ItemDto(**response.json())


def add_existing_item(item_id: int, amount: int):
    address = get_service_address(ServiceNames.CatalogService)
    request_url = "http://%s/items/%s/addition/%s/" % (
        address,
        item_id,
        amount,
    )
    response = requests.put(request_url)
    return ItemDto(**response.json())


def dec_existing_item(item_id: int, amount: int):
    address = get_service_address(ServiceNames.CatalogService)
    request_url = "http://%s/items/%s/decrease/%s/" % (
        address,
        item_id,
        amount,
    )
    response = requests.put(request_url)
    return ItemDto(**response.json())


# Order service api
def get_orders():
    address = get_service_address(ServiceNames.OrderService)
    request_url = "http://%s/orders/" % (
        address
    )
    response = requests.get(request_url)

    return response.json()


def get_order_by_id(order_id: int):
    address = get_service_address(ServiceNames.OrderService)
    request_url = "http://%s/orders/%s/" % (
        address,
        order_id
    )
    response = requests.get(request_url)
    return OrderDto(**response.json())


def create_order(item: ItemAdditionParametersDto):
    address = get_service_address(ServiceNames.OrderService)
    request_url = "http://%s/orders/null/item/" % (
        address
    )
    response = requests.post(request_url, json.dumps(item.dict()))
    return OrderIdDto(**response.json())


def add_item_to_order(order_id: int, item: ItemAdditionParametersDto):
    address = get_service_address(ServiceNames.OrderService)
    request_url = "http://%s/orders/%s/item/" % (
        address,
        order_id
    )
    response = requests.post(request_url, json.dumps(item.dict()))
    return OrderIdDto(**response.json())


def change_order_status(order_id: int, status: str):
    address = get_service_address(ServiceNames.OrderService)
    request_url = "http://%s/orders/%s/status/%s/" % (
        address,
        order_id,
        status
    )
    response = requests.put(request_url)
    return OrderStatusDto(**response.json())


# Payment service api
def perform_payment(order_id: int, user_detail: CardAuthorizationInfo):
    address = get_service_address(ServiceNames.PaymentService)
    request_url = "http://%s/order/%s/payment/" % (
        address,
        order_id
    )
    response = requests.put(request_url, json.dumps(user_detail.dict()))
    return OrderDto(**response.json())
