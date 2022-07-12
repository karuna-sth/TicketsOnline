from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def holiday(request):
    context = {}
    return render(request, 'tour/holiday.html', context)