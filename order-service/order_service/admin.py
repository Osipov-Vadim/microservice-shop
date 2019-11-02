from django.contrib import admin
from order_service.models.order import Order
from order_service.models.reserved_item import ReservedItem
# Register your models here.

admin.site.register(Order)
admin.site.register(ReservedItem)
