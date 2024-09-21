from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView
from catalog.views import ProductListView, contacts, ProductDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    # path('edit/<int:pk>/', ..., name='edit'),
    # path('delete/,<int:pk>/', ..., name='delete'),
]
