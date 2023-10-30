from . import views
from django.urls import path, include

urlpatterns = [
    path('home/', views.turtles, name='turtles'),
    path('<turtle_id>/', views.turtle_details, name='turtle_details'),
]