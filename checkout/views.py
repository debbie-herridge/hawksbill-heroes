from django.shortcuts import render, redirect

# Create your views here.

def basket(request):
    return render(request, 'basket.html',{})

def checkout(request):
    return render(request, 'checkout.html',{})