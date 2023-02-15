from django.contrib import admin
from .models import *
# Register your models here.
#Brands > Models admin
class ModelInline(admin.TabularInline):
        model = Brand
class BrandsAdmin(admin.ModelAdmin):
        list_display = ("name",)
        search_fields = ["name",]
        inlines = [ ModelInline,]

class ModelInline(admin.TabularInline):
        model = Product
class ProductsAdmin(admin.ModelAdmin):
        list_display = ("name",)
        search_fields = ["name",]
        inlines = [ ModelInline,]


admin.site.register(Brand, BrandsAdmin)
admin.site.register(Product, ProductsAdmin)