from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.basket, name='basket'),
    path('details/', views.checkout, name='checkout'), 
]