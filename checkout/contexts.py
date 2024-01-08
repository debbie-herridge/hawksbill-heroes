from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from merchandise.models import Product

def basket_contents(request):
    """
    Handles basket item data and total cost including delivery.
    """
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        # Updates basket data with item
        if isinstance(item_data,int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id':item_id,
                'quantity':item_data,
                'product':product,
            })
    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total
    context = {
        'basket_items':basket_items,
        'total':total,
        'product_count':product_count,
        'delivery':delivery,
        'grand_total':grand_total,
    }
    return context