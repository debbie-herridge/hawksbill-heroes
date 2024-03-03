from . import views
from django.urls import path, include
from .views import handler404

urlpatterns = [
    path('', views.home, name='home'),
    path('donate', views.donate, name='donate'),
    path('charge/', views.charge, name='charge'),
    path('success/<str:args>/', views.success_msg, name='success'),
]

handler404 = 'home.views.handler404'