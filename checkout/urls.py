from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.basket, name='basket'),
    path('checkout_payment/', views.checkout, name='checkout'),  
]