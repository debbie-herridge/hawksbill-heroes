from django.shortcuts import render
from django.contrib import messages
from .forms import TurtleForm
from .models import Turtle

def turtles(request):
    turtle = Turtle.objects.all()
    turtle_form = TurtleForm()

    if request.method == "POST":
        turtle_form = TurtleForm(request.POST)
        if turtle_form.is_valid():
            turtle_form.save()
            messages.success(request, 'One more turtle added to the family.')
            return render(request, 'turtles.html',{'turtle':turtle})
        else:
            messages.error(request, 'Error saving form. Please refresh and try again.')
            return render(request, 'turtles.html',{'turtle':turtle})
    
    context={
	'turtle':turtle,
    'turtle_form':turtle_form,
    }
    return render(request, 'turtles.html', context)