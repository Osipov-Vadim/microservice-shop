from django.urls import path, re_path

from payment_service.routers import perform_payment, check_order

urlpatterns = [
    path('orders/<int:order_id>/payment/', perform_payment),
    path('orders/check', check_order),
]
