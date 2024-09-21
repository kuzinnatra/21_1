from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import products_list, contacts, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list, name='products_list'),
    path('contacts/', contacts),
    path('product/<int:pk>', product_detail, name='products_detail')
]
