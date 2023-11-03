from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def basket(request):
    return render(request, 'basket.html',{})

def checkout(request):
    basket = request.session.get('basket',{})
    if not basket:
        return redirect(reverse('merchandise'))

    order_form = OrderForm()
    context = {
        'order_form':order_form,
    }

    return render(request, 'checkout.html' , context)
