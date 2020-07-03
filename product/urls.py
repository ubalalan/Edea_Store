from django.urls import path
from . import views

urlpatterns = [

    path('', views.product, name="product"),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('delete/<product_id>/', views.delete, name="delete"),


]
