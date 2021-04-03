from .models import Product
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q


class SearchResultsView(ListView):
    model = Product
    template_name = 'products/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('search')

        if query:
            products_list = Product.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query)
            ).order_by('price')

        else:
            products_list = Product.objects.all().order_by('price')
        return products_list


class ProductCategView(ListView):
    template_name = 'products/product_categ.html'
    model = Product

    def get_queryset(self):
        query = self.request.GET.get('product_categ')

        if query:
            products_list = Product.objects.filter(category=query)
        else:
            products_list = Product.objects.all()
        return products_list


class ProductListView(ListView):
    template_name = 'products/products_list.html'
    model = Product
    context_object_name = 'product_list'


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product_details"


class ProductTemplateView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
