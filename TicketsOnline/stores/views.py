from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'stores/index.html', context)

def event(request):
    context = {}
    return render(request, 'stores/event.html', context)

def checkout(request):
    context = {}
    return render(request, 'stores/checkout.html', context)



