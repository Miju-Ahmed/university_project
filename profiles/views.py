# profiles/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
# This next import is very important for the profile_view function
from django.contrib.auth.models import User


# profiles/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm # Make sure this is imported
# ... other imports ...

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # The form's new save method handles everything now!
            form.save()
            
            # We NO LONGER need these lines:
            # user = form.save()
            # user.profile.user_type = 'student'
            # user.profile.save()
            
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'profiles/register.html', {'form': form})

# ... other views (profile_view, profile_edit) remain the same ...
# ======================================================= #
# ====         THIS IS THE MISSING FUNCTION            ==== #
# ======================================================= #
@login_required
def profile_view(request, username=None):
    if username:
        # If a username is provided in the URL, view that user's profile
        user = get_object_or_404(User, username=username)
    else:
        # If no username is provided, view the currently logged-in user's profile
        user = request.user
    return render(request, 'profiles/profile_detail.html', {'profile_user': user})
# ======================================================= #
# ====              END OF MISSING FUNCTION          ==== #
# ======================================================= #


@login_required
def profile_edit(request):
    if request.method == 'POST':
        # You MUST pass request.FILES to the form when handling file uploads
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'profiles/profile_form.html', {'form': form})


# profiles/views.py
# ... other imports
from .models import Profile

# ... your other views (register, profile_view, profile_edit)

def faculty_directory(request):
    # Get all profiles that are teachers, and pre-fetch the related user data
    # to avoid extra database queries in the template.
    teacher_profiles = Profile.objects.filter(user_type='teacher').select_related('user')
    
    context = {
        'teacher_profiles': teacher_profiles,
    }
    return render(request, 'profiles/directory.html', context)