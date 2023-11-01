from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_profile/', views.EditUser.as_view(), name='edit_profile'),
    path('update_profile_picture/', views.UpdateProfilePicture, name='update_picture'),
    path('delete/', views.UserDeleteView.as_view(), name='delete'),
    path('user_deleted/', views.userDeleted, name='user-deleted'),
]