from django.shortcuts import render
from .models import Product
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy

def home(request):
    product_list = Product.objects.all()
    return render(request, 'products/home2.html', context={'product_list':product_list})

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_details.html"
    context_object_name = "product"

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/product_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("products: product_list")
    fields = ["name","price","description","image"]
    pk_url_kwarg = "product_id"

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "products/product_update.html"
    context_object_name = "product"
    success_url = reverse_lazy("products: product_list")
    fields = ["name", "price", "description", "image"]
