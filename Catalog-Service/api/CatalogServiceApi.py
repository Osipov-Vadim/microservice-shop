import requests
import json

from dto import ItemDto, CItemDto


def get_items():
    url = "http://hostname/api/warehouse/items"
    response = requests.get(url)
    return response.json()


def get_item_by_id(item_id: int):
    url = "http://hostname/api/warehouse/items/%s" % \
          item_id
    response = requests.get(url)
    return ItemDto(**response.json())


def add_existing_item(item_id: int, amount: int):
    url = "http://hostname/api/warehouse/items/%s/additional/%s" % (
        int,
        amount,
    )
    response = requests.get(url)
    return ItemDto(**response.json())


def create_items(c_item_dto: CItemDto):
    url = "http://hostname/api/warehouse/items"
    response = requests.post(url, json.dumps(CItemDto.dict()))
    return ItemDto(**response.json())