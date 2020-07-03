from django.shortcuts import render
from .models import  Order
# Create your views here.



def addorder(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            Orders = Order.objects.all()
            context = {'Orders': Orders}
            return render(request, "addorder.html", context)
    else:
        Products = Order.objects.all()
        return render(request, "addorder.html")   

def order(request):
    context = {}
    return render(request, 'order.html', context)

