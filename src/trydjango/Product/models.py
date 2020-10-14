from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=15)

