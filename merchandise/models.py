from django.db import models

# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=6, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

