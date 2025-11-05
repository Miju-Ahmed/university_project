# events/models.py
from django.db import models
from django.urls import reverse
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['start_time'] # Default order is by the start time

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk})

    @property
    def is_upcoming(self):
        return self.start_time > timezone.now()