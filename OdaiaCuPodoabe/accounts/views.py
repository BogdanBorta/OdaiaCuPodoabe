from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def login(request):
    form = AuthenticationForm
    return render(request, 'accounts/login.html', {'form': form})
