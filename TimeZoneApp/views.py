from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
from django.http import HttpResponse
from .models import *
from . import forms
import uuid


def index(request):
    print('You are ', request.session.get('user_id'))
    flag = False
    if request.session.get('user_id') is None:
        flag = True

    form = {'user': flag }
    return render(request, 'watches/index.html', form)


def register_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']

        try:
            if Profile.objects.filter(user__email=email).exists():
                messages.error(request, "This email is already taken")
                return redirect('register')

            if get_user_model().objects.filter(username=username).exists():
                messages.error(request, "This username is already taken")
                return redirect('register')

            auth_token = str(uuid.uuid4())
            user_obj = User.objects.create_user(username, email, password, first_name=fname, last_name=lname)
            profile_obj = Profile.objects.create(user = user_obj, auth_token=auth_token)
            profile_obj.save()
            send_mail_after_registration(email,auth_token)
            return redirect('auth')

        except Exception as e:
            print(e)

        messages.success(request, "Your account is successfully created")
        return redirect('login')

    return render(request, 'watches/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user_login = authenticate(username=username, password=password)
        profile_obj = Profile.objects.filter(user__username=username).first()
        if user_login is not None:
            if profile_obj.is_verified:
                login(request, user_login)
                request.session['user_id'] = user_login.username

                return redirect('index')
            else:

                auth_token = str(uuid.uuid4())
                profile_obj.auth_token = auth_token
                profile_obj.save()
                email = User.objects.get(username=username).email
                send_mail_after_registration(email,auth_token)
                return redirect('auth')

        else:
            messages.error(request, "Bad Credentials")
            return redirect('login')

    return render(request, 'watches/login.html')


def send_mail_after_registration(email,token):
    subject = "Your accounts need to be verified"
    message = f'Hi pass the link to verify your account http://127.0.0.1:8000/TimeZone/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)

def auth_token(request):
    return render(request, 'watches/auth_token.html')

def auth_verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
            return redirect('auth_success')
        else:
            return redirect('error')
    except Exception as e:
        print(e)


def auth_success(request):
    return render(request, 'watches/auth_success.html')


def contact_us(request):
    if request.method == 'POST':
        form = forms.CreateContact(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contactus')

    form = forms.CreateContact()
    return render(request, "watches/contact_us.html", {'form': form})


def upload_prod(request):
    if request.method == 'POST':
        form = forms.CreateProduct(request.POST, request.FILES)
        images = request.FILES.getlist('images')

        if form.is_valid():
            form = form.save()
            count = 1
            for image in images:
                image.name = 'otherimages'+str(count)+'.'+image.name.split('.')[-1]
                count += 1
                ProductImages.objects.create(product=form, images=image)

            return redirect('login')
        else:
            print(form.errors.as_data())
    form = forms.CreateProduct()
    form2 = forms.ProductImages()
    return render(request, 'watches/add_product.html', {'form': form, 'form2': form2})


def shop_prod(request,nproducts=2):
    # products = Product.objects.all()
    # Default no of items showed on the page

    products = Product.objects.order_by('product_price')[:nproducts]
    priceHighToLow = Product.objects.order_by('-product_price')[:nproducts]
    return render(request, 'watches/shop.html', {'products': products,'priceHighToLow':priceHighToLow})

def product(request,slug):
    # product = Product.objects.get(product_uuid='b459f199-9140-4764-be43-0eb4f17767e5')
    product = Product.objects.get(product_uuid=slug)
    return render(request, 'watches/product.html', {'product': product})


# Dynamically checking the username and email exists or not


def check_username(request):
    username = request.POST.get('username')

    if get_user_model().objects.filter(username=username).exists():
        profile_obj = Profile.objects.get(user__username=username)
        if profile_obj.is_verified:
            return HttpResponse('<div style="color: red"> This username already exists </div>')
    return HttpResponse('<div style="color: red"></div>')


def check_email(request):
    email = request.POST.get('email')

    if get_user_model().objects.filter(email=email).exists():
        profile_obj = Profile.objects.get(user__email=email)
        if profile_obj.is_verified:
            return HttpResponse('<div style="color: red"> This email already exists </div>')
    return HttpResponse('<div style="color: red"></div>')


def check_fname(request):
    fname = request.POST.get('fname')
    if fname.isspace():
        return HttpResponse('<div style="color: red">Only Space is not allowed...</div>')
    return HttpResponse('<div style="color: green"></div>')


def check_lname(request):
    lname = request.POST.get('lname')
    if lname.isspace():
        return HttpResponse('<div style="color: red">Only Space is not allowed...</div>')
    return HttpResponse('<div style="color: green"></div>')





