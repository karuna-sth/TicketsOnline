from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register_user(request):
    context = {}
    if request.method == "POST":
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=email).exists():
                messages.info(request, ("Username already exists, Try another"))
                return render(request, 'authenticate/register_user.html', context)
            else:
                user = User.objects.create_user(username= email, password=password1, email= email, first_name=first_name, last_name=last_name)
                user.save()
                user = authenticate(request, username=email, password=password1)
                login(request, user)
        else:
            messages.info(request, ("Password dont match. Please try again."))
            return render(request, 'authenticate/register_user.html', context)
        return redirect("stores:index")
        # messages.success(request, ("Registration Successfull! you are now logged in!"))
    else:    
        return render(request, 'authenticate/register_user.html', context)
    

def login_users(request): 
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("stores:index")
        else:
            messages.info(request, ("Username or Password is incorrect. Please try again."))
            return redirect('users:login_users')
    else:
        return render(request, 'authenticate/login_users.html', context)
    

def logout_users(request):
    logout(request)
    return redirect("stores:index")