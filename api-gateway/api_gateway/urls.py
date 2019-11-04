"""api_gateway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from .routers import *

schema_view = get_swagger_view(title='API Gateway')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/warehouse/items/', items_handler),
    path('api/warehouse/items/<int:item_id>/', get_item_by_id),
    path('api/warehouse/items/<int:item_id>/addition/<int:amount>/', add_existing_item),
    path('api/warehouse/items/<int:item_id>/decrease/<int:amount>/', dec_existing_item),
    path('api/orders/', get_orders),
    path('api/orders/<int:order_id>/', get_order_by_id),
    path('api/orders/null/item/', create_order),
    path('api/orders/<int:order_id>/item/', add_item_to_order),
    path('api/orders/<int:order_id>/status/<str:new_status>/', change_order_status),
    path('api/orders/<int:order_id>/payment/', perform_payment),
    path("swagger/", schema_view),
]
