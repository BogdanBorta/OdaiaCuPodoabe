from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

def login(request):
    form = AuthenticationForm
    return render(request, 'users/login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect("products/welcome.html")


def welcome_page(request):
    return render(request, 'users/welcome.html',)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # stocam intr-o variabila username-ul completat de utilizator
            username = form.cleaned_data.get('username')
            # afisam un mesaj de creare a contului
            messages.success(request, f'Contul {username} a fost creat!')
            # redirectionam userul catre pagina cu produse
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


