from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('donate', views.donate, name='donate'),
]