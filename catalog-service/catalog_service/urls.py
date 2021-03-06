from django.urls import path, re_path
from catalog_service.routers import get_items, create_items, get_item_by_id, add_existing_item, dec_existing_item

urlpatterns = [
    path('items/', get_items),
    path('items/create/', create_items),
    path('items/<int:item_id>/', get_item_by_id),
    path('items/<int:item_id>/addition/<int:amount>/', add_existing_item),
    path('items/<int:item_id>/decrease/<int:amount>/', dec_existing_item),
]
