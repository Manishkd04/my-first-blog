from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Category, Sub_category

# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminSub_category(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, AdminCategory)
admin.site.register(Sub_category, AdminSub_category)
admin.site.unregister(Group)

