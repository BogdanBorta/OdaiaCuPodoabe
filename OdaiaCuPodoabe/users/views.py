from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login , logout

def login(request):
    form = AuthenticationForm
    return render(request, 'registration/login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect("products/home.html")

