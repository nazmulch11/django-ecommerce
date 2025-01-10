from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def homepage(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
