from django.contrib import admin
from .models import *

#Cities > Areas admin
class AreaInlines(admin.TabularInline):
        model = Model
class CityAdmin(admin.ModelAdmin):
        list_display = ("name",)
        inlines = [AreaInlines]

class CustomerInlines(admin.TabularInline):
        model = Model
class CustomerAdmin(admin.ModelAdmin):
        list_display = ("name", "area")
        inlines = [CustomerInlines]

class DiscountInlines(admin.TabularInline):
        model = Model
class DiscountAdmin(admin.ModelAdmin):
        list_display = ("customer", "product", "discount")
        inlines = [DiscountInlines]

class InvoiceInlines(admin.TabularInline):
        model = Model
class InvoiceItemAdmin(admin.ModelAdmin):
        list_display = ("invoce", "product", "quantity")
        inlines = [InvoiceInlines]


admin.site.register(City, CityAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
