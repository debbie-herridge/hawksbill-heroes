from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product

# Create your views here.
def merchandise(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'merchandise.html', context)

def merchandise_details(request, merchandise_id):
    product = get_object_or_404(Product, pk=merchandise_id)
    context={
	    'product':product,
    }
    return render(request, 'merchandise_detail.html', context)