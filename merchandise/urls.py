from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.merchandise, name='merchandise'),
    path('<merchandise_id>/', views.merchandise_details, name='merchandise_details'),
    path('checkout_basket/', views.checkout_basket, name='checkout_basket'),
    path('checkout/', views.checkout, name='checkout'),
]