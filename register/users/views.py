from django.shortcuts import render, redirect
from .models import Name
from .forms import NameForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'users/index.html')

def user_login(request):
    return render(request,)

def us_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # после входы возврашает на главную страницу
        # return redirect('users')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'users/login.html', context)

def logoutUsers(request):
    logout(request)
    return redirect('login')

def us_regis(request):
    form = CreateUserForm(request.POST)

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            # после регистрации переходит на страницу входа
            return redirect('us_login')

    context = {'form': form}
    return render(request, 'users/register.html', context)


def xnx(request):
    users = Name.objects.all()
    return render(request, 'users/in.html', {'users': users})


def regi(request):
    error = ''
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('regis')
        else:
            error = "Форма была не верной"

    form = NameForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'users/registr.html', data)


