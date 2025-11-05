# courses/forms.py
from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        # We only need the teacher to fill out these fields
        fields = ['title', 'code', 'department', 'level', 'overview', 'entry_requirements']