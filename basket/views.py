from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages

from merchandise.models import Product

def add_to_basket(request, item_id):
    """
    Handles users adding items to their basket, including size and quantity.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    # Simple add to basket if item has no sizing
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys(): 
                # Update quantity of basket with same size item
                basket[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 (f'Updated size {size.upper()} '
                                  f'{product.name} quantity to '
                                  f'{basket[item_id]["items_by_size"][size]}'))
            else:
                # Add new item with size data
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
        # Update quantity of basket with same item
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request,
                            (f'Updated {product.name}' 
                            f' quantity to {basket[item_id]}'))
        else:
            # Add item to basket
            basket[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag!')
        
    request.session['basket'] = basket 
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """
    Remove an item from the shopping bag.
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        if size:
            # Deletes item with specific size
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{product.name} from your bag'))
        else:
            # Simple delete item
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)