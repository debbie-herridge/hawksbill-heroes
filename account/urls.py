from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_profile/', views.EditUser.as_view(), name='edit_profile')
]