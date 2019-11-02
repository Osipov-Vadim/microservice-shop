from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError
from django.http.response import JsonResponse
import json

from django.http import HttpResponseRedirect

from catalog_service.models.item import Item
from catalog_service.dto.item_dto import ItemDto
from catalog_service.dto.citem_dto import CItemDto


def items_handler(request):
    if request.method == 'GET':
        # get all items
        return JsonResponse(list(Item.objects.all().values()), safe=False)
        # return HttpResponse([i.to_dict() for i in Item.objects.all()])
    elif request.method == 'POST':
        # create items
        item = None
        try:
            item_dto = CItemDto(**json.loads(request.body))
            item = Item(
                name=item_dto.name,
                amount=item_dto.amount,
                price=item_dto.price)
            item.save()
        except ValueError as e:
            return HttpResponseServerError("hmm")
        return JsonResponse(ItemDto(
            id=item.id,
            name=item.name,
            amount=item.amount,
            price=item.price).dict())
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def get_item_by_id(request, item_id=None):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    return JsonResponse(Item.objects.get(id=item_id).to_dict())


def add_existing_item(request, item_id=None, amount=0):
    if request.method != 'PUT':
        return HttpResponseNotAllowed(['PUT'])
    item = Item.objects.get(id=item_id)
    item.amount += amount
    item.save()
    return JsonResponse(ItemDto(
        id=item.id,
        name=item.name,
        amount=item.amount,
        price=item.price).dict())


def dec_existing_item(request, item_id=None, amount=0):
    if request.method != 'PUT':
        return HttpResponseNotAllowed(['PUT'])
    item = Item.objects.get(id=item_id)
    item.amount -= amount
    item.save()
    return JsonResponse(ItemDto(
        id=item.id,
        name=item.name,
        amount=item.amount,
        price=item.price).dict())
