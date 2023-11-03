from . import views
from django.urls import path, include

urlpatterns = [
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),  
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]