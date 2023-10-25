from django.shortcuts import render
from .models import Product

# Create your views here.
def merchandise(request):
    product = Product.objects.all()
    context = {
        'product': product,
    }
    return render(request, 'merchandise.html', context)