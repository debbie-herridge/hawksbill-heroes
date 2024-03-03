from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    RATING = (
        ('*','1'),
        ('* *','2'),
        ('* * *','3'),
        ('* * * *','4'),
        ('* * * * *','5'),
    )
    customer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    rating = models.CharField(max_length=200, null=True, choices=RATING)
    review = models.CharField(max_length=500, null=True)
