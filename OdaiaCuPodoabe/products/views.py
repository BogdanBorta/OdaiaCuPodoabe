from django.shortcuts import render
from .models import Product
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView


def home(request):
    product_list = Product.objects.all()
    return render(request, 'products/home2.html', context={'product_list': product_list})


class ProductCreateView(CreateView):
    template_name = 'products/product_create.html'
    model = Product
    fields = "__all__"
    success_url = reverse_lazy('products:product_list')


class ProductListView(ListView):
    template_name = 'products/products_list.html'
    model = Product
    context_object_name = 'product_list'


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    model = Product
    context_object_name = 'product_detail'



