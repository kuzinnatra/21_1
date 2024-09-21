from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contacts, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('contacts/', contacts),
    path('product/<int:pk>', ProductDetailView.as_view(), name='products_detail')
]
