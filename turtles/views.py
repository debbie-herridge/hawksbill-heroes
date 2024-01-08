from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import TurtleForm
from .models import Turtle

def turtles(request):
    """
    Show all turtles in database and allow admin users to add more.
    """
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

def turtleDetails(request, turtle_id):
    turtle = get_object_or_404(Turtle, pk=turtle_id)
    context={
	    'turtle':turtle,
    }
    return render(request, 'turtle-details.html', context)

def deleteTurtle(request, pk):
    """
    Allow admin users to delete a turtle.
    """
    turtle = get_object_or_404(Turtle, pk=pk)
    if request.method == 'POST':
        turtle.delete()
        return redirect('turtles')
    else:
        print('form not valid')
    context = {
        'turtle':turtle,
    }
    return render(request, 'delete-turtle.html', context)

def updateTurtle(request, pk):
    """
    Allow users to update their specific booking.
    """
    turtle = get_object_or_404(Turtle, pk=pk)
    if request.method == 'POST':
        form = TurtleForm(request.POST, instance=turtle)
        if form.is_valid():
            form.save()
            return redirect('turtles')
        else:
            print('form not valid')
            print(form.errors)
    else:
        form = TurtleForm(instance=turtle, initial={
            "name":turtle.name,
            "description":turtle.description,
            "weight":turtle.weight,
            "age":turtle.age,
            "size":turtle.size,
            "discovery_date":turtle.discovery_date,
            })
    context = {
        'form':form,
    }
    return render(request, 'update-turtle.html', context)
