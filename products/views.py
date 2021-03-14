from django.shortcuts import render
from .models import Product
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q


def category_page(request):
    categories = request.GET.get("categ")
    print(categories)
    return render(request, "products/product_categ.html", {'categories': categories})


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


# class ProductCategView(ListView):
#     template_name = 'products/product_categ.html'
#     model = Product
#     context_object_name = 'product_categ'
#
#     def get_queryset(self):
#         query = self.request.GET.get('categ')
#         print('my quesry is:', query)
#
#         products_list = Product.objects.filter(category=query)
#         if not products_list.exists():
#             Product.objects.all()
#         return products_list


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
    template_name = "products/product_detail.html"
    context_object_name = "product_details"


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/product_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("products:product_list")
    fields = ["name", "price", "description", "image"]


class ProductTemplateView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "products/product_update.html"
    context_object_name = "product"
    success_url = reverse_lazy("products:product_list")
    fields = ["name", "price", "description", "image"]
