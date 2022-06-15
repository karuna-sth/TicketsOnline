from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'stores/index.html', context)

def aboutUs(request):
    context = {}
    return render(request, 'stores/AboutUs.html', context)

def event(request):
    context = {}
    return render(request, 'stores/event.html', context)

def checkout(request):
    context = {}
    return render(request, 'stores/checkout.html', context)

def sports(request):
    context = {}
    return render(request, 'stores/sports.html', context)

def register(request):
    context = {}
<<<<<<< HEAD
    return render(request, 'stores/football.html', context)

def bookticket(request):
    context = {}
    return render(request, 'stores/bookticket.html', context)    
=======
    return render(request, 'stores/register.html', context)
>>>>>>> 440dcce667b84d3f51988692eba65f2b830a7a2c
