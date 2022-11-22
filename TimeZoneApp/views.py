from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def register_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username, email, password, first_name=fname, last_name=lname)

        messages.success(request, "Your account is successfully created")
        return redirect('login')

    return render(request, 'watches/register.html')


def login_user(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passwd = request.POST['password']

        user = authenticate(username=uname, password=passwd)

        if user is not None:
            login(request, user)
            return render(request, 'watches/base.html')
        else:
            messages.error(request, "Bad Credentials")
            return redirect('login')

    return render(request, 'watches/login.html')


# Dynamically checking the username and email exists or not


def check_username(request):
    username = request.POST.get('username')

    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('<div style="color: red"> This username already exists </div>')
    else:
        return HttpResponse('<div style="color: green"></div>')


def check_email(request):
    email = request.POST.get('email')

    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse('<div style="color: red"> This email already exists </div>')
    else:
        return HttpResponse('<div style="color: green"></div>')



