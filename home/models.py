from django.db import models
from django.contrib.auth.models import User

class Donation(models.Model):
    customer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField(null=True)