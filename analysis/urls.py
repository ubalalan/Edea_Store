from django.urls import path
from . import views

urlpatterns = [

    path('', views.analysis, name="analysis"),
    path('basabas/', views.basabas, name="basabas"),



]
