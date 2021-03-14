import django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm



def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None and username != 'admin':
            login(request, user)
            return redirect("products:product_list")
        elif username == 'admin':
            login(request, user)
            return redirect('admin:index')
    return render(request, 'users/login.html', {})


def logout_view(request):
    logout(request)
    return redirect("welcome_page")


def welcome_page(request):
    return render(request, 'users/welcome.html', )


@login_required
def home(request):
    return render(request, 'users/home.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # stocam intr-o variabila username-ul completat de utilizator
            username = form.cleaned_data.get('username')
            # afisam un mesaj de creare a contului
            messages.success(request, f'Contul {username} a fost creat!')
            # redirectionam userul catre pagina cu produse
            return redirect('login_view')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def profile_view(request):
    context = {'user': request.user}  # requesting the user object
    return render(request, 'users/profile.html', context)

def edit_profile_view(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/users/profile/')
    else:
        form = UserChangeForm(instance=request.user)
        context={'form':form}
        return render(request, 'users/edit_profile.html', context)

