from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import CreateUserForm

# Create your views here.
def index(request):
    return render(request, 'muviera/landing.html')
def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('recommend')
        else:
            messages.info(request, 'Username or Password is Incorrect')
    return render(request, 'muviera/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was Created for ' + user)
            return redirect('login')

    context = {'form': form}

    return render(request, 'muviera/register.html', context)

@login_required(login_url='login')
def home(request):
    return render(request, 'muviera/third.html')

def contact(request):
    return render(request, 'muviera/contact.html')

@login_required(login_url='login')
def recommend(request):
    return render(request, 'muviera/afterlogin.html')