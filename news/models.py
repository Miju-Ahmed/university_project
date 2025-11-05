# news/models.py
from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published_date')
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-published_date',)

    def __str__(self):
        return self.title