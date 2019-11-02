from django.urls import path, re_path
from order_service.routers import get_orders, get_order_by_id, create_order, add_item_to_order, change_order_status

urlpatterns = [
    path('orders/', get_orders),
    path('orders/<int:order_id>/', get_order_by_id),
    path('orders/null/item/', create_order),
    path('orders/<int:order_id>/item/', add_item_to_order),
    path('orders/<int:order_id>/status/<str:new_status>/', change_order_status),
]
