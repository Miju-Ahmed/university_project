# core/admin.py
from django.contrib import admin
# This is the corrected line: Import HeroSection instead of HomePageImage
from .models import HeroSection

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'is_active')
    list_filter = ('is_active',)

# Make sure any old code related to HomePageImageAdmin is deleted.