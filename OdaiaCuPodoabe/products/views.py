from django.shortcuts import render
from .models import Product

def home(request):
    product_list = Product.objects.all()
    return render(request, 'products/home2.html', context={'product_list':product_list})
