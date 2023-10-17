from django.forms import ModelForm
from .models import Turtles

class AddTurtle(ModelForm):
    class Meta:
       model = Turtles
       fields = ('name','image','description')
