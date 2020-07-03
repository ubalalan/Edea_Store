from django.shortcuts import render
from .models import Customer
# Create your views here.

def customer(request):
    context = {}
    return render(request, 'customer.html', context)
