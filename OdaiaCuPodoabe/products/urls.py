from django.urls import path
from .views import home, ProductCreateView, ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path("home", home, name='home'),
    path('create_product', ProductCreateView.as_view(), name='product_create'),
    path('products_list', ProductListView.as_view(), name='products_list'),
    path('products_list/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
