from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import TurtleForm
from .models import Turtle

def turtles(request):
    turtles = Turtle.objects.all()
    turtle_form = TurtleForm()

    if request.method == "POST":
        turtle_form = TurtleForm(request.POST, request.FILES)
        if turtle_form.is_valid():
            turtle_form.save()
            messages.success(request, 'One more turtle added to the family!')
            return render(request, 'turtles.html',{'turtles':turtles})
        else:
            messages.error(request, 'Error saving form, please refresh and try again.')
            print (turtle_form.errors)
            return render(request, 'turtles.html',{'turtles':turtles})
    
    context={
	'turtles':turtles,
    'turtle_form':turtle_form,
    }
    return render(request, 'turtles.html', context)

def turtle_details(request, turtle_id):
    turtle = get_object_or_404(Turtle, pk=turtle_id)
    context={
	    'turtle':turtle,
    }
    return render(request, 'turtle_details.html', context)