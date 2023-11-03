from django.db import models
from account.models import Profile

class Turtle(models.Model):
    """
    Handles all data information for each turtle.
    """
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to='turtles')
    description = models.CharField(max_length=500)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    age = models.IntegerField(null=True)
    size = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    discovery_date = models.DateField(null=True)

    def __str__(self):
        return self.name