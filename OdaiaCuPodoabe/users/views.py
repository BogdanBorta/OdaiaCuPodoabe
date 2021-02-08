from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def login(request):
    form = UserCreationForm()
    return render(request, 'users/login.html', {'form': form})
