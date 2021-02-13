from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1> Tot ok </h1> ")

def home(request):
    return render(request, "products/home.html")


