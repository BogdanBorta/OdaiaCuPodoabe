from django.urls import path
from .views import ProductListView, ProductDetailView, SearchResultsView, ProductCategView


app_name = 'products'

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path("details/<int:pk>", ProductDetailView.as_view(), name="product_details"),
    path('products_list', ProductListView.as_view(), name='product_list'),
    path('product_categ/', ProductCategView.as_view(), name='product_categ'),
]