from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Tot ok </h1> ")

def products_list(request):
    return render(request, "products/products_list.html")