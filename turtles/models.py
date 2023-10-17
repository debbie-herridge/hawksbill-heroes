from django.db import models
from account.models import Profile

# Model for all turtles
class Turtles(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to='turtles')
    description = models.TextField()
    status = models.BooleanField(default=False)
    sponsor = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, default=False)

    def __str__(self):
        return self.name