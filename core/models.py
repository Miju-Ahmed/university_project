# core/models.py
from django.db import models

class HeroSection(models.Model):
    # The main background image
    background_image = models.ImageField(upload_to='hero_section', help_text="Large background image for the hero section.")
    
    # Text content
    heading = models.CharField(max_length=200, help_text="The main, large headline.")
    subheading = models.TextField(blank=True, help_text="A smaller line of text below the headline.")
    
    # Call-to-action buttons
    button_text = models.CharField(max_length=50, default="Learn More", help_text="Text for the call-to-action button.")
    button_link = models.URLField(help_text="The URL the button should link to (e.g., /courses).")
    
    # Control which hero section is currently active
    is_active = models.BooleanField(default=True, help_text="Only one hero section can be active at a time.")

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"

    def __str__(self):
        return self.heading