from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.merchandise, name='merchandise'),
    path('<merchandise_id>/', views.merchandise_details, name='merchandise_details'),
]