from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

def merchandise(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'merchandise.html', context)

def merchandise_details(request, merchandise_id):
    product = get_object_or_404(Product, pk=merchandise_id)
    reviews = Review.objects.all()
    context={
	    'product':product,
        'reviews':reviews,
    }
    return render(request, 'merchandise_detail.html', context)
