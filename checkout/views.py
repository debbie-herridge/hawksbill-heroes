from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def basket(request):
    return render(request, 'basket.html',{})

def checkout(request):
    """
    Pass form for users to input checkout details
    """
    basket = request.session.get('basket',{})
    if not basket:
        return redirect(reverse('merchandise'))

    order_form = OrderForm()
    context = {
        'order_form':order_form,
    }
    return render(request, 'checkout.html' , context)