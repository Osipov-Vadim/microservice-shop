from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.db import transaction

from catalog_service.models.item import Item, CreateItemSerializer
from microservices_api import dto, serializers
from microservices_api.api import json_error


@require_http_methods(["GET"])
def get_items(request):
    return JsonResponse(
        data={"items: ": list(Item.objects.all().values())}
        # model_serializers.serialize("json", Item.objects.all()),
    )


@require_http_methods(["POST"])
def create_items(request):
    _data = serializers.parse_raw_data(request.body)
    if _data is None:
        # TODO
        return JsonResponse(
            data=json_error("cant deserialize"),
            status=500
        )

    c_item = CreateItemSerializer(data=_data)
    if not c_item.is_valid():
        # TODO
        return JsonResponse(
            data=json_error("cant parse item: %s" % c_item.error_messages),
            status=500
        )
    item = c_item.save()
    return JsonResponse(item.to_dict())


@require_http_methods(["GET"])
def get_item_by_id(request, item_id: int):
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return JsonResponse(
            data=json_error("not item with id = %s" % item_id),
            status=500
        )
    return JsonResponse(
        item.to_dict()
    )


@require_http_methods(["PUT"])
def add_existing_item(request, item_id=None, amount=0):
    with transaction.atomic():
        item_qs = Item.objects.select_for_update().filter(pk=item_id)
        if not item_qs.exists():
            return JsonResponse(
                data=json_error("not item with id = %s" % item_id),
                status=500
            )
        item = item_qs.first()
        try:
            item.change_amount(amount)
        except ValidationError as e:
            return JsonResponse(
                data=json_error(e.message),
                status=500
            )
        return JsonResponse(
            item.to_dict()
        )


@require_http_methods(["PUT"])
def dec_existing_item(request, item_id=None, amount=0):
    with transaction.atomic():
        item_qs = Item.objects.select_for_update().filter(pk=item_id)
        if not item_qs.exists():
            return JsonResponse(
                data=json_error("not item with id = %s" % item_id),
                status=500
            )
        item = item_qs.first()
        try:
            item.change_amount(-amount)
        except ValidationError as e:
            return JsonResponse(
                data=json_error(e.message),
                status=500
            )
        return JsonResponse(
            item.to_dict()
        )
