from django.shortcuts import render
from .models import Store
# Create your views here.

def store(request):
    context = {}
    return render(request, 'store.html', context)