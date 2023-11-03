from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from merchandise.models import Product

# Create your views here.
def add_to_basket(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 (f'Updated size {size.upper()} '
                                  f'{product.name} quantity to '
                                  f'{basket[item_id]["items_by_size"][size]}'))
            else:
                basket[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 (f'Added size {size.upper()} '
                                  f'{product.name} to your basket'))
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             (f'Added size {size.upper()} '
                              f'{product.name} to your basket'))
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request,
                            (f'Updated {product.name}' 
                            f' quantity to {basket[item_id]}'))
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag!')
        
    request.session['basket'] = basket 
    return redirect(redirect_url)