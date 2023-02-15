from django.contrib import admin
from .models import *

#Cities > Areas admin
class AreaInlines(admin.TabularInline):
        model = Area
class CityAdmin(admin.ModelAdmin):
        list_display = ("name",)
        inlines = [AreaInlines]


class CustomerAdmin(admin.ModelAdmin):
        list_display = ("name", "area")

class DiscountAdmin(admin.ModelAdmin):
        list_display = ("customer", "product", "discount")

class InvoiceItemInlines(admin.TabularInline):
        model = Invoice
class InvoiceAdmin(admin.ModelAdmin):
        list_display = ("invoce", "customer")
        inlines = [InvoiceItemInlines]


admin.site.register(City, CityAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
