from django.contrib import admin
from .models import School, Newsletter, Job, Blog, Event

# Register your models here.


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("school_name", "address_city", "category")


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email_address",)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "company_name", "company_summary")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "blog_category")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("event_title", "event_location", "event_speaker")
