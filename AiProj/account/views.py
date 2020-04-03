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
            return redirect("/")
        else:
            context['registeration_form'] = form
    else:
        form = RegistrationForm()
        context['registeration_form'] = form
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
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
                return redirect('/')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html')


def update_view(request):

    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.initial = {
                "email": request.POST['email'], "username": request.POST['username']}
            form.save()
            context['success_message'] = "updated"

    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )

    context['account_form'] = form

    return render(request, "account/account.html", context)
