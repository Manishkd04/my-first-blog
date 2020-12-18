from django.contrib import admin
from .models import Product

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'sub_category', 'description']

admin.site.register(Product, AdminProduct)
