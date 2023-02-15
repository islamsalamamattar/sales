from django.contrib import admin
from .models import *

# Register your models here.
#Cities > Areas admin
class AreaInlines(admin.TabularInline):
        model = Area
class CityAdmin(admin.ModelAdmin):
        list_display = ("name",)
        inlines = [AreaInlines]

class CustomerInlines(admin.TabularInline):
        model = Customer
class CustomerAdmin(admin.ModelAdmin):
        list_display = ("number", "customer", "date")
        inlines = [CustomerInlines]

class DiscountInlines(admin.TabularInline):
        model = Discount
class DiscountAdmin(admin.ModelAdmin):
        list_display = ("customer", "product", "quantity", "price")
        inlines = [DiscountInlines]

class InvoiceInlines(admin.TabularInline):
        model = Area
class InvoiceItemAdmin(admin.ModelAdmin):
        list_display = ("invoce", "product", "quantity")
        inlines = [InvoiceInlines]


admin.site.register(City, CityAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
