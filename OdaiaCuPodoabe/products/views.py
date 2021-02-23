from django.shortcuts import render
from .models import Product
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from django.urls import reverse_lazy


def home(request):
    search = request.GET.get('search')
    if search:
        product_list = Product.objects.filter(name__icontains=search)
    else:
        product_list = Product.objects.all()
    return render(request, 'products/products_list.html', context={'product_list': product_list})


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
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product_details"


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/product_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("products:product_list")
    fields = ["name","price","description","image"]

class ProductTemplateView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "products/product_update.html"
    context_object_name = "product"
    success_url = reverse_lazy("products:product_list")
    fields = ["name", "price", "description", "image"]
