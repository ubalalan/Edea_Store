from django.shortcuts import render
from .models import Ship
# Create your views here.


def ship(request):
    context = {}
    return render(request, 'ship.html', context)
