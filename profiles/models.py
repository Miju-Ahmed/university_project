# profiles/models.py

from django.db import models
from django.contrib.auth.models import User
# The signal-related imports have been removed from here
from courses.models import Course

class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    bio = models.TextField(blank=True, help_text="A short biography.")
    profile_picture = models.ImageField(
        default='profile_pics/default.jpg',
        upload_to='profile_pics'
    )

    enrolled_courses = models.ManyToManyField(
        Course,
        related_name='students',
        blank=True
    )

    teaching_courses = models.ManyToManyField(
        Course,
        related_name='teachers',
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"

#
# The entire @receiver(post_save, sender=User) function block
# has been completely removed from the end of the file.
#