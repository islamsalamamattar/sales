from django.contrib import admin
from .models import *

#Brands > Models admin
class ProductInline(admin.TabularInline):
        model = Product
class BrandsAdmin(admin.ModelAdmin):
        list_display = ("name",)
        search_fields = ["name",]
        inlines = [ ProductInline,]




admin.site.register(Brand, BrandsAdmin)
