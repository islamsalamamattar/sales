from django.contrib import admin
from .models import *

#Cities > Areas admin
class AreaInlines(admin.TabularInline):
        model = Area
class CityAdmin(admin.ModelAdmin):
        list_display = ("name",)
        inlines = [AreaInlines]


class DiscountInlines(admin.TabularInline):
        model = Discount
class CustomerAdmin(admin.ModelAdmin):
        list_display = ("name", "area")
        inlines = [DiscountInlines]


class InvoiceItemInlines(admin.TabularInline):
        model = InvoiceItem
class InvoiceAdmin(admin.ModelAdmin):
        list_display = ("number", "customer", "date")
        inlines = [InvoiceItemInlines]


admin.site.register(City, CityAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Invoice, InvoiceAdmin)
