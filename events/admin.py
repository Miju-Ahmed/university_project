from django.contrib import admin

# Register your models here.
# events/admin.py
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'location')
    list_filter = ('start_time',)