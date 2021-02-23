from django.shortcuts import render
from .models import Product
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy

def home(request):
    product_list = Product.objects.all()
    return render(request, 'products/home2.html', context={'product_list': product_list})


class ProductCreateView(CreateView):
    template_name = 'products/product_create.html'
    model = Product
    fields = '__all__'
    success_url = reverse_lazy("products:product_list")
    context_object_name = "product"

class ProductListView(ListView):
    template_name = 'products/products_list.html'
    model = Product
    context_object_name = 'product_list'

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_details.html"
    context_object_name = "product_detail"
    fields = '__all__'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/product_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("products:product_list")
    fields = ["name","price","description","image"]

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "products/product_update.html"
    context_object_name = "product"
    success_url = reverse_lazy("products:product_list")
    fields = ["name", "price", "description", "image"]
