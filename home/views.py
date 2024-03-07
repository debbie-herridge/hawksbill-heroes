from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.http import JsonResponse

import stripe

def home(request):
    return render(request, 'index.html')

@login_required
def donate(request):
    return render(request, 'donate.html')

@login_required
def charge(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        
        amount = int(request.POST['amount'])
        customer = stripe.Customer.create(
            source=request.POST['stripeToken']
            )
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='gbp',
            description="Donation"
            )
    return redirect(reverse('success', args=[amount]))

@login_required
def success_msg(request, args):
    amount = args
    return render(request, 'donation_success.html', {'amount':amount})

def handler404(request, exception):
    """ 
    Error Handler 404 - Page Not Found
    """
    return render(request, "errors/404.html", status=404)
