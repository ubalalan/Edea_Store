from django.shortcuts import render
from .models import Analysis
# Create your views here.

import requests
from bs4 import BeautifulSoup

r = requests.get(
    'https://www.n11.com/telefon-ve-aksesuarlari')
soup = BeautifulSoup(r.content, "lxml")
title = soup.find_all("h3", class_="productName")
tits = []

for tit in title:
    tits.append(tit.text)


def analysis(request):
    context = {'tits': tits}
    return render(request, 'analysis.html', context)


def basabas(request):
    context = {}
    return render(request, 'basabas.html', context)
