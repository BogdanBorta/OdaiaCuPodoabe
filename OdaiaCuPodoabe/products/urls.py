from django.urls import path
from .views import ProductDetailView, ProductDeleteView, ProductUpdateView, home

urlpatterns = [
    path("home", home, name='home'),
    path("details/<int:pk>", ProductDetailView.as_view(), name="product_details"),
    path("delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
]