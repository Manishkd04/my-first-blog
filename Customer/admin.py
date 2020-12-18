from django.contrib import admin
from .models import Customer

# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']

admin.site.register(Customer, AdminCustomer)
