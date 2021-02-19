from django.shortcuts import render
from .models import Product
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, TemplateView


def home(request):
    context = {'product_list': Product.objects.all()}
    return render(request, 'products/home2.html', context)


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


class ProductTemplateView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        return context

