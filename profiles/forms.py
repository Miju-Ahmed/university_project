# profiles/forms.py
from django import forms
from django.db import transaction # Import transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

USER_TYPE_CHOICES = (
    ('student', 'Register as a Student'),
    ('teacher', 'Register as a Teacher'),
)

class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        label="I am a:"
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

    @transaction.atomic # Ensures both User and Profile are created successfully
    def save(self, commit=True):
        # First, save the User using the parent form's save method
        user = super().save(commit=True)
        
        # Now, create the profile directly, using the saved user instance
        user_type = self.cleaned_data['user_type']
        Profile.objects.create(user=user, user_type=user_type)
        
        return user


# This form remains unchanged
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type', 'bio', 'profile_picture')