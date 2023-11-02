from django.shortcuts import render

# Create your views here.

def checkout_basket(request):
    return render(request, 'checkout_basket.html',{})

def checkout(request):
    return render(request, 'checkout.html',{})