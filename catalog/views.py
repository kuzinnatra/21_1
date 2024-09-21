from django.shortcuts import render, get_object_or_404
from catalog.models import Product

import catalog


# Create your views here.
# def index(request):
#     return render(request, 'catalog/base.html')

def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/products_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'catalog/product_detail.html', context)



def contacts(request):
    return render(request, 'catalog/contacts.html')


