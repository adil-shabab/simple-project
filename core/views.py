from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import Cart, Product
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def home(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' +user)
            return redirect('login')
        else:
            messages.info(request, "please enther correct information and enter the unique username and strong password")


    form = CreateUserForm()
    context={'form': form}
    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    
    return render(request, 'login.html')

@login_required(login_url='login')
def addtocart(request, pk):

    product=Product.objects.get(id=pk)
    cart = Cart(product=product, quantity=1)
    if Cart.objects.filter(product=product):
        messages.success(request, 'alreay added')
    else:
        cart.save()

    allcart = Cart.objects.all()
    context={
        'carts': allcart
    }
    return render(request, 'cart.html', context)


@login_required(login_url='login')
def delete(request, pk):
    cart = Cart.objects.get(id=pk)
    cart.delete()
    return redirect('home')