from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist

from catalog_service.models.item import Item
from microservices_api import dto, serializers


@require_http_methods(["GET", "POST"])
def items_handler(request):
    if request.method == 'GET':
        # get all items
        return JsonResponse(list(Item.objects.all().values()), safe=False)
        # return HttpResponse([i.to_dict() for i in Item.objects.all()])
    elif request.method == 'POST':
        # create items
        try:
            _data = serializers.parse_raw_data(request.body)
        except:
            # TODO
            return HttpResponseServerError("cant deserialize")

        serializer = serializers.CItemSerializer(
            data=_data
        )
        if not serializer.is_valid():
            # TODO
            return HttpResponseServerError("cant parse item")

        c_item = serializer.save()
        item = Item(
            name=c_item.name,
            amount=c_item.amount,
            price=c_item.price)
        item.save()

        return JsonResponse(
            dto.Item(
                id=item.id,
                name=item.name,
                amount=item.amount,
                price=item.price
            ).dict()
        )
    return HttpResponseNotAllowed(['GET', 'POST'])


@require_http_methods(["GET"])
def get_item_by_id(request, item_id: int):
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseServerError("not item with id=%s" % item_id)
    return JsonResponse(
        item.to_dict()
    )


@require_http_methods(["PUT"])
def add_existing_item(request, item_id=None, amount=0):
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseServerError("not item with id=%s" % item_id)
    if amount < 0:
        return HttpResponseServerError("hmm, you're try to add neg amount")
    item.amount += amount
    item.save()
    return JsonResponse(
        dto.Item(
            id=item.id,
            name=item.name,
            amount=item.amount,
            price=item.price
        ).dict()
    )


@require_http_methods(["PUT"])
def dec_existing_item(request, item_id=None, amount=0):
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseServerError("not item with id=%s" % item_id)
    if amount < 0:
        return HttpResponseServerError("hmm, you're try to dec pos amount")
    item.amount -= amount
    item.save()
    return JsonResponse(
        dto.Item(
            id=item.id,
            name=item.name,
            amount=item.amount,
            price=item.price
        ).dict()
    )
