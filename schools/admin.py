from django.contrib import admin
from .models import School, Newsletter

# Register your models here.


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("school_name", "address_city", "category")


@admin.register(Newsletter)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("email_address",)
