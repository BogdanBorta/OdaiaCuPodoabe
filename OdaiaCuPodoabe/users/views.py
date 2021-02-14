from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# message.debug, info, succes, warning, error
from django.contrib import messages


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
    return render(request, 'users/register.html', {'form': form})


def home(request):
    return render(request, 'users/home2.html')
