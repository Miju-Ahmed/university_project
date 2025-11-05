# core/views.py
from django.shortcuts import render
from news.models import Article
# This is the corrected line: Import HeroSection instead of HomePageImage
from .models import HeroSection

from django.shortcuts import render
from news.models import Article
from core.models import HeroSection
from profiles.models import Profile # <--- Import Profile
from courses.models import Course # <--- Import Course

def homepage(request):
    # We will fetch 4 articles to better fit the new card grid design
    latest_articles = Article.objects.order_by('-published_date')[:4]
    
    # Fetch the one active hero section from the database
    # .first() is a safe way to get the object, or None if it doesn't exist
    active_hero = HeroSection.objects.filter(is_active=True).first()

    # Create the context dictionary to pass to the template
    context = {
        'latest_articles': latest_articles,
        'hero': active_hero, # Pass the hero object, not gallery_images
    }
    
    return render(request, 'core/homepage.html', context)


def about_us(request):
    # Gather some interesting stats from the database
    stats = {
    'student_count': Profile.objects.filter(user_type='student').count(),
    'teacher_count': Profile.objects.filter(user_type='teacher').count(),
    'course_count': Course.objects.count(),
    }
    return render(request, 'core/about.html', {'stats': stats})