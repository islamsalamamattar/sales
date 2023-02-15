from django.db import models
from product.models import *


# Cities > Areas Settings
class City(models.Model):
    name = models.CharField(max_length=25)
    name_ar = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class Area(models.Model):
    city = models.ForeignKey(City, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    name_ar = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

# Customer
class Customer(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=25)  #PhoneNumberField()
    logo = models.ImageField(blank=True)
    city = models.ForeignKey(City, null=True, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

class Discount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    discount = models.PositiveIntegerField(max_digits=2)
    valid_till = models.DateField(auto_now=False, auto_now_add=False, )
    def __str__(self):
        return f"{self.name}"

class Invoice(models.Model):
    number = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    date = models.DateTimeField(auto_now_add=True)

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='invoice_items')
    quantity = models.PositiveIntegerField()
    discount = models.ForeignKey(Discount, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

