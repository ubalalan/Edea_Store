from django.shortcuts import render
from .models import Accounting
# Create your views here.


def accounting(request):
    context = {}
    return render(request, 'accounting.html', context)
