from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.checkout_basket, name='checkout_basket'),
    path('checkout_payment/', views.checkout, name='checkout'),
]