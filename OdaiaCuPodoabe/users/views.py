from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

def login(request):
    form = AuthenticationForm
    return render(request, 'registration/login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect("products/home.html")


def welcome_page(request):
    return render(request, 'registration/home.html',)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # stocam intr-o variabila username-ul completat de utilizator
            username = form.cleaned_data.get('username')
            # afisam un mesaj de creare a contului
            messages.success(request, f'Account created for {username}!')
            # redirectionam userul catre pagina cu produse
            return redirect('products_home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


