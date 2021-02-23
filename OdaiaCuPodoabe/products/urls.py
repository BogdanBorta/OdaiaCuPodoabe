from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDetailView, ProductDeleteView, ProductUpdateView, home

app_name = 'products'

urlpatterns = [
    path("home", home, name='home'),
    path("details/<int:pk>", ProductDetailView.as_view(), name="product_details"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('products_list', ProductListView.as_view(), name='product_list'),
]