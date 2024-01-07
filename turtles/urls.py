from . import views
from django.urls import path, include

urlpatterns = [
    path('home/', views.turtles, name='turtles'),
    path('delete_turtle/<pk>', views.deleteTurtle, name='delete_turtle'),
    path('<turtle_id>/', views.turtleDetails, name='turtle_details'),
]