import requests
import json
import enum
from microservices_api import dto, serializers


# TODO Integrate Discovery service
class ServiceNames(enum.Enum):
    CatalogService = "CATALOG"
    OrderService = "ORDER"
    PaymentService = "PAYMENT"


# TODO Integrate Discovery service
def get_service_address(service_name: ServiceNames):
    # order-service:80
    if service_name == ServiceNames.CatalogService:
        return "127.0.0.1:9003"
    elif service_name == ServiceNames.OrderService:
        return "127.0.0.1:9002"
    elif service_name == ServiceNames.PaymentService:
        return "127.0.0.1:9001"
    else:
        return None


# Catalog service api
def get_items(do_not_create=False):
    address = get_service_address(ServiceNames.CatalogService)
    request_url = "http://%s/items/" % (
        address
    )
    response = requests.get(request_url)

    if do_not_create is True:
        return response.text, response.status_code

    # TODO check status code
    # if response.status_code == 500:
    #     return response.text

    return "response.json()"


def create_item(data, raw_data=False, do_not_create=False):
    address = get_service_address(ServiceNames.CatalogService)
    request_url = "http://%s/items/" % (
        address
    )
    _data = data if raw_data is True else serializers.get_raw_data(data)
    response = requests.post(request_url, data=_data)
    if do_not_create is True:
        return response.text, response.status_code

    # TODO
    return "dto.Item(**response.json())"


def get_item_by_id(item_id: int, do_not_create=False):
    address = get_service_address(ServiceNames.CatalogService)
    request_url = "http://%s/items/%s/" % (
        address,
        item_id
    )
    response = requests.get(request_url)
    if do_not_create is True:
        return response.text, response.status_code

    # TODO
    return "dto.Item(**response.json())"


def add_existing_item(item_id: int, amount: int, do_not_create=False):
    address = get_service_address(ServiceNames.CatalogService)
    request_url = "http://%s/items/%s/addition/%s/" % (
        address,
        item_id,
        amount,
    )
    response = requests.put(request_url)
    if do_not_create is True:
        return response.text, response.status_code

    # TODO
    return serializers.ItemSerializer.create(validated_data=response.text), response.status_code


def dec_existing_item(item_id: int, amount: int,  do_not_create=False):
    address = get_service_address(ServiceNames.CatalogService)
    request_url = "http://%s/items/%s/decrease/%s/" % (
        address,
        item_id,
        amount,
    )
    response = requests.put(request_url)
    if do_not_create is True:
        return response.text, response.status_code

    # TODO
    return serializers.ItemSerializer.create(validated_data=response.text), response.status_code


# Order service api
def get_orders(do_not_create=False):
    address = get_service_address(ServiceNames.OrderService)
    request_url = "http://%s/orders/" % (
        address
    )
    response = requests.get(request_url)
    if do_not_create is True:
        return response.text, response.status_code

    # TODO
    return "response.json()"


def get_order_by_id(order_id: int, do_not_create=False):
    address = get_service_address(ServiceNames.OrderService)
    request_url = "http://%s/orders/%s/" % (
        address,
        order_id
    )
    response = requests.get(request_url)
    if do_not_create is True:
        return response.text, response.status_code

    # TODO
    return "dto.Order(**response.json())"


def create_order(data, raw_data=False, do_not_create=False):
    address = get_service_address(ServiceNames.OrderService)
    request_url = "http://%s/orders/null/item/" % (
        address
    )
    _data = data if raw_data is True else serializers.get_raw_data(data)
    response = requests.post(request_url, data=_data)
    if do_not_create is True:
        return response.text, response.status_code

    # TODO
    return "dto.OrderId(**response.json())"


def add_item_to_order(order_id: int, data, raw_data=False, do_not_create=False):
    address = get_service_address(ServiceNames.OrderService)
    request_url = "http://%s/orders/%s/item/" % (
        address,
        order_id
    )
    _data = data if raw_data is True else serializers.get_raw_data(data)
    response = requests.post(request_url, data=_data)
    if do_not_create is True:
        return response.text, response.status_code

    # TODO
    return "dto.OrderId(**response.json())"


def change_order_status(order_id: int, status: str, do_not_create=False):
    address = get_service_address(ServiceNames.OrderService)
    request_url = "http://%s/orders/%s/status/%s/" % (
        address,
        order_id,
        status
    )
    response = requests.put(request_url)
    if do_not_create is True:
        return response.text, response.status_code

    # TODO
    return "dto.OrderStatus(**response.json())"


# Payment service api
def perform_payment(order_id: int, data, raw_data=False, do_not_create=False):
    address = get_service_address(ServiceNames.PaymentService)
    request_url = "http://%s/orders/%s/payment/" % (
        address,
        order_id
    )
    _data = data if raw_data is True else serializers.get_raw_data(data)
    response = requests.put(request_url, data=_data)
    if do_not_create is True:
        return response.text, response.status_code

    # TODO check status code
    # if response.status_code == 500:
    #     return response.text

    return serializers.OrderIdSerializer.create(validated_data=response.text)
