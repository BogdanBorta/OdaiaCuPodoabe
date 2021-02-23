from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('products:home')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect("products:home")

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # stocam intr-o variabila username-ul completat de utilizator
            username = form.cleaned_data.get('username')
            # afisam un mesaj de creare a contului
            messages.success(request, f'Account created for {username}!')
            # redirectionam userul catre pagina cu produse*
            return redirect('products:home')
        else:
            form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


