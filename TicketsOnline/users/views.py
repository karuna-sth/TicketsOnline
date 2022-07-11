from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def register_user(request):
    context = {}
    
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
            messages.success(request, ("Username or Password is incorrect. Please try again."))
            return redirect('users:login_users')
    else:
        return render(request, 'authenticate/login_users.html', context)
    

def logout_users(request):
    logout(request)
    return redirect("stores:index")