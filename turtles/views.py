from django.shortcuts import render
from django.contrib import messages
from .forms import AddTurtle
from .models import Turtles

def turtles(request):
    turtle = Turtles.objects.all()
    add_turtle = AddTurtle()

    if request.method == "POST":
        add_turtle = AddTurtle(request.POST)
        if add_turtle.is_valid():
            add_turtle.save()
            messages.success(request, 'One more turtle added to the family.')
            return render
        else:
            messages.error(request, 'Error saving form. Please refresh and try again.')
            return render
    
    context={
	'turtle':turtle,
    'add_turtle':add_turtle,
    }
    return render(request, 'turtles.html', context)