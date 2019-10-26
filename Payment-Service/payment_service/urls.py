from django.urls import path, re_path

from payment_service.routers import perform_payment

urlpatterns = [
    path('orders/<int:order_id>/payment/', perform_payment),
]
