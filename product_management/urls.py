from django.urls import path
from product_management.views import list_product_skus

app_name = "product_management"

urlpatterns = [
    path('skus/', list_product_skus, name='list_product_skus'),
]