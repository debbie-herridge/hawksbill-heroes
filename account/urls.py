from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('edit_profile/', views.EditUser.as_view(), name='edit_profile'),
    
    path('delete/', views.UserDeleteView.as_view(), name='delete'),
    path('user_deleted/', views.userDeleted, name='user-deleted'),

    path('dashboard/', views.dashboard, name='dashboard'),
]