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

def bookticket(request):
    context = {}
    return render(request, 'stores/bookticket.html', context)



