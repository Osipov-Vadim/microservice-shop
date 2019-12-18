from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Order, OrderStatus, ReservedItem, is_possible_to_change_status
from django.http import HttpResponse, HttpResponseServerError
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


# @shared_task(name="test")
# def test(**arg):
#     print(arg['a'])



@shared_task(name="test")
def change_order_status(**args):
    
    order_id = int(args['id'])
    new_status = args['new_status']

    print('Received order: {0!r}'.format(order_id))
    try:
        order = Order.objects.get(id=order_id)
    except ObjectDoesNotExist:
        return HttpResponseServerError("not order with id=%s" % order_id)

    if not is_possible_to_change_status(order.status, new_status):
        return HttpResponseServerError("cant change status from %s to %s" % order.status, new_status)
    # TODO RabbitMQ tasks
    if new_status == OrderStatus.PAID.value:
        pass
    elif new_status == OrderStatus.SHIPPING.value:
        pass
    elif new_status == OrderStatus.COMPLETE.value:
        pass
    elif new_status == OrderStatus.FAILED.value:
        pass
    elif new_status == OrderStatus.CANCELLED.value:
        pass

    order.status = new_status
    order.save()

    return "OK"