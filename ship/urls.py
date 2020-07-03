
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ship, name="ship"),

]
