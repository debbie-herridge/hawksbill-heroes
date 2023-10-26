from django.forms import ModelForm
from .models import Turtle

class TurtleForm(ModelForm):
    class Meta:
       model = Turtle
       fields = ['name','image','description']
