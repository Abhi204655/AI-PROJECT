from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from .models import Account
from django.contrib import messages

# Create your views here.


def registeration_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            form.save()
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            messages.success(request, "Account created Successfully....")
            return redirect("/")
        else:
            messages.warning(request, "Please fill the form correctly!!!")
            context['registeration_form'] = form
    else:
        form = RegistrationForm()
        context['registeration_form'] = form
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, "You are successfully Logged out...")
    return redirect("/")


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("/")

    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, "Logged in Successfully...")
                return redirect('/')
            else:
                messages.warning(request, "User Doesn't exist..")
        else:
            messages.warning(request, "Please fill the form correctly!!!")
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'account/login.html')
