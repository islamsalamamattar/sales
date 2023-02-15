from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


# Brands > Products

class Brand(models.Model):
    name = models.CharField(max_length=25)
    name_ar = models.CharField(max_length=64)
    logo = models.CharField(max_length=128, blank=True)  #format
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    name_ar = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.name}"


